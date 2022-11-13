# import Libraries
import os
import pandas as pd
from bs4 import BeautifulSoup

# Set the path to the folder containing the html files
filename = []
for files in os.listdir("./train/"):
    if files.endswith(".html"):
        filename.append(files)

# Create a list columns for html files
column_names = ['File_Name','Location','Sector','Employees','Company_Background','Revenue','Net_Valuation','Share_Price']

# Create a dataframe
df = pd.DataFrame(columns = column_names)

# Loop through the html files and extract the data
for file in filename:
    with open("./train/"+file, "r", encoding="utf8") as f:
        soup = BeautifulSoup(f)
        data = []
        row = []
        data.append(file)
        for i in soup.find_all('p'):
                data.append(i.text)
        row.append(data[0])
        row.append(data[1].split(':')[1])
        row.append(data[2].split(':')[1])
        row.append(data[3].split(':')[1])
        row.append(data[6])
        row.append(data[7].split(':')[1])
        row.append(data[8].split(':')[1])
        row.append(data[9].split(':')[1])   
        df.loc[len(df)] = row
        del row, data

# Load File_Name from train.csv
train = pd.read_csv("train.csv")
df = pd.merge(train,df, 
                   on='File_Name', 
                   how='inner')

# rearrange the columns and save the final dataframe
df = df [['File_Name','Location','Sector','Employees','Revenue','Net_Valuation','Share_Price','Company_Background','Product']]
df.to_csv("train0.csv", index=False)
del df, train, filename, column_names

# Test to CSV
filename = []
for files in os.listdir("./test/"):
    if files.endswith(".html"):
        filename.append(files)

column_names = ['File_Name','Location','Sector','Employees','Company_Background','Revenue','Net_Valuation','Share_Price']
df = pd.DataFrame(columns = column_names)
for file in filename:
    with open("./test/"+file, "r", encoding="utf8") as f:
        soup = BeautifulSoup(f)
        data = []
        row = []
        data.append(file)
        for i in soup.find_all('p'):
                data.append(i.text)
        row.append(data[0])
        row.append(data[1].split(':')[1])
        row.append(data[2].split(':')[1])
        row.append(data[3].split(':')[1])
        row.append(data[6])
        row.append(data[7].split(':')[1])
        row.append(data[8].split(':')[1])
        row.append(data[9].split(':')[1])   
        df.loc[len(df)] = row
        del row, data

df = df [['File_Name','Location','Sector','Employees','Revenue','Net_Valuation','Share_Price','Company_Background']]
df.to_csv("test0.csv", index=False)
