from main import error_logs
from hypothesis import given, settings, strategies as st
from hypothesis.extra.pandas import column, data_frames, range_indexes
import pandas as pd
from datetime import datetime
import pytest

colnames = ['error_code', 'error_message', 'severity', 'log_location', 'mode', 'model', 'graphics', 'session_id', 'sdkv', 'test_mode', 'flow_id', 'flow_type', 'sdk_date', 'publisher_id', 'game_id', 'bundle_id', 'appv', 'language', 'os', 'adv_id', 'gdpr', 'ccpa', 'country_code', 'date']



def df_gen_hypo():
    df_ex =  data_frames(
        columns = [
            column(name = 'error_code', elements = st.sampled_from([0, 203])),
            column(name = 'severity', elements = st.sampled_from(['Error', 'Successful'])),
            column(name = 'bundle_id', elements = st.sampled_from([ 'com.thg.battleops.shooting.game',
                                                                    'com.pregnantcatemma.virtualpet',
                                                                    'com.mytalkingcatemma.ballerinagames',
                                                                    'com.sayollo.cobra_Android_RealBundleId',
                                                                    'com.sayollo.cobra2_Android_RealBundleId',
                                                                    'com.sayollo.JetpackCatGame'])),
            column(name = 'date', elements = st.datetimes(min_value=datetime(2020,7,1), max_value=datetime(2020,7,2)))],
        index = range_indexes(max_size = 100))
    return df_ex


@settings(max_examples = 10)
@given(df = df_gen_hypo())
def test_error_logs(df):
    print(df)
    print(error_logs(df,'60Min','bundle_id'))
    assert 1