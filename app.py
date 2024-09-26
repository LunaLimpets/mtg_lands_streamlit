import streamlit as st
import plotly.express as px
import pandas as pd

#test
grouped_df = pd.DataFrame({
    'name': ['Land 1', 'Land 2', 'Land 3'],
    'usd': [100, 200, 300],
    'set': ['Set A', 'Set B', 'Set C'],
    'usd_foil': [120, 220, 320],
    'usd_etched': [130, 230, 330],
})


st.title("Market Share of Basic Lands by Set")


fig = px.bar_polar(
    grouped_df, 
    theta='name', 
    r='usd',
    hover_data=['set', 'usd', 'usd_foil', 'usd_etched'],
    color='set', 
    height=600,
)

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-.05,
    xanchor="right",
    x=1
))

fig.update_layout(
    title={
        'text': "Market Share of Basic Lands by Set<br><sup>sorted by initial release date</sup>",  
        'font': {
            'size': 24,          
            'color': "Black"     
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
