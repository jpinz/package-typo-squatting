# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    lodash      |     |     lo-dash       |
  +----------------+     +-------------------+

"""

# Add Dash
def addDash(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Add a dash between characters in the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Add Dash")

        resultLoc = list()
        name = package

        if len(name) > 1:
            for i in range(1, len(name)):
                # Don't add a dash next to an existing dash
                if name[i-1] != '-' and name[i] != '-':
                    variation = name[:i] + '-' + name[i:]
                    if variation != name and variation not in resultLoc:
                        resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "addDash")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "addDash")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "addDash")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "addDash")

    return resultList
