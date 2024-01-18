#Import Modules
import os
import csv
import statistics

# Designate path to the PyBank csv file 
PollDataPath = os.path.join('Resources','election_data.csv')

#Read the csv file
with open(PollDataPath) as Voter_File:
    VoteReader = csv.reader(Voter_File, delimiter=',')
    header = next(VoteReader)

#Create empty lists for Votes and Populate it
    Votes = []
    for row in VoteReader:
        Votes.append(row[2])

#Total number of Votes Cast
    TotalVotes = len(Votes)

#List of Candidates
    Cand_List = []
    for name in Votes:
        if name not in Cand_List:
                Cand_List.append(name)

#Count the Values for each Candidate
    Cand_1_Count = Votes.count(Cand_List[0])
    Cand_2_Count = Votes.count(Cand_List[1])
    Cand_3_Count = Votes.count(Cand_List[2])

#Percentage of Votes for each Candidate
    Cand_1_Pct = round((Cand_1_Count/TotalVotes)*100,3)
    Cand_2_Pct = round((Cand_2_Count/TotalVotes)*100,3)
    Cand_3_Pct = round((Cand_3_Count/TotalVotes)*100,3)

#Find Winner
    Winner = statistics.mode(Votes)

#Print Analysis
    print('Election Results')
    print('------------------------------')
    print(f'Total Votes: {TotalVotes}')
    print('------------------------------')
    print(f'{Cand_List[0]}: {Cand_1_Pct}% ({Cand_1_Count})')
    print(f'{Cand_List[1]}: {Cand_2_Pct}% ({Cand_2_Count})')
    print(f'{Cand_List[2]}: {Cand_3_Pct}% ({Cand_3_Count})')
    print('------------------------------')
    print(f'Winner: {Winner}')
    print('------------------------------')

#Write Output to Text File
    VoteAnalysisPath = os.path.join('Analysis','PyPoll_Analysis_JMeyer.txt')

    with open(VoteAnalysisPath, 'w') as Text_File:
        print('Election Results', file=Text_File)
        print('------------------------------', file=Text_File)
        print(f'Total Votes: {TotalVotes}', file=Text_File)
        print('------------------------------', file=Text_File)
        print(f'{Cand_List[0]}: {Cand_1_Pct}% ({Cand_1_Count})', file=Text_File)
        print(f'{Cand_List[1]}: {Cand_2_Pct}% ({Cand_2_Count})', file=Text_File)
        print(f'{Cand_List[2]}: {Cand_3_Pct}% ({Cand_3_Count})', file=Text_File)
        print('------------------------------', file=Text_File)
        print(f'Winner: {Winner}', file=Text_File)
        print('------------------------------', file=Text_File)
        