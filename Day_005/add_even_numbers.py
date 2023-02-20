#write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100
total = 0
for i in range(0,101,2):
    total += i
print(total)