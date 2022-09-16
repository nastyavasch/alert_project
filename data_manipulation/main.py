import pandas as pd

colnames = ['error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date']

df = pd.read_csv('data/data.csv', names = colnames, header = None, engine = 'python', skiprows = 1)
df['date'] = pd.to_datetime(df['date'], errors = 'coerce', unit = 's')
df_errors = df[df.severity == 'Error']

#condition 1
def error_logs(df, freq, col= 'severity'):
    df_errors = df[df.severity == 'Error']
    error_num = df_errors.groupby([pd.Grouper(key='date', freq=freq, dropna=True)] + [col])['severity'].count()
    result = error_num[error_num > 10]
    return result
# freq - time frequency
# col - columns we want to add to group by. default = 'severity' column

print(error_logs(df,'1Min')) #condition 1
print(error_logs(df,'60Min', 'bundle_id')) #condition 2
