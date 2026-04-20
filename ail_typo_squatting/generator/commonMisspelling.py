# Import all the utils
import os
from .utils.generator_functions import *
from .utils.get_pathetc import get_path_etc

import json


pathEtc = get_path_etc()


def commonMisspelling(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Change a word by its misspellings"""
    # https://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Common Misspelling")

        with open(os.path.join(pathEtc, "common-misspellings.json"), "r") as read_json:
            misspelling = json.load(read_json)
            keys = misspelling.keys()

        resultLoc = list()
        name = package

        # Split on separators to find words to check for misspellings
        # Try the full name first
        if name in keys:
            misspell = misspelling[name].split(",")
            for mis in misspell:
                variation = mis.replace(" ", "")
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        # Also try individual parts split by common separators
        for sep in ['-', '_', '.']:
            if sep in name:
                parts = name.split(sep)
                for idx, part in enumerate(parts):
                    if part in keys:
                        misspell = misspelling[part].split(",")
                        for mis in misspell:
                            new_parts = parts.copy()
                            new_parts[idx] = mis.replace(" ", "")
                            variation = sep.join(new_parts)
                            if variation != name and variation not in resultLoc:
                                resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "commonMisspelling")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "commonMisspelling")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "commonMisspelling")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "commonMisspelling")

    return resultList
