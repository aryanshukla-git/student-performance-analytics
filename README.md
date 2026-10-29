# Student Performance Analytics System

A Python data-analysis project that reads student records, processes them with **NumPy** and **Pandas**, and reports totals, averages, grades, pass/fail statistics, subject-wise performance and top performers.

## Project Structure
```
student-performance-analytics/
├── main.py                   # Runs the project and prints the analysis
├── functions.py              # Reusable calculation/processing functions
├── students.csv              # Dataset (20 students)
├── student_results.csv       # Generated results (output of main.py)
├── output.txt                # Saved program output
├── screenshots/              # Output screenshots
├── Project_Documentation.md  # Full project documentation
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Rules Used
- **Grades (by average):** A+ ≥ 90, A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, E ≥ 40, F below 40 (or failed)
- **Pass condition:** at least 35 marks in **every** subject
- **Attendance flag:** below 75%

## What It Reports
1. Dataset overview (records, columns, missing values)
2. Per-student total, average, grade, result and rank
3. Highest, lowest and class average
4. Pass/fail count and percentage
5. Grade distribution
6. Subject-wise analysis
7. Department-wise analysis
8. Top 5 performers
9. Attendance insights

## Sample Results
| Question | Answer |
|----------|--------|
| Highest average | Sneha Patel (93.2) |
| Best subject | English (73.35) |
| Students passed | 18 of 20 (90%) |
| Class average | 70.06 |

## Output Preview
![Class performance](screenshots/03_class_and_pass_fail.png)

See `Project_Documentation.md` for the full documentation.
