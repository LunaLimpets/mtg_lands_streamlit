import streamlit as st
import plotly.express as px
import pandas as pd

grouped_df = pd.read_csv('grouped_lands.csv')

st.title("Total Price of Basic Lands by Set")

chart_type = st.radio(
    "Select chart type:",
    ('Polar Chart', 'Bar Chart')
)

if chart_type == 'Polar Chart':
    fig = px.bar_polar(
        grouped_df, 
        theta='name', 
        r='usd',
        hover_data=['set', 'usd', 'usd_foil', 'usd_etched'],
        color='set', 
        height=1000,
    )

    fig.update_layout(
        legend=dict(),
        margin=dict(t=50, b=50, l=50, r=50)
    )

    fig.update_layout(
        title={
            'text': "Price of Lands per Set<br><sup> Data From Scryfall.com</sup><sup> sorted by initial release date</sup>",  
            'font': {
                'size': 24,          
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

elif chart_type == 'Bar Chart':
    fig = px.bar(
        grouped_df, 
        x='name', 
        y='usd', 
        color='set', 
        hover_data=['set', 'usd', 'usd_foil', 'usd_etched'],
        height=1000
    )

    fig.update_layout(
        title={
            'text': "Price of Lands per Set<br><sup>Data From Scryfall.com</sup><sup>sorted by initial release date</sup>",  
            'font': {
                'size': 24,          
            },
            'x': 0.5,               
            'xanchor': 'center',   
            'y': 0.95,              
            'yanchor': 'top'       
        },
        titlefont=dict(
            family="Arial, sans-serif",  
        ),
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )

    st.plotly_chart(fig)
