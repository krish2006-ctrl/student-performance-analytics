import numpy as np


def calculate_total_marks(df, subjects):
    marks_array = df[subjects].to_numpy()
    return np.sum(marks_array, axis=1)


def calculate_average_marks(total_marks, num_subjects):
    return np.round(total_marks / num_subjects, 2)


def assign_grade(avg_score):
    if avg_score >= 90:
        return 'A+'
    elif avg_score >= 80:
        return 'A'
    elif avg_score >= 70:
        return 'B'
    elif avg_score >= 60:
        return 'C'
    elif avg_score >= 50:
        return 'D'
    else:
        return 'F'



def check_pass_status(row, subjects):
    
    for sub in subjects:
        if row[sub] < 40:
            return 'Fail'
    
    if row['Attendance'] < 75:
        return 'Fail'
    
    if row['Average'] < 50:
        return 'Fail'
    return 'Pass'

def get_subject_stats(df, subjects):
    stats = {}
    for sub in subjects:
        data = df[sub].to_numpy()
        stats[sub] = {
            'Average': round(float(np.mean(data)), 2),
            'Max': int(np.max(data)),
            'Min': int(np.min(data))
        }
    return stats