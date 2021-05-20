n = int(input("Enter a Positive Number  : "))
Result = 0
for i in range(1, 2*n):
    for j in range(1, i+1):
        for k in range(1, 2*j):
            Result += 1
print("Sum=",Result) pip install -U numpy