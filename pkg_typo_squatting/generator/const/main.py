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
    "closeLetters",
    "doubleHit",
    "removeSeparatedSection",
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

# Common affixes shared across both npm and PyPI ecosystems
COMMON_AFFIXES = [
    "lib",
    "library",
    "utils",
    "util",
    "utility",
    "api",
    "cli",
    "config",
    "cfg",
    "helper",
    "helpers",
    "core",
    "client",
    "sdk",
]

# Common abbreviation swap pairs (apply to both ecosystems)
COMMON_ABBREV_SWAPS = [
    ("lib", "library"),
    ("util", "utils"),
    ("util", "utility"),
    ("utils", "utility"),
    ("config", "cfg"),
]

# npm ecosystem-specific suffixes/prefixes (base terms, separators applied by generators)
NPM_AFFIXES = [
    "js",
    "javascript",
    "node",
    "ts",
    "typescript",
    "react",
    "ng",
    "vue",
]

# Separators used when generating suffix/prefix variations
AFFIX_SEPARATORS = ["-", ".", ""]

# Abbreviation swap pairs for npm (short <-> long)
NPM_ABBREV_SWAPS = [
    ("js", "javascript"),
    ("ts", "typescript"),
]

# pypi ecosystem-specific suffixes/prefixes (base terms, separators applied by generators)
PYPI_AFFIXES = ["py", "python"]

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


def const_get_npm_affixes():
    """Return npm base affix terms (common + npm-specific)"""
    return COMMON_AFFIXES + NPM_AFFIXES


def const_get_affix_separators():
    """Return separators used for affix generation"""
    return AFFIX_SEPARATORS


def const_get_pypi_affixes():
    """Return pypi base affix terms (common + pypi-specific)"""
    return COMMON_AFFIXES + PYPI_AFFIXES


def const_get_common_abbrev_swaps():
    """Return common abbreviation swap pairs"""
    return COMMON_ABBREV_SWAPS


def const_get_pypi_version_suffixes():
    """Return pypi version suffixes"""
    return PYPI_VERSION_SUFFIXES


def const_get_npm_abbrev_swaps():
    """Return npm abbreviation swap pairs"""
    return NPM_ABBREV_SWAPS


def const_get_pypi_abbrev_swaps():
    """Return pypi abbreviation swap pairs"""
    return PYPI_ABBREV_SWAPS
