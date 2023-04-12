import pandas as pd
import re
import json

# function to map age values to age groups
def map_age_to_group(age):
    # define the age groups
    age_groups = {
        (0, 15): '0-15', 
        (15, 20): '15-20', 
        (20, 25): '20-25', 
        (25, 30): '25-30',
        (30, 35): '30-35', 
        (35, 40): '35-40', 
        (40, 45): '40-45', 
        (45, 50): '45-50', 
        (50, 200): '50+'
    }

    for age_range, age_group in age_groups.items():
        if age in range(*age_range):
            return age_group
    return 'Unknown'

# function to clean narrative
def remove_tags(text):
    clean_text = re.sub('<[^<]+?>', '', text)
    clean_text = re.sub(r'(?:\d+&#\d+;+)+', '', clean_text)
    clean_text = re.sub(r'\( \)', '', clean_text)
    clean_text = re.sub(r'\(\)', '', clean_text)
    clean_text = re.sub(r'\n', '', clean_text)
    clean_text = re.sub(r'\*', '', clean_text)  
     
    return clean_text

def length_age_gender():
    df_all = pd.read_csv('../data/pixstory/pixstory_final.homework2.csv')

    # create a new column for age groups
    df_all['Age_Group'] = df_all['Age'].apply(map_age_to_group)

    # filter out those with too long narrative
    filtered_df = df_all[df_all['Narrative'].str.len() <= 2500]
    
    # clean the narrative
    filtered_df['Narrative'] = filtered_df['Narrative'].apply(remove_tags)

    # group by age group and gender and calculate the mean length of Narrative
    grouped_df = filtered_df[filtered_df['Gender'] != 'others'].groupby(['Age_Group', 'Gender'])['Narrative'].apply(lambda x: x.str.len().mean()).unstack()
    grouped_df = grouped_df.apply(lambda x: round(x, 3))
    grouped_df = grouped_df[['male', 'female']]

    # convert the data frame to dict
    result = []
    for index, row in grouped_df.iterrows():
        for col in grouped_df.columns:
            result.append({
                'age': index,
                'gender': col,
                'mean': row[col] * (-1 if col == 'male' else 1)
            })

    # save the dict as json
    with open("length.json", "w") as outfile:
        json.dump(result, outfile)
