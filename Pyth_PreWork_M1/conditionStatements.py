# Exercise Conditional Statements
#1.
# Prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = float(input("Enter the second number: "))

# Compare the two numbers and print the result
if num1 > num2:
    print(f"{num1} is larger than {num2}.")
elif num2 > num1:
    print(f"{num2} is larger than {num1}.")
else:
    print("Both numbers are equal.")

#2.
# Prompt the user to enter a numerical grade
grade = float(input("Enter your numerical grade: "))

# Determine and print the grade classification
if grade >= 90:
    print("Your grade is: A")
elif grade >= 80:
    print("Your grade is: B")
elif grade >= 70:
    print("Your grade is: C")
elif grade >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

#3.

# Vowels and consonants
letter = input('Enter a letter of the alphabet: ')
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

# Check if the input is valid
if len(letter) == 1 and letter.isalpha():
    # Convert to lowercase
    letter = letter.lower()

    # Now check vowel or consonant
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
else:
    print("Invalid input, please insert a letter of the alphabet")


#Bonus Exercise
#1. 
inte= input('Please enter an integer: ')

#2.
# digits: from 0 to 9
#  
if inte.isdigit():
    print (f"{inte} The input inserted is a number")
else:
    print ('The input was not an integer')


#3.

if inte==0
    print(f"{inte} The number is zero")