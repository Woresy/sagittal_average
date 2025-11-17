from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np


def run_averages(file_input: str = "brain_sample.csv",
                 file_output: str = "brain_average.csv") -> None:
    """
    Calculates the average through the coronal planes.

    The input file should have as many columns as coronal planes.
    The rows are intersections of the sagittal/horizontal planes.

    The result is the average for each sagittal/horizontal plane (rows),
    written as a single-row CSV.
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int, delimiter=",")

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    averages = planes.mean(axis=1)[np.newaxis, :]

    # Write it out to the output file
    np.savetxt(file_output, averages, fmt="%.1f", delimiter=",")


def build_arg_parser() -> ArgumentParser:
    """Build the CLI argument parser for this tool."""
    parser = ArgumentParser(
        description="Calculates the average for each sagittal-horizontal plane.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "file_input",
        nargs="?",
        default="brain_sample.csv",
        help=(
            "Input CSV file with the results from the scikit-brain "
            "binning algorithm."
        ),
    )
    parser.add_argument(
        "--file_output",
        "-o",
        default="brain_average.csv",
        help="Name of the output CSV file.",
    )
    return parser


def main() -> None:
    """Entry point for the command-line interface."""
    parser = build_arg_parser()
    args = parser.parse_args()
    run_averages(args.file_input, args.file_output)


if __name__ == "__main__":
    main()
