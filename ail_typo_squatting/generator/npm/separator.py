from ..utils.generator_functions import *

"""

   Original Package        Typosquatted Package
  +----------------+     +-------------------+
  |  my-package    |     |  my_package       |
  +----------------+     +-------------------+

"""


def npmSeparator(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Swap separators in npm package names (hyphens, underscores, dots, or no separator)"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Separator")

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

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "npmSeparator")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "npmSeparator")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "npmSeparator")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "npmSeparator")

    return resultList
