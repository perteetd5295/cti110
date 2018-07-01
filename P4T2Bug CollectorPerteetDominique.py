## CTI-110 
## P4T2: Bug Collector
## Dominique Perteet
## 6/28/2018


# Initialize the accumlator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bus collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('Collected a total of', total, 'bugs')
