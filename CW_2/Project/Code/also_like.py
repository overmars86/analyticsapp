import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FC
from flask import send_file
import seaborn as sns
import io, base64
import numpy as np
import pandas as pd

def also_like(doc_uuid):
    user_here = []
    doc_like = []
    doc_like_count = []
    df = pd.read_json('../data/sample_small.json', lines=True)
    df_like = df[['visitor_uuid','subject_doc_id']]
    # doc_uuid = "130822235319-831e8a551d644af105e96c00cdc7b169"
    df_like_doc = df_like.loc[df_like['subject_doc_id'] == doc_uuid]
    like = df_like_doc.groupby(by=['visitor_uuid']).count().sort_values(
        by='subject_doc_id', ascending=False).reset_index()
    for i in range(like.shape[0]):
        df_like_other = df_like.loc[df_like['visitor_uuid'] == like.iloc[i,0]]
        if df_like_other.shape[0] > 0:
            user_here.append(like.iloc[i,0])
        for x in range(len(user_here)):
            df_like_other_2 = df_like.loc[df_like['visitor_uuid'] == user_here[x]]
            df_like_other_3 = df_like_other_2['subject_doc_id'].value_counts().reset_index()
            if df_like_other_3.shape[0] > 0:
                for n in range(df_like_other_3.shape[0]):
                    doc_like.append(df_like_other_3.iloc[n,0])
                    doc_like_count.append(df_like_other_3.iloc[n,1])
    like_final = pd.DataFrame(list(zip(doc_like, doc_like_count)), columns=['Doc Liked', 'Count'])
    like_final = like_final.loc[like_final['Doc Liked'] != doc_uuid]
    like_final.sort_values(by='Count', ascending=False)
    #Styling
    styles = [
    dict(selector="tr:hover",
                props=[("background", "green")]),
    dict(selector="th", props=[("color", "#fff"),
                               ("border", "1px solid black"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("background", "#00cccc"),
                               ("text-transform", "uppercase"),
                               ("font-size", "18px")
                               ]),
    dict(selector="td", props=[("color", "black"),
                               ("border", "1px solid black"),
                               ("padding", "12px 35px"),
                               ("border-collapse", "collapse"),
                               ("font-size", "15px")
                               ]),
    dict(selector="table", props=[
                                    ("font-family" , 'Arial'),
                                    ("margin" , "25px auto"),
                                    ("border-collapse" , "collapse"),
                                    ("border" , "1px solid black"),
                                    ("border-bottom" , "2px solid #00cccc"),                                    
                                      ]),
    dict(selector="caption", props=[("caption-side", "bottom")])]

    like_final = like_final.style.hide_index().set_table_styles(
        styles).set_caption(f"Other users also like to read") # Apply the above styling
    #Styling
    like_final = like_final.to_html()
    return like_final