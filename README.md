
# Phonepe Pulse


Workflow:
Install required packages(pandas, os, 
First part is data cloning, extraction, preprocessing and uploading it to Database
Data cloning:
-Dataset is cloned from github through !git script
-From the dataset json files are extracted using filepath by os library and read json with its library then got those with DataFrame
-Total Dataset is extracted to 8 Dataframes first.
-Now DataBase connection is made through sqlalchemy libray and a connection engine is created to mysql database in server based platform (planet-scale)
-Now its preprocessing time,from the 8 Dataframes needful data is processed for end use like ploting
-Around 6 Dataframes are created newly and it is uploaded to Database through engine.

Now its 2nd part, visualisation
phase
First get data from database and add it to dataframe by making a engine connection again.
- Use pd.read_sql to read and asign it to Dataframes
-These dataframes are directly used for plots and graphs without any processing which is already preprocessed.
-here streamlit app is used for visualisation part like geo, bar, line
-using Plotly, Scatter_geo, line graph, bar graphs are created.
-

