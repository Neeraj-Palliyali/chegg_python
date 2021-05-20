
# getting account number
accountNo=input("Enter the 8 digit account number:")

# try catch for if the input cannot be converted to integer
try:
    account=int(accountNo)

    # if the length is not equal to 8
    if(len(str(account))==8):
        print("The account number is valid")

    else:
        print("Invalid account number")

# the input will be invalid 
except:
    print("Invalid account number")