

#3 Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for num in range(1, 21):
    if num%2 == 0:
        type = "This number is even"
        print(num, type)
    else:
        type = "This number is odd"
        print(num, type)
