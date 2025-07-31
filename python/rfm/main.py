import pandas as pd
from datetime import datetime

df = pd.read_csv('transactions.csv')

today = datetime(2025, 7, 25)

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (today - pd.to_datetime(x).max()).days, # recency
    'InvoiceNo': 'count', # frequency
    'Amount': 'sum' # monetary
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

print(rfm)