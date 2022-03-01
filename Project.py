from statistics import correlation
import numpy as np
import csv

file1 = open("Sleep Vs Coffee.csv")
file2 = open("Student Vs Presentdays.csv")
reader1 = csv.reader(file1)
file_data1  = list(reader1)
file_data1.pop(0)

reader2 = csv.reader(file2)
file_data2  = list(reader2)
file_data2.pop(0)

def getDataSource():
    SleepList = []
    CoffeeList = []
    MarksList = []
    PresentDaysList = []
    for i in range(len(file_data1)):
        sleep = file_data1[i][2]
        coffe = file_data1[i][1]
        marks = file_data2[i][1]
        presentDays = file_data2[i][2]
        SleepList.append(float(sleep))
        CoffeeList.append(float(coffe))
        MarksList.append(float(marks))
        PresentDaysList.append(float(presentDays))
    correlation1 = np.corrcoef(SleepList,CoffeeList)
    correlation2 = np.corrcoef(MarksList,PresentDaysList)
    print(correlation1)
    print(correlation2)
getDataSource()