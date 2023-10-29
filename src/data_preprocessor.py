from sklearn.preprocessing import LabelEncoder
import pandas as pd

label_encoder = LabelEncoder()

def preprocess_data(df):
    df['has_premium_tech_support'] = label_encoder.fit_transform(df['has_premium_tech_support'])
    df['contract_type'] = label_encoder.fit_transform(df['contract_type'])
    df['internet_type'] = label_encoder.fit_transform(df['internet_type'])
    df['has_unlimited_data'] = label_encoder.fit_transform(df['has_unlimited_data'])
    df['churn_label'].replace(['Yes','No',''],[1,0,0], inplace=True)
   
    
    df_labeled = df 

    return df_labeled

def feature_and_targets(df):
    X = df.drop('churn_label', axis=1)
    y = df['churn_label']
    return X, y
