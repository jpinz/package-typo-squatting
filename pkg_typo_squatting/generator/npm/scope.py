from ..utils.generator_functions import *

"""

   Original Package            Typosquatted Package
  +---------------------+     +-----------------------------+
  |  @babel/core        |     |  babel-core, core,          |
  |                     |     |  babelcore, core-babel      |
  +---------------------+     +-----------------------------+
  |  express            |     |  @express/express            |
  +---------------------+     +-----------------------------+

"""

SEPARATORS = ["-", "_", "."]


def npmScopeSquat(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Generate scope-related typosquatting variations for npm packages.

    For scoped packages (@scope/name):
    - Remove scope entirely: @babel/core -> core
    - Flatten scope into name with separators: babel-core, babel_core, babelcore, babel.core
    - Reverse order: core-babel, core_babel, corebabel, core.babel
    - Typosquat the scope name (omission, adjacent swap)

    For unscoped packages:
    - Split at separators into scope/name: babel-core -> @babel/core
    - Use package name as both scope and name: express -> @express/express
    """

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Scope Squat")

        resultLoc = list()
        scope, name = parse_package_name(package, "npm")

        if scope:
            # Package is scoped (@scope/name)
            scope_name = scope[1:]  # Remove the @ prefix

            # 1. Remove the scope entirely
            if name not in resultLoc:
                resultLoc.append(name)

            # 2. Flatten scope into package name: scope{sep}name
            for sep in [""] + SEPARATORS:
                variation = scope_name + sep + name
                if variation not in resultLoc:
                    resultLoc.append(variation)

            # 3. Reverse order: name{sep}scope
            for sep in [""] + SEPARATORS:
                variation = name + sep + scope_name
                if variation not in resultLoc:
                    resultLoc.append(variation)

            # 4. Typosquat the scope name (omission - remove one char)
            for i in range(len(scope_name)):
                typo_scope = scope_name[:i] + scope_name[i + 1:]
                if typo_scope:
                    variation = f"@{typo_scope}/{name}"
                    if variation not in resultLoc:
                        resultLoc.append(variation)

            # 5. Typosquat the scope name (adjacent character swap)
            for i in range(len(scope_name) - 1):
                typo_scope = (scope_name[:i] + scope_name[i + 1] +
                              scope_name[i] + scope_name[i + 2:])
                variation = f"@{typo_scope}/{name}"
                if variation != package and variation not in resultLoc:
                    resultLoc.append(variation)

        else:
            # Package is unscoped

            # 1. Split at separators into @scope/name
            for sep in SEPARATORS:
                if sep in name:
                    parts = name.split(sep, 1)
                    if parts[0] and parts[1]:
                        variation = f"@{parts[0]}/{parts[1]}"
                        if variation not in resultLoc:
                            resultLoc.append(variation)
                        # Also try reversed: @name_part/scope_part
                        variation = f"@{parts[1]}/{parts[0]}"
                        if variation not in resultLoc:
                            resultLoc.append(variation)

            # 2. Use the package name as its own scope: express -> @express/express
            variation = f"@{name}/{name}"
            if variation not in resultLoc:
                resultLoc.append(variation)

        if verbose:
            print(f"{len(resultLoc)}\n")

        if combo:
            rLoc = checkResult(resultLoc, resultList, givevariations, "npmScopeSquat")
            rLoc = final_treatment(package, rLoc, limit, givevariations, keeporiginal, "npmScopeSquat")
            return rLoc

        resultList = checkResult(resultLoc, resultList, givevariations, "npmScopeSquat")
        resultList = final_treatment(package, resultList, limit, givevariations, keeporiginal, "npmScopeSquat")

    return resultList
