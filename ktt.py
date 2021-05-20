def squares(a, b):
    # Write your code here
    count=0
    for i in range (a,b+1):

        p=(i)**(1/2)
        ls=str(p)
        k=ls.split(".")
        if(k[1]=='0'):
            count+=1
    return count
        
        
print(squares(17, 24))