with open("Day_026/file1.txt") as data1:
    file1_numbers = data1.readlines()


with open("Day_026/file2.txt") as data2:
    file2_numbers = data2.readlines()

result = [int(num) for num in file1_numbers if num in file2_numbers]

print(result)


