from ..utils.generator_functions import *
from ..const.main import const_get_npm_common_scopes

NPM_COMMON_SCOPES = const_get_npm_common_scopes()

"""

   Original Package            Typosquatted Package
  +---------------------+     +-----------------------------+
  |  @babel/core        |     |  @bable/core, babel-core    |
  +---------------------+     +-----------------------------+

"""


def npmScopeSquat(package, resultList, verbose, limit, givevariations=False, keeporiginal=False, combo=False):
    """Generate scope-related typosquatting variations for npm packages.

    Techniques:
    - If scoped: generate unscoped version, swap scope for similar ones
    - If unscoped: add common scopes, generate scoped versions
    - Typosquat the scope name itself (omission, swap)
    """

    if not len(resultList) >= limit:
        if verbose:
            print("[+] npm Scope Squat")

        resultLoc = list()
        scope, name = parse_package_name(package, "npm")

        if scope:
            # Package is scoped (@scope/name)
            scope_name = scope[1:]  # Remove the @ prefix

            # 1. Remove the scope entirely - publish as unscoped
            if name not in resultLoc:
                resultLoc.append(name)

            # 2. Flatten scope into package name with separator
            for sep in ['-', '_', '']:
                variation = scope_name + sep + name
                if variation not in resultLoc:
                    resultLoc.append(variation)

            # 3. Typosquat the scope name (omission)
            for i in range(len(scope_name)):
                typo_scope = scope_name[:i] + scope_name[i+1:]
                if typo_scope:
                    variation = f"@{typo_scope}/{name}"
                    if variation not in resultLoc:
                        resultLoc.append(variation)

            # 4. Typosquat the scope name (adjacent swap)
            for i in range(len(scope_name) - 1):
                typo_scope = (scope_name[:i] + scope_name[i+1] +
                              scope_name[i] + scope_name[i+2:])
                variation = f"@{typo_scope}/{name}"
                if variation != package and variation not in resultLoc:
                    resultLoc.append(variation)

            # 5. Try other common scopes
            for common_scope in NPM_COMMON_SCOPES:
                if common_scope != scope:
                    variation = f"{common_scope}/{name}"
                    if variation not in resultLoc:
                        resultLoc.append(variation)

        else:
            # Package is unscoped - try adding common scopes
            for common_scope in NPM_COMMON_SCOPES:
                variation = f"{common_scope}/{name}"
                if variation not in resultLoc:
                    resultLoc.append(variation)

            # Try splitting the name into scope + name at separator positions
            for sep in ['-', '_']:
                if sep in name:
                    parts = name.split(sep, 1)
                    variation = f"@{parts[0]}/{parts[1]}"
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
