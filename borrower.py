# all you need to find the result of comuptation
# is this method. To find the interest
def interest(amount):
    return amount*.05


# getting the namem address and phone number
name = input(" Enter borrower name:")
address = input(" Enter full address:")
number = input(" Enter phone number:")

# asking for the borrowal amount
amount=input(" Enter amount:")

# outputting the name, address and phone number
print("\n "+name,"\n",address,"\n",str(number))
# showing the inpur amount
print(" Amount:",amount)

# printing the input amount after computation
print(" The interest is:", str(interest(float(amount))))