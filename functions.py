"""
functions.py
Reusable functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------
# Configuration (grading rule and pass condition)
# ---------------------------------------------------------------
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]
SUBJECT_PASS_MARK = 35      # minimum marks needed in EVERY subject
MIN_ATTENDANCE = 75         # minimum attendance % (informational flag)

# Grading rule based on average marks: (minimum average, grade)
GRADE_RULES = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (40, "E"),
]
FAIL_GRADE = "F"


# ---------------------------------------------------------------
# Loading and inspection
# ---------------------------------------------------------------
def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def check_data(df):
    """Print basic information about the dataset."""
    print(f"Number of records : {df.shape[0]}")
    print(f"Number of columns : {df.shape[1]}")
    print(f"Columns           : {', '.join(df.columns)}")
    print(f"Missing values    : {int(df.isnull().sum().sum())}")
    print(f"Duplicate IDs     : {int(df['Student_ID'].duplicated().sum())}")


# ---------------------------------------------------------------
# Processing
# ---------------------------------------------------------------
def calculate_total_and_average(df, subjects=SUBJECTS):
    """Add Total and Average columns using NumPy."""
    marks = df[subjects].to_numpy()                     # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)                 # row-wise sum
    df["Average"] = np.round(np.mean(marks, axis=1), 2) # row-wise mean
    return df


def assign_grade(average):
    """Return a grade for a given average using GRADE_RULES."""
    for min_avg, grade in GRADE_RULES:
        if average >= min_avg:
            return grade
    return FAIL_GRADE


def add_grades(df):
    """Loop over every student and assign a grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df


def check_pass_fail(row, subjects=SUBJECTS):
    """A student passes only if marks >= SUBJECT_PASS_MARK in every subject."""
    for subject in subjects:
        if row[subject] < SUBJECT_PASS_MARK:
            return "Fail"
    return "Pass"


def add_pass_fail(df):
    """Add Result column (Pass/Fail). A failed student also gets grade F."""
    df["Result"] = df.apply(check_pass_fail, axis=1)
    df.loc[df["Result"] == "Fail", "Grade"] = FAIL_GRADE
    return df


def add_attendance_status(df):
    """Flag students below the minimum attendance requirement."""
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "OK", "Low")
    return df


def process_data(df):
    """Run the complete processing pipeline."""
    df = calculate_total_and_average(df)
    df = add_grades(df)
    df = add_pass_fail(df)
    df = add_attendance_status(df)
    df["Rank"] = df["Total"].rank(method="min", ascending=False).astype(int)
    return df


# ---------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------
def class_statistics(df):
    """Highest, lowest and average performance of the class."""
    best = df.loc[df["Average"].idxmax()]
    worst = df.loc[df["Average"].idxmin()]
    return {
        "highest_name": best["Name"],
        "highest_avg": best["Average"],
        "lowest_name": worst["Name"],
        "lowest_avg": worst["Average"],
        "class_average": round(float(np.mean(df["Average"])), 2),
        "median_average": round(float(np.median(df["Average"])), 2),
        "std_dev": round(float(np.std(df["Average"])), 2),
    }


def pass_fail_statistics(df):
    """Count of passed/failed students and pass percentage."""
    total = len(df)
    passed = int((df["Result"] == "Pass").sum())
    failed = total - passed
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_percentage": round(passed / total * 100, 2),
    }


def grade_distribution(df):
    """Number of students in each grade (in rule order)."""
    order = [g for _, g in GRADE_RULES] + [FAIL_GRADE]
    counts = df["Grade"].value_counts()
    return pd.Series({g: int(counts.get(g, 0)) for g in order})


def subject_analysis(df, subjects=SUBJECTS):
    """Subject-wise average, highest, lowest and pass percentage."""
    rows = []
    for subject in subjects:                     # loop through each subject
        col = df[subject].to_numpy()
        top_student = df.loc[df[subject].idxmax(), "Name"]
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(col)), 2),
            "Highest": int(np.max(col)),
            "Lowest": int(np.min(col)),
            "Topper": top_student,
            "Pass_%": round(float(np.mean(col >= SUBJECT_PASS_MARK) * 100), 1),
        })
    return pd.DataFrame(rows).sort_values("Average", ascending=False).reset_index(drop=True)


def department_analysis(df):
    """Department-wise performance using Pandas groupby."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
        Passed=("Result", lambda r: int((r == "Pass").sum())),
    ).round(2)
    return summary.sort_values("Avg_Marks", ascending=False)


def top_performers(df, n=5):
    """Return the top n students by total marks."""
    cols = ["Rank", "Student_ID", "Name", "Department", "Total", "Average", "Grade"]
    return df.sort_values("Total", ascending=False).head(n)[cols]


def failed_students(df):
    """Students who did not pass."""
    return df[df["Result"] == "Fail"][["Student_ID", "Name", "Department", "Average"]]


def attendance_vs_marks(df):
    """Correlation between attendance and average marks (NumPy)."""
    return round(float(np.corrcoef(df["Attendance"], df["Average"])[0, 1]), 3)
