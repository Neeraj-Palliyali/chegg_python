def factorial(n,c):
    c+=1
    if n<2:
        print("It ran ", str(c)," times recursively")
        return 1
    return n*factorial(n-1, c)

def factorial2(n):
    count=0
    product=1
    while n>0:
        count+=1 
        product=n*product
        n-=1
    print("It ran ",str(count),"times iteratively")
    return product

k=[5,7,12,15]
for i in k:
    print("And the Factorial is:",str(factorial(i,0)))
    print("And the Factorial is:",str(factorial2(i)))