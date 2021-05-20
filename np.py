num1 = int(input("Enter a non-zero integer number"))
num2 = int(input("Enter another non-zero integer number"))
num = num1*num2
if(num<0):
    if(num1<0):
        signs="NP"
        if num%2==1:
            numbers = "00"
        else:
            numbers = "EN/Eo/OE"
    else:
        signs="PN"
        numbers = "OO/OE/EO/EE"
else:
    signs="PN"
    numbers = "EE/ED/OE/OO"
print("Signs are",signs,"Numbers are",numbers)