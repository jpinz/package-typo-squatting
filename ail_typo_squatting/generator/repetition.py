# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +----------------------+
  |    lodash      |     |      lodassh         |
  +----------------+     +----------------------+

"""

# Repetition
def repetition(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Characters Repetition"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Characters Repetition")

        resultLoc = list()
        name = package

        for i, c in enumerate(name):
            variation = name[:i] + c + name[i:]
            if variation != name and variation not in resultLoc:
                resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, 'repetition')
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "repetition")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, 'repetition')
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "repetition")

    return resultList
