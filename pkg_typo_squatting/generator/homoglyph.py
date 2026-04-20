# Import all the utils
from .utils.generator_functions import *
from .const.main import *

glyphs = const_get_similar_chars()

# Homoglyph
def homoglyph(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, all=False, combo=False):
    """One or more characters that look similar to another character but are different are called homoglyphs"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Homoglyph")

        def mix(name):
            for w in range(1, len(name)):
                for i in range(len(name)-w+1):
                    pre = name[:i]
                    win = name[i:i+w]
                    suf = name[i+w:]
                    for c in win:
                        for g in glyphs.get(c, []):
                            yield pre + win.replace(c, g) + suf

        name = package

        result1 = set(mix(name))
        result2 = set()
        cp = 0
        loc_result_list = resultList.copy()

        if all:
            for r in result1:
                result2.update(set(mix(r)))

        for element in list(result1 | result2):
            if givevariations:
                flag = False
                for var in all_algo_names:
                    if [element, var] in resultList:
                        flag = True
                if not flag:
                    cp += 1
                    loc_result_list.append([element, "homoglyph"])

            elif element not in resultList:
                cp += 1
                loc_result_list.append(element)

        if verbose:
            print(f"{cp}\n")

        return final_treatment(package, loc_result_list, limit, givevariations, keeporiginal, "homoglyph")

    return resultList
