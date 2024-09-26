'''
Dictionaries are used to store ata values in key:value paris
They are unorderd,mutable(changeable) & don't allow
duplicate keys. Dictionaries are unorder.

-- we can store one datatype in another datatype like dictonary 
  
KEYS:- We can also make string,int,float,boolean,Tuple as a KEY which are not 
change after the assign,for this reason list are not allowed
to assign as a KEY.

VALUES:- We can assign any datatype list or tuple as a values'''



# info = {
#     "name" : "Sonu",
#     "subject" : ["python", "Java", "C++"],
#     "learning": ("python", "JS", "HTML"),
#     "age" : 21,
#     "is_adult" : True,
#     "marks" : 98.21
# }

# print (info)
# print (type(info))

#we can also print individual value 
# print(info["name"])

# We can also modify our value
# info["name"] = "Tanay"

# # We can also add in value
# info["surname"] = "Mahale"
# print(info)

#we can also create an empty dictionary 
# Null_dict = {}
# Null_dict ["name"] = "Tanay Mahale"
# print(Null_dict)

'''Nested Dictionary'''
# student = {
#     "name" : "Tanay",
#     "subject" : {
#         "phy" : 89,
#         "chem" : 93,
#         "maths" : 79,
#     }
# }

# print (student)
# print (student["subject"])
# print (student["subject"]["maths"])

'''Dictionary methods'''
# 1) Return all keys  -  dict.keys()
# student = {
#     "name" : "Tanay",
#     "subject" : {
#         "phy" : 89,
#         "chem" : 93,
#         "maths" : 79, 
#     } 
# }
# print(student.keys())

## 2) Return all value  -  dict.value()
# print(student.values())

## 3) Return all value in the form of tuples  -  dict.item()
# print(student.items())

# 4) Return the key according to value  -  dict.get("key")
#there are two methods to print the value
# print (student["name2"]) #prefer at beginner level
# print("1")
# print("2")
# print("3")

# print (student.get("name2")) #prefer at industry level
# print("1")
# print("2")
# print("3")

'''print (student.get("name")) prefer at industry level because python is excuted line by line
if we use this code "print (student["name"])" then it show error and next code which are below that code
are not excute if its right also. if we use "print (student.get("name"))" this code then 
it show "none" value and excute the below code '''
#better is used differnts methods for coding

#5) Insert the specified items to the dictionary dict.update(newDict)
info = {
    "name" : "Sonu",
    "subject" : ["python", "Java", "C++"],
    "learning": ("python", "JS", "HTML"),
    "age" : 21,
    "is_adult" : True,
    "marks" : 98.21
}
#1) method
# info.update({"city" : "surat", "pincode" : 394650})
# print(info)

# 2) method
new_dict = {"city" : "surat", "pincode" : 394650}
info.update(new_dict)
print(info)
