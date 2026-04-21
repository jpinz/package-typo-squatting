# Import all the utils
from .utils.generator_functions import *
from .utils.qwerty import get_neighbors

"""

   Original Package        Typosquatted Package
  +----------------+     +----------------------+
  |    lodash      |     |      lpodash         |
  +----------------+     +----------------------+

  Insert a QWERTY keyboard neighbor next to each character.
  Simulates accidentally hitting an adjacent key along with the intended one.

"""


def doubleHit(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Insert a QWERTY keyboard neighbor next to each character"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Double Hit")

        resultLoc = list()
        name = package

        for i in range(len(name)):
            neighbors = get_neighbors(name[i])
            for neighbor in neighbors:
                variation = name[:i] + neighbor + name[i:]
                if variation != name and variation not in resultLoc:
                    resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "doubleHit")
            rLoc = final_treatment(
                package, rLoc, limit, givevariations, keeporiginal, "doubleHit"
            )
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "doubleHit")
        resultList = final_treatment(
            package, resultList, limit, givevariations, keeporiginal, "doubleHit"
        )

    return resultList
