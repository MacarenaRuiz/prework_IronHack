# VARIABLES AND OPERATORS


x1 = 1.1
x2 = "Ironhack"
x3 = "1.1"
x4 = True
x5 = "True"
x6 = -1
# 1.2 What is the difference between variables x1 and x3? x1 is decimal and x3 is string
# 1.3 What happens if you subtract x3 from x1?is not possible, different type of data, unless you convert string tu numerical type
# 1.4 What is the difference between variables x4 and x5? x4 is a boolen type data and x5 is an string
# 1.5 What happens if you subtract x5 from x4? is not possible because are different type of data



x1 = input("Please enter an integer number: ")

x2 = input("Please enter another integer number: ")

print(type(x1))
print(type(x2))

x7=int(float(x1))
print(type(x7))
x8=int(x2)
print(type(x8))


# Question 2 
#1.
x1=2
x2=3
print("x1 == x2:", x1 == x2)
#2.
print ("x1>x2", x1>x2)
#3.
print ("x2>x1", x2>x1)
#4.
print ("x1!=x2", x1!=x2)

x3=x1-x2
print('Difference x3=x1-x2, is: ', x3)
x1 = x1 + x3
print ('x1 with his incremental is: ', x1)

print(x1==x2)

# 3. Exercise - concatenation
name=input('What is your name: ')
lastName=input('What is your last name: ')

NconcatL= ('Name and last name are:', name + " " + lastName)
print(NconcatL)
