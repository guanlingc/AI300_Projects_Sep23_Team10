import pandas as pd
import pymysql


ENDPOINT = 'heicoders-playground.c2ced10ceyki.ap-southeast-1.rds.amazonaws.com'
PORT = 3306
USERNAME = 'student300'
DBNAME = 'ai300_capstone'
PASSWORD = 'heicoders_AI300'   
CURSORCLASS = pymysql.cursors.DictCursor

# sql_query = '''
#         SELECT * 
#         FROM churn_status cs
#         INNER JOIN customer c ON cs.customer_id = c.customer_id 
#         INNER JOIN account a ON cs.customer_id = a.customer_id
#         INNER JOIN city ci ON c.zip_code = ci.zip_code
#         INNER JOIN account_usage au ON a.account_id = au.account_id;
# '''


def initiate_local_connection():
    try:
        connection = pymysql.connect(host=ENDPOINT,
                                     port=PORT,
                                     user=USERNAME,
                                     passwd=PASSWORD,
                                     db=DBNAME,
                                     cursorclass=CURSORCLASS)
        print('[+] Local Connection Successful')
    except Exception as e:
        print(f'[+] Local Connection Failed: {e}')
        connection = None

    return connection

def get_records(sql_query):
    try:
        with initiate_local_connection().cursor() as cursor:
            cursor.execute(sql_query)

        # Connection is not autocommit by default, so we must commit to save changes
        initiate_local_connection().commit()
        
        # Fetch all the records from SQL query output
        results = cursor.fetchall()
        
        # Convert results into pandas dataframe
        df = pd.DataFrame(results)
        
        print(f'Successfully retrieved records')
        
        return df
        
    except Exception as e:
        print(f'Error encountered: {e}')


def select_features(df):
    selected_df = df[['has_premium_tech_support', 'contract_type', 'internet_type', 
            'has_unlimited_data', 'num_dependents','num_referrals','churn_label']]

    return selected_df

    
# df = get_records(sql_query)
# df = df['has_premium_tech_support', 'contract_type', 'internet_type', 
#             'has_unlimited_data', 'num_dependents','num_referrals']


# df