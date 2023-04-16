import pandas as pd
import json

# Load the CSV file into a Pandas dataframe
data='./data/geo_df.csv'

df = pd.read_csv(data)

# Define lambda function to extract values
def extract_values(x):
    loc_dict = eval(x)
    name = loc_dict.get('name', None)
    latitude = loc_dict.get('latitude', None)
    longitude = loc_dict.get('longitude', None)
    return pd.Series([name, latitude, longitude])

# Apply lambda function to 'location' column and create new columns
df[['name', 'latitude', 'longitude']] = df['Location'].apply(lambda x: extract_values(x))

# Drop original 'location' column
df.drop('Location', axis=1, inplace=True)

# Drop rows where 'name' is null
df = df[pd.notna(df['name'])]

# Split the data into separate columns for age and location
age = df["Age"].tolist()
location = df["name"].tolist()

# Combine the age and location lists into a list of dictionaries
data = [{"age": a, "name": l} for a, l in zip(age, location)]

# Get summary statistics for the age column
summary = df["Age"].describe()

# Convert the summary statistics to a dictionary
summary_dict = summary.to_dict()

# Add the number of rows to the summary dictionary
summary_dict['nrows'] = df.shape[0]

# Combine the summary and data dictionaries into a single dictionary
data_dict = {'summary': summary_dict, 'data': data}

# Write the data dictionary to a JSON file
with open('data.json', 'w') as f:
    json.dump(data_dict, f, indent=2)