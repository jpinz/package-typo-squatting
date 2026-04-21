# Import all the utils
from .utils.generator_functions import *

"""

   Original Package            Typosquatted Package
  +--------------------+     +----------------------+
  |  foo-bar-js        |     |  bar-js, foo-js,     |
  |                    |     |  foo-bar              |
  +--------------------+     +----------------------+

  Remove one section from a separated package name.
  e.g. foo-bar-js -> bar-js, foo-js, foo-bar

"""

SEPARATORS = ["-", "_", "."]


def removeSeparatedSection(
    package,
    resultList,
    verbose,
    limit,
    givevariations=False,
    keeporiginal=False,
    combo=False,
):
    """Remove one section from a separated package name"""

    if not len(resultList) >= limit:
        if verbose:
            print("[+] Remove Separated Section")

        resultLoc = list()
        name = package

        for sep in SEPARATORS:
            parts = name.split(sep)
            if len(parts) >= 2:
                for i in range(len(parts)):
                    remaining = parts[:i] + parts[i + 1 :]
                    variation = sep.join(remaining)
                    if variation and variation != name and variation not in resultLoc:
                        resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(
                resultLoc, resultList, givevariations, "removeSeparatedSection"
            )
            rLoc = final_treatment(
                package,
                rLoc,
                limit,
                givevariations,
                keeporiginal,
                "removeSeparatedSection",
            )
            return rLoc

        resultList = checkResult(
            resultLoc, resultList, givevariations, "removeSeparatedSection"
        )
        resultList = final_treatment(
            package,
            resultList,
            limit,
            givevariations,
            keeporiginal,
            "removeSeparatedSection",
        )

    return resultList
