import streamlit as st
import numpy as np
import pandas as pd
import pickle
dff= pd.read_csv('last.csv')
df = pd.read_csv('final_airlines.csv')
st.title('Airline Fare Predictor')
# Load the trained model
model = pickle.load(open('LR.pkl', 'rb'))

st.markdown( "## All the fields are mandatory.")
st.subheader('Enter the details to get the fare prediction')

#-------------------------------------------------------------------------------------------------------------------------

# for airlines
airline_name= st.selectbox("Airline", options=dff['Company_names'].unique())

def airlines(airline_name):
    if airline_name == "IndiGo":
        return 40
    elif airline_name ==  "Air India":
        return 46
    elif airline_name ==  "Vistara":
        return 47
    elif airline_name ==  "AirAsia India, IndiGo":
        return 35
    elif airline_name ==  "IndiGo, Air India":
        return 38
    elif airline_name ==  "GoFirst, IndiGo":
        return 39

    elif airline_name ==  "IndiGo, AirAsia India":
        return 30
    elif airline_name ==  "IndiGo, GoFirst":
        return 32
    elif airline_name ==  "Air India, IndiGo":
        return 44
    elif airline_name ==  "Vistara, IndiGo":
        return 42
    elif airline_name ==  "AirAsia India":
        return 24
    elif airline_name ==  "Air India, GoFirst":
        return 25
    elif airline_name ==  "GoFirst":
        return 23
    elif airline_name ==  "AirAsia India, Air India":
        return 28
    elif airline_name ==  "Akasa Air, GoFirst":
        return 1
    elif airline_name ==  "AirAsia India, GoFirst":
        return 22


    elif airline_name ==  "IndiGo, Vistara":
        return 36

    elif airline_name ==  "GoFirst, Air India":
        return 37

    elif airline_name ==  "Akasa Air, Air India":
        return 7

    elif airline_name ==  "Air India, AirAsia India":
        return 26

    elif airline_name ==  "GoFirst, AirAsia India":
        return 21
    elif airline_name ==  "Air India, Vistara":
        return 41

    elif airline_name ==  "Akasa Air, AirAsia India":
        return 13

    elif airline_name ==  "Vistara, Air India":
        return 33

    elif airline_name ==  "Akasa Air, Vistara":
        return 15

    elif airline_name ==  "Vistara, GoFirst":
        return 34

    elif airline_name ==  "Akasa Air":
        return 8

    elif airline_name ==  "AirAsia India, Vistara":
        return 27

    elif airline_name ==  "Vistara, AirAsia India":
        return 29

    elif airline_name ==  "GoFirst, Vistara":
        return 31

    elif airline_name ==  "GoFirst, Akasa Air":
        return 5

    elif airline_name ==  "Akasa Air, IndiGo":
        return 10

    elif airline_name ==  "Air India, Akasa Air":
        return 4

    elif airline_name ==  "Multiple Airlines":
        return 45

    elif airline_name ==  "IndiGo, Akasa Air":
        return 16

    elif airline_name ==  "AirAsia India, Akasa Air":
        return 9
    elif airline_name ==  "Vistara, Akasa Air":
        return 43
    elif airline_name ==  "SpiceJet, IndiGo":
        return 18
    elif airline_name ==  "SpiceJet, AirAsia India":
        return 12
    elif airline_name ==  "IndiGo, Hahn Air Systems":
        return 51
    elif airline_name ==  "Air India, Hahn Air Systems":
        return 52
    elif airline_name ==  "SpiceJet, Air India":
        return 11
    elif airline_name ==  "IndiGo, SpiceJet":
        return 17
    elif airline_name ==  "SpiceJet, Vistara":
        return 20
    elif airline_name ==  "GoFirst, Hahn Air Systems":
        return 48
    elif airline_name ==  "AirAsia India, Hahn Air Systems":
        return 49
    elif airline_name ==  "SpiceJet, GoFirst":
        return 0
    elif airline_name ==  "Vistara, SpiceJet":
        return 19
    elif airline_name ==  "AirAsia India, SpiceJet":
        return 3
    elif airline_name ==  "Air India, SpiceJet":
        return 14
    elif airline_name ==  "Vistara, Hahn Air Systems":
        return 50
    elif airline_name ==  "GoFirst, SpiceJet":
        return 2
    elif airline_name ==  "Akasa Air, SpiceJet":
        return 6

airline = airlines(airline_name)

#-------------------------------------------------------------------------------------------------------------------------
origin = st.selectbox("Origin", options=dff["Origin_Dest"].unique())
#for origin 
def origin_name(origin):
    if origin == "BOM":
        return 1
    else:
        return 0
Origin_DestBOM = origin_name(origin)
#-------------------------------------------------------------------------------------------------------------------------
#for destination
destination= st.selectbox("Destination", options=dff["Destination"].unique())


def dest_name(destination):
    if destination == "COK":
        return 2
    elif destination == "BLR":
        return 0
    elif destination == "HYD":
        return 1

DDestination=dest_name(destination)
#-------------------------------------------------------------------------------------------------------------------------

#for total stops 
Stops = st.selectbox("Total stops", options=dff['Stops'].unique())


def stops(Stops):
    if Stops == "direct":
        return 0
    elif Stops == "1 stop":
        return 1
    elif Stops == "2 stops":
        return 2
    elif Stops == "3 stops":
        return 3
Total_Stops=stops(Stops)

#-------------------------------------------------------------------------------------------------------------------------
##jonery start month and date 
start_date=st.date_input("Journey start day")
import datetime as dt 
jstart_day=start_date.day
jstart_month=start_date.month

#-------------------------------------------------------------------------------------------------------------------------

##jonery end month and date 
end_date=st.date_input("Journey End day")
import datetime as dt 
jend_day=end_date.day
jend_month=end_date.month

#-------------------------------------------------------------------------------------------------------------------------

## departure time hour and minute
dep_time_hours = st.number_input('Departure time in hours')
dept_time_minutes = st.number_input('Departure time in minites')




#-------------------------------------------------------------------------------------------------------------------------
## Arrival time hour and minute
arrival_time_hours = st.number_input('Arrival time in hours')
arrival_time_minutes = st.number_input('Arrival time in minites')

#-------------------------------------------------------------------------------------------------------------------------

Duration_hours=st.number_input('Duration time of hours')

Duration_minutes=st.number_input('Duration time of minutes')

total_duration =  Duration_hours*60 + Duration_minutes*1


features=[airline, DDestination, Total_Stops, jstart_day,jstart_month, jend_day, jend_month, dep_time_hours,dept_time_minutes, arrival_time_hours,arrival_time_minutes, Duration_hours,Duration_minutes, total_duration,Origin_DestBOM]
final_features = np.array(features).reshape(1, -1)
st.table(final_features)

if st.button('Predict'):
    prediction = model.predict(final_features)

    #st.success(f'Your predicted price of the laptop is {round(prediction[0],3)}')
    st.success(f'Your predicted Fare of the airline is {prediction[0]}')