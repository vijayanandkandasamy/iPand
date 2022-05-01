# iPand
## A Smart Time Series Analytics and Forecasting Application for Novel Pandemic  - Community Proliferation Prediction

#### Project Summary:

COVID-19, the respiratory syndrome that started in 2019 quickly escalated to a pandemic proportion causing catastrophic impact globally affecting more than 192 countries. As on date, we have surpassed 3 dreadly waves affecting multitude with loss of lives of millions of people. Together with all disciplines of human knowledge, we have been able to come up with recovery drugs, multiple vaccines, treatment protocols, waves start and end prediction data, the contamination data projections and much more to handle this infectious disease. Data has played a Pivotal role in COVID-19 management. Prior to the 2019 Pandemic, we did not have such massive historical data of a global pandemic to steer the scientists on pandemic containment and management. With experts talking about the next waves in the upcoming months, the Time Series Analysis of the COVID-19 data is making more meaningful impacts as a tool to make the COVID-19 Projections. The proposed i-Pand web application will be designed to be a Smart and generic application to derive any epidemic or pandemic projection that shares the characteristics of virulent spread.

#### Project Description

##### Objectives:

The proposed web application is conceptualized with the notion of making it more generic to adopt the application for any type of pandemic projection of viral origin. The application will be developed incorporating the Time Series Analysis statistical technique that consists of historical wave data points listed in chronological order. The dataset will be consisting of the previous wave’s community proliferation data to help us predict the future scales of spread. i-Pand web application will primarily be built incorporating the Autoregressive Integrated Moving Average (ARIMA) time series analysis model which has great accuracy in the shorter time series dataset.

##### Usefulness:
   The Novel COVID-19 is just the beginning of a large scale pandemic that the world has undergone and scientists predict more of such dreadlier events in the upcoming years. Preparedness and wisdom is the key to manage any such cataclysmic diseases that might threaten the mankind. Being able to make accurate predictions with the i-Pand web application, the government and the health care sectors can be more vigilant and prepared to handle the epidemic or pandemic. The forecast will help the governments to enforce civil regulations based on the spread rate. This will also enable the government to implement planned lockdown procedures smoothly thus reducing the discomfort of the people with last minute spree and similarly determine the timelines of phased unlock procedures and implement them. The health care organizations can be prepared to enable or re-purpose more of their units to handle such health situations. The targeted user group is the health care sector and the governments across the globe.

#### Application Architecture

##### Python-Flask:

The Web application is being built on Flask-Python micro web framework, considering the flexibility it provides to develop and customize. renders full control and is highly suitable for small projects that necessitate experimentation


##### Front End:

The Application’s front end user interface will be designed using Bootstrap Framework which is imported as a dependency in the Flask Web Framework. All the UI customizations is being handled in HTML5, CSS & JS files that we create for the users to interact with the iPand application.

##### Back End:
The Backend of iPand web application is Python language. Javascript is used to manipulate the web page DOM elements. The below python libraries are currently used in our project to experiment with the Time Series Analysis, Visualization and Forecast reporting.

###### Firebase Authentication:
Firebase Authentication provides backend services, easy-to-use SDKs, and ready-made UI libraries to authenticate users to web applications. It supports authentication using passwords, phone numbers, popular federated identity providers like Google, Facebook and Twitter, and more. iPand Application uses Firebase Authentication API to authenticate users into the system. Also the same API is used to register the Users into the System. iPand uses Email ID / Password option for user signup and login.

###### Python Libraries:

####### Pandas: 
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. It contains extensive capabilities and features for working with time series data for all domains.

####### Pyrebase4: 
A simple python wrapper for the Firebase API. Pyrebase4 is a python library that is used to interact with Google Firebase. Firebase provides its users with various features like authentication, database, hosting, etc. As Firebase was primarily based on JavaScript, the Pyrebase4 library was created to facilitate the Python developers.

####### folium
Matplotlib library is used for data visualization in various formats such as line plot, bar graph, heat maps, scatter plots, histogram etc. It contains all the graph related functionalities required from plotting to labelling.

####### plotly
The plotly Python library is an interactive, open-source plotting library that supports over 40 unique chart types covering a wide range of statistical, financial, geographic, scientific, and 3-dimensional use-cases. Built on top of the Plotly JavaScript library (plotly.js), plotly enables Python users to create beautiful interactive web-based visualizations that can be displayed in Jupyter notebooks, saved to standalone HTML files, or served as part of pure Python-built web applications using Dash.

####### Flask-Dropzone 
Flask-Dropzone packages Dropzone.js into an extension to add file upload support for Flask. Flask-Dropzone is an useful JavaScript library that lets you upload files immediately by dragging a file to a zone and dropping it. It has abilities to send your file off to be saved in the destination mentioned. It also can handle single/multiple files drop/upload.

##### Build & Deployment:
The iPand Application is hosted in the Heroku Platform. The source code is available in github and as well as updated in the Heroku Git Repository. Due to recent change of Heroku – Github Integration, the Heroku Git has been used to deploy the application in Heroku.
