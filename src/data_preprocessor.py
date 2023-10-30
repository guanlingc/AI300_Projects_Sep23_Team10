import pandas as pd

def preprocess_data(df):
    df['has_premium_tech_support'].replace(['Yes','No'],[1,0], inplace=True) 
    df['contract_type'].replace(['Month-to-Month', 'Two Year', 'One Year'],[0,1,2], inplace=True) 
    df['internet_type'].replace(['Fiber Optic', 'Cable', 'DSL', 'None'],[1,2,3,0], inplace=True) 
    df['has_unlimited_data'].replace(['Yes','No'],[1,0], inplace=True)

    df['churn_label'].replace(['Yes','No',''],[1,0,0], inplace=True)
    
    
    
    df_labeled = df 

    return df_labeled

def feature_and_targets(df):
    X = df.drop('churn_label', axis=1)
    y = df['churn_label']
    return X, y
