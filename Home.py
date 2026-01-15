import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

from workout import load_daily_workouts


DOW = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
       'Saturday']


# Initalizing the Workouts_Per_Day dictionary that will be used through other pages
Workouts_Per_Day = {}
Workouts_Per_Day = load_daily_workouts(file_name = 'Workout 2026.xlsx')


day = 'Sunday'
# Excercise Name	Excercise Description	Date	Rest between Sets (Minutes)	Weight (lbs)	Sets (Count)	Reps (Count)	Volume (lbs)

for workout in Workouts_Per_Day[day]:
    day_df = pd.read_excel('Workout 2026.xlsx', sheet_name=workout)
    figure = px.bar(data_frame=day_df, x='Date', y='Volume (lbs)',hover_data=['Date', 'Sets (Count)', 'Reps (Count)','Weight (lbs)' ,'Volume (lbs)'] ,title=day_df['Excercise Name'][1], color='Volume (lbs)', color_continuous_scale=px.colors.sequential.dense)
    st.plotly_chart(figure)

