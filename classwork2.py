"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: the internet
    I attended lecture today.
    Row: 4
    Seat: 42
"""

import pandas as pd

# Ask user for input and output file names
inFile = input("Enter input file name: ")
outFile = input("Enter output file name: ")

# Open and read file into dataframe
df = pd.read_csv(inFile)

# Select rows where 'Grade' = 3 and 'Year' = 2019, and write to new csv
out_df = df[(df['Grade'] == 3) and (df['Year'] == 2019)]

# .to_csv(outFile)
out_df.to_csv((outFile))
