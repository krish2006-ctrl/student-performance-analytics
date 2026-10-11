import pandas as pd
import numpy as np
import functions as fn

def main():
    print("=" * 50)
    print("      STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 50)

    
    df = pd.read_csv('students.csv')
    subjects = ['Math', 'Science', 'English']

    
    df['Total'] = fn.calculate_total_marks(df, subjects)
    df['Average'] = fn.calculate_average_marks(df['Total'], len(subjects))

   
    grades = []
    statuses = []
    for _, row in df.iterrows():
        grades.append(fn.assign_grade(row['Average']))
        statuses.append(fn.check_pass_status(row, subjects))

    df['Grade'] = grades
    df['Status'] = statuses

    
    print("\n[STUDENT RECORDS SUMMARY]")
    print(df[['StudentID', 'Name', 'Total', 'Average', 'Grade', 'Status']].to_string(index=False))

    
    print("\n" + "=" * 50)
    print("                 KEY METRICS")
    print("=" * 50)

    class_avg = round(float(np.mean(df['Average'].to_numpy())), 2)
    total_passed = (df['Status'] == 'Pass').sum()
    total_failed = (df['Status'] == 'Fail').sum()

    print(f"Overall Class Average : {class_avg}%")
    print(f"Total Students Passed : {total_passed}")
    print(f"Total Students Failed : {total_failed}")

   
    top_student = df.loc[df['Average'].idxmax()]
    low_student = df.loc[df['Average'].idxmin()]
    print(f"\nHighest Scorer: {top_student['Name']} ({top_student['Average']}%)")
    print(f"Lowest Scorer : {low_student['Name']} ({low_student['Average']}%)")

   
    print("\n[SUBJECT-WISE PERFORMANCE]")
    sub_stats = fn.get_subject_stats(df, subjects)
    for sub, vals in sub_stats.items():
        print(f"{sub:8s} -> Avg: {vals['Average']} | Max: {vals['Max']} | Min: {vals['Min']}")

    
    print("\n[TOP 3 PERFORMERS]")
    top_3 = df.sort_values(by='Average', ascending=False).head(3)
    for rank, (_, row) in enumerate(top_3.iterrows(), start=1):
        print(f"{rank}. {row['Name']} ({row['Department']}) - {row['Average']}%")

    print("\n" + "=" * 50)

if __name__ == '__main__':
    main()