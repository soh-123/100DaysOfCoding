# write a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
student_number = n+1
total_num = 0
for i in student_heights:
    total_num += i
average = round(total_num/student_number)
print(average)

'another solution:'
#total_height = sum(student_heights)
#number_of_students = len(student_heights)
#average = total_height/number_of_students