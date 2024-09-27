'''Set is the collection of the Unordered items
Each Element in the set must be unique & immutable(no changes).

- we can't store any value in the form List and Dictionary in Set because
list and dictionary are mutable (change).

- >>>>> IMP POINT <<<<<<
- SET is mutable but SET Elements are immutable.
-we can add or remove the element but we can't change or update the element which are
already assign in a set. 
'''

# num = {1,2,3,3,1,4,"tanay","Mahale","tanay","Mahale"}
# print(type(num))
# print(len(num))
# print(num)
''' -if we print the set then it print our values in different order-
so tha's why SET is immutable.(print 3-4 time to see result proper).
- Duplicate value are ignore
- length len(num) also ignore the duplicate values '''

# num1= {} #empty dictionary
# num2= set()#Empty Set
# print(type(num1)) 
# print(type(num2)) 

'''Method of SET'''

# -Add Element
# num = set()
# num.add(1)
# num.add(1)
# num.add(2)
# num.add(2)
# num.add("Tanay")
# num.add((4,5,6)) #add Tuple but we can't add list or Dictionary
# print(num)

# # -Remove Element
# num.remove(2)
# print(num)

# -POP Element
# num1 = {"Tanay","Mahale","Developer","Data Analyst"}
# print(num2.pop())

# -Union 
# num1 = {"Tanay","Mahale","Developer","Data Analyst"}
# num2 = {1,2,3,3,1,4}
# print(num1.union(num2))

# # -Intersection
# num1 = {"Tanay","Mahale","Developer","Data Analyst"}
# num2 = {1,2,3,3,1,4,"Tanay","Mahale"}
# print(num1.intersection(num2))
