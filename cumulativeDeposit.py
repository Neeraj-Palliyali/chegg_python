apr = float(input("Enter the APR for the CD: \n"))/100
no_years = int(input("Enter the number of years: \n"))
balance = float(input("Enter initial deposit: \n"))

mpr = apr/12

for i in range(no_years):
    print("\nYear "+str(i+1)+":\n")
    print("\t    Month \tBalance")
    print("\t   ________   ___________")
    for j in range(12):
    
        balance=balance+(balance*(mpr))
        balance = round(balance,2)
        
        print(format("\t      " + str(j + 1) + " \t$ ",">11s")+str(round(balance,2)))
    print("\nBalance end of year ",i+1," is $",balance)