import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import datetime

from workout import load_daily_workouts, plot_daily_workouts


day = datetime.datetime.now().strftime("%A")
file_name = 'Workout 2026.xlsx'
Workouts_Per_Day = load_daily_workouts()

st.header("Today is " + day + " the " + datetime.datetime.now().strftime("%d") + " of " + datetime.datetime.now().strftime("%B"))

# COLUMNS -------------------
# Excercise Name	
# Excercise Description	
# Date	
# Rest between Sets (Minutes)	
# Weight (lbs)	Sets (Count)	
# Reps (Count)	
# Volume (lbs)
# ---------------------------

with st.sidebar:
    day = st.radio(
        "Choose a different day",
        ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday')
    )
    print(day)

st.subheader("Showing Plots for " + day)
daily_workout_plotly_figures = plot_daily_workouts(day = day, Workouts_Per_Day = Workouts_Per_Day)
for figure in daily_workout_plotly_figures:
    st.plotly_chart(figure)