# write a program that calculates the highest score from a List of scores
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_number = 0
for i in student_scores:
    if i > max_number:
        max_number = i
print(f"The highest score in the class is: {max_number}")

# 78 65 89 86 55 91 64 89
