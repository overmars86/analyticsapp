import matplotlib as plt
import numpy as np
import pandas as pd


def doc_by_country(uuid="140222143932-91796b01f94327ee809bd759fd0f6c76"):
    df = pd.read_json('../data/sample_small.json', lines=True)
    df_count = df[['visitor_uuid','visitor_country','env_doc_id']]
    df_count = df_count.loc[df_count['env_doc_id'] == uuid]
    df_count['visitor_uuid'] = df_count['visitor_uuid'].drop_duplicates()
    df_count = df_count[['visitor_uuid','visitor_country']]
    df_count_gp = df_count.groupby(by='visitor_country').count().sort_values(by='visitor_uuid', 
        ascending=False).reset_index()
    df_count_gp.plot(kind='bar', x='visitor_country')