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
  |    requests    |     |   requests-py     |
  +----------------+     +-------------------+

"""


def pypiSuffix(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Add common PyPI ecosystem suffixes like -py, .py, py to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Suffix")

        resultLoc = list()
        name = package

        for affix in PYPI_AFFIXES:
            for sep in AFFIX_SEPARATORS:
                suffix = sep + affix
                # Don't add a suffix if the name already ends with it
                if not name.endswith(suffix):
                    variation = name + suffix
                    if variation not in resultLoc:
                        resultLoc.append(variation)

                # Also try removing the suffix if the package already has it
                if name.endswith(suffix):
                    variation = name[: -len(suffix)]
                    if variation and variation not in resultLoc:
                        resultLoc.append(variation)

        # Abbreviation swaps across all separators
        for short, long in ABBREV_SWAPS:
            for sep in AFFIX_SEPARATORS:
                short_suffix = sep + short
                long_suffix = sep + long
                if name.endswith(short_suffix):
                    variation = name[: -len(short_suffix)] + long_suffix
                    if variation != name and variation not in resultLoc:
                        resultLoc.append(variation)
                if name.endswith(long_suffix):
                    variation = name[: -len(long_suffix)] + short_suffix
                    if variation != name and variation not in resultLoc:
                        resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "pypiSuffix")
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "pypiSuffix"
            )
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "pypiSuffix")
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "pypiSuffix"
        )

    return resultList
