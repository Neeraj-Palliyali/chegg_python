
# writing the funtion naming it add_one
def add_one(k):

    # LOOPING over each element in the  list    
    for i in range (len(k)):

        # adding indiviually one over each element in the list
        k[i]+=1

    # finally returning the list 
    return k



p=[]
#accepting input of space seperated integers
k=input().split()

#writing integers to list
for i in k:
    p.append(int(i))

print("The given list is:", p)
# calling the function
s=add_one(p)


#showing the resultant list
print("The output is:",s)