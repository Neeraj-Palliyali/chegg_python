# intializing the list
list1=[5, 4, 7, 4, 2, 9, 6, 4, 3, 2]

# looping throught the list with its index
# skipping through 2 indexes
for i in range(0,len(list1),2):

    # suming the first two elements by getting the 
    #values from the list
    sum1=list1[i]+list1[i+1]
    
    # printing the sum
    print(sum1)