# Enter number of fixed deposits
n=int(input("Enter number of fixed deposits:"))
fd=[]
print("Enter each values:")
for i in range(n):
    fixeddeposit=int(input())
    fd.append(fixeddeposit)


#creating array for interest rates
interestRate=[]
for i in fd:

    if(i>=0 and i<=500):
        interestRate.append(9)
    elif(i>500 and i<=1000):
        interestRate.append(15)
    else:
        interestRate.append(20)

#print fixed deposits and their interest rates
print("The interest rates are")
for i in range(n):
    print(str(fd[i])+"-"+str(interestRate[i]))
