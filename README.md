# pkg-typo-squatting

pkg-typo-squatting is a Python library to generate potential typosquatting package names for **npm** and **PyPI** ecosystems. It uses various name permutation techniques to detect potential supply chain attacks through package name confusion.

The tool supports two separate systems with ecosystem-specific techniques:
- **npm packages**: Includes scope/namespace squatting, JS/Node-specific suffixes and prefixes
- **PyPI packages**: Includes Python-specific suffixes and prefixes, separator normalization, version confusion

# Requirements

- Python 3.8+
- [inflect](https://github.com/jaraco/inflect) library
- [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation)

# Installation

## Source install

pkg-typo-squatting can be installed with uv. If you don't have uv installed, you can do the following `curl -LsSf https://astral.sh/uv/install.sh | sh`.

```bash
$ uv sync
$ uv run pkg-typo-squatting -h
```

## pip installation

```bash
$ pip3 install pkg-typo-squatting
```

# Usage

```bash
$ uv run pkg-typo-squatting --help
usage: pkg-typo-squatting [-h] [-v] [-pn PACKAGENAME [PACKAGENAME ...]] [-fpn FILEPACKAGENAME]
               [-e {npm,pypi}] [-o OUTPUT] [-fo FORMATOUTPUT] [-br] [-l LIMIT]
               [-var] [-ko] [-a] [-om] [-repe] [-repl] [-drepl] [-cho] [-add]
               [-sd] [-vs] [-ada] [-hg] [-ahg] [-cm] [-hp] [-sp] [-ns]
               [--npmsuffix] [--npmprefix] [--npmscopesquat] [--npmseparator]
               [--pypisuffix] [--pypiprefix] [--pypiseparator] [--pypiversionsuffix]
               [-combo]
```

## Key arguments

| Argument | Description |
|:---------|:-----------|
| `-pn` | List of package names to check |
| `-fpn` | File containing list of package names |
| `-e` | Ecosystem: `npm` or `pypi` (default: npm) |
| `-a` | Use all algorithms for the chosen ecosystem |
| `-o` | Output path (`-` for stdout) |
| `-fo` | Output format: text, json, yaml, regex |
| `-var` | Show which algorithm generated each variation |

# Usage examples

1. Generate all variations for `lodash` (npm):

```bash
$ uv run pkg-typo-squatting -pn lodash -e npm -a -o .
```

2. Generate all variations for `requests` (PyPI):

```bash
$ uv run pkg-typo-squatting -pn requests -e pypi -a -o .
```

3. Generate variations for a scoped npm package:

```bash
$ uv run pkg-typo-squatting -pn "@babel/core" -e npm -a -o - -var
```

4. Use specific algorithms only:

```bash
$ uv run pkg-typo-squatting -pn express -e npm -om --npmsuffix --npmscopesquat -o -
```

5. Generate from a file of package names:

```bash
$ uv run pkg-typo-squatting -fpn packages.txt -e pypi -a -o .
```

# Used as a library

## Run all algorithms for an ecosystem

```python
from pkg_typo_squatting import runAll
import math

resultList = runAll(
    package="lodash",
    ecosystem="npm",
    limit=math.inf,
    verbose=False,
    givevariations=False,
    keeporiginal=False
)
print(f"Generated {len(resultList)} variations")
for variation in resultList[:10]:
    print(variation)
```

## Run specific algorithms

```python
from pkg_typo_squatting import omission, npmSuffix, npmScopeSquat
import math

resultList = list()
package = "express"
limit = math.inf

resultList = omission(package=package, resultList=resultList, verbose=False, limit=limit,
                       givevariations=False, keeporiginal=False)

resultList = npmSuffix(package=package, resultList=resultList, verbose=False, limit=limit,
                        givevariations=False, keeporiginal=False)

resultList = npmScopeSquat(package=package, resultList=resultList, verbose=False, limit=limit,
                            givevariations=False, keeporiginal=False)

print(resultList)
```

## PyPI example

```python
from pkg_typo_squatting import omission, pypiSuffix, pypiPrefix, pypiVersionSuffix
import math

resultList = list()
package = "requests"
limit = math.inf

resultList = omission(package=package, resultList=resultList, verbose=False, limit=limit)
resultList = pypiSuffix(package=package, resultList=resultList, verbose=False, limit=limit)
resultList = pypiPrefix(package=package, resultList=resultList, verbose=False, limit=limit)
resultList = pypiVersionSuffix(package=package, resultList=resultList, verbose=False, limit=limit)

print(resultList)
```

# List of algorithms

## Common algorithms (both npm and PyPI)

| Algorithm | Description | Example |
|:----------|:-----------|:--------|
| Omission | Remove one character at a time | lodash → odash, ldash, loash |
| Repetition | Duplicate one character | lodash → llodash, loodash |
| Replacement | Replace each character with a-z, 0-9 | lodash → aodash, l0dash |
| DoubleReplacement | Replace two consecutive characters | lodash → aadash, bbdash |
| Addition | Insert a character at each position | lodash → alodash, loadash |
| ChangeOrder | Reorder characters | lodash → oldash, ldoash |
| StripDash | Remove dashes | my-package → mypackage |
| VowelSwap | Swap vowels | lodash → ladash, ledash |
| AddDash | Insert dashes | lodash → l-odash, lo-dash |
| Homoglyph | Replace with visually similar characters | lodash → 1odash, l0dash |
| CommonMisspelling | Use common misspellings | (from Wikipedia misspelling list) |
| Homophones | Replace with same-sounding words | (from homophone list) |
| SingularPluralize | Toggle singular/plural | request → requests |
| NumeralSwap | Swap numbers and words | babel7 → babelseven |

## npm-specific algorithms

| Algorithm | Description | Example |
|:----------|:-----------|:--------|
| npmSuffix | Add/remove JS ecosystem suffixes | express → express-js, express-node, express-ts |
| npmPrefix | Add/remove JS ecosystem prefixes | express → js-express, node-express |
| npmScopeSquat | Scope/namespace manipulation | @babel/core → core, babel-core, @babe/core |
| npmSeparator | Swap separators (-, _, .) | my-package → my_package, my.package, mypackage |

## PyPI-specific algorithms

| Algorithm | Description | Example |
|:----------|:-----------|:--------|
| pypiSuffix | Add/remove Python ecosystem suffixes | requests → requests-py, requests-python, requests-lib |
| pypiPrefix | Add/remove Python ecosystem prefixes | requests → py-requests, python-requests |
| pypiSeparator | Swap separators (-, _, .) | my-package → my_package, my.package, mypackage |
| pypiVersionSuffix | Add version numbers | requests → requests2, requests3, requests-v2 |

# Sample output

## Text format (default)

```
lodash
odash
ldash
loash
lodsh
lodah
lodas
llodash
loodash
...
lodash-js
lodash-node
js-lodash
node-lodash
```

## JSON format

```json
{
  "package": "lodash",
  "variations": [
    "odash",
    "ldash",
    "loash",
    "lodash-js",
    "lodash-node"
  ]
}
```

## YAML format

```yaml
title: lodash
variations:
- odash
- ldash
- loash
- lodash-js
- lodash-node
```

## Regex format

```
odash|ldash|loash|lodsh|lodah|lodas|llodash|loodash
```

# Acknowledgment

![](./img/cef.png)

The project has been co-funded by CEF-TC-2020-2 - 2020-EU-IA-0260 - JTAN - Joint Threat Analysis Network.
