## CTI-110 
## P3HW2 SoftwareSales 
## Dominique Perteet
## 6/21/2018


# Find out discount for purchases

packages = int(input("Enter the packages bought: "))
packageprice = 99

if packages < 10:
    discount =0;
elif packages < 20:
    discount = 0.10
elif packages < 50:
    discount = 0.20
elif packages < 100:
    discount = 0.30
else:
    discount = 0.40

# Get the total price   

subTotal = packages * packageprice
discountAmount = discount * subTotal
total = subTotal - discountAmount


print ("Amount of discount: $" + format(discountAmount, ",.2f" ) + \
      "\nTotal amount: $" + format(total, ",.2f"))




