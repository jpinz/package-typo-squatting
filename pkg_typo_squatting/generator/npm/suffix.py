from ..utils.generator_functions import *
from ..const.main import const_get_npm_suffixes

NPM_SUFFIXES = const_get_npm_suffixes()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    express     |     |     express-js    |
  +----------------+     +-------------------+

"""


def npmSuffix(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Add common npm ecosystem suffixes like -js, -node, -ts to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Suffix")

        resultLoc = list()
        name = package

        for suffix in NPM_SUFFIXES:
            # Don't add a suffix if the name already ends with it
            if not name.endswith(suffix):
                variation = name + suffix
                if variation not in resultLoc:
                    resultLoc.append(variation)

            # Also try removing the suffix if the package already has it
            if name.endswith(suffix):
                variation = name[:-len(suffix)]
                if variation and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "npmSuffix")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "npmSuffix")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "npmSuffix")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "npmSuffix")

    return resultList
