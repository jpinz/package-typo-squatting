# Import all the utils
from .utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    lodash      |     |     ldoash        |
  +----------------+     +-------------------+

"""

# Change Order
def changeOrder(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Change the order of letters in word"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Change Order")

        resultLoc = list()
        name = package

        if len(name) > 1:
            for i in range(0, len(name)):
                loc = name[0:i] + name[i+1:]
                for j in range(0, len(loc)):
                    inter = loc[:j] + name[i] + loc[j:]
                    if inter != name and inter not in resultLoc:
                        resultLoc.append(inter)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, 'changeOrder')
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "changeOrder")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, 'changeOrder')
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "changeOrder")

    return resultList
