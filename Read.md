
Weather Analysis Dashboard for Dublin

The Weather Analysis Dashboard is a tool to study Dublin's weather. The goal is to create a user-friendly platform that collects, store and display weather data. We've used Python and MongoDB to build to store the data, and we've connected to external weather data sources to get real-time updates. This document explains how the dashboard works.

Objectives

The project focuses on collecting Dublin's weather data using an API, analyzing it with Python libraries, visualizing insights in a dashboard, integrating with Git for version control, deploying on Google Cloud for accessibility, and maintaining documentation for clarity and collaboration.

    Data collection
        The main task is to gather data from an outside source to understand Dublin's weather better. With the help of an API from www.visualcrossing.com to get detailed information like temperature, humidity, and more for each hour of the day. We collect thid data every day and store it in the database.

        After setting up our Flask application and importing necessary libraries including Flask and requests, it establish a connection with the Visual Crossing API to retrieve the weather data. After receiving the JSON response from the API, I've observed its structure and identify that it contains both current weather information and forecasts for the next 14 days. However, I've focused on the current date, which gathering data for each hour of the day.

        For each hourly interval, the data collection program extract various weather parameters including datetime, datetimeEpoch, temp, feelslike, humidity, dew, precip, precipprob, snow, snowdepth, preciptype, windgust, winddir, pressure, visibility, cloudcover, solarradiation, solarenergy, uvindex, severerisk, conditions, icon, stations and source . This data is collected and stored in MongoDB database.This stored data becomes accessible for further use. In the analysis section, we'll dive into this data to extract insights and perform additional processing.

    Analysis
        Utilizin Python libraries such as Flask, Request, JSON, PyMongo, Numpy, and datetime, we process and analyze the weather data collected from the API, stored it in the DB and transformed data to visuallise it. The analysis is conducted within the VS Code environment, ensuring efficiency and accuracy.

    Visualization
        To make it easier to understand the weather data, we've created visual displays in our dashbord. These show hourly details, past days' weather, and summarises of each day's weather, like the highest and lowest temperature.
    
    Integration
        Dashboard is integrated with Git for for keeping track of changes and collaborating with others. Additionally, the deployment of the dashboard on the Goodle Cloud platform allowing anyone can access it easily form anywhere.

    Documentation
        Maintained the commits in the Git. Additionally, a README.md file is created in the Git repository provides aoverview of project structure. This documentation helps everyone involved understand what's going on and how to work with the project.