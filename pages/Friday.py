from workout import load_daily_workouts, plot_daily_workouts
import streamlit as st
import pandas as pd
import plotly.express as px

day = 'Friday'
file_name = 'Workout 2026.xlsx'
Workouts_Per_Day = load_daily_workouts(file_name = file_name)

# Excercise Name	Excercise Description	Date	Rest between Sets (Minutes)	Weight (lbs)	Sets (Count)	Reps (Count)	Volume (lbs)

daily_workout_plotly_figures = plot_daily_workouts(file_name = file_name, day = day, Workouts_Per_Day = Workouts_Per_Day)
for figure in daily_workout_plotly_figures:
    st.plotly_chart(figure)