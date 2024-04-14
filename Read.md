
Weather Analysis Dashboard for Dublin

The Weather Analysis Dashboard is a tool to study Dublin's weather. The goal is to create a user-friendly platform that collects, store and display weather data. We've used Python and MongoDB to build to store the data, and we've connected to external weather data sources to get real-time updates. This document explains how the dashboard works.

Objectives

The project focuses on collecting Dublin's weather data using an API, analyzing it with Python libraries, visualizing insights in a dashboard, integrating with Git for version control, deploying on Google Cloud for accessibility, and maintaining documentation for clarity and collaboration.

    Data collection and storing in the DB
        The main task is to gather data from an outside source to understand Dublin's weather better. With the help of an API from www.visualcrossing.com to get detailed information like temperature, humidity, and more for each hour of the day. We collect this data every day and store it in the database.

        After setting up our Flask application and importing necessary libraries including Flask,json and requests, it establish a connection with the Visual Crossing API to retrieve the weather data. After receiving the JSON response from the API, I've observed its structure and identified that it contains both current weather information and forecasts for the next 14 days. However, I've focused on the current date, which gathering data for each hour of the day. 

        For each hourly interval, the data collection program extracts various weather parameters including datetime, datetimeEpoch, temp, feelslike, humidity, dew, precip, precipprob, snow, snowdepth, preciptype, windgust, winddir, pressure, visibility, cloudcover, solarradiation, solarenergy, uvindex, severerisk, conditions, icon, stations and source . This data is collected and stored in to the MongoDB collection named "test".This stored data becomes accessible for further use. I've used library called pymongo to work with our MongoDB databas

        After collecting and storing the weather data in the database, we proceed with further processing. One crucial task involves determining the daily maximum and minimum temperatures, as well as the "feels like" temperature, for computing the maximum, minimum, and mean values we have used the numpy library. I've done this by creating separate arrays for each parameter and appending the respective hourly values to them. By analyzing these arrays, we can easily identify the highest and lowest temperatures recorded throughout the day.

        Additionally, I've calculated the mean (average) value for each numerical parameter by appending the hourly data into their respective arrays and calculating their averages. These mean, maximum, and minimum values are then stored in a separate collection within our Mongodb, named "min_max."


    Analysis and Transforming the data
        Using the Python libraries such as Flask, Request, JSON, PyMongo, Numpy, and datetime, we process and analyze the weather data collected from the API, stored it in the DB and transformed data to visuallise it. The analysis is conducted within the VS Code environment, ensuring efficiency and accuracy.

        The hourly parameters timestamp is provided in epoch time. Epoch time represents the number of seconds that have elapsed since January 1, 1970. However, to align with Dublin's standard time (GMT+1 after April 1st), we need to convert this epoch time accordingly.

        In the "Preciptype" column, we are having categorical values indicating precipitation type, such as snow or rain. To simplify analysis, we transform this column into three separate columns: "None," "Snow," and "Rain." Each column will have a value of "Yes" if the corresponding precipitation type occurs, otherwise "No.

        Similarly, the "Condition" column contains values like Rain, Overcast, Partially cloudy, and Clear. To make it more clear, we create four separate columns: "Rain," "Overcast," "Partially cloudy," and "Clear." Each column will be marked with "Yes" if the condition is present, otherwise "No.".


    Visualization
        To make it easier to understand the weather data, we've created visual displays in our dashbord. These show hourly details, past days' weather, and summarises of each day's weather, like the highest and lowest temperature.

        On the website's frontend, I've crafted a dashboard using HTML. It features tables that display parameters fetched from the API. Each parameter is listed with its corresponding value underneath. Whenever the page reloads, the data is updated in our MongoDB collection. If the data is already in the database, it's simply updated; if not, the new values are added.

        Additionally, on the homepage, there's a button labeled "Previous Days Details." Clicking this button navigates to the "/processed-data" page. At the top of the table on this page, there are buttons labeled "Hourly" and "Daily." Clicking "Hourly" displays transformed data from MongoDB collection "test", showcasing hourly data from previous days. Clicking "Daily" shows summaries such as maximum and minimum temperatures, along with the mean of all numerical parameters from the MongoDB collection "min-max".

        For styling and design, we've utilized the Bootstrap framework by including the following link: <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">.
    
    Integration
        Dashboard is integrated with Git for for keeping track of changes and collaborating with others. Additionally, the deployment of the dashboard on the Goodle Cloud platform allowing anyone can access it easily form anywhere.

    Documentation
        Maintained the commits in the Git. Additionally, a README.md file is created in the Git repository provides aoverview of project structure. This documentation helps everyone involved understand what's going on and how to work with the project.