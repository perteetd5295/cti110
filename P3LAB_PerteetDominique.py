## CTI-110 
## P3TLAB: Debugging
## Dominique Perteet
## 6/21/2018

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores

    
score = int(input("What is the test score?: "))

if score >= 90:
    letterGrade = "A"
    print("You made an A!")
    print("Your numeric grade of",score,"is an A!")
elif score >= 80:
    letterGrade = "B"
    print("You made an B!")
    print("Your numeric grade of",score,"is an B!")
elif score >= 70:
    letterGrade = "C"
    print("You made an C!")
    print("Your numeric grade of",score,"is an C!")
elif score >= 60:
    letterGrade = "D"
    print("You made an D!")
    print("Your numeric grade of",score,"is an D!")
else:
    letterGrade = "Too Low"
    print("You made an F!")
    print("Your numeric grade of",score,"is an F!")






# program start
main()
