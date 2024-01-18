#Import Modules
import os
import csv

# Designate path to the PyBank csv file 
DataPath = os.path.join('Resources','budget_data.csv')

#Read the csv file
with open(DataPath) as DataFile:
    DataReader = csv.reader(DataFile, delimiter=',')
    header = next(DataReader)

#Create empty lists for Months and Profit/Loss
    months = []
    PandL = []

#Create the lists   
    for row in DataReader:
        months.append(row[0])
        PandL.append(row[1])

    #Make PandL List integers
    PandL_Integers=[]
    for number in PandL:
        PandL_Integers.append(int(number))

#Find Total Months
    ListLength = int(len(months))

#Find Net Total
    NetTotal = 0
    for num in PandL_Integers:
        NetTotal += int(num)

#Find the Average Change in Profit/Loss 
    #Make a List of Changes over Time
    i=0
    Change = 0
    ChangeList = []
    for number in PandL_Integers:
            Change = (number - (PandL_Integers[i-1]))
            if (i > 0):
                 ChangeList.append(Change)
            i=i+1

    #Find Sum and Average
    SumChange = 0
    for numbers in ChangeList:
         SumChange += int(numbers)
    AvChange = round(SumChange/len(ChangeList),2)

#Find Greatest Increase and Decrease in Profits
    GreatestInc = max(ChangeList)
    GreatestDec = min(ChangeList)

#Delete first entry from months list
    months.pop(0)

#Find months associated with Greatest Increase/Decrease in Profits
    Inc_Index = ChangeList.index(GreatestInc)
    Inc_Month = months[Inc_Index]
    Dec_Index = ChangeList.index(GreatestDec)
    Dec_Month = months[Dec_Index]

# #Print Analysis
    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Months: {ListLength}')
    print(f'Total: ${NetTotal}')
    print(f'Average Change: ${AvChange}')
    print(f'Greatest Increase in Profits: {Inc_Month} (${GreatestInc})')
    print(f'Greatest Decrease in Profits: {Dec_Month} (${GreatestDec})')

#Write Analysis to Text File
    AnalysisPath = os.path.join('Analysis','PyBank_Analysis_JMeyer.txt')

    with open(AnalysisPath, 'w') as Text_File:
        print('Financial Analysis', file=Text_File)
        print('-----------------------------', file=Text_File)
        print(f'Total Months: {ListLength}', file=Text_File)
        print(f'Total: ${NetTotal}', file=Text_File)
        print(f'Average Change: ${AvChange}', file=Text_File)
        print(f'Greatest Increase in Profits: {Inc_Month} (${GreatestInc})', file=Text_File)
        print(f'Greatest Decrease in Profits: {Dec_Month} (${GreatestDec})', file=Text_File)
     

    