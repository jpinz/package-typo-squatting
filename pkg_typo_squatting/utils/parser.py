import argparse


def getArguments():
    parser = argparse.ArgumentParser(
        description="Generate typosquatting variations for npm and PyPI package names"
    )
    parser.add_argument("-v", help="verbose, more display", action="store_true")

    parser.add_argument("-pn", "--packageName", nargs="+", help="list of package names")
    parser.add_argument(
        "-fpn", "--filepackageName", help="file containing list of package names"
    )

    parser.add_argument(
        "-e",
        "--ecosystem",
        choices=["npm", "pypi"],
        default="npm",
        help="package ecosystem: npm or pypi (default: npm)",
    )

    parser.add_argument("-o", "--output", help="path to output location")
    parser.add_argument(
        "-fo",
        "--formatoutput",
        help="format for the output file: json - regex - yaml - text. Default: text",
    )
    parser.add_argument(
        "-br", "--betterregex", help="Use retrie for faster regex", action="store_true"
    )

    parser.add_argument("-l", "--limit", help="limit of variations for a package name")
    parser.add_argument(
        "-var",
        "--givevariations",
        help="give the algo that generate variations",
        action="store_true",
    )
    parser.add_argument(
        "-ko",
        "--keeporiginal",
        help="Keep in the result list the original package name",
        action="store_true",
    )

    parser.add_argument("-a", "--all", help="Use all algo", action="store_true")

    # Common algorithms
    parser.add_argument(
        "-om",
        "--omission",
        help="Leave out a letter of the package name",
        action="store_true",
    )
    parser.add_argument(
        "-repe", "--repetition", help="Character Repeat", action="store_true"
    )
    parser.add_argument(
        "-repl", "--replacement", help="Character replacement", action="store_true"
    )
    parser.add_argument(
        "-drepl",
        "--doublereplacement",
        help="Double Character Replacement",
        action="store_true",
    )
    parser.add_argument(
        "-cho",
        "--changeorder",
        help="Change the order of letters in the name",
        action="store_true",
    )
    parser.add_argument(
        "-add",
        "--addition",
        help="Add a character in the package name",
        action="store_true",
    )
    parser.add_argument(
        "-sd",
        "--stripdash",
        help="Delete a dash from the package name",
        action="store_true",
    )
    parser.add_argument(
        "-vs",
        "--vowelswap",
        help="Swap vowels within the package name",
        action="store_true",
    )
    parser.add_argument(
        "-ada",
        "--adddash",
        help="Add a dash between characters in the name",
        action="store_true",
    )
    parser.add_argument(
        "-hg",
        "--homoglyph",
        help="Replace characters with visually similar ones",
        action="store_true",
    )
    parser.add_argument(
        "-ahg",
        "--all_homoglyph",
        help="Generate all possible homoglyph permutations",
        action="store_true",
    )
    parser.add_argument(
        "-cm",
        "--commonmisspelling",
        help="Change a word by its misspellings",
        action="store_true",
    )
    parser.add_argument(
        "-hp",
        "--homophones",
        help="Change word by another that sounds the same",
        action="store_true",
    )
    parser.add_argument(
        "-sp",
        "--singularpluralize",
        help="Make a singular name plural and vice versa",
        action="store_true",
    )
    parser.add_argument(
        "-ns",
        "--numeralswap",
        help="Change numbers to words and vice versa",
        action="store_true",
    )
    parser.add_argument(
        "-cl",
        "--closeletters",
        help="Replace characters with QWERTY keyboard neighbors",
        action="store_true",
    )
    parser.add_argument(
        "-dh",
        "--doublehit",
        help="Insert a QWERTY keyboard neighbor next to each character",
        action="store_true",
    )
    parser.add_argument(
        "-rss",
        "--removeseparatedsection",
        help="Remove one section from a separated package name",
        action="store_true",
    )

    # npm-specific algorithms
    parser.add_argument(
        "--npmsuffix",
        help="Add npm-specific suffixes (-js, -node, -ts)",
        action="store_true",
    )
    parser.add_argument(
        "--npmprefix",
        help="Add npm-specific prefixes (js-, node-, ts-)",
        action="store_true",
    )
    parser.add_argument(
        "--npmscopesquat",
        help="Generate npm scope squatting variations",
        action="store_true",
    )
    parser.add_argument(
        "--npmseparator",
        help="Swap separators in npm package names",
        action="store_true",
    )
    parser.add_argument(
        "--npmsubstitution",
        help="Substitute abbreviations in npm names (js<->javascript, ts<->typescript)",
        action="store_true",
    )

    # pypi-specific algorithms
    parser.add_argument(
        "--pypisuffix",
        help="Add PyPI-specific suffixes (-py, -python, -lib)",
        action="store_true",
    )
    parser.add_argument(
        "--pypiprefix",
        help="Add PyPI-specific prefixes (py-, python-)",
        action="store_true",
    )
    parser.add_argument(
        "--pypiseparator",
        help="Swap separators in PyPI package names",
        action="store_true",
    )
    parser.add_argument(
        "--pypiversionsuffix",
        help="Add version suffixes (2, 3, -v2)",
        action="store_true",
    )
    parser.add_argument(
        "--pypisubstitution",
        help="Substitute abbreviations in PyPI names (py<->python)",
        action="store_true",
    )

    parser.add_argument(
        "-combo", help="Combine multiple algo on a package name", action="store_true"
    )

    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=None,
        help="number of parallel workers (default: number of CPU cores)",
    )

    # Training data generation
    parser.add_argument(
        "--training",
        help="Generate training data for embedding models (CSV or JSON with anchor/positive/technique columns)",
        action="store_true",
    )
    parser.add_argument(
        "--training-format",
        choices=["csv", "json"],
        default="csv",
        help="Format for training data output: csv or json (default: csv)",
    )

    return parser
