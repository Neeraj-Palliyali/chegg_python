# import pandas
# df = pandas.read_csv('C:/Users/Neeraj_P/Desktop/archive/start.csv')
# print(df.head())

from csv import reader
import os
import time


arr = os.listdir('D:/flutter_projects/chegg/archive')
for i in arr:
    with open(f'D:/flutter_projects/chegg/archive/{i}', 'r') as read_obj:
        
        csv_reader = reader(read_obj)
        
        for row in csv_reader:
            
            print(row)
            time.sleep(2)

