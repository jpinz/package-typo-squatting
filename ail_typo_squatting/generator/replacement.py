# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +----------------------+
  |    lodash      |     |      lodask          |
  +----------------+     +----------------------+

"""

# Replacement
def replacement(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Character replacement with a-z and 0-9"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Replacement")

        resultLoc = list()
        name = package

        for i in (*range(48, 58), *range(97, 123)):
            for j in range(0, len(name)):
                pre = name[:j]
                suf = name[j+1:]
                variation = pre + chr(i) + suf
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, 'replacement')
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "replacement")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, 'replacement')
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "replacement")

    return resultList
