from ..const.main import (
    const_get_affix_separators,
    const_get_common_abbrev_swaps,
    const_get_npm_abbrev_swaps,
    const_get_npm_affixes,
)
from ..utils.generator_functions import *

NPM_AFFIXES = const_get_npm_affixes()
ABBREV_SWAPS = const_get_common_abbrev_swaps() + const_get_npm_abbrev_swaps()
AFFIX_SEPARATORS = const_get_affix_separators()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    express     |     |     js-express    |
  +----------------+     +-------------------+

"""


def npmPrefix(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Add common npm ecosystem prefixes like js-, js., js to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Prefix")

        resultLoc = list()
        name = package

        for affix in NPM_AFFIXES:
            for sep in AFFIX_SEPARATORS:
                prefix = affix + sep
                # Don't add a prefix if the name already starts with it
                if not name.startswith(prefix):
                    variation = prefix + name
                    if variation not in resultLoc:
                        resultLoc.append(variation)

                # Also try removing the prefix if the package already has it
                if name.startswith(prefix):
                    variation = name[len(prefix) :]
                    if variation and variation not in resultLoc:
                        resultLoc.append(variation)

        # Abbreviation swaps across all separators
        for short, long in ABBREV_SWAPS:
            for sep in AFFIX_SEPARATORS:
                short_prefix = short + sep
                long_prefix = long + sep
                if name.startswith(short_prefix):
                    variation = long_prefix + name[len(short_prefix) :]
                    if variation != name and variation not in resultLoc:
                        resultLoc.append(variation)
                if name.startswith(long_prefix):
                    variation = short_prefix + name[len(long_prefix) :]
                    if variation != name and variation not in resultLoc:
                        resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "npmPrefix")
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "npmPrefix"
            )
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "npmPrefix")
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "npmPrefix"
        )

    return resultList
