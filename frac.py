L = ["1 3\n", "1 4\n", "2 4\n"] 
  
# writing to file 
file1 = open('myfile.txt', 'w') 
file1.writelines(L) 
file1.close() 
  
 
file1 = open('myfile.txt', 'r')     # creates a handle on the file
Lines = file1.readlines()           #read each Line from the input
k=[]
for line in Lines:                  #get each line from all lines
    s=[]
    for i in line.split():
        s.append(int(i))            #get the individual integers from each line seperately as integers
    m=round(s[0]/s[1], 2)
    print(str(s[0])+'/'+str(s[1]),str(m))   #to get the output as specified

    