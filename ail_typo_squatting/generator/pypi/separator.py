from ..utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |  my-package    |     |  my_package       |
  +----------------+     +-------------------+

PyPI normalizes package names: hyphens, underscores, and dots are all
treated as equivalent. This generator creates variations using different
separators that would NOT be normalized to the same name, as well as
separator removal.

"""


def pypiSeparator(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Swap separators in PyPI package names.

    PyPI normalizes -, _, and . to be equivalent, but attackers can still
    exploit this by registering names that look different visually.
    This also generates no-separator variations.
    """

    if not len(resultList) >= limit:
        if verbose:
            print("[+] PyPI Separator")

        resultLoc = list()
        name = package
        separators = ['-', '_', '.', '']

        has_separator = any(sep in name for sep in ['-', '_', '.'])

        if has_separator:
            for old_sep in ['-', '_', '.']:
                if old_sep in name:
                    for new_sep in separators:
                        if new_sep != old_sep:
                            variation = name.replace(old_sep, new_sep)
                            if variation and variation != name and variation not in resultLoc:
                                resultLoc.append(variation)

            # Also try double-separator (e.g., my--package)
            for sep in ['-', '_', '.']:
                if sep in name:
                    variation = name.replace(sep, sep + sep)
                    if variation != name and variation not in resultLoc:
                        resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "pypiSeparator")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "pypiSeparator")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "pypiSeparator")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "pypiSeparator")

    return resultList
