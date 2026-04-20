# Import all the modules

## The public libraries
import math
import os
import pathlib
import sys

sys.path.append(str(os.path.join(pathlib.Path(__file__).parent)))

## The local libraries
## The format function
from format.output import formatOutput

## The common typo generators
from generator.const.main import *

## npm-specific generators
## pypi-specific generators
from generator.utils.generator_functions import (
    parse_package_name,
    reassemble_package_name,
)

## The utils
from utils.parser import getArguments

# Import all the constants
common_algo_list = const_get_common_algo_list()
npm_algo_list = const_get_npm_algo_list()
pypi_algo_list = const_get_pypi_algo_list()


def get_algo_list(ecosystem):
    """Get the full list of algorithms for a given ecosystem"""
    if ecosystem == "npm":
        return common_algo_list + npm_algo_list
    elif ecosystem == "pypi":
        return common_algo_list + pypi_algo_list
    else:
        return common_algo_list


def runAll(
    package,
    ecosystem,
    limit,
    formatoutput=None,
    pathOutput=None,
    verbose=False,
    givevariations=False,
    keeporiginal=False,
    all_homoglyph=False,
):
    """Run all algorithms for the given ecosystem on the package name.

    Args:
        package: Package name (e.g., 'lodash', '@babel/core', 'requests')
        ecosystem: 'npm' or 'pypi'
        limit: Maximum number of variations
        formatoutput: Output format ('text', 'json', 'regex', 'yaml')
        pathOutput: Path for output file
        verbose: Print progress information
        givevariations: Include algorithm name with each variation
        keeporiginal: Keep original package name in results
        all_homoglyph: Generate all homoglyph permutations
    """

    resultList = list()
    algo_list = get_algo_list(ecosystem)

    # For npm scoped packages, run common generators on the name part
    scope, name = parse_package_name(package, ecosystem)

    for algo in algo_list:
        func = globals()[algo]
        if algo in common_algo_list and scope:
            # For scoped npm packages, run common algos on name part, then reassemble
            name_results = list()
            name_results = func(
                name, name_results, verbose, limit, givevariations, keeporiginal
            )

            # Reassemble with scope
            for result in name_results:
                if givevariations:
                    scoped_result = [
                        reassemble_package_name(scope, result[0]),
                        result[1],
                    ]
                    if scoped_result not in resultList:
                        resultList.append(scoped_result)
                else:
                    scoped_result = reassemble_package_name(scope, result)
                    if scoped_result not in resultList:
                        resultList.append(scoped_result)
        else:
            if algo == "homoglyph":
                if scope:
                    name_results = list()
                    name_results = func(
                        name,
                        name_results,
                        verbose,
                        limit,
                        givevariations,
                        keeporiginal,
                        all=all_homoglyph,
                    )
                    for result in name_results:
                        if givevariations:
                            scoped_result = [
                                reassemble_package_name(scope, result[0]),
                                result[1],
                            ]
                            if scoped_result not in resultList:
                                resultList.append(scoped_result)
                        else:
                            scoped_result = reassemble_package_name(scope, result)
                            if scoped_result not in resultList:
                                resultList.append(scoped_result)
                else:
                    resultList = func(
                        package,
                        resultList,
                        verbose,
                        limit,
                        givevariations,
                        keeporiginal,
                        all=all_homoglyph,
                    )
            else:
                resultList = func(
                    package, resultList, verbose, limit, givevariations, keeporiginal
                )

    if verbose:
        print(f"Total: {len(resultList)}")

    if formatoutput and pathOutput:
        formatOutput(formatoutput, resultList, package, pathOutput, givevariations)

    return resultList


def main():
    # Step 1: Get the arguments
    parser = getArguments()
    args = parser.parse_args()

    resultList = list()

    # Step 2: Assign some variables
    verbose = args.v
    givevariations = args.givevariations
    keeporiginal = args.keeporiginal
    ecosystem = args.ecosystem

    limit = math.inf
    if args.limit:
        limit = int(args.limit)

    pathOutput = args.output

    if pathOutput and not pathOutput == "-":
        try:
            os.makedirs(pathOutput)
        except:
            pass

    # Step 3: Check the format output
    if args.formatoutput:
        if args.formatoutput in ["text", "json", "yaml", "regex"]:
            formatoutput = args.formatoutput
        else:
            print("[-] Format type error")
            exit(-1)
    else:
        formatoutput = "text"

    # Verify that a package name is received
    if args.packageName:
        packageList = args.packageName
    elif args.filepackageName:
        with open(args.filepackageName, "r") as read_file:
            packageList = [
                line.strip() for line in read_file.readlines() if line.strip()
            ]
    else:
        print("[-] No Entry")
        parser.print_help()
        exit(-1)

    # Step 4: Process each package
    for package in packageList:
        package = package.strip()
        if not package:
            continue

        if pathOutput:
            print(f"\n\t[*****] {package} ({ecosystem}) [*****]")

        # Determine which algorithms to run
        if args.combo:
            base_result = list()
            algo_list = get_algo_list(ecosystem)
            for arg in vars(args):
                for algo in algo_list:
                    if algo.lower() == arg:
                        if getattr(args, arg):
                            if verbose:
                                print(f"[+] {algo}")

                            func = globals()[algo]
                            # First Iteration
                            if not base_result:
                                if algo == "homoglyph":
                                    base_result = func(
                                        package,
                                        resultList,
                                        False,
                                        limit,
                                        givevariations,
                                        keeporiginal,
                                        all=args.all_homoglyph,
                                    )
                                else:
                                    base_result = func(
                                        package,
                                        resultList,
                                        False,
                                        limit,
                                        givevariations,
                                        keeporiginal,
                                    )
                                resultList = base_result.copy()

                                if verbose:
                                    print(f"{len(resultList)}\n")
                            else:
                                loc_result = list()
                                loc_result = base_result.copy()
                                for r in loc_result:
                                    if type(r) == list:
                                        r = r[0]

                                    if algo == "homoglyph":
                                        loc_result = func(
                                            r,
                                            loc_result,
                                            False,
                                            limit,
                                            givevariations,
                                            keeporiginal,
                                            all=args.all_homoglyph,
                                            combo=True,
                                        )
                                    else:
                                        loc_result = func(
                                            r,
                                            loc_result,
                                            False,
                                            limit,
                                            givevariations,
                                            keeporiginal,
                                            True,
                                        )
                                resultList = resultList + loc_result
                                base_result = loc_result

                                if verbose:
                                    print(f"{len(loc_result)}\n")
        elif args.all:
            resultList = runAll(
                package=package,
                ecosystem=ecosystem,
                limit=limit,
                formatoutput=None,
                pathOutput=None,
                verbose=verbose,
                givevariations=givevariations,
                keeporiginal=keeporiginal,
                all_homoglyph=args.all_homoglyph,
            )
        else:
            algo_list = get_algo_list(ecosystem)
            for arg in vars(args):
                for algo in algo_list:
                    if algo.lower() == arg:
                        if getattr(args, arg):
                            func = globals()[algo]
                            if algo == "homoglyph":
                                resultList = func(
                                    package,
                                    resultList,
                                    verbose,
                                    limit,
                                    givevariations,
                                    keeporiginal,
                                    all=args.all_homoglyph,
                                )
                            else:
                                resultList = func(
                                    package,
                                    resultList,
                                    verbose,
                                    limit,
                                    givevariations,
                                    keeporiginal,
                                )

        # Step 5: Final treatment
        if verbose:
            print(f"Total: {len(resultList)}")

        formatOutput(
            formatoutput,
            resultList,
            package,
            pathOutput,
            givevariations,
            args.betterregex,
        )

        resultList = list()


# Main file function
if __name__ == "__main__":
    main()
