import csv
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
1

with open('rates.csv', 'r') as file:
            i=0
            reader = csv.reader(file)
            for row in reader:
                if(i==0 or i==1):
                    i+=1
                    continue
                p=row[0].split('-')
                print(int(p[0]))