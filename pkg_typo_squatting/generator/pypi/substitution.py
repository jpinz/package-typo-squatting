from ..const.main import const_get_common_abbrev_swaps, const_get_pypi_abbrev_swaps
from ..utils.generator_functions import *

ABBREV_SWAPS = const_get_common_abbrev_swaps() + const_get_pypi_abbrev_swaps()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    pyaudio     |     |   pythonaudio     |
  +----------------+     +-------------------+

  Replaces abbreviation substrings anywhere in the package name,
  not just at prefix/suffix positions.
  e.g. py <-> python

"""


def pypiSubstitution(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Substitute abbreviations anywhere in PyPI package names (py<->python)"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Substitution")

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
            rLoc = checkResult(
                resultLoc, resultList, givevariations, "pypiSubstitution"
            )
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "pypiSubstitution"
            )
            return rLoc

        resultList = checkResult(
            resultLoc, resultList, givevariations, "pypiSubstitution"
        )
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "pypiSubstitution"
        )

    return resultList
