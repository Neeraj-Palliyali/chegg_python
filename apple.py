import random
def Apple(n):
    
    if n==1:
        print("An apple a day keeps the doctor away")
    else:
        l=random.randint(1,n-1)
       
        Apple(l)
        Apple(n-l)

k=int(input())
Apple(k)
