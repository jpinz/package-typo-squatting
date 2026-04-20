from ..utils.generator_functions import *
from ..const.main import const_get_pypi_version_suffixes

PYPI_VERSION_SUFFIXES = const_get_pypi_version_suffixes()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    requests    |     |   requests2       |
  +----------------+     +-------------------+

"""


def pypiVersionSuffix(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Add version-related suffixes to create confusion with versioned packages.

    Common in PyPI: package2, package3, package-v2, etc.
    """

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Version Suffix")

        resultLoc = list()
        name = package

        for suffix in PYPI_VERSION_SUFFIXES:
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
            rLoc = checkResult(resultLoc, resultList, givevariations, "pypiVersionSuffix")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "pypiVersionSuffix")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "pypiVersionSuffix")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "pypiVersionSuffix")

    return resultList
