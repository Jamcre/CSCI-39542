"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: the internet
    I attended lecture today.
    Row: 4
    Seat: 42
"""

import pandas as pd

# ask user for input and output file names
inFile = input("Enter input file name: ")
outFile = input("Enter output file name: ")

# open and read file into dataframe
df = pd.read_csv(inFile)

# select rows where 'Grade' = 3 and 'Year' = 2019
df = df.loc[(df['Grade'] == '3')]
df = df.loc[(df['Year'] == 2019)]

# create csv from new df
df.to_csv(outFile, index=False)
