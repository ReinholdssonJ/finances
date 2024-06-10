# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import functions as f
import pandas as pd
import matplotlib.pyplot as plt

#load CSV files
csv_folder = "C:/Users/jakob/OneDrive/finances/csv/"
files = ['amex_statement_1.csv',
         'amex_statement_2.csv',
         "nationwide_statement_1.csv",
         "nationwide_statement_2.csv"]


amex_1_df = pd.read_csv(f"{csv_folder}{files[0]}")
amex_2_df = pd.read_csv(f"{csv_folder}{files[1]}")
nationwide_1_df = pd.read_csv(f"{csv_folder}{files[2]}", encoding='latin1')
nationwide_2_df = pd.read_csv(f"{csv_folder}{files[3]}", encoding='latin1')

# Clean Nationwide data
nationwide_df = pd.concat([nationwide_1_df, nationwide_2_df], ignore_index=True)

nationwide_df['Paid in'] = nationwide_df['Paid in'].astype('str')
nationwide_df['Paid in'] = nationwide_df['Paid in'].apply(lambda x : f.remove_substr(x))
nationwide_df['Paid in'] = nationwide_df['Paid in'].astype('float')

nationwide_df['Paid out'] = nationwide_df['Paid out'].astype('str')
nationwide_df['Paid out'] = nationwide_df['Paid out'].apply(lambda x : f.remove_substr(x))
nationwide_df['Paid out'] = nationwide_df['Paid out'].astype('float')

nationwide_df = nationwide_df.fillna(0)

nationwide_df['Amount'] = nationwide_df['Paid out'] - nationwide_df['Paid in']

nationwide_df['Date'] = pd.to_datetime(nationwide_df['Date'], format='%d-%b-%y').dt.strftime('%d/%m/%Y')
                                       
# Combine Amex data with Current Account Data
narrow_col = ['Date', 'Description', 'Amount']

narrow_df = pd.concat([amex_1_df[narrow_col], 
                       amex_2_df[narrow_col],
                       nationwide_df[narrow_col]], 
                      ignore_index=True)

narrow_df['Date'] = pd.to_datetime(narrow_df['Date'], format="%d/%m/%Y")

narrow_df = narrow_df.sort_values(by='Date')

narrow_df['Amount'] = narrow_df['Amount'].apply(lambda x: x*(-1)) 

# Create a new "balance" column
narrow_df['balance'] = narrow_df['Amount'].cumsum()
narrow_df['montly_rolling_balance'] = narrow_df['balance'].rolling(window=30).mean()

# Plot the balance over time
plot_over_time(narrow_df, 'balance')









