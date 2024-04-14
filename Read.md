
Weather Analysis Dashboard for Dublin

The Weather Analysis Dashboard is a tool to study Dublin's weather. The goal is to create a user-friendly platform that collects, store and display weather data. We've used Python and MongoDB to build to store the data, and we've connected to external weather data sources to get real-time updates. This document explains how the dashboard works.

Objectives

    Data collection
        The main task is to gather data from an outside source to understand Dublin's weather better. With the help of an API from www.visualcrossing.com to get detailed information like temperature, humidity, and more for each hour of the day. We collect thid data every day and store it in the database.

    Analysis
        Utilizin Python libraries such as Flask, Request, JSON, PyMongo, Numpy, and datetime, we process and analyze the weather data collected from the API, stored it in the DB and transformed data to visuallise it. The analysis is conducted within the VS Code environment, ensuring efficiency and accuracy.

    Visualization
        To make it easier to understand the weather data, we've created visual displays in our dashbord. These show hourly details, past days' weather, and summarises of each day's weather, like the highest and lowest temperature.
    
    Integration
        Dashboard is integrated with Git for for keeping track of changes and collaborating with others. Additionally, the deployment of the dashboard on the Goodle Cloud platform allowing anyone can access it easily form anywhere.

    Documentation
        Maintained the commits in the Git. Additionally, a README.md file is created in the Git repository provides aoverview of project structure. This documentation helps everyone involved understand what's going on and how to work with the project.