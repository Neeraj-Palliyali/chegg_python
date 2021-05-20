def binomialCoeff(n, r):
 
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
 
    # Recursive Call
    return binomialCoeff(n , r-1) + binomialCoeff(n-1, r)
 
 
n = int(input("Enter n:"))
r = int(input("Enter r:"))

print("Value of n:\t",n)
print("Value of r:\t",r)

print("Value of nCr:\t",binomialCoeff(n,r))