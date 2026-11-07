Grades = {"Мухамед": [6, 7, 11, 9, 5], "Їшак": [2, 4, 5, 2, 2], "Давид": [11, 10, 7, 9, 12], "Ваня": [1, 4, 8, 8, 3]}
min = 6
def avg_grade(arr):
     return sum(arr) // len(arr)
def has_passed(average):
    return average >= min
def report(student, average, passed):
    status = "пройшов мінімальний бал" if passed else "не пройшов Мінімальний бал"
    print(f"Студент {student} {status} із середнім балом: {average}")
def analyze(student, arr):
    average = avg_grade(arr)
    passed = has_passed(average)
    report(student, average, passed)
def main(grades):
    for student, arr in grades.items():
        analyze(student, arr)

main(Grades)
