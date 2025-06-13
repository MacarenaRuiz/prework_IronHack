
# DataStructure - dictionaries

word_freq = {
  'love': 25,
  'conversation': 1,
  'every': 6,
  "we're": 1,
  'plate': 1,
  'sour': 1,
  'jukebox': 1,
  'now': 11,
  'taxi': 1,
  'fast': 1,
  'bag': 1,
  'man': 1,
  'push': 3,
  'baby': 14,
  'going': 1,
  'you': 16,
  "don't": 2,
  'one': 1,
  'mind': 2,
  'backseat': 1,
  'friends': 1,
  'then': 3,
  'know': 2
}

print(len(word_freq))

#what keys are present in the list?
print(list(word_freq.keys()))

#What is the frequency of following words in the dictionary:
print(word_freq.get('friends'))
print(word_freq.get('taxi'))
print(word_freq.get('jukebox'))

#Is the word begin present in the dictionary?
if 'begin' in word_freq:
    print("YES, 'begin' is present")
else:
    print("No, 'begin' is not present")


#Add the following words and their frequencies to the dictionary
# 'begin': 1
# 'start': 2
# 'over': 1
# 'body': 17

word_freq['begin']=1
word_freq['start']=2
word_freq['over']=1
word_freq['body']=17

print(list(word_freq.keys()))

#convert the keys to a list
word_list=list(word_freq.keys())

#print the list
print(word_list)

word=word_list
print(word)


# #first element in the list
# print(lst[0])
# #last element in the list
# print(lst[-1])
#first word of word_list
print(word_list[1])

#last word of word_list
print(word_list[-1])


#1.2 Can a dictionary have two key-value pairs with the same key?
#No, a dictionary just can have one key. Keys must be unique

#1.3 Can a dictionary have two key-value pairs with the same value but different keys?
#Yes, can have same value but with different key
# example names={'Gonzalo': 2, 'Luis':2}