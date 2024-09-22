str1 = 'Tanay Mahale'
str2 = "Tanay Mahale"
str3 = '''Tanay Mahale'''
print(str1)
print(str2)
print(str3)

# '''Note:- Why we use 3 type of string instead one
# ans:- beacause when we use single inverted coma then we can't able to use double inverted coma
# like 
# str1 = 'How's your days' //error--> s your days python can't recognize beacause of extra coma
# str2 = "How's Your Day" // Correct
# str3 = '''How's your day'''
# '''
print("--------------------------------------------------------")

str4 = "Hello Tanay.\nHow are you my Friend" #for new line \n
str5 = "Hello Tanay.\tHow are you my Friend" #for extra space \t
print(str4)
print(str5)

print("--------------------------------------------------------")

#concatenation
str6 = "Tanay"
str7 = "Mahale"
print (str6 + str7)

#  --------OR---------
str6 = "Tanay"
str7 = "Mahale"
final = str6 + str7
print (final)

#length of string using function
str8 = "Tanay Mahale"
print(len(str8))
