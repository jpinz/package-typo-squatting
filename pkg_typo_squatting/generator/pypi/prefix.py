from ..const.main import (
    const_get_affix_separators,
    const_get_common_abbrev_swaps,
    const_get_pypi_abbrev_swaps,
    const_get_pypi_affixes,
)
from ..utils.generator_functions import *

PYPI_AFFIXES = const_get_pypi_affixes()
ABBREV_SWAPS = const_get_common_abbrev_swaps() + const_get_pypi_abbrev_swaps()
AFFIX_SEPARATORS = const_get_affix_separators()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    requests    |     |   py-requests     |
  +----------------+     +-------------------+

"""


def pypiPrefix(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Add common PyPI ecosystem prefixes like py-, py., py to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Prefix")

        resultLoc = list()
        name = package

        for affix in PYPI_AFFIXES:
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
            rLoc = checkResult(resultLoc, resultList, givevariations, "pypiPrefix")
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "pypiPrefix"
            )
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "pypiPrefix")
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "pypiPrefix"
        )

    return resultList
