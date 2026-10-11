# Project Documentation: Student Performance Analytics System

### 1. Project Title
- **Project Name:** Student Performance Analytics System
- **Student Name:** Krish
- **Technologies:** Python, NumPy, Pandas
- **Submission Date:** October 2026

### 2. Objective
Automate student academic data analysis from a CSV dataset: compute total and average marks, assign letter grades based on rules, verify attendance and pass/fail thresholds, and summarize class-level insights without external machine learning models.

### 3. Technologies Used
- Python 3.x
- NumPy (array aggregations, min/max/mean computations)
- Pandas (DataFrame creation, CSV reading, column operations)

### 4. Dataset Description
The dataset (`students.csv`) contains 15 student records across CS, IT, and ECE departments.
- Columns: StudentID, Name, Department, Math, Science, English, Attendance.

### 5. Implementation
1. **Data Loading:** Loaded records using Pandas `read_csv()`.
2. **Numerical Aggregation:** Converted mark columns to NumPy arrays to compute row totals and averages.
3. **Evaluation Logic:** Iterated rows using modular functions to assign grades (A+ to F) and check pass/fail criteria.
4. **Analytics Summary:** Calculated class average, pass/fail counts, subject-wise statistics, and top 3 students.

### 6. Key Features
- Total and average marks calculation using NumPy array operations.
- Rule-based grading scale (A+, A, B, C, D, F).
- Strict pass/fail validation (min 40 marks in each subject, >=50% average, >=75% attendance).
- Subject-level performance analysis (Mean, Max, Min).
- Identification of top-performing students.

### 7. Output Summary
- Overall Class Average: 68.89%
- Total Passed: 10 | Total Failed: 5
- Highest Scorer: Sneha Singh (94.33%)
- Lowest Scorer: Amit Kumar (35.67%)
- Best Subject Average: Science (69.93)

### 8. Final Outcome
The project successfully processes academic data and generates human-readable performance reports to evaluate class and subject performance.

### 9. Challenges & Learning
- Configured Python and PATH environment variables in Windows PowerShell.
- Handled multi-dimensional array operations using NumPy `axis=1`.
- Structured reusable helper functions in `functions.py` separated from the execution driver `main.py`.

### 10. GitHub Repository
https://github.com/krish2006-ctrl/student-performance-analytics