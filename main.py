"""
main.py
Student Performance Analytics System
Runs the full pipeline: load -> process -> analyse -> display -> save.
"""

import os
import pandas as pd
import functions as fn

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 20)

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_results.csv")


def heading(title):
    """Print a neat section heading."""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 1: Load and inspect
    heading("1. DATASET OVERVIEW")
    df = fn.load_data(DATA_FILE)
    fn.check_data(df)
    print("\nFirst 5 records:")
    print(df.head().to_string(index=False))

    # Step 2: Process
    df = fn.process_data(df)
    heading("2. STUDENT RESULTS (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result", "Rank"]]
          .to_string(index=False))

    # Step 3: Class statistics
    stats = fn.class_statistics(df)
    heading("3. CLASS PERFORMANCE")
    print(f"Highest average : {stats['highest_name']} ({stats['highest_avg']})")
    print(f"Lowest average  : {stats['lowest_name']} ({stats['lowest_avg']})")
    print(f"Class average   : {stats['class_average']}")
    print(f"Median average  : {stats['median_average']}")
    print(f"Std deviation   : {stats['std_dev']}")

    # Step 4: Pass / fail
    pf = fn.pass_fail_statistics(df)
    heading("4. PASS / FAIL STATISTICS")
    print(f"Total students : {pf['total']}")
    print(f"Passed         : {pf['passed']}")
    print(f"Failed         : {pf['failed']}")
    print(f"Pass percentage: {pf['pass_percentage']}%")
    print("\nFailed students:")
    print(fn.failed_students(df).to_string(index=False))

    # Step 5: Grades
    heading("5. GRADE DISTRIBUTION")
    for grade, count in fn.grade_distribution(df).items():
        print(f"Grade {grade:<2}: {'#' * count} ({count})")

    # Step 6: Subject-wise
    heading("6. SUBJECT-WISE ANALYSIS")
    subj = fn.subject_analysis(df)
    print(subj.to_string(index=False))
    print(f"\nBest subject (highest average)  : {subj.iloc[0]['Subject']} ({subj.iloc[0]['Average']})")
    print(f"Weakest subject (lowest average): {subj.iloc[-1]['Subject']} ({subj.iloc[-1]['Average']})")

    # Step 7: Department-wise
    heading("7. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df))

    # Step 8: Top performers
    heading("8. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string(index=False))

    # Step 9: Attendance
    heading("9. ATTENDANCE INSIGHTS")
    low = df[df["Attendance_Status"] == "Low"]
    print(f"Students with attendance below {fn.MIN_ATTENDANCE}%: {len(low)}")
    if len(low):
        print(low[["Student_ID", "Name", "Attendance", "Average"]].to_string(index=False))
    print(f"\nCorrelation between attendance and average marks: {fn.attendance_vs_marks(df)}")

    # Step 10: Save
    df.to_csv(OUTPUT_FILE, index=False)
    heading("DONE")
    print(f"Detailed results saved to: {os.path.basename(OUTPUT_FILE)}")


if __name__ == "__main__":
    main()
