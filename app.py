import streamlit as st
import plotly.express as px
import pandas as pd

#test
grouped_df = pd.read_csv('grouped_lands.csv')


st.title("Market Share of Basic Lands by Set")


fig = px.bar_polar(
    grouped_df, 
    theta='name', 
    r='usd',
    hover_data=['set', 'usd', 'usd_foil', 'usd_etched'],
    color='set', 
    height=1000,
)

fig.update_layout(
    legend=dict(
    #     orientation="v",
    #     yanchor="bottom",
    #     y=1,  
    #     xanchor="right",
    #     x=1,
    #     title=dict(font=dict(size=14)), 
    #     font=dict(size=12) 
    ),
    margin=dict(t=50, b=50, l=50, r=50)  
)


fig.update_layout(
    title={
        'text': "Price of Lands per Set<br><sup>sorted by initial release date</sup>",  
        'font': {
            'size': 24,          
            # 'color': "Black"     
        },
        'x': 0.5,               
        'xanchor': 'center',   
        'y': 0.95,              
        'yanchor': 'top'       
    },
    titlefont=dict(
        family="Arial, sans-serif",  
    )
)

st.plotly_chart(fig)
