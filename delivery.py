import csv

# A fuction to print the output
def printsPrice(val):
    print("Values is:",str(val))
    return


# creating a csv file and writing the table to it
with open('rates.csv', 'w', newline='') as file:
            fieldnames = ['Weight', 'Price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Weight': '<=1', 'Price': 3.84})
            writer.writerow({'Weight': '1-5', 'Price': 4.8})
            writer.writerow({'Weight': '5-8', 'Price': 5.52})
            writer.writerow({'Weight': '8-12', 'Price': 6.48})
            writer.writerow({'Weight': '12-18', 'Price': 7.92})
            writer.writerow({'Weight': '18-20', 'Price': 8.4})    

# try catch for exiting with float input
try:
    while(1):
        # flag if all conditions fail
        flag = 0

        # getting the input
        weight = int(input("Enter the weight of parcel:"))

        # opening the csv file
        with open('rates.csv', 'r') as file:
            i=0
            reader = csv.reader(file)
            for row in reader:
                # first row is the class names ie Weight & Price
                if(i==0):
                    i+=1
                    continue

                # first row is an edge condition as <=1
                if(i==1):
                    i+=1
                    if(weight<=1):
                        printsPrice(row[1])
                        flag=1
                    continue
                
                # split the row's first element 
                p=row[0].split('-')
                # finding the lower bound from csv
                loweBound = int(p[0])
                # finding the upper bound form csv
                upperBound = int(p[1])
                # checking the input
                if(loweBound < weight and weight <= upperBound):
                    printsPrice(row[1])
                    flag=1
            # if outside all the bounds ie weight>20
            if(flag==0):
                print("No Service")
# if weight is float
except:
    print("DONE")