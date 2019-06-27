import csv
import os
import nltk

#list of keywords, positive and negative labels
keywords = ['warfarin', 'coumadin', 'dabigatran', 'pradaxa', 'rivaroxaban', 'rivaraox', 'xarelto', 'apixaban', 'apixiban', 'apixa', 'apix', 'dabi', 'eliquis', 'elaquis', 'elliquis', 'savaysa', 'edoxaban', 'edoxa', 'edox']
pos_keywords = ['continue', 'start', 'restart' 'begin', 'use', 'remain', 'back to', 'will be on', 'resume', 'reverse', 'Chronic', 'recommended', 'recommending', 'started', 'bedtime', 'is on',     
                     'mg', 'every day']
neg_keywords = ['discontinue', 'stop', 'hold', 'go off']

#getting the name for all the .txt files in the directory
fName=[]
for root, dirs, files in os.walk("."):  
    for filename in files:
        if (filename.split('.'))[1]=='txt':
            fName.append(filename)
csvw=[['note name','kewyword','sentence','sentence above','sentence below','label']] #first row of csv with headings
lst=[]
for file in fName:
    f=open(file,'r')  
    data = f.read().split('\n')
    data = [x for x in data if x] #removing empty strings
    for keyword in keywords:
        for sentence in data:
            if keyword in sentence:
                lst.append(file)
                lst.append(keyword)
                lst.append(sentence)
                lst.append(data[data.index(sentence)-1])
                lst.append(data[data.index(sentence)+1])
                if any(elem in sentence for elem in pos_keywords): #checking for labels
                    lst.append('positive')
                elif any(elem in sentence for elem in neg_keywords):
                    lst.append('negative')
                else:
                    lst.append('neutral')
                csvw.append(lst)
                lst=[]
    with open("output2.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csvw)
print('finished, open csv now')
