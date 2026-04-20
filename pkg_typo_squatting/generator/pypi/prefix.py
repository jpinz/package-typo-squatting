from ..const.main import const_get_pypi_abbrev_swaps, const_get_pypi_prefixes
from ..utils.generator_functions import *

PYPI_PREFIXES = const_get_pypi_prefixes()
PYPI_ABBREV_SWAPS = const_get_pypi_abbrev_swaps()

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
    """Add common PyPI ecosystem prefixes like py-, python- to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Prefix")

        resultLoc = list()
        name = package

        for prefix in PYPI_PREFIXES:
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

        # Abbreviation swaps: e.g. py-requests <-> python-requests
        for short, long in PYPI_ABBREV_SWAPS:
            short_prefix = short + "-"
            long_prefix = long + "-"
            if name.startswith(short_prefix):
                variation = long_prefix + name[len(short_prefix) :]
                if variation not in resultLoc:
                    resultLoc.append(variation)
            if name.startswith(long_prefix):
                variation = short_prefix + name[len(long_prefix) :]
                if variation not in resultLoc:
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
