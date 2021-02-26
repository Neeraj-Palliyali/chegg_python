n=int(input("Enter range Number:"))
for j in range(1,n+1):
    for i in range (0,5):
        print((j**i), end=" ")
    print()