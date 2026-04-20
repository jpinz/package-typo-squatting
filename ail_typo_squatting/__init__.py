from ail_typo_squatting.typo import runAll

from ail_typo_squatting.typo import formatOutput

from ail_typo_squatting.typo import omission
from ail_typo_squatting.typo import repetition
from ail_typo_squatting.typo import changeOrder
from ail_typo_squatting.typo import replacement
from ail_typo_squatting.typo import doubleReplacement
from ail_typo_squatting.typo import addition
from ail_typo_squatting.typo import stripDash
from ail_typo_squatting.typo import vowelSwap
from ail_typo_squatting.typo import addDash
from ail_typo_squatting.typo import homoglyph
from ail_typo_squatting.typo import commonMisspelling
from ail_typo_squatting.typo import homophones
from ail_typo_squatting.typo import singularPluralize
from ail_typo_squatting.typo import numeralSwap

# npm-specific generators
from ail_typo_squatting.typo import npmSuffix
from ail_typo_squatting.typo import npmPrefix
from ail_typo_squatting.typo import npmScopeSquat
from ail_typo_squatting.typo import npmSeparator

# pypi-specific generators
from ail_typo_squatting.typo import pypiSuffix
from ail_typo_squatting.typo import pypiPrefix
from ail_typo_squatting.typo import pypiSeparator
from ail_typo_squatting.typo import pypiVersionSuffix

from ail_typo_squatting.generator.utils.generator_functions import parse_package_name
