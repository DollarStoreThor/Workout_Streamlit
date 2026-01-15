# Used Libraries
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import datetime

# Custom Script Import
from workout import load_daily_workouts, plot_daily_workouts

# Loading current day
day = datetime.datetime.now().strftime("%A")
Workouts_Per_Day = load_daily_workouts()

# Header
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

# Sidebar
with st.sidebar:
    day = st.radio(
        "Choose a different day",
        ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday')
    )
    print(day)

# Plotly Charts
st.subheader("Showing Plots for " + day)
daily_workout_plotly_figures = plot_daily_workouts(day = day, Workouts_Per_Day = Workouts_Per_Day)

# for figure in daily_workout_plotly_figures:
#    st.plotly_chart(figure)


# Editing the Data
for workout in Workouts_Per_Day[day]:
    st.session_state.df = pd.read_csv(f'./Datasets/Excercises/{workout}.csv')

    
    # Plot the data
    st.plotly_chart(daily_workout_plotly_figures[workout])

    edited_df = st.data_editor(st.session_state.df, use_container_width=True, num_rows="dynamic")

    # Save Changes Button
    if st.button(f'Save Changes to {workout}', key=workout):
        st.session_state.df = edited_df
        # Ensure index is not written to CSV
        st.session_state.df.to_csv(f'./Datasets/Excercises/{workout}.csv', index=False) 
        st.success("Changes saved to " + f'./Datasets/Excercises/{workout}.csv' + "!")

        Workouts_Per_Day = load_daily_workouts()
        daily_workout_plotly_figures = plot_daily_workouts(day = day, Workouts_Per_Day = Workouts_Per_Day)

    
    st.write('---')

