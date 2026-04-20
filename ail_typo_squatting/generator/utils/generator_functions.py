# Import the constants stored in "../const/main.py"
from ..const.main import *

# The constants
common_algo_list = const_get_common_algo_list()
npm_algo_list = const_get_npm_algo_list()
pypi_algo_list = const_get_pypi_algo_list()

# Combined list of all algo names for deduplication checks
all_algo_names = common_algo_list + npm_algo_list + pypi_algo_list


def parse_package_name(package, ecosystem="npm"):
    """Parse a package name based on the ecosystem.

    For npm: handles @scope/name -> (scope, name) and plain name -> ('', name)
    For pypi: normalizes separators and returns ('', name)

    Returns (scope, name) tuple.
    """
    if ecosystem == "npm" and package.startswith("@"):
        parts = package.split("/", 1)
        if len(parts) == 2:
            return (parts[0], parts[1])
    return ("", package)


def reassemble_package_name(scope, name):
    """Reassemble a package name with an optional npm scope."""
    if scope:
        return f"{scope}/{name}"
    return name


def checkResult(resultLoc, resultList, givevariations, algoName=''):
    """
    Verify if element in resultLoc not exist in resultList before adding them in resultList
    """
    loc_result_list = resultList.copy()
    for element in resultLoc:
        if givevariations:
            flag = False
            for var in all_algo_names:
                if [element, var] in resultList:
                    flag = True
            if not flag:
                loc_result_list.append([element, algoName])
        else:
            if element not in resultList:
                loc_result_list.append(element)

    return loc_result_list


def final_treatment(package, resultList, limit, givevariations, keeporiginal, algo_name):
    """Final treatment of a variation's function, keep original and name of variations' algorithm"""
    if not keeporiginal:
        try:
            if givevariations:
                resultList.remove([package, algo_name])
            else:
                resultList.remove(package)
        except:
            pass
    elif givevariations:
        try:
            resultList.remove([package, algo_name])
        except:
            pass
        if not [package, 'original'] in resultList:
            resultList.insert(0, [package, 'original'])

    while len(resultList) > limit:
        resultList.pop()

    return resultList
