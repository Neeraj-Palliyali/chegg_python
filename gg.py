k=input()
n=int(input())
binary=bin(n)
m=binary[2:]
if m in k :
    print("true")
else:
    print("false")