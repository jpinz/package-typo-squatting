# Here are stored all the constants used in the project
# The constants are stored in a separate file to make it easier to change them

SIMILAR_CHAR = {
    "0": ["o"],
    "1": ["l", "i"],
    "2": ["z"],
    "5": ["s"],
    "a": ["e", "o"],
    "b": ["d", "p"],
    "c": ["e", "k"],
    "d": ["b", "cl"],
    "e": ["c", "a"],
    "f": ["t"],
    "g": ["q", "j"],
    "h": ["n", "b"],
    "i": ["1", "l", "j"],
    "j": ["i", "g"],
    "k": ["lc", "c"],
    "l": ["1", "i"],
    "m": ["n", "nn", "rn", "rr"],
    "n": ["m", "r"],
    "o": ["0", "a"],
    "p": ["q", "b"],
    "q": ["g", "p"],
    "r": ["n", "v"],
    "s": ["5", "z"],
    "t": ["f", "l"],
    "u": ["v", "w"],
    "v": ["u", "w"],
    "w": ["vv", "v"],
    "x": ["z", "k"],
    "y": ["i", "v"],
    "z": ["s", "2", "x"],
}

NUMERAL = [
    ["0", "zero"],
    ["1", "one", "first"],
    ["2", "two", "second"],
    ["3", "three", "third"],
    ["4", "four", "fourth", "for"],
    ["5", "five", "fifth"],
    ["6", "six", "sixth"],
    ["7", "seven", "seventh"],
    ["8", "eight", "eighth"],
    ["9", "nine", "ninth"],
]

# Common algorithms that apply to both npm and pypi package names
COMMON_ALGO_LIST = [
    "omission",
    "repetition",
    "changeOrder",
    "replacement",
    "doubleReplacement",
    "addition",
    "stripDash",
    "vowelSwap",
    "addDash",
    "homoglyph",
    "commonMisspelling",
    "homophones",
    "singularPluralize",
    "numeralSwap",
]

# npm-specific algorithms
NPM_ALGO_LIST = [
    "npmSuffix",
    "npmPrefix",
    "npmScopeSquat",
    "npmSeparator",
    "npmSubstitution",
]

# pypi-specific algorithms
PYPI_ALGO_LIST = [
    "pypiSuffix",
    "pypiPrefix",
    "pypiSeparator",
    "pypiVersionSuffix",
    "pypiSubstitution",
]

# npm ecosystem-specific suffixes commonly seen in package names
NPM_SUFFIXES = [
    "-js",
    "-javascript",
    "-node",
    "-ts",
    "-typescript",
    "-react",
    "-ng",
    "-vue",
    "-cli",
    "-lib",
    "-utils",
    "-api",
    "js",
    ".js",
    "javascript",
    "ts",
    ".ts",
    "typescript",
    "node",
]

# npm ecosystem-specific prefixes commonly seen in package names
NPM_PREFIXES = [
    "js-",
    "javascript-",
    "node-",
    "ts-",
    "typescript-",
    "react-",
    "ng-",
    "vue-",
    "cli-",
    "lib-",
    "js",
    "node",
    "ts",
]

# Abbreviation swap pairs for npm (short <-> long)
NPM_ABBREV_SWAPS = [
    ("js", "javascript"),
    ("ts", "typescript"),
]

# Common npm scopes that could be typosquatted
NPM_COMMON_SCOPES = [
    "@types",
    "@babel",
    "@angular",
    "@vue",
    "@react",
    "@aws-sdk",
    "@google-cloud",
    "@azure",
    "@nestjs",
    "@emotion",
    "@mui",
    "@testing-library",
    "@typescript-eslint",
    "@eslint",
]

# pypi ecosystem-specific suffixes commonly seen in package names
PYPI_SUFFIXES = [
    "-py",
    "-python",
    "-lib",
    "-sdk",
    "-api",
    "-client",
    "-core",
    "-utils",
    "py",
    ".py",
    "python",
]

# pypi ecosystem-specific prefixes commonly seen in package names
PYPI_PREFIXES = ["py-", "python-", "lib-", "py"]

# Abbreviation swap pairs for pypi (short <-> long)
PYPI_ABBREV_SWAPS = [
    ("py", "python"),
]

# pypi version suffixes for version confusion attacks
PYPI_VERSION_SUFFIXES = ["2", "3", "-v2", "-v3", "4"]


# Getters for constants
def const_get_similar_chars():
    """Return the dictionary of similar characters"""
    return SIMILAR_CHAR


def const_get_numeral():
    """Return the list of numeral"""
    return NUMERAL


def const_get_common_algo_list():
    """Return the list of common algorithm names"""
    return COMMON_ALGO_LIST


def const_get_npm_algo_list():
    """Return the list of npm-specific algorithm names"""
    return NPM_ALGO_LIST


def const_get_pypi_algo_list():
    """Return the list of pypi-specific algorithm names"""
    return PYPI_ALGO_LIST


def const_get_npm_suffixes():
    """Return npm-specific suffixes"""
    return NPM_SUFFIXES


def const_get_npm_prefixes():
    """Return npm-specific prefixes"""
    return NPM_PREFIXES


def const_get_npm_common_scopes():
    """Return common npm scopes"""
    return NPM_COMMON_SCOPES


def const_get_pypi_suffixes():
    """Return pypi-specific suffixes"""
    return PYPI_SUFFIXES


def const_get_pypi_prefixes():
    """Return pypi-specific prefixes"""
    return PYPI_PREFIXES


def const_get_pypi_version_suffixes():
    """Return pypi version suffixes"""
    return PYPI_VERSION_SUFFIXES


def const_get_npm_abbrev_swaps():
    """Return npm abbreviation swap pairs"""
    return NPM_ABBREV_SWAPS


def const_get_pypi_abbrev_swaps():
    """Return pypi abbreviation swap pairs"""
    return PYPI_ABBREV_SWAPS
