# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +----------------------+
  |    lodash      |     |    ledash            |
  +----------------+     +----------------------+

"""

# Vowel Swap
def vowelSwap(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Swap vowels within the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Vowel Swap")

        resultLoc = list()
        vowels = ["a", "e", "i", "o", "u", "y"]
        name = package

        for j in vowels:
            for k in vowels:
                if j != k:
                    loc = name.replace(k, j)
                    if loc != name and loc not in resultLoc:
                        resultLoc.append(loc)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "vowelSwap")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "vowelSwap")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "vowelSwap")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "vowelSwap")

    return resultList
