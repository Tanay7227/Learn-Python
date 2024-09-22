# Indexing

str = "Tanay Mahale"
print (str[0])
print (str[1])
print (str[2])
print (str[3])
print (str[4])
print (str[5])
print (str[6]) # index also assign to space
print (str[7])
print (str[8])
print (str[9])
print (str[10])
print (str[11])

'''Note:- we can assign or modify the string
like on above example str[0] has "T" 
we can assign str[0] = S'''

#Slicing---Mostly use in Machine Learning

str1 = "Tanay Mahale"
print(str[0:12]) # [0 to last character]
print(str[0:5]) # [0 to last character]
print(str[6:12]) # [0 to last character]
print(str[0:len(str)]) # [0 to last character]
print(str[0:]) # [0 to last character]
print(str[:len(str)]) # [0 to last character]
 
# Negative Slicing

''' a     p    p    l    e
   -5    -4   -3   -2   -1'''

str2 = "Apple"
print (str[-3:-1]) #pl
print (str[-5:-2]) #app