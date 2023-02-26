# Write a program that converts student's scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
# key is the key name to point to the value we need to change
for key in student_scores:
    # grade is the value of the dictionary
    grade = student_scores[key]
    if grade > 90:
        student_grades[key] = "Outstanding"
    elif grade > 80:
        student_grades[key] = "Exceeds Expectations"
    elif grade > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
