"""Mini-project: summarize Iris measurements by variety."""

from pathlib import Path

import pandas as pd


DAY_DIRECTORY = Path(__file__).parent.parent
DATA_PATH = DAY_DIRECTORY / "data" / "iris_sample.csv"

iris = pd.read_csv(DATA_PATH)
measurement_columns = [
    "sepal.length",
    "sepal.width",
    "petal.length",
    "petal.width",
]

print("\nDataset shape:", iris.shape)
print("Varieties:", sorted(iris["variety"].unique()))
print("Missing values:", int(iris.isna().sum().sum()))

# here we group the dataset by variety and calculate the count and mean of each measurement.
species_summary = (
    iris.groupby("variety")[measurement_columns]
    .agg(["count", "mean"])
    .round(2)
)

print("\n\nIris variety summary:\n", species_summary)

# here we find the name of the variety (the index label) that has the highest average petal length.
largest_average_petals = (
    iris.groupby("variety")["petal.length"].mean().idxmax()
)
print("\n\nVariety with the largest average petals:", largest_average_petals)

