import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles_nov_2019.csv')

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Fill missing values with something meaningful
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('01 January 1900')  
df['rating'] = df['rating'].fillna('Unknown')

# 3. Convert 
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')  # convert to datetime type
df['date_added'] = df['date_added'].dt.strftime('%Y-%m-%d')  # format for Excel

# 4. Clean up and standardize text fields
df['type'] = df['type'].str.strip().str.lower()     
df['country'] = df['country'].str.strip()
df['rating'] = df['rating'].str.strip().str.upper()  

# 5. Make column names lowercase with underscores 
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

