## CTI-110 
## P3HW1 - Age Classifier 
## Dominique Perteet
## 6/20/2018



# Find out the person's age

age = int(input("Enter person's age?: " ))

if age <= 1:
    print("The person is a:" ,"Infant")
elif age < 13:
    print("The person is a:" ,"Child")
elif age < 20:
    print("The person is a:" ,"Teenager")
elif age >= 20:
    print("The person is a:" ,"Adult")
