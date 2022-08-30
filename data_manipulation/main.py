import pandas as pd
from datetime import datetime

colnames = 'error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode',
'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date'

df = pd.read_csv('data/data.csv', names = colnames, header = None, engine = 'python', skiprows = 1)
df['date'] = pd.to_datetime(df['date'], errors = 'coerce')

df['date'] = df['date'].values.astype(float)

sec = 1000000000 #one second in ns
minute = sec * 60 #one minute
hour = minute * 60 #one hour

error_counter = 0
dt_counter = 0

#condition 1
for i in range(len(df.index)):
    if df['severity'].iloc[i] == 'Error':
        error_counter += 1
    if (error_counter > 10) and (dt_counter < minute):
        print(f"ALERT! {error_counter} errors in {dt_counter/sec} seconds") 
        error_counter = 0
        dt_counter = 0 
    dt_counter += df['date'].iloc[i] 
    continue
#condition 2


print('test')