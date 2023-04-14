import pandas as pd 
import numpy as np

def generate_avg_toxicity_age_gender():
    pixstory_filepath = '../data/pixstory/pixstory_final.csv'
        
    pixstory_df = pd.read_csv(pixstory_filepath, delimiter=',', encoding='utf-8')
    
    pixstory_df = pixstory_df[['Gender', 'Age', 'toxicity']]
    
    pixstory_df = pixstory_df[pixstory_df['Gender'].str 
                              .contains('|'.join(['male', 'female', 'others']), na=False, case=False)]
    
    pixstory_df = pixstory_df[(pixstory_df['Age'] >= 10) & (pixstory_df['Age'] <= 80)]
    
    pixstory_df = pixstory_df[pixstory_df['toxicity'].notna()]
    
    def bin_ages(age):
        if (age >= 10) & (age < 20):
            return '10-19'
        if (age >= 20) & (age < 30):
          return '20-29'
        if (age >= 30) & (age < 40):
          return '30-39'
        if (age >= 40) & (age < 50):
          return '40-49'
        if (age >= 50) & (age < 60):
          return '50-59'
        if (age >= 60) & (age < 70):
          return '60-69'
        if (age >= 70) & (age <= 80):
          return '70-80' 
    
    pixstory_df['Age'] = pixstory_df['Age'].apply(bin_ages)
    pixstory_df = pixstory_df.rename(columns={'Age': 'age_group'})
    
    pixstory_df = pd.pivot_table(pixstory_df, values='toxicity', index='age_group', 
                                  columns=['Gender'], aggfunc=np.mean)
    
    pixstory_df.reset_index() \
                .to_csv('../data/pixstory/avg_toxicity_age_gender.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    generate_avg_toxicity_age_gender()
