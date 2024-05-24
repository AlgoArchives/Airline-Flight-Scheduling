import pandas as pd
import os
import zipfile

# Ensure the Kaggle API token is in the correct location
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()

# # Download the dataset
# !kaggle datasets download -d usdot/flight-delays

# Unzip the dataset
with zipfile.ZipFile('flight-delays.zip', 'r') as zip_ref:
    zip_ref.extractall('flight-delays')

# Load the dataset into a pandas DataFrame
df = pd.read_csv('flight-delays/flights.csv')

# Display basic information about the dataset
print(df.head())
print(df.info())