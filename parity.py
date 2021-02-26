n=354234345434
k=str(n)
map1={}
for i in k:
    if(i in map1.keys()):
        map1[i]+=1
    else:
        map1[i]=1
m=map1.keys()
flag=False
for i in m:
    p=int(i)
    if(p%2==0 and map1[i]%2!=0):
        flag=True
    elif(p%2!=0 and map1[i]%2==0):
        flag=True
    else:
        flag=False
        break

if(flag==False):
    print("FALSE")
else:
    print("TRUE")