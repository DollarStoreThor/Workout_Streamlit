import numpy as np
import pandas as pd
import streamlit as st


df = pd.read_excel('Workout 2026.xlsx')[:6]
DOW = df.columns

Excercises_Per_Day = {}
for day in DOW:
    current_day_excecises = df[day]
    Excercises_Per_Day[day] = []


    #print(current_day_excecises.dropna())

    for item in current_day_excecises.dropna()[1:]:
        if item != "Relax - Stretch - Yoga":
            Excercises_Per_Day[day].append(pd.read_excel('Workout 2026.xlsx', sheet_name=item)['Excercise Name'][0])


