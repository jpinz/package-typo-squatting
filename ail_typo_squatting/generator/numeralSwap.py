# Import all the utils
from .utils.generator_functions import *
from .const.main import *

numerals = const_get_numeral()

"""

   Original Package        Typosquatted Package
  +----------------+     +--------------------+
  |    babel7      |     |      babel-seven   |
  +----------------+     +--------------------+

"""

# Numeral Swap
def numeralSwap(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Change a numbers to words and vice versa"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Numeral Swap")

        resultLoc = list()
        name = package

        for numerals_list in numerals:
            for nume in numerals_list:
                if nume in name:
                    for nume2 in numerals_list:
                        if not nume2 == nume:
                            loc = name.replace(nume, nume2)
                            if loc != name and loc not in resultLoc:
                                resultLoc.append(loc)

        if resultLoc:
            if verbose:
                print(f"{len(resultLoc)}\n")

            if combo:
                rLoc = checkResult(resultLoc, resultList, givevariations, "numeralSwap")
                rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "numeralSwap")
                return rLoc

            resultList = checkResult(resultLoc, resultList, givevariations, "numeralSwap")
            resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "numeralSwap")
        elif verbose:
            print("0\n")

    return resultList
