import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FC
from flask import send_file
import seaborn as sns
import io, base64
import numpy as np
import pandas as pd


def doc_by_country(uuid="140222143932-91796b01f94327ee809bd759fd0f6c76"):

    #setting up the chart options
    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.set_style(style = "darkgrid")

    #reading the data and summarize it
    df = pd.read_json('../data/sample_small.json', lines=True)
    df_count = df[['visitor_uuid','visitor_country','env_doc_id']]
    df_count = df_count.loc[df_count['env_doc_id'] == uuid]
    df_count['visitor_uuid'] = df_count['visitor_uuid'].drop_duplicates()
    df_count = df_count[['visitor_uuid','visitor_country']]
    df_count_gp = df_count.groupby(by='visitor_country').count().sort_values(
        by='visitor_uuid', ascending=False).reset_index()
    # df_count = df_count.rename({"visitor_uuid":"No._of_unique_Vistors"}, axis=1)
    # df_count = df_count.rename({"visitor_country":"Vistors'_Countries"}, axis=1)
    
    #identify x and y
    x, y = "visitor_country", "visitor_uuid"

    #build the chart
    sns.barplot(data=df_count_gp, x = x, y = y, hue = x).set(
        title="Doc UUID is : {uuid}".format(uuid=uuid))
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")



def add_cont():
    df = pd.read_json('../data/sample_small.json', lines=True)
    df['Continent'] = 'none'
    df.loc[df['visitor_country'] == 'BR', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'US', 'Continent'] = 'Noth America'
    df.loc[df['visitor_country'] == 'MX', 'Continent'] = 'Noth America'
    df.loc[df['visitor_country'] == 'CA', 'Continent'] = 'Noth America'
    df.loc[df['visitor_country'] == 'GB', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'ES', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'PE', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'IT', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'CO', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'CL', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'AU', 'Continent'] = 'Australia & Oceania'
    df.loc[df['visitor_country'] == 'AR', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'RU', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'FR', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'PT', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'PL', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'NL', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'SV', 'Continent'] = 'Noth America'
    df.loc[df['visitor_country'] == 'DE', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'EC', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'KR', 'Continent'] = 'Asia'
    df.loc[df['visitor_country'] == 'GT', 'Continent'] = 'Noth America'
    df.loc[df['visitor_country'] == 'JP', 'Continent'] = 'Asia'
    df.loc[df['visitor_country'] == 'UA', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'CR', 'Continent'] = 'South America'
    df.loc[df['visitor_country'] == 'IS', 'Continent'] = 'Europe'
    df.loc[df['visitor_country'] == 'RS', 'Continent'] = 'Europe'
    return df

def doc_by_continent(uuid:str("140222143932-91796b01f94327ee809bd759fd0f6c76"), df):
    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.set_style(style = "darkgrid")
    df_count = df[['visitor_uuid','Continent','env_doc_id']]
    df_count = df_count.loc[df_count['env_doc_id'] == uuid]
    df_count['visitor_uuid'] = df_count['visitor_uuid'].drop_duplicates()
    df_count = df_count[['visitor_uuid','Continent']]
    df_count_gp = df_count.groupby(by='Continent').count().sort_values(
        by='visitor_uuid', ascending=False).reset_index()
    
    #identify x and y
    x, y = 'Continent', 'visitor_uuid'

    #build the chart
    sns.barplot(data=df_count_gp, x = x, y = y, hue = x).set(
        title="Doc UUID is : {uuid}".format(uuid=uuid))
    print("done...")
    canvas = FC(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")