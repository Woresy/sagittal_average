from pathlib import Path

import numpy as np

from sagittal_brain import run_averages

TEST_DIR = Path(__file__).resolve().parent


def test_run_averages_last_row_is_one():
    data_input = np.zeros((20, 20), dtype=int)
    data_input[-1, :] = 1

    input_path = TEST_DIR / "brain_sample.csv"
    np.savetxt(input_path, data_input, fmt="%d", delimiter=",")

    expected = np.zeros(20, dtype=float)
    expected[-1] = 1.0

    output_path = TEST_DIR / "brain_average.csv"
    run_averages(
        file_input=str(input_path),
        file_output=str(output_path),
    )

    result = np.loadtxt(output_path, delimiter=",")

    np.testing.assert_array_equal(result, expected)
