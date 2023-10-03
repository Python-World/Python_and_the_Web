from datetime import datetime

import requests
import streamlit as st
from pytablewriter import MarkdownTableWriter

response = requests.get(
    "https://api.covid19api.com/summary"
)  # Get Request to pull down data from Covid19 data source
data = response.json()

st.markdown(
    MarkdownTableWriter(
        table_name="Covid19 Worldwide Data",
        headers=["Total Confirmed", "Total Recovered", "Total Deaths"],
        value_matrix=[
            [
                data["Global"]["TotalConfirmed"],
                data["Global"]["TotalRecovered"],
                data["Global"]["TotalDeaths"],
            ]
        ],
    )
)  # To form a Table for Live World data stat

st.write("")
st.write(
    "**Last Updated Time: {} **".format(
        datetime.strptime(data["Date"][:-1], "%Y-%m-%dT%H:%M:%S").strftime(
            "%b %d %Y %H:%M:%S"
        )
    )
)
# To Display the date & time of Last updated data of Covid19 Reports

st.write("")
country = st.text_input(
    "Enter Country Name:", ""
)  # Input to filter according to country name

table_data = [
    [i["Country"], i["TotalConfirmed"], i["TotalRecovered"], i["TotalDeaths"]]
    for i in data["Countries"]
]

if country != "":
    table_data = []
    table_data = [
        [
            i["Country"],
            i["TotalConfirmed"],
            i["TotalRecovered"],
            i["TotalDeaths"],
        ]
        for i in data["Countries"]
        if i["Country"].lower() == country.lower()
    ]
# If country name is not entered then display all Country

st.markdown(
    MarkdownTableWriter(
        table_name="CountryWise Data",
        headers=["Country Name", "Confirmed", "Recovered", "Deaths"],
        value_matrix=table_data,
    )
)  # table to display countrywise count reports
