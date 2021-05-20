# We use a dictionary here because the given structure resembeles one of a key-value pair
# The key we use here is the continent since that is the only value that can occur once
# The Number of students can be same so we can't take that value as a key so we  choose 
# The CONTINENT as key



# Intialising the dictionary as given

dictionary1={"Africa": 100, "America": 200 , "Asia": 300, "Europe": 100}

print("Continent       Number of Students")
# Here we are showing the intialised dictionary as given in the question
for i in dictionary1.keys():
    str1=i+str(dictionary1[i])
    print("{}\t   \t \t {}".format(i,dictionary1[i]))


# here we append the value of OCEANIA
print("\nPrinting dictionary again after the append function:")
dictionary1['Oceania']=50
print("Continent       Number of Students")
# Here we print dictionary again after the append function
for i in dictionary1.keys():
    str1=i+str(dictionary1[i])
    print("{}\t   \t \t {}".format(i,dictionary1[i]))



# in this method we compare the key values using the "keys()" function to check for AFRICA
print("\nChecking if Africa exists in method1:")
if('Africa' in dictionary1.keys()):
    print("Africa Exists")


# Here we loop through the values in dictionary and if AFRICA exitsts it is printed
print("\nChecking if Africa exists in method2:")
for i in dictionary1:
    if(i=="Africa"):
        print("Africa Exists")


# here we find the continents where atleast 50 students are there
print("\nThe continents where there are atleast 50 students")
for i in dictionary1.keys():
    if(dictionary1[i]>=50):
        print(i)

