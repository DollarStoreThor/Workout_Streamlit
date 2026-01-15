import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

DOW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
       'Saturday']

Workouts_Per_Day = {}
@st.cache_data
def load_daily_workouts(file_name = 'Workout 2026.xlsx'):

    df = pd.read_excel(file_name)[:6]
    # Iterate over the days in the week
    for day in DOW:
        # Grab the daily excercises
        current_day_excercises = df[day]
        Workouts_Per_Day[day] = []

        # Iterate over the excercises
        for item in current_day_excercises.dropna()[1:]:

            # Ensure it's not a rest day
            if item != "Rest":
                # Load in the Workout from the .xlsx excel sheet named 'item'
                Workouts_Per_Day[day].append(pd.read_excel(file_name, sheet_name=item)['Excercise Name'][0])
    
    return Workouts_Per_Day


@st.cache_data
def plot_daily_workouts(file_name = 'Workout 2026.xlsx', day = 'Wednesday', Workouts_Per_Day = Workouts_Per_Day):
    
    Figures = []
    for workout in Workouts_Per_Day[day]:
        day_df = pd.read_excel(file_name, sheet_name=workout)
        
        # COLUMNS -------------------
        # Excercise Name	
        # Excercise Description	
        # Date	
        # Rest between Sets (Minutes)	
        # Weight (lbs)	Sets (Count)	
        # Reps (Count)	
        # Volume (lbs)
        # ---------------------------

        figure = px.bar(data_frame=day_df, x='Date', y='Volume (lbs)',hover_data=['Date', 'Sets (Count)', 'Reps (Count)','Weight (lbs)' ,'Volume (lbs)'] ,title=day_df['Excercise Name'][1], color='Volume (lbs)', color_continuous_scale=px.colors.sequential.dense)
        Figures.append(figure)

    return Figures

    