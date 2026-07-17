# Crash-course practice: add, transform, and export columns.

from pathlib import Path

import pandas as pd


DAY_DIRECTORY = Path(__file__).parents[2]
DATA_PATH = DAY_DIRECTORY / "data" / "iris_sample.csv"
OUTPUT_DIRECTORY = DAY_DIRECTORY / "outputs"


def square(value: float) -> float:
    # Return a squared measurement.
    return value**2


iris = pd.read_csv(DATA_PATH)

# Add reviewed column using broadcast for every row.
iris["reviewed"] = False

# Add sepal area using vectorized arithmetic.
iris["sepal.area"] = iris["sepal.length"] * iris["sepal.width"]

# Use apply() when a reusable custom function is needed.
iris["sepal.length.squared"] = iris["sepal.length"].apply(square)

print(
    iris[
        [
            "variety",
            "sepal.length",
            "reviewed",
            "sepal.area",
            "sepal.length.squared",
        ]
    ].head()
)

# Create output directory if it does not exist.
OUTPUT_DIRECTORY.mkdir(exist_ok=True)
output_path = OUTPUT_DIRECTORY / "iris_new.csv"

# index=False avoids adding the DataFrame index as an extra CSV column.
iris.to_csv(output_path, index=False)
print("\nExported data to:", output_path)

