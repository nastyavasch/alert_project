import pandas as pd
from datetime import datetime 

colnames = 'error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date'

df = pd.read_csv('data/data.csv', names = colnames, header = None, engine = 'python', skiprows = 1)
df['date'] = pd.to_datetime(df['date'], errors = 'coerce', unit = 's')
df_errors = df[df.severity == 'Error']

#condition 1
def error_logs(df):
    error_num = df_errors.groupby(pd.Grouper(key='date', freq='1Min', dropna=True))['severity'].count()
    result = error_num[error_num > 10]
    return result

#condition 2
def error_logs_for_bundle(df):
    error_num = df_errors.groupby([pd.Grouper(key='date', freq='60Min', dropna=True),'bundle_id'])['severity'].value_counts()
    result = error_num[error_num > 10]
    return result

print(error_logs(df))
print(error_logs_for_bundle(df))