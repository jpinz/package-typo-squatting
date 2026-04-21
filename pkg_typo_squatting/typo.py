# Import all the modules

## The public libraries
import json
import math
import os
import pathlib
import sys
import threading
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Manager

from tqdm import tqdm

sys.path.append(str(os.path.join(pathlib.Path(__file__).parent)))

## The local libraries
## The format function
from format.output import formatOutput
from format.training import appendTrainingData, formatTrainingData
from generator.addDash import addDash  # noqa: F401
from generator.addition import addition  # noqa: F401
from generator.changeOrder import changeOrder  # noqa: F401
from generator.closeLetters import closeLetters  # noqa: F401
from generator.commonMisspelling import commonMisspelling  # noqa: F401

## The common typo generators
from generator.const.main import *
from generator.doubleHit import doubleHit  # noqa: F401
from generator.doubleReplacement import doubleReplacement  # noqa: F401
from generator.homoglyph import homoglyph  # noqa: F401
from generator.homophones import homophones  # noqa: F401
from generator.npm.prefix import npmPrefix  # noqa: F401
from generator.npm.scope import npmScopeSquat  # noqa: F401
from generator.npm.separator import npmSeparator  # noqa: F401
from generator.npm.substitution import npmSubstitution  # noqa: F401

## npm-specific generators
from generator.npm.suffix import npmSuffix  # noqa: F401
from generator.numeralSwap import numeralSwap  # noqa: F401
from generator.omission import omission  # noqa: F401
from generator.pypi.prefix import pypiPrefix  # noqa: F401
from generator.pypi.separator import pypiSeparator  # noqa: F401
from generator.pypi.substitution import pypiSubstitution  # noqa: F401

## pypi-specific generators
from generator.pypi.suffix import pypiSuffix  # noqa: F401
from generator.pypi.version_suffix import pypiVersionSuffix  # noqa: F401
from generator.removeSeparatedSection import removeSeparatedSection  # noqa: F401
from generator.repetition import repetition  # noqa: F401
from generator.replacement import replacement  # noqa: F401
from generator.singularPluralize import singularPluralize  # noqa: F401
from generator.stripDash import stripDash  # noqa: F401
from generator.utils.generator_functions import (
    parse_package_name,
    reassemble_package_name,
)
from generator.vowelSwap import vowelSwap  # noqa: F401

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
    progress_queue=None,
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

    algo_iter = algo_list
    if verbose:
        algo_iter = tqdm(
            algo_list,
            desc=package,
            unit="algo",
            leave=False,
            file=sys.stderr,
        )

    for algo in algo_iter:
        if verbose:
            algo_iter.set_postfix_str(algo)
        if progress_queue is not None:
            progress_queue.put((package, "algo_start", algo))

        func = globals()[algo]
        if algo in common_algo_list and scope:
            # For scoped npm packages, run common algos on name part, then reassemble
            name_results = list()
            name_results = func(
                name, name_results, False, limit, givevariations, keeporiginal
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
                        False,
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
                        False,
                        limit,
                        givevariations,
                        keeporiginal,
                        all=all_homoglyph,
                    )
            else:
                resultList = func(
                    package, resultList, False, limit, givevariations, keeporiginal
                )

        if progress_queue is not None:
            progress_queue.put((package, "algo_done", algo))

    if verbose:
        tqdm.write(f"Total: {len(resultList)}", file=sys.stderr)

    if formatoutput and pathOutput:
        formatOutput(formatoutput, resultList, package, pathOutput, givevariations)

    return resultList


def _run_package(
    package,
    ecosystem,
    limit,
    givevariations,
    keeporiginal,
    all_homoglyph,
    mode,
    selected_algos,
    progress_queue=None,
):
    """Process a single package. Designed to run in a worker process."""
    package = package.strip()
    if not package:
        return (package, [])

    if mode == "all":
        algo_count = len(get_algo_list(ecosystem))
    else:
        algo_count = len(selected_algos)

    if progress_queue is not None:
        progress_queue.put((package, "start", algo_count))

    resultList = list()

    if mode == "all":
        resultList = runAll(
            package=package,
            ecosystem=ecosystem,
            limit=limit,
            verbose=False,
            givevariations=givevariations,
            keeporiginal=keeporiginal,
            all_homoglyph=all_homoglyph,
            progress_queue=progress_queue,
        )
    elif mode == "combo":
        base_result = list()
        for algo in selected_algos:
            if progress_queue is not None:
                progress_queue.put((package, "algo_start", algo))
            func = globals()[algo]
            if not base_result:
                if algo == "homoglyph":
                    base_result = func(
                        package,
                        resultList,
                        False,
                        limit,
                        givevariations,
                        keeporiginal,
                        all=all_homoglyph,
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
            else:
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
                            all=all_homoglyph,
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
            if progress_queue is not None:
                progress_queue.put((package, "algo_done", algo))
    else:
        for algo in selected_algos:
            if progress_queue is not None:
                progress_queue.put((package, "algo_start", algo))
            func = globals()[algo]
            if algo == "homoglyph":
                resultList = func(
                    package,
                    resultList,
                    False,
                    limit,
                    givevariations,
                    keeporiginal,
                    all=all_homoglyph,
                )
            else:
                resultList = func(
                    package,
                    resultList,
                    False,
                    limit,
                    givevariations,
                    keeporiginal,
                )
            if progress_queue is not None:
                progress_queue.put((package, "algo_done", algo))

    if progress_queue is not None:
        progress_queue.put((package, "done", len(resultList)))

    return (package, resultList)


def _progress_listener(queue, worker_bars):
    """Background thread that reads worker progress messages and updates per-worker bars."""
    slot_map = {}  # package_name -> bar_index
    free_slots = list(range(len(worker_bars)))

    while True:
        msg = queue.get()
        if msg is None:
            break

        package, event, data = msg

        if event == "start":
            if free_slots:
                slot = free_slots.pop(0)
            else:
                continue
            slot_map[package] = slot
            bar = worker_bars[slot]
            bar.bar_format = (
                "  {desc}: {percentage:3.0f}%|{bar:20}| {n_fmt}/{total_fmt} [{postfix}]"
            )
            bar.reset(total=data)
            bar.set_description(package)
            bar.refresh()
        elif event == "algo_start":
            if package in slot_map:
                worker_bars[slot_map[package]].set_postfix_str(data)
        elif event == "algo_done":
            if package in slot_map:
                worker_bars[slot_map[package]].update(1)
        elif event == "done":
            if package in slot_map:
                slot = slot_map.pop(package)
                bar = worker_bars[slot]
                bar.bar_format = "{desc}"
                bar.set_description("")
                bar.clear()
                free_slots.append(slot)


def main():
    # Step 1: Get the arguments
    parser = getArguments()
    args = parser.parse_args()

    # Step 2: Assign some variables
    verbose = args.v
    givevariations = args.givevariations
    keeporiginal = args.keeporiginal
    ecosystem = args.ecosystem
    training_mode = args.training

    # Training mode forces givevariations to get technique labels
    if training_mode:
        givevariations = True

    limit = math.inf
    if args.limit:
        limit = int(args.limit)

    pathOutput = args.output

    if pathOutput and not pathOutput == "-" and not training_mode:
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
            if args.filepackageName.endswith(".json"):
                packageList = json.load(read_file)
            else:
                packageList = [
                    line.strip() for line in read_file.readlines() if line.strip()
                ]
    else:
        print("[-] No Entry")
        parser.print_help()
        exit(-1)

    # Step 4: Determine processing mode and selected algorithms
    if args.combo:
        mode = "combo"
    elif args.all:
        mode = "all"
    else:
        mode = "individual"

    selected_algos = []
    if mode in ("combo", "individual"):
        algo_list = get_algo_list(ecosystem)
        for arg in vars(args):
            for algo in algo_list:
                if algo.lower() == arg and getattr(args, arg):
                    selected_algos.append(algo)

    workers = args.workers if args.workers is not None else os.cpu_count() or 1
    total_packages = len(packageList)
    workers = min(workers, total_packages)

    # Step 5: Process packages
    training_results = []
    total_squats = 0

    run_args = [
        (
            pkg,
            ecosystem,
            limit,
            givevariations,
            keeporiginal,
            args.all_homoglyph,
            mode,
            selected_algos,
        )
        for pkg in packageList
    ]

    if workers > 1:
        manager = Manager()
        progress_queue = manager.Queue()

        overall_bar = tqdm(
            total=total_packages,
            desc="Overall",
            position=0,
            unit="pkg",
            file=sys.stderr,
        )
        worker_bars = [
            tqdm(
                total=0,
                position=i + 1,
                bar_format="{desc}",
                leave=False,
                file=sys.stderr,
            )
            for i in range(workers)
        ]

        listener = threading.Thread(
            target=_progress_listener,
            args=(progress_queue, worker_bars),
            daemon=True,
        )
        listener.start()

        executor = ProcessPoolExecutor(max_workers=workers)
        futures = {
            executor.submit(_run_package, *a, progress_queue): a[0] for a in run_args
        }

        try:
            for future in as_completed(futures):
                package, resultList = future.result()
                overall_bar.update(1)

                if not package:
                    continue

                total_squats += len(resultList)
                overall_bar.set_postfix(squats=total_squats)

                if training_mode:
                    training_results.append((package, resultList))
                    training_output = pathOutput if pathOutput else "-"
                    if training_output != "-" and len(training_results) >= 50:
                        appendTrainingData(
                            training_results,
                            training_output,
                            args.training_format,
                        )
                        training_results = []
                else:
                    formatOutput(
                        formatoutput,
                        resultList,
                        package,
                        pathOutput,
                        givevariations,
                        args.betterregex,
                    )
        finally:
            progress_queue.put(None)
            listener.join(timeout=5)
            executor.shutdown(wait=False)
            for bar in worker_bars:
                bar.close()
            manager.shutdown()

        overall_bar.set_description("Done")
        overall_bar.set_postfix(squats=total_squats)
        overall_bar.close()

    else:
        # Single worker: simple sequential processing with per-algo progress
        pkg_bar = tqdm(
            total=total_packages,
            desc="Processing",
            unit="pkg",
            file=sys.stderr,
        )

        for args_tuple in run_args:
            package, resultList = _run_package(*args_tuple)
            pkg_bar.set_description(package or "skip")
            pkg_bar.update(1)

            if not package:
                continue

            if verbose:
                tqdm.write(f"{package}: {len(resultList)} variations", file=sys.stderr)

            total_squats += len(resultList)
            pkg_bar.set_postfix(squats=total_squats)

            if training_mode:
                training_results.append((package, resultList))
                training_output = pathOutput if pathOutput else "-"
                if training_output != "-" and len(training_results) >= 50:
                    appendTrainingData(
                        training_results, training_output, args.training_format
                    )
                    training_results = []
            else:
                formatOutput(
                    formatoutput,
                    resultList,
                    package,
                    pathOutput,
                    givevariations,
                    args.betterregex,
                )

        pkg_bar.set_description("Done")
        pkg_bar.set_postfix(squats=total_squats)
        pkg_bar.close()

    # Step 6: Write training data if in training mode
    if training_mode:
        training_output = pathOutput if pathOutput else "-"
        if training_output == "-":
            # Stdout: write everything at once
            formatTrainingData(training_results, training_output, args.training_format)
        elif training_results:
            # Flush remaining buffered results to file
            appendTrainingData(training_results, training_output, args.training_format)


# Main file function
if __name__ == "__main__":
    main()
