import os
import sys
import math
import pathlib

pathProg = pathlib.Path(__file__).parent.absolute()

pathWork = ""
for i in str(pathProg).replace("\\", "/").split("/")[:-1]:
    pathWork += i + "/"
pathBin = os.path.join(pathWork, "ail_typo_squatting")
sys.path.append(pathBin)

from typo import runAll, omission, repetition, replacement, addition, changeOrder
from typo import stripDash, vowelSwap, addDash, homoglyph, numeralSwap, singularPluralize
from typo import commonMisspelling, homophones, doubleReplacement
from typo import npmSuffix, npmPrefix, npmScopeSquat, npmSeparator
from typo import pypiSuffix, pypiPrefix, pypiSeparator, pypiVersionSuffix


def test_omission():
    """Test that omission generates correct variations"""
    results = omission("lodash", [], False, math.inf)
    assert len(results) > 0
    assert "lodash" not in results  # original should not be in results
    assert "odash" in results
    assert "ldash" in results
    assert "loash" in results
    assert "lodsh" in results
    assert "lodah" in results
    assert "lodas" in results
    print("[✅] omission")


def test_repetition():
    """Test that repetition generates correct variations"""
    results = repetition("lodash", [], False, math.inf)
    assert len(results) > 0
    assert "llodash" in results
    assert "llodash" in results
    assert "loddash" in results
    print("[✅] repetition")


def test_replacement():
    """Test that replacement generates correct variations"""
    results = replacement("abc", [], False, math.inf)
    assert len(results) > 0
    # Should replace each character with a-z, 0-9
    assert "bbc" in results
    assert "aac" in results
    assert "abd" in results
    print("[✅] replacement")


def test_addition():
    """Test that addition generates correct variations"""
    results = addition("ab", [], False, math.inf)
    assert len(results) > 0
    assert "aab" in results
    assert "bab" in results
    assert "abc" in results
    print("[✅] addition")


def test_change_order():
    """Test that changeOrder generates correct variations"""
    results = changeOrder("abc", [], False, math.inf)
    assert len(results) > 0
    assert "bac" in results
    assert "acb" in results
    print("[✅] changeOrder")


def test_strip_dash():
    """Test that stripDash generates correct variations"""
    results = stripDash("my-package", [], False, math.inf)
    assert len(results) > 0
    assert "mypackage" in results
    print("[✅] stripDash")


def test_strip_dash_no_dash():
    """Test that stripDash returns empty for packages without dashes"""
    results = stripDash("lodash", [], False, math.inf)
    assert len(results) == 0
    print("[✅] stripDash (no dash)")


def test_vowel_swap():
    """Test that vowelSwap generates correct variations"""
    results = vowelSwap("lodash", [], False, math.inf)
    assert len(results) > 0
    # 'o' should be swapped with other vowels
    assert "ladash" in results or "ledash" in results
    print("[✅] vowelSwap")


def test_add_dash():
    """Test that addDash generates correct variations"""
    results = addDash("lodash", [], False, math.inf)
    assert len(results) > 0
    assert "l-odash" in results
    assert "lo-dash" in results
    assert "lod-ash" in results
    print("[✅] addDash")


def test_homoglyph():
    """Test that homoglyph generates correct variations"""
    results = homoglyph("lodash", [], False, math.inf)
    assert len(results) > 0
    # 'l' can be replaced with '1' or 'i'
    assert "1odash" in results or "iodash" in results
    # 'o' can be replaced with '0'
    assert "l0dash" in results
    print("[✅] homoglyph")


def test_numeral_swap():
    """Test that numeralSwap generates correct variations"""
    results = numeralSwap("babel7", [], False, math.inf)
    assert len(results) > 0
    assert "babelseven" in results or "babelseventh" in results
    print("[✅] numeralSwap")


def test_numeral_swap_no_numbers():
    """Test that numeralSwap returns empty for packages without numbers"""
    results = numeralSwap("lodash", [], False, math.inf)
    assert len(results) == 0
    print("[✅] numeralSwap (no numbers)")


def test_singular_pluralize():
    """Test that singularPluralize generates correct variations"""
    results = singularPluralize("request", [], False, math.inf)
    assert len(results) > 0
    assert "requests" in results
    print("[✅] singularPluralize")


def test_double_replacement():
    """Test that doubleReplacement generates correct variations"""
    results = doubleReplacement("abc", [], False, math.inf)
    assert len(results) > 0
    print("[✅] doubleReplacement")


# npm-specific tests

def test_npm_suffix():
    """Test npm suffix generator"""
    results = npmSuffix("express", [], False, math.inf)
    assert len(results) > 0
    assert "express-js" in results
    assert "express-node" in results
    assert "express-ts" in results
    print("[✅] npmSuffix")


def test_npm_suffix_removal():
    """Test npm suffix removal when package already has suffix"""
    results = npmSuffix("express-js", [], False, math.inf)
    assert "express" in results
    print("[✅] npmSuffix (removal)")


def test_npm_prefix():
    """Test npm prefix generator"""
    results = npmPrefix("express", [], False, math.inf)
    assert len(results) > 0
    assert "js-express" in results
    assert "node-express" in results
    print("[✅] npmPrefix")


def test_npm_prefix_removal():
    """Test npm prefix removal when package already has prefix"""
    results = npmPrefix("js-express", [], False, math.inf)
    assert "express" in results
    print("[✅] npmPrefix (removal)")


def test_npm_scope_squat_scoped():
    """Test npm scope squatting for scoped packages"""
    results = npmScopeSquat("@babel/core", [], False, math.inf)
    assert len(results) > 0
    # Should include unscoped version
    assert "core" in results
    # Should include flattened versions
    assert "babel-core" in results or "babel_core" in results or "babelcore" in results
    print("[✅] npmScopeSquat (scoped)")


def test_npm_scope_squat_unscoped():
    """Test npm scope squatting for unscoped packages"""
    results = npmScopeSquat("express", [], False, math.inf)
    assert len(results) > 0
    # Should try adding common scopes
    assert any(r.startswith("@") for r in results)
    print("[✅] npmScopeSquat (unscoped)")


def test_npm_separator():
    """Test npm separator generator"""
    results = npmSeparator("my-package", [], False, math.inf)
    assert len(results) > 0
    assert "my_package" in results
    assert "my.package" in results
    assert "mypackage" in results
    print("[✅] npmSeparator")


def test_npm_separator_no_sep():
    """Test npm separator with no separators in name"""
    results = npmSeparator("lodash", [], False, math.inf)
    assert len(results) == 0
    print("[✅] npmSeparator (no separator)")


# PyPI-specific tests

def test_pypi_suffix():
    """Test PyPI suffix generator"""
    results = pypiSuffix("requests", [], False, math.inf)
    assert len(results) > 0
    assert "requests-py" in results
    assert "requests-python" in results
    assert "requests-lib" in results
    print("[✅] pypiSuffix")


def test_pypi_suffix_removal():
    """Test PyPI suffix removal when package already has suffix"""
    results = pypiSuffix("requests-py", [], False, math.inf)
    assert "requests" in results
    print("[✅] pypiSuffix (removal)")


def test_pypi_prefix():
    """Test PyPI prefix generator"""
    results = pypiPrefix("requests", [], False, math.inf)
    assert len(results) > 0
    assert "py-requests" in results
    assert "python-requests" in results
    print("[✅] pypiPrefix")


def test_pypi_prefix_removal():
    """Test PyPI prefix removal when package already has prefix"""
    results = pypiPrefix("py-requests", [], False, math.inf)
    assert "requests" in results
    print("[✅] pypiPrefix (removal)")


def test_pypi_separator():
    """Test PyPI separator generator"""
    results = pypiSeparator("my-package", [], False, math.inf)
    assert len(results) > 0
    assert "my_package" in results
    assert "my.package" in results
    assert "mypackage" in results
    print("[✅] pypiSeparator")


def test_pypi_version_suffix():
    """Test PyPI version suffix generator"""
    results = pypiVersionSuffix("requests", [], False, math.inf)
    assert len(results) > 0
    assert "requests2" in results
    assert "requests3" in results
    print("[✅] pypiVersionSuffix")


# Integration tests

def test_run_all_npm():
    """Test runAll with npm ecosystem"""
    results = runAll(
        package="lodash",
        ecosystem="npm",
        limit=math.inf,
        verbose=False,
        givevariations=False,
        keeporiginal=False
    )
    assert len(results) > 0
    # Should include results from common algos
    assert "odash" in results  # omission
    # Should include npm-specific results
    assert "lodash-js" in results  # npmSuffix
    print(f"[✅] runAll npm: {len(results)} variations for 'lodash'")


def test_run_all_pypi():
    """Test runAll with pypi ecosystem"""
    results = runAll(
        package="requests",
        ecosystem="pypi",
        limit=math.inf,
        verbose=False,
        givevariations=False,
        keeporiginal=False
    )
    assert len(results) > 0
    # Should include results from common algos
    assert "equests" in results  # omission
    # Should include pypi-specific results
    assert "requests-py" in results  # pypiSuffix
    assert "requests2" in results  # pypiVersionSuffix
    print(f"[✅] runAll pypi: {len(results)} variations for 'requests'")


def test_run_all_npm_scoped():
    """Test runAll with npm scoped package"""
    results = runAll(
        package="@babel/core",
        ecosystem="npm",
        limit=math.inf,
        verbose=False,
        givevariations=False,
        keeporiginal=False
    )
    assert len(results) > 0
    # Should include scoped variations from common algos
    assert any("@babel/" in r for r in results if isinstance(r, str))
    # Should include scope squatting variations
    assert "core" in results  # scope removal
    print(f"[✅] runAll npm scoped: {len(results)} variations for '@babel/core'")


def test_give_variations():
    """Test givevariations flag"""
    results = runAll(
        package="lodash",
        ecosystem="npm",
        limit=50,
        verbose=False,
        givevariations=True,
        keeporiginal=False
    )
    assert len(results) > 0
    # Each result should be [name, algo_name]
    assert isinstance(results[0], list)
    assert len(results[0]) == 2
    print("[✅] givevariations")


def test_keep_original():
    """Test keeporiginal flag"""
    results = omission("lodash", [], False, math.inf, keeporiginal=True)
    assert len(results) > 0
    assert "lodash" in results
    print("[✅] keeporiginal")


def test_limit():
    """Test limit parameter"""
    results = runAll(
        package="lodash",
        ecosystem="npm",
        limit=10,
        verbose=False,
        givevariations=False,
        keeporiginal=False
    )
    assert len(results) <= 10
    print("[✅] limit")


# Run all tests
if __name__ == "__main__":
    tests = [
        test_omission,
        test_repetition,
        test_replacement,
        test_addition,
        test_change_order,
        test_strip_dash,
        test_strip_dash_no_dash,
        test_vowel_swap,
        test_add_dash,
        test_homoglyph,
        test_numeral_swap,
        test_numeral_swap_no_numbers,
        test_singular_pluralize,
        test_double_replacement,
        test_npm_suffix,
        test_npm_suffix_removal,
        test_npm_prefix,
        test_npm_prefix_removal,
        test_npm_scope_squat_scoped,
        test_npm_scope_squat_unscoped,
        test_npm_separator,
        test_npm_separator_no_sep,
        test_pypi_suffix,
        test_pypi_suffix_removal,
        test_pypi_prefix,
        test_pypi_prefix_removal,
        test_pypi_separator,
        test_pypi_version_suffix,
        test_run_all_npm,
        test_run_all_pypi,
        test_run_all_npm_scoped,
        test_give_variations,
        test_keep_original,
        test_limit,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"[❌] {test.__name__}: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")
    if failed > 0:
        exit(1)