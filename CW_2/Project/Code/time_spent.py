import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FC
from flask import send_file
import seaborn as sns
import io, base64
import numpy as np
import pandas as pd


#Function to analyize by browser type
def by_time():

    df = pd.read_json('../data/sample_small.json', lines=True)
    #setting up the chart options
    fig, ax = plt.subplots(figsize=(12,12))
    ax = sns.set_style(style = "darkgrid")
    
    df_time = df[['visitor_uuid','event_readtime']]
    df_time['event_readtime'] = df_time['event_readtime'].fillna(0)
    df_time_tot = df_time.groupby(by='visitor_uuid').sum().reset_index().sort_values(
        by='event_readtime', ascending=False)
    df_time_tot['event_readtime'] = df_time_tot['event_readtime'] / 60000
    df_time_tot = df_time_tot.rename(
        columns={'visitor_uuid':'User UUID','event_readtime':'Time spent in Mins'})
    df_time_tot = df_time_tot.iloc[:10, :]
    
    # plt.set_xticklabels(rotation=45)
    x, y = "User UUID", "Time spent in Mins"

    #build the chart
    sns.barplot(data=df_time_tot, x = x, y = y, hue = x).set(
        title="Time spent by user - Top 10")
    plt.xticks(rotation=45)
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")


