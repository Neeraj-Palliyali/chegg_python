import random

print("Enter 15 number")
s=[]
for i in range (15):    #get 15 random numbers
    k=float(input())
    s.append(k)         #appending it to a list
print("Printing numbers randomly")
for i in range(88):         
    print(random.choice(s)) #printing 88 times from the list randomly
