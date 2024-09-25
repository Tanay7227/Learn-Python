''' if-elif-else (syntax)
if(condion):
    Statement1
elif(condition):
    statement2
else:
    StatementN '''

# Eligiable for licenes or Not
# num = int(input("Enter Your Age:"))

# if(num >= 18):
#     print ("Eligiable for license")
# else:
#     print("Not Eligiable for license")

# Traffic Light Red,Yellow,Green
# light = str(input("Enter Traffic Color:"))

# if (light == "Red"):
#     print("Stop")
# elif (light == "Yellow"):
#     print("Wait")
# elif (light == "Green"):
#     print("GO")

'''IF Statement is check everytime but elif statement is check when the if statement may wrong'''

# Grade Student based on marks

marks = int(input("Enter Student Marks:"))

if (marks >= 90):
    print("Grade A")
elif (marks >=80 and marks < 90):
    print("Grade B")
elif (marks >=70 and marks < 80):
    print("Grade C")
else:
    print("Fail")