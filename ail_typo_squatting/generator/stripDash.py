# Import all the utils
from .utils.generator_functions import *

"""

   Original Package            Typosquatted Package
  +--------------------+     +----------------------+
  |  i-love-potato     |     |   ilove-potato       |
  +--------------------+     +----------------------+

"""

def stripDash(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Delete a dash from the package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Strip Dash")

        loc = package
        cp = 0
        loc_result_list = resultList.copy()
        while "-" in loc:
            loc2 = loc[::-1].replace("-", "", 1)[::-1]
            loc = loc.replace("-", "", 1)

            if givevariations:
                flag = False
                for var in all_algo_names:
                    if [loc, var] in resultList:
                        flag = True
                if not flag:
                    cp += 1
                    loc_result_list.append([loc, "stripDash"])

                flag = False
                for var in all_algo_names:
                    if [loc2, var] in resultList:
                        flag = True
                if not flag:
                    cp += 1
                    loc_result_list.append([loc2, "stripDash"])
            else:
                if loc not in resultList:
                    cp += 1
                    loc_result_list.append(loc)

                if loc2 not in resultList:
                    cp += 1
                    loc_result_list.append(loc2)

        if verbose:
            print(f"{cp}\n")

        return final_treatment(package, loc_result_list, limit, givevariations, keeporiginal, "stripDash")

    return resultList
