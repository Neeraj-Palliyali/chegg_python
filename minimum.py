list1=[20,22,3,4,5,12,53,18] 
min1 = list1[0] 
min2 = list1[0] 

for item in list1[1:]:      

    if item < min1:

        min2 = min1
        min1 = item 

    elif item < min2: 
        min2 = item 

print(min1, min2)