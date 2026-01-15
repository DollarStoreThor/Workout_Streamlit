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

