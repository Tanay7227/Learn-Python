# List 

'''
- A build-in data type that stores set of values
- It can store elements of different types(integer,float,string,etcc)
- list is written in []-square brackets
- Indexing start from zero 0
'''

# marks = [45, 45.2, 45.1, 87, 89, 54.2]
# print(marks)
# print(len(marks))
# print(marks[0]) #shows the index value
# print(marks[1]) #shows the index value
# print(marks[4]) #shows the index value

'''
- String are immutable(immutable means we cannot change the value)
  and List are mutable(mutable means we can change the value)
  '''
# student = ["Sonu", 95.4, 21, "Gujarat"]
# print(student[0])
# student[0]= "tanay"
# print (student[0])
# print (student)


#list Slicing

'''In a list Slicing also possible like String 
- we can call sublist in list
- we can all substring in string
- syntax:
        list_name = [starting_index : ending_index] 
- In list Ending index is not included
 '''
# list = "Tanay Mahale"
# print(list[0:12]) # [0 to last character]
# print(list[0:3]) # output- Tan 

# # Negative Slicing

# ''' a     p    p    l    e
#    -5    -4   -3   -2   -1'''

# list2 = "Apple"
# print (list2[-3:-1]) #pl
# print (list2[-5:-2]) #app

# List Methods

# 1) list.append()
# list = [2, 1, 3]
# list.append(4) #add one element at the end
# print(list)

# 2) list.sort
# list = [2,5,8,9,6,3,1,4,7]
# list.sort() #sort the number in ascending order
# print(list)

# 3) list.sort(reverse=True)

# list = [2,5,8,9,6,3,1,4,7]
# list.sort(reverse=True) #sort the number in descending order
# print(list)

# list1 = ['banana', 'apple', 'watermelon', 'litchi', 'chiku' ]
# list.sort(list1) #sort alphabetically a,b,c,d,e,f.
# print(list1)

# 4)list.reverse()

# list = [4,1,5,3]
# list.reverse() #reverse the list [3,5,1,4]
# print(list)

# 5) list.insert(idx,el)

# list = [1,2,4,6]
# list.insert(2,3) # add 3 on index 2 
# list.insert(4,5) # add 6 on index 5 after excuation of above 78 line
# print(list)

# 6) list.remove()

# list = [1,2,4,1,4,5]
# list.remove(4) #remove first occurrence of element [1,2,1,4,5]
# print(list)

# 6) list.pop(idx)

# list = [1,2,4,1,4,5]
# list.pop(3) #remove element from particular index [1,2,1,4,5]
# print(list)


#Tuples

'''Tuples are immutable like string never change their value after define
tup = (2,1,3,4)
print(tup[0])
print(tup[1])
print(tup[2])
tup[0]=5 #ERROR we cant assign value after declaration value 
'''
# tup = (2,1,3,4)
# print(tup[0])
# print(tup[1])
# print(tup[2])

# tup = (2)
# print(type(tup)) output- Integer (wrong way to declare single tuple)

# tup1 = (2,)
# print(type(tup1)) output- tuple (right way to declare single tuple)

'Important point'''

# list = ["tanay","Sonu","Dhruvi","kuki"]
# print(type(list))

# list1 = ("tanay","Sonu","Dhruvi","kuki")
# print(type(list1))

# list2 = ("tanaymahale")
# print(type(list2))

# list3 = (1, 2, 3, 4)
# print(type(list3))


#Tuple Methods

# 1)Tuple Slicing
# list4 = (1, 2, 3, 4)
# print(list4[1:3]) #Tuple Slicing- first index will print and last element not print

# 2) Tuple index
# list5 = (4,8,7,6,2)
# print(list5.index(8)) #output-2 #index method find a given number index position

# 3) Tuple count
# tup = [1, 2, 3, 8, 7, 2, 2]
# print(tup.count(2))





