import csv
import io
import json as json_lib
import os


def formatTrainingData(results_by_package, output_path, format="csv"):
    """Generate training data for embedding model typosquat detection.

    Produces anchor/positive pairs with technique labels, suitable for
    contrastive learning (e.g., training a custom embedding model).

    Args:
        results_by_package: list of (package_name, results) where results
            is a list of [variation, algorithm] pairs
        output_path: file path to write output, or "-" for stdout
        format: "csv" or "json"
    """
    rows = _results_to_rows(results_by_package)

    if format == "csv":
        _write_csv(rows, output_path)
    elif format == "json":
        _write_json(rows, output_path)


def appendTrainingData(results_by_package, output_path, format="csv"):
    """Incrementally save training data to a file.

    For CSV: appends rows, writing a header only if the file is new/empty.
    For JSON: rewrites the full file (reads existing rows first).

    Args:
        results_by_package: list of (package_name, results) for this batch
        output_path: file path to write output (cannot be "-"/stdout)
        format: "csv" or "json"
    """
    new_rows = _results_to_rows(results_by_package)
    if not new_rows:
        return

    if format == "csv":
        write_header = (
            not os.path.exists(output_path) or os.path.getsize(output_path) == 0
        )
        with open(output_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["anchor", "positive", "technique"])
            if write_header:
                writer.writeheader()
            writer.writerows(new_rows)
    elif format == "json":
        existing = []
        if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
            with open(output_path, "r", encoding="utf-8") as f:
                existing = json_lib.load(f)
        existing.extend(new_rows)
        with open(output_path, "w", encoding="utf-8") as f:
            json_lib.dump(existing, f, indent=2, ensure_ascii=False)


def _results_to_rows(results_by_package):
    """Convert results list to flat row dicts."""
    rows = []
    for package_name, variations in results_by_package:
        for variation in variations:
            if isinstance(variation, list) and len(variation) == 2:
                rows.append(
                    {
                        "anchor": package_name,
                        "positive": variation[0],
                        "technique": variation[1],
                    }
                )
    return rows


def _write_csv(rows, output_path):
    """Write training rows as CSV."""
    fieldnames = ["anchor", "positive", "technique"]

    if output_path == "-":
        writer = csv.DictWriter(
            io.TextIOWrapper(
                open(1, "wb", closefd=False), newline="", encoding="utf-8"
            ),
            fieldnames=fieldnames,
        )
        writer.writeheader()
        writer.writerows(rows)
    else:
        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


def _write_json(rows, output_path):
    """Write training rows as JSON array."""
    if output_path == "-":
        print(json_lib.dumps(rows, indent=2, ensure_ascii=False))
    else:
        with open(output_path, "w", encoding="utf-8") as f:
            json_lib.dump(rows, f, indent=2, ensure_ascii=False)
