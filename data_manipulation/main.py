import pandas as pd
from datetime import datetime

colnames = 'error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date'

df = pd.read_csv('data/data.csv', names = colnames, header = None, engine = 'python', skiprows = 1)
df['date'] = pd.to_datetime(df['date'], errors = 'coerce')

print(df.info())