## CTI-110 
## P4HW1: Distance Traveled   
## Dominique Perteet
## 6/28/2018




## Run loop for distance traveled.

vehicleSpeed = float(input('What is the speed of the vehicle:'))
timeTraveled = int(input('How many hours has it traveled?:'))

print('\n')
y = "Hours"
z ="Distance Traveled"
print(y.ljust(10) + z.ljust(20))
print("-"*30)

## Display the total distance.
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour,"\t" ,distanceTraveled, "miles" )
   

