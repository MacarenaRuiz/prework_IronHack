
import math
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit) #

    print(fruit[1])

names = ["Alice", "Bob", "Charlie", "Dave"]

for name in names:
    print("Hello, " + name + "!")

  #Exercise
  # 1.1 Write a simple for loop to print integers from 10 to 30
for i in range (10,31):
    print(i, end=',')

    #1.2 multiples of 5
    for i in range (10,31):
        if i % 5 ==0:
            print(i, end=', ')



## Complete exercise from chat gpt
import math  # To use math.factorial for verification

# Step 1: Prompt the user for an integer
num = input("Enter an integer number: ")

# Step 2: Validate that the input is an integer
if num.isdigit():  # Only works for positive integers
    num = int(num)

    # Step 3: Calculate factorial using a loop
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print(f"Factorial of {num} (calculated with loop): {factorial}")

    # Step 4: Verify with math.factorial
    math_factorial = math.factorial(num)
    print(f"Factorial of {num} (calculated with math.factorial): {math_factorial}")

    # Check if both match
    if factorial == math_factorial:
        print("✅ The results match!")
    else:
        print("❌ The results do not match!")

else:
    print("Invalid input. Please enter a positive integer.")



x = [12,43,4,1,6,343,10, 34, 12, 93, 783, 330, 896, 1, 55]

#2.1 Write code to find only those numbers in the list that are divisible by 3.
for number in x:
    if number % 3 == 0:
        print(number, end= '. Numbers multiple of 3: , ')

# end digit 3
for number in x:
    if number % 10 == 3:
        print (number, end= '. Numbers ending with digit 3 , ')
#create new list with the previous list
end_with_3 = [number for number in x if number % 10 ==3]
print (end_with_3)
#Convert the integers to strings and ude indexing to acces the last digit

x = [12,43,4,1,6,343,10, 34, 12, 93, 783, 330, 896, 1, 55]

#2.1 Write code to find only those numbers in the list that are divisible by 3.
for number in x:
    if number % 3 == 0:
        print(number, end= '. Numbers multiple of 3: , ')

# end digit 3
for number in x:
    if number % 10 == 3:
        print (number, end= '. Numbers ending with digit 3 , ')
#create new list with the previous list
end_with_3 = [number for number in x if number % 10 ==3]
print (end_with_3)
#Convert the integers to strings and ude indexing to acces the last digit
