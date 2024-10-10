import streamlit as st
import plotly.express as px
import pandas as pd


st.set_page_config(layout="wide")

grouped_df = pd.read_csv('grouped_lands.csv')

st.title("Total Price of Basic Lands by Set ")
st.header("Data From Scryfall.com")

col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
with col2:
    st.markdown(
        '''<div style="text-align: Centure;  display: inline-block;width: auto; left:30%"><h4>Notes/Warnings:</h4>
        <li>This data is not live</li>
        <li>Last update from scryfall was in early October 2024</li>
        <li>This only displays cards with a USD price</li>
        </div>
        ''', unsafe_allow_html=True
    ) 
with col3:
    st.markdown(
        '''<div style="text-align: Left;  display: inline-block;width: auto; left:30%;margin-bottom:5%"><h4>For Easier Viewing:</h4>
        <li>View in "Fullscreen" or on Desktop</li>
        <li>Ctrl+F and Click set name in Legend to remove from graph</li>
        <li>Mouseover/Touch for details</li>
        </div>
        ''', unsafe_allow_html=True
    ) 
with col1:
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
        height=1250,
    )
    
    fig.update_layout(
        legend=dict(
            orientation="h", 
            yanchor="top", 
            y=-0.1, 
            xanchor="center", 
            x=0.5 
            ),
        margin=dict(t=50, b=50, l=50, r=50),

    )


    fig.update_layout(
        title={
            'text': "Sorted outward by initial release date",  
            'font': {
                'size': 18,          
            },
            'x': 0.5,               
            'xanchor': 'center',   
            'y': 1,              
            'yanchor': 'top'       
        },
        titlefont=dict(
            family="Arial, sans-serif",  
        )
    )

    st.plotly_chart(fig, use_container_width=True)

elif chart_type == 'Bar Chart':
    fig = px.bar(
        grouped_df, 
        x='name', 
        y='usd', 
        color='set', 
        hover_data=['set', 'usd', 'usd_foil', 'usd_etched'],
        height=1000,
        labels={
                     "name": "Land Type",
                     "usd": "Price in USD"
        }
    )
 
    fig.update_layout(
        title={
            'text': "Sorted by initial release date",  
            'font': {
                'size': 18,          
            },
            'x': 0.5,    
            'xanchor': 'center',   
            'y': 1,              
            'yanchor': 'top'       
        },
        titlefont=dict(
            family="Arial, sans-serif",  
        ),
        margin=dict(t=50, b=100, l=50, r=50), 
        legend=dict(
            orientation="h", 
            yanchor="bottom", 
            y=-1.3,  
            xanchor="center", 
            x=0.5
        ),
        xaxis_title=dict(
            font=dict(size=14),
           
        )
    )

    st.plotly_chart(fig, use_container_width=True)
    # st.markdown(''' 
    #     <style>
    #     .appview-container .main .block-container {
    #         padding-left: 0%;  /* Adjust these values */
    #         padding-right: 0%; /* Adjust these values */
    #     }
    #     </style>
    # ''', unsafe_allow_html=True)
