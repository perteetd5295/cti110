## CTI-110 
## P5HW1 - Test Grading Program    
## Dominique Perteet
## 7/9/2018



def main():

     score1=int(input('Enter your first grade: '))
     score2=int(input('Enter your second grade: '))
     score3=int(input('Enter your third grade: '))
     score4=int(input('Enter your fourth grade: '))
     score5=int(input('Enter your fith grade: '))


     average=calc_average(score1,score2,score3,score4,score5)
     print('Your average score is ', average)

     determine_grade(average)

def calc_average(score1,score2,score3,score4,score5):
     average_score = (score1+score2+score3+score4+score5)/5
     return average_score

def determine_grade(score):
    if score > 89 and score < 101:
        print("You made an A!")
        print("Your numeric grade of",score,"is an A!")
    elif score > 79 and score < 90:
        print("You made an B!")
        print("Your numeric grade of",score,"is an B!")
    elif score > 69 and score < 80:
        print("You made an C!")
        print("Your numeric grade of",score,"is an C!")
    elif score > 59 and score < 70:
        print("You made an D!")
        print("Your numeric grade of",score,"is an D!")
    elif score >= 0 and score < 60:
        print("You made an F!")
        print("Your numeric grade of",score,"is an F!")
    else:
        print()
    


main()
