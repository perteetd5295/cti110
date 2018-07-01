## CTI-110 
## P4HW2:Running Total
## Dominique Perteet
## 6/28/2018


total = 0
userNumber = float(input( "Please enter first number or negative number to quit: "))

while userNumber > -1:
    total = total + userNumber
    userNumber = float(input( "Please enter the next number or a negative number to quit: "))

print()
print("The sum of all the numbers you entered is",format(total,',.0f'))
      
    
