# EasyMatchy

Text Mining using Match Words From Multiple Files : for Clinical Notes

## Project Concept

- load txt Note File

- match any word exits in Keyword File from lines with txt in Note 

- exctract the sentnce that contain the word from Keyword

- label postive for any matching word per line in pos txt 

- label negative for any matching word per line in neg txt 

- label neutral for none matching from pos or neg 

- exctract date from file1 export in excel file as following 

- name of text Note File , matched word from keyword, exctracted sentnce , label


#### Format of CSV
+ file1 name | matched sentence | Label ( postive or negative or neutral )

**Steps**

**(1) Exploratory data analysis (EDA)**


- Descriptive statistics of word counts
 
- Identify common words
 
- Identify uncommon words
 
- Libraries for text preprocessing
 
- Creating a list of stop words and adding custom stopwords
 
- Word cloud
 
- Most frequently occuring words
 
- Convert most freq words to dataframe for plotting bar plot
 
- Barplot of most freq words
 
- Most frequently occuring Bi-grams
 
- Most frequently occuring Tri-grams
 
- Barplot of most freq Tri-grams
 
- Fetch document for which keywords needs to be extracted
 
- Generate tf-idf for the given document



**(2) Match Words From Multiple Files**

load txt Note File

Match any word exits in Keyword File from lines with txt in Note

Exctract the sentnce that contain the word from Keyword

Label postive for any matching word per line in pos txt

Label negative for any matching word per line in neg txt

Label neutral for none matching from pos or neg

Exctract date from file1 export in excel file as following

Name of text Note File , matched word from keyword, exctracted sentnce , label Format of CSV

Note Name | matched sentence | Label ( postive or negative or neutral )

**How to Use **

- Requirements ;

- pip3 install click

- pip3 install fuzzywuzzy


1-Obtain your clinical notes

2-you can merge all clinical notes in one for data exploration (optional)

3-Use terminal command ( cat * > ClinicalNotes.txt ) to merge all notes

4-Use EasyMatchy.ipynb Jupyter Notebook for data exploration

5-Use Task-Match.ipynb Jupyter Notebook for each note for matching and labeling

6-Use the following command for mlutiple files match

python3  matchtagger.py bulkmatch .

Note : put all notes in same folder of matchtagger.py





