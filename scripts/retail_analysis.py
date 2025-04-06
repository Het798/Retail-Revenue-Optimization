import pandas as pd
import os

# Get the current script directory
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, '..', 'data', 'online_retail_II.xlsx')

# Load the Excel file
df = pd.read_excel(file_path, sheet_name='Year 2009-2010')

# Preview the data
print("✅ Loaded data:")
print(df.head())

# Drop missing customer IDs
df.dropna(subset=['Customer ID'], inplace=True)

# ✅ FIX: Use 'Price' instead of 'UnitPrice'
df['TotalPrice'] = df['Quantity'] * df['Price']

# Save cleaned data
cleaned_path = os.path.join(current_dir, '..', 'data', 'cleaned_data.csv')
df.to_csv(cleaned_path, index=False)
print(f"✅ Cleaned data saved at: {cleaned_path}")
