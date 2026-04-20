# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +--------------------+
  |    lodash      |     |      lodsh         |
  +----------------+     +--------------------+

"""

# Omission
def omission(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Leave out a letter of the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Omission")

        resultLoc = list()
        name = package

        for i in range(0, len(name)):
            variation = name[0:i] + name[i+1:len(name)]
            if variation and variation not in resultLoc:
                resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "omission")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "omission")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "omission")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "omission")

    return resultList