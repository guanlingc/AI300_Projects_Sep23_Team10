
import pandas as pd
from data_loader import initiate_local_connection, get_records, select_features
from data_preprocessor import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn import metrics
from catboost import CatBoostClassifier 
import statistics
from pathlib import Path
import joblib

# Obtaining data 
initiate_local_connection() #establish connection with remote database

# Setting your sql syntax
sql_query = '''
        SELECT * 
        FROM churn_status cs
        INNER JOIN customer c ON cs.customer_id = c.customer_id 
        INNER JOIN account a ON cs.customer_id = a.customer_id
        INNER JOIN city ci ON c.zip_code = ci.zip_code
        INNER JOIN account_usage au ON a.account_id = au.account_id;
'''

df = get_records(sql_query) # data is now in a pandas dataframe

df = select_features(df) # splits df into X (features) and y (target)

df = preprocess_data(df) # Preprocessing of data 

X = df.drop('churn_label', axis=1)
y = df['churn_label']

# Using X and y, train-test split of data before data cleansing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)

# Model training
model = CatBoostClassifier(learning_rate=0.1, depth=2, random_seed=5)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

accuracy_test = metrics.accuracy_score(y_test, y_predict)
print('\nAccuracy_score on test dataset : ', accuracy_test)

# Path("../model").mkdir(exist_ok=True)

# joblib.dump(model, '../model/catboost_model.pkl')

