
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
numb =input('Give me a number: ')

#sum multiple 4 and 9
def multiples_of_4_9(numb):
    total=0
    for numb in range(numb):
     if numb % 4 == 0 or numb % 9 ==0:
         total +=numb
    return total
     
print('Multiples of 4 and 9 sum, is :  ', multiples_of_4_9(numb))
