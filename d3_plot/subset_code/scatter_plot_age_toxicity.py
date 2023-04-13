import pandas as pd
import numpy as np

def get_pixstory_df(pixstory_df_path):
    pixstory_df = pd.read_csv(pixstory_df_path)
    return pixstory_df 

def subset_pixstory_df(pixstory_df):
    subset_df = pixstory_df[["Gender", "Age", "toxicity"]]

    q_low = subset_df["toxicity"].quantile(0.05)
    q_hi  = subset_df["toxicity"].quantile(0.95)

    df_filtered = subset_df[(subset_df["toxicity"] < q_hi) & (subset_df["toxicity"] > q_low)].sample(frac = 0.5)

    df_filtered["Gender"] = df_filtered["Gender"].replace(np.nan, "other")
    df_filtered["Gender"] = df_filtered["Gender"].replace("others", "other")

    df_filtered.to_csv('../subset_data/scatter_plot_age_toxicity.csv', index=False)
    return df_filtered


def run_subset():
    pixstory_df_path = "../../data/pixstory/pixstory_detoxify.csv"
    pixstory_df = get_pixstory_df(pixstory_df_path)
    pixstory_df = subset_pixstory_df(pixstory_df)

if __name__ == '__main__':
    run_subset()