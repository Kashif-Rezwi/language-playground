# Exercise: clean a small student dataset with Pandas.

import pandas as pd


raw_students = pd.DataFrame(
    {
        "student_name": ["  kashif", "THAMIZH ", None, "ken", "  zoya  "],
        "marks": ["53", "70", "unknown", None, "88"],
        "city": ["kolkata", "CHENNAI", "Mumbai", None, "delhi"],
    }
)

print("Raw data:\n", raw_students)
print("\n\nMissing values before cleanup:\n", raw_students.isna().sum())

# here we drop the rows that have missing values in the student_name column.
clean_students = raw_students.dropna(subset=["student_name"]).copy()

clean_students["student_name"] = clean_students["student_name"].str.strip().str.title()
clean_students["city"] = clean_students["city"].fillna("Unknown").str.title()

# here we convert the marks column to numeric type and fill the missing values with the median marks.
clean_students["marks"] = pd.to_numeric(clean_students["marks"], errors="coerce")
median_marks = clean_students["marks"].median()
clean_students["marks"] = clean_students["marks"].fillna(median_marks).astype("Int64")

clean_students["result"] = clean_students["marks"].ge(60).map(
    {True: "Pass", False: "Fail"}
)

print("\n\nCleaned data:\n", clean_students)
print("\n\nCleaned data types:\n", clean_students.dtypes)
print("\n\nMissing values after cleanup:\n", clean_students.isna().sum())

