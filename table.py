# creating the dictionary
marks = {'Name':['Lab1', 'Lab2'],'Jack':[80, 85], 'Mike':[70, 70], 'Kate':[65, 72], 'Vera':[75, 60]}

# initialize the array for lab sums
labSums=[0,0]
# finding the total number of students
totalNo = len(marks)-1

# looping through teh dictionary
for i in marks:
    # skipping the first line
    if(i=='Name'):
        continue
    # adding values to the sums array
    else:
        labSums[0]+=marks[i][0]
        labSums[1]+=marks[i][1]

# printing the avg sums of the labs
print("Lab1 avg:",labSums[0]/totalNo)
print("Lab2 avg:",labSums[1]/totalNo)

# opening the file
fp=open("marks.csv", "w+")

# writing to the file as csv
for i in marks:
    fp.write(i+","+str(marks[i][0])+","+str(marks[i][1])+"\n")

fp.close()
