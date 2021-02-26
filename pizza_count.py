# L = ["1230 bagel\n", "452345 pizza\n", "12314 pizza\n", ] 
  
# # writing to file 
# file1 = open('myfile.txt', 'w') 
# file1.writelines(L) 
# file1.close() 
  
 
file1 = open('myfile.txt', 'r')     # creates a handle on the file
Lines = file1.readlines()           #read each Line from the input
bagelCount=0
pizzaCount=0
for line in Lines:                  #get each line from all lines
    s=[]
    for i in line.split():
        s.append(i)            #get the individual integers from each line seperately as integers
    if(s[1]=='pizza'):         #if it is a pizza. count of pizza is incremented
        pizzaCount+=1
    elif(s[1]=='bagel'):       #if it is a bagel. count of bagel is incremented
        bagelCount+=1

#The product with larger count is printed else it will be a tie
if(pizzaCount>bagelCount):
    print(str(bagelCount)+" bagel "+str(pizzaCount)+" pizza"+". Pizza wins!")
elif(bagelCount>pizzaCount):
    print(str(bagelCount)+" bagel "+str(pizzaCount)+" pizza"+". Bagel wins!")
else:
    print("It is a tie!")
    



    