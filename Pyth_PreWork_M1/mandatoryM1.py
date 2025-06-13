

#PREWORK MANDATORY - M1
import jupytext

#TASK 1
numbers = [34, 15, 88, 2]
smallest= min(numbers)
print (smallest)
  
numbers1 = [34, -345, -1, 100]
smallest1= min(numbers1)
print (smallest1)


#TASK 2
#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#If the function is passed a valid PIN string, return true, else return false.

#3 attempts is the only possible (3 intentos)
attempts= 3

for atmMachine in range(attempts):
    atmMachine = input ('Enter a pin code: ')
    if atmMachine.isdigit() and (len (atmMachine)==4 or (atmMachine)==6):
        print('Pin success')
        break
    else:
        atmMachine=input('Invalid code, try again: ')
        retry = input ('Try again, last chance: ')
        print('Invalid code. The code needs to be 4 or 6 digits')
        break

else:
    print('3 attempts is the maximum, You account has been blocked')

#TASK 3
#Given a String,
#return the integer 1 if the String begins with the character capital A, lowercase a, or 1
#return the integer 0 if the String begins with the character capital B, lowercase b, or 2
#return -1 if the String begins with any other character.

#But in total are 3 attempt (2+1 in else)
attempts=2

for number1 in range(attempts):
    number1= input('Please, enter an input: ')

    if number1.startswith('A') or number1.startswith('a') or number1.startswith('1'):
        print('Integer 1')
        break
    elif (number1.startswith)('B') or number1.startswith ('b') or number1.startswith('2'):
        print('Integer 0')
        break
else:
    number1=input('Invalid input, try again: ')
    print('Integer -1')



    #TASK 4
    #multiples_of_3_and_5. And to return the sum of multiple 3 and multiple of 5
    num=(1,2,3,4,5,6,7,8,9,10)


def multiples_of_3_5(num):
    total=0
    for num in range(num):
     if num % 3 == 0 or num % 5 ==0:
         total +=num
    return total
     
print('Multiples of 3 and 5 sum, is :  ', multiples_of_3_5(10))


#5 Given a number n return the difference of n and the sum of all multiples of 4 or 9 between 1 and n inclusively.
#NOT CLEAR ??????
numb =input('Give me a number: ')

#sum multiple 4 and 9
def multiples_of_4_9(numb):
    total=0
    for numb in range(numb):
     if numb % 4 == 0 or numb % 9 ==0:
         total +=numb
    return total
     
print('Multiples of 4 and 9 sum, is :  ', multiples_of_4_9(numb))


#test for a new push

