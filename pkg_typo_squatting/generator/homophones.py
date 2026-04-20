# Import all the utils
import os
from .utils.generator_functions import *
from .utils.get_pathetc import get_path_etc

pathEtc = get_path_etc()

"""

   Original Package        Typosquatted Package
  +----------------+     +-----------------+
  |    base        |     |     bass        |
  +----------------+     +-----------------+

"""

# Homophones
def homophones(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Change word by another that sounds the same when spoken"""
    # From http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/Homophones

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Homophones")

        with open(os.path.join(pathEtc, "homophones.txt"), "r") as read_file:
            homophones_list = read_file.readlines()

        resultLoc = list()
        name = package

        # Check the full name against homophones
        for lines in homophones_list:
            line = lines.split(",")
            for word in line:
                if name == word.rstrip("\n"):
                    for otherword in line:
                        cleaned = otherword.rstrip("\n")
                        if cleaned != name and cleaned not in resultLoc:
                            resultLoc.append(cleaned)

        # Also check individual parts split by common separators
        for sep in ['-', '_', '.']:
            if sep in name:
                parts = name.split(sep)
                for idx, part in enumerate(parts):
                    for lines in homophones_list:
                        line = lines.split(",")
                        for word in line:
                            if part == word.rstrip("\n"):
                                for otherword in line:
                                    cleaned = otherword.rstrip("\n")
                                    if cleaned != part:
                                        new_parts = parts.copy()
                                        new_parts[idx] = cleaned
                                        variation = sep.join(new_parts)
                                        if variation != name and variation not in resultLoc:
                                            resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "homophones")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "homophones")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "homophones")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "homophones")

    return resultList
 