def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1    
    return True

def main():
    cases=int(input())
    for j in range (cases):
        l,r=map(int, input().split())
        lowest=0
        highest=0
        for i in range(l,r+1):
            if(is_prime(i)):
                lowest=i
                break
        
        for i in range(r,l-1,-1):
            print(i)
            if(is_prime(i)):
                highest=i
                break
        
        if(highest==0 and lowest==0):
            print(-1)
        else:
            print(highest, lowest)
            print(highest-lowest)        

 # Write code here 

main()