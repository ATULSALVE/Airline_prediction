import streamlit as st
import numpy as np
import pandas as pd
import pickle
import datetime as dt

# Load data
dff = pd.read_csv('last.csv')
df = pd.read_csv('final_airlines.csv')

# Load the trained model
model = pickle.load(open('Random.pkl', 'rb'))

# Title and header
st.title('Airline Fare Predictor')
st.markdown("## All the fields are mandatory.")
st.subheader('Enter the details to get the fare prediction')

# Function to convert airline names to numerical values
def airlines(airline_name):
    # Mapping of airline names to numerical values
    airline_mapping = {
        "IndiGo": 40, "Air India": 46, "Vistara": 47, "AirAsia India, IndiGo": 35,
        "IndiGo, Air India": 38, "GoFirst, IndiGo": 39, "IndiGo, AirAsia India": 30,
        "IndiGo, GoFirst": 32, "Air India, IndiGo": 44, "Vistara, IndiGo": 42,
        "AirAsia India": 24, "Air India, GoFirst": 25, "GoFirst": 23,
        "AirAsia India, Air India": 28, "Akasa Air, GoFirst": 1, "AirAsia India, GoFirst": 22,
        "IndiGo, Vistara": 36, "GoFirst, Air India": 37, "Akasa Air, Air India": 7,
        "Air India, AirAsia India": 26, "GoFirst, AirAsia India": 21, "Air India, Vistara": 41,
        "Akasa Air, AirAsia India": 13, "Vistara, Air India": 33, "Akasa Air, Vistara": 15,
        "Vistara, GoFirst": 34, "Akasa Air": 8, "AirAsia India, Vistara": 27,
        "Vistara, AirAsia India": 29, "GoFirst, Vistara": 31, "GoFirst, Akasa Air": 5,
        "Akasa Air, IndiGo": 10, "Air India, Akasa Air": 4, "Multiple Airlines": 45,
        "IndiGo, Akasa Air": 16, "AirAsia India, Akasa Air": 9, "Vistara, Akasa Air": 43,
        "SpiceJet, IndiGo": 18, "SpiceJet, AirAsia India": 12, "IndiGo, Hahn Air Systems": 51,
        "Air India, Hahn Air Systems": 52, "SpiceJet, Air India": 11, "IndiGo, SpiceJet": 17,
        "SpiceJet, Vistara": 20, "GoFirst, Hahn Air Systems": 48, "AirAsia India, Hahn Air Systems": 49,
        "SpiceJet, GoFirst": 0, "Vistara, SpiceJet": 19, "AirAsia India, SpiceJet": 3,
        "Air India, SpiceJet": 14, "Vistara, Hahn Air Systems": 50, "GoFirst, SpiceJet": 2,
        "Akasa Air, SpiceJet": 6
    }
    return airline_mapping.get(airline_name, 0)  # Return 0 if not found

# Function to convert origin name to numerical value
def origin_name(origin):
    return 1 if origin == "BOM" else 0

# Function to convert destination name to numerical value
def dest_name(destination):
    dest_mapping = {"COK": 2, "BLR": 0, "HYD": 1}
    return dest_mapping.get(destination, 0)  # Return 0 if not found

# Function to convert total stops to numerical value
def stops(Stops):
    stops_mapping = {"direct": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3}
    return stops_mapping.get(Stops, 0)  # Return 0 if not found

# Function to calculate total duration
def calculate_total_duration(hours, minutes):
    return hours * 60 + minutes

# User inputs
airline_name = st.selectbox("Airline", options=dff['Company_names'].unique())
origin = st.selectbox("Origin", options=dff["Origin_Dest"].unique())
destination = st.selectbox("Destination", options=dff["Destination"].unique())
Stops = st.selectbox("Total stops", options=dff['Stops'].unique())
start_date = st.date_input("Journey start day")
end_date = st.date_input("Journey End day")
dep_time_hours = st.number_input('Departure time in hours')
dept_time_minutes = st.number_input('Departure time in minutes')
arrival_time_hours = st.number_input('Arrival time in hours')
arrival_time_minutes = st.number_input('Arrival time in minutes')
Duration_hours = st.number_input('Duration time of hours')
Duration_minutes = st.number_input('Duration time of minutes')

# Convert user inputs to numerical values
airline = airlines(airline_name)
Origin_DestBOM = origin_name(origin)
DDestination = dest_name(destination)
Total_Stops = stops(Stops)
jstart_day = start_date.day
jstart_month = start_date.month
jend_day = end_date.day
jend_month = end_date.month
total_duration = calculate_total_duration(Duration_hours, Duration_minutes)

# Construct features array
features = [
    airline, DDestination, Total_Stops, jstart_day, jstart_month,
    jend_day, jend_month, dep_time_hours, dept_time_minutes,
    arrival_time_hours, arrival_time_minutes, Duration_hours,
    Duration_minutes, total_duration, Origin_DestBOM
]
final_features = np.array(features).reshape(1, -1)

# Display user inputs
st.table(final_features)

# Prediction
if st.button('Predict'):
    prediction = model.predict(final_features)
    st.success(f'Your predicted Fare of the airline is {prediction[0]}')
