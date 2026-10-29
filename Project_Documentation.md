# Project Documentation

## 1. Project Title
**Student Performance Analytics System**

- Student Name: Aryan Shukla
- Course: Python with AI – EWB Courses
- Submission Date: 29th October 2026.\.venv\Scripts\python.exe -m pip install -r requirements.txt

## 2. Objective
Teachers often hold student marks in spreadsheets and have to work out totals, grades and pass/fail status by hand. This is slow and easy to get wrong. This project automates that work. It reads student records from a CSV file and calculates totals, averages, grades and pass/fail results. It also produces subject-wise, department-wise and top-performer analysis, so a class's performance can be understood at a glance.

## 3. Technologies Used
| Tool | Purpose |
|------|---------|
| Python 3 | Core language (variables, data types, loops, functions, conditions) |
| NumPy | Numerical calculations (sum, mean, median, std, max, min, correlation) |
| Pandas | Loading the CSV, DataFrame operations, filtering, sorting, groupby |

## 4. Dataset Description
`students.csv` contains **20 student records** and **9 columns**:

| Column | Description |
|--------|-------------|
| Student_ID | Unique ID (S101–S120) |
| Name | Student name |
| Department | Computer Science, Electronics, Mechanical or Civil |
| Maths, Physics, Chemistry, English, Computer_Science | Marks out of 100 |
| Attendance | Attendance percentage |

The data was created for this project and covers a realistic spread: high scorers, average students and a few weak students.

## 5. Implementation

**Step 1 – Load the data.** `load_data()` reads `students.csv` into a Pandas DataFrame. `check_data()` prints the number of records and columns, missing values and duplicate IDs.

**Step 2 – Total and average.** `calculate_total_and_average()` converts the subject columns to a NumPy array with `.to_numpy()`. It then uses `np.sum(axis=1)` and `np.mean(axis=1)` to get each student's total and average.

**Step 3 – Grading rule.** `assign_grade()` applies the following rule to the average, using a loop over a rules list:

| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 – 89.99 | A |
| 70 – 79.99 | B |
| 60 – 69.99 | C |
| 50 – 59.99 | D |
| 40 – 49.99 | E |
| Below 40, or failed | F |

**Step 4 – Pass/fail condition.** A student **passes only if they score at least 35 in every subject**. `check_pass_fail()` loops through the subjects and returns "Fail" at the first subject below 35. A failed student is given grade F. A student can therefore have a decent average and still fail because of one weak subject.

**Step 5 – Extra columns.** `np.where()` flags attendance below 75%, and Pandas `rank()` gives each student a rank by total marks.

**Step 6 – Analysis.**
- `class_statistics()` finds the highest, lowest, average, median and standard deviation of the averages.
- `pass_fail_statistics()` finds the pass count, fail count and pass percentage.
- `grade_distribution()` counts students per grade.
- `subject_analysis()` loops over subjects and reports each one's average, highest, lowest, topper and pass percentage.
- `department_analysis()` uses Pandas `groupby().agg()`.
- `top_performers()` sorts by total marks.
- `attendance_vs_marks()` uses `np.corrcoef()` to find the correlation.

**Step 7 – Output.** `main.py` calls all of these functions, prints a labelled report and saves the full results to `student_results.csv`.

## 6. Key Features
- Reusable functions kept in `functions.py`, with the report logic in `main.py`
- Configurable grading rule and pass mark, defined as constants at the top of `functions.py`
- Automatic total, average, grade, result and rank for every student
- Class, subject-wise and department-wise analysis
- Top 5 performers and a list of failed students
- Attendance check and attendance-vs-marks correlation
- Exports a results file (`student_results.csv`)

## 7. Output / Screenshots
The complete program output is also saved in `output.txt`.

**Dataset overview**
![Dataset overview](screenshots/01_dataset_overview.png)

**Student results**
![Student results](screenshots/02_student_results.png)

**Class performance and pass/fail statistics**
![Class and pass/fail](screenshots/03_class_and_pass_fail.png)

**Grade distribution and subject-wise analysis**
![Grades and subjects](screenshots/04_grades_and_subjects.png)

**Department analysis and top performers**
![Department and top performers](screenshots/05_department_and_top_performers.png)

**Attendance insights**
![Attendance insights](screenshots/06_attendance_insights.png)

Sample results:
- Highest average: **Sneha Patel (93.2)**
- Lowest average: Deepak Kumar (41.2)
- Class average: **70.06**
- Passed: **18 / 20 (90%)**
- Best subject: **English (73.35)**
- Best department: **Computer Science (82.93)**

## 8. Final Outcome
The system runs without errors and answers the questions set in the assignment: the student with the highest average, the best subject, the number of students who passed, and the overall class average. The output is labelled and readable without opening the code. Two further patterns show up in the data. Attendance is strongly linked to marks (correlation ≈ 0.99), and all 5 students with attendance below 75% are the weakest performers.

## 9. Challenges & Learning
- **Pass/fail vs. grade:** Two students (Arjun Reddy and Siddharth Rao) have the same average (42.2) but different results. Arjun scored 33 in Maths, so he fails, while Siddharth scored at least 35 in every subject, so he passes. Defining the pass rule per subject made this clear, and I documented it so the result is not mistaken for an error.
- **Ties in ranking:** Students with equal totals needed a rule. I used `rank(method="min")`, so tied students share the same rank.
- **Choosing NumPy vs. Pandas:** I used NumPy for the row-wise maths and Pandas for loading, grouping and sorting.
- **Learning:** I practised structuring code into reusable functions, using vectorised NumPy operations instead of manual loops where possible, and presenting results clearly.

## 10. GitHub Repository
`<paste your repository link here>`
