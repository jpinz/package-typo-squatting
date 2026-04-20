# Import all the utils
from .utils.generator_functions import *

# Double Character Replacement
def doubleReplacement(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Double Character Replacement"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Double Character Replacement")

        resultLoc = list()
        name = package

        for i in (*range(48, 58), *range(97, 123)):
            for j in range(0, len(name)):
                pre = name[:j]
                suf = name[j+2:]
                variation = pre + chr(i) + chr(i) + suf
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, 'doubleReplacement')
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "doubleReplacement")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, 'doubleReplacement')
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "doubleReplacement")

    return resultList
