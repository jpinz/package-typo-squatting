from ..utils.generator_functions import *
from ..const.main import const_get_pypi_suffixes

PYPI_SUFFIXES = const_get_pypi_suffixes()

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |    requests    |     |   requests-py     |
  +----------------+     +-------------------+

"""


def pypiSuffix(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Add common PyPI ecosystem suffixes like -py, -python, -lib to the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Suffix")

        resultLoc = list()
        name = package

        for suffix in PYPI_SUFFIXES:
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
            rLoc = checkResult(resultLoc, resultList, givevariations, "pypiSuffix")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "pypiSuffix")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "pypiSuffix")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "pypiSuffix")

    return resultList
