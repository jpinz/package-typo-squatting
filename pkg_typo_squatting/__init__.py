from pkg_typo_squatting.typo import runAll

from pkg_typo_squatting.typo import formatOutput

from pkg_typo_squatting.typo import omission
from pkg_typo_squatting.typo import repetition
from pkg_typo_squatting.typo import changeOrder
from pkg_typo_squatting.typo import replacement
from pkg_typo_squatting.typo import doubleReplacement
from pkg_typo_squatting.typo import addition
from pkg_typo_squatting.typo import stripDash
from pkg_typo_squatting.typo import vowelSwap
from pkg_typo_squatting.typo import addDash
from pkg_typo_squatting.typo import homoglyph
from pkg_typo_squatting.typo import commonMisspelling
from pkg_typo_squatting.typo import homophones
from pkg_typo_squatting.typo import singularPluralize
from pkg_typo_squatting.typo import numeralSwap

# npm-specific generators
from pkg_typo_squatting.typo import npmSuffix
from pkg_typo_squatting.typo import npmPrefix
from pkg_typo_squatting.typo import npmScopeSquat
from pkg_typo_squatting.typo import npmSeparator

# pypi-specific generators
from pkg_typo_squatting.typo import pypiSuffix
from pkg_typo_squatting.typo import pypiPrefix
from pkg_typo_squatting.typo import pypiSeparator
from pkg_typo_squatting.typo import pypiVersionSuffix

from pkg_typo_squatting.generator.utils.generator_functions import parse_package_name
