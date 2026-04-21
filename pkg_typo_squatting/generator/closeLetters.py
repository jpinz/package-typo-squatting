# Import all the utils
from .utils.generator_functions import *
from .utils.qwerty import get_neighbors

"""

   Original Package        Typosquatted Package
  +----------------+     +----------------------+
  |    lodash      |     |      kodash          |
  +----------------+     +----------------------+

  Replace each character with a nearby key on the QWERTY keyboard.
  Simulates a typo where the wrong adjacent key was pressed.

"""


def closeLetters(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Replace each character with a QWERTY keyboard neighbor"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Close Letters")

        resultLoc = list()
        name = package

        for i in range(len(name)):
            neighbors = get_neighbors(name[i])
            for neighbor in neighbors:
                variation = name[:i] + neighbor + name[i + 1 :]
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "closeLetters")
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "closeLetters"
            )
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "closeLetters")
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "closeLetters"
        )

    return resultList
