from ..utils.generator_functions import *
from ..const.main import const_get_npm_prefixes

NPM_PREFIXES = const_get_npm_prefixes()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    express     |     |     js-express    |
  +----------------+     +-------------------+

"""


def npmPrefix(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Add common npm ecosystem prefixes like js-, node-, ts- to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Prefix")

        resultLoc = list()
        name = package

        for prefix in NPM_PREFIXES:
            # Don't add a prefix if the name already starts with it
            if not name.startswith(prefix):
                variation = prefix + name
                if variation not in resultLoc:
                    resultLoc.append(variation)

            # Also try removing the prefix if the package already has it
            if name.startswith(prefix):
                variation = name[len(prefix):]
                if variation and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "npmPrefix")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "npmPrefix")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "npmPrefix")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "npmPrefix")

    return resultList
