import streamlit as st
import requests
from pytablewriter import MarkdownTableWriter
from datetime import datetime

response = requests.get('https://api.covid19api.com/summary')
data = response.json()

st.markdown(MarkdownTableWriter(
    table_name="Covid19 Worldwide Data",
    headers=["Total Confirmed", "Total Recovered", "Total Deaths"],
    value_matrix=[[data['Global']['TotalConfirmed'], data['Global']['TotalRecovered'], data['Global']['TotalDeaths']]],
))
st.write("")
st.write("**Last Updated Time: {} **".format(datetime.strptime(data['Date'][:-1],"%Y-%m-%dT%H:%M:%S").strftime("%b %d %Y %H:%M:%S")))


st.write("")
country = st.text_input("Enter Country Name:","")

table_data = [ [i['Country'],i['TotalConfirmed'],i['TotalRecovered'],i['TotalDeaths']] for i in data['Countries'] ]

if country != "":
    table_data=[]
    table_data = [ [i['Country'],i['TotalConfirmed'],i['TotalRecovered'],i['TotalDeaths']] for i in data['Countries'] if i['Country'].lower() == country.lower() ]

st.markdown(MarkdownTableWriter(
    table_name="CountryWise Data",
    headers=["Country Name", "Confirmed", "Recovered", "Deaths"],
    value_matrix=table_data,
))