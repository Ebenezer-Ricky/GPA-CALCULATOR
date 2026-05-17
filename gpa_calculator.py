#!/usr/bin/env python3
import argparse

GRADE_POINTS = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'F': 0.0,
}

def numeric_to_points(score):
    s = float(score)
    if s >= 93: return 4.0
    if s >= 90: return 3.7
    if s >= 87: return 3.3
    if s >= 83: return 3.0
    if s >= 80: return 2.7
    if s >= 77: return 2.3
    if s >= 73: return 2.0
    if s >= 70: return 1.7
    if s >= 67: return 1.3
    if s >= 60: return 1.0
    return 0.0

def grade_to_points(grade):
    g = str(grade).strip().upper()
    if g in GRADE_POINTS:
        return GRADE_POINTS[g]
    try:
        return numeric_to_points(float(g))
    except Exception:
        raise ValueError(f"Unrecognized grade: {grade}")

def calculate_gpa(courses):
    total_credits = 0.0
    total_points = 0.0
    for credits, grade in courses:
        pts = grade_to_points(grade)
        total_credits += float(credits)
        total_points += float(credits) * pts
    if total_credits == 0:
        return 0.0, 0.0
    return total_points / total_credits, total_credits

def run_interactive():
    try:
        n = int(input('Number of courses: ').strip())
    except Exception:
        print('Invalid number, exiting.')
        return
    courses = []
    for i in range(1, n+1):
        while True:
            try:
                c = float(input(f'Course {i} credits: ').strip())
                break
            except Exception:
                print('Enter a numeric credit value (e.g. 3, 4).')
        g = input(f'Course {i} grade (letter or numeric): ').strip()
        courses.append((c, g))
    gpa, credits = calculate_gpa(courses)
    print(f'GPA: {gpa:.3f} over {credits:.2f} credits')

def run_demo():
    sample = [
        (3, 'A'),
        (4, 'B+'),
        (3, '90'),
    ]
    gpa, credits = calculate_gpa(sample)
    print('Demo courses:')
    for c, g in sample:
        print(f' - {c} credits: {g}')
    print(f'GPA: {gpa:.3f} over {credits:.2f} credits')

def main():
    parser = argparse.ArgumentParser(description='Simple GPA calculator')
    parser.add_argument('--demo', action='store_true', help='Run demo')
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        run_interactive()

if __name__ == '__main__':
    main()
