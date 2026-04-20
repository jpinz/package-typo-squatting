# Import all the utils
from .utils.generator_functions import *

import inflect

def singularPluralize(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Create by making a singular package name plural and vice versa"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Singular Pluralize")

        resultLoc = list()
        inflector = inflect.engine()
        name = package

        loc = inflector.plural(name)
        if loc and loc != name and loc not in resultLoc:
            resultLoc.append(loc)

        # Also try singularizing (in case the name is already plural)
        loc_singular = inflector.singular_noun(name)
        if loc_singular and loc_singular != name and loc_singular not in resultLoc:
            resultLoc.append(loc_singular)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "singularPluralize")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "singularPluralize")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "singularPluralize")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "singularPluralize")

    return resultList
