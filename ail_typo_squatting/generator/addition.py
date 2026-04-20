# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +----------------------+
  |    lodash      |     |     lodasih          |
  +----------------+     +----------------------+

"""


# Addition
def addition(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Add a character in the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Addition")

        resultLoc = list()
        name = package

        for i in (*range(48, 58), *range(97, 123)):
            # Adding 'i' in front of 'name'
            variation = chr(i) + name
            if variation not in resultLoc:
                resultLoc.append(variation)

            # Adding 'i' at the end of 'name'
            variation = name + chr(i)
            if variation not in resultLoc:
                resultLoc.append(variation)

            for j in range(0, len(name)):
                variation = name[:j] + chr(i) + name[j:]
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, 'addition')
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "addition")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, 'addition')
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "addition")

    return resultList
