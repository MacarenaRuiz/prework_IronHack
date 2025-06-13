#1. Given the list
lst = [1, 2, 34, 5, 3, 12, 9, 8, 67, 89, 98, 90, 39, 21, 45, 46, 23, 13]
print(len(lst))

#first element in the list
print(lst[0])
#last element in the list
print(lst[-1])

#what is the index of element 90 in the list?
index_of_90=lst.index(90)
print(index_of_90)

#First 8 elements in the list
print(lst[:8])

#Append elements 100 and 110 in the list
#lst.append(100 and 110)
lst.append(100)
print(lst)
lst.append(110)
print(lst)

#sort the element in the list: sort in ascending/descending
lst.sort()
print(lst)

#2. 
names = ["Alice", "Bob", "Charlie", "Dave"] 
search_name = "Bob" # Element to search in "names" list

search_name= input('Writte the name you are looking for: ')

if search_name in names:
    index= search_name.index(names)
    print(f"{search_name==names} was found at names {names}")
else:
    print(f"{search_name} was not found at names {names}") 

#3.
numbers = [2, 4, 6, 8, 10]
average=sum(numbers)/len(numbers)
print(f"The average is: {average}")