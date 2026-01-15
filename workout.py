import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

DOW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
       'Saturday']

Workouts_Per_Day = {}
@st.cache_data
def load_daily_workouts():
    # Iterate over the days in the week
    for day in DOW:
        
        # Grab the daily excercises
        current_day_excercises_series = pd.read_csv(f'./Datasets/Daily Excercise Series/{day}.csv')
        Workouts_Per_Day[day] = current_day_excercises_series[day].values.tolist()
    return Workouts_Per_Day


@st.cache_data
def plot_daily_workouts(day = 'Wednesday', Workouts_Per_Day = Workouts_Per_Day):
    
    Figures = []
    for workout in Workouts_Per_Day[day]:
        day_df = pd.read_csv(f'./Datasets/Excercises/{workout}.csv')
        figure = px.bar(data_frame=day_df, x='Date', y='Volume (lbs)',hover_data=['Date', 'Sets (Count)', 'Reps (Count)','Weight (lbs)','Volume (lbs)'] ,title=day_df['Excercise Name'][1], color='Volume (lbs)', color_continuous_scale=px.colors.sequential.dense)
        
        # COLUMNS -------------------
        # Excercise Name	
        # Excercise Description	
        # Date	
        # Rest between Sets (Minutes)	
        # Weight (lbs)	Sets (Count)	
        # Reps (Count)	
        # Volume (lbs)
        # ---------------------------

        Figures.append(figure)

    return Figures

    