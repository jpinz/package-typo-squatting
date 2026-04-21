from ..const.main import const_get_common_abbrev_swaps, const_get_npm_abbrev_swaps
from ..utils.generator_functions import *

ABBREV_SWAPS = const_get_common_abbrev_swaps() + const_get_npm_abbrev_swaps()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    jsdom       |     |   javascriptdom   |
  +----------------+     +-------------------+

  Replaces abbreviation substrings anywhere in the package name,
  not just at prefix/suffix positions.
  e.g. js <-> javascript, ts <-> typescript

"""


def npmSubstitution(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Substitute abbreviations anywhere in npm package names (js<->javascript, ts<->typescript)"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Substitution")

        resultLoc = list()
        name = package

        for short, long in ABBREV_SWAPS:
            if short in name:
                variation = name.replace(short, long)
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

            if long in name:
                variation = name.replace(long, short)
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "npmSubstitution")
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "npmSubstitution"
            )
            return rLoc

        resultList = checkResult(
            resultLoc, resultList, givevariations, "npmSubstitution"
        )
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "npmSubstitution"
        )

    return resultList
