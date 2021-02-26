# get the speed of the car 
speed=int(input("The speed of the car in km per hour:"))
# enter the number of hours it traveled
hours=int(input("The number of hours the car has traveled:"))

# print the required output
print("HOUR     Distance traveled")
distance=1
for i in range(1,hours+1):
    distance=speed*i
    print(str(i)+"               "+str(distance))
