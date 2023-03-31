
# Phonepe Pulse
Phonepe Pulse with streamlite is a report generation from PhonePe Pulse - Dataset (github)with Aggregated - Aggregated values of various payment categories as shown under Categories section, Map - Total values at the State and District levels, Top - Totals of top States / Districts /Pin Codes  and extracted a required amount of data and made visualization using plotly line graph, bar graph and geo visualizations with animation scale.
## Demo:
With this link you can see the execution demo and code explanation.
## Workflow:
- Packages needed(pandas,os,json,sqlalchemy,pysql,Streamlite and extra needful lib's)

First part is data cloning, extraction, preprocessing and uploading it to Database
### Data cloning and Extraction
- Dataset is cloned from github through !git clone https://github.com/PhonePe/pulse.git script
- From the dataset json files are extracted using filepath by os library and read json with its library with loops and conditions, then get them with DataFrame.
- Total Dataset is extracted into 8 Dataframes first.

### Preprocessing and DB upload
- Now DataBase connection is made through sqlalchemy libray and a connection engine is created to mysql database in server based platform (planet-scale)
- Now its preprocessing time,from the 8 Dataframes needful data is processed for the report visualization purpose.
- Around 6 Dataframes are created newly and it is uploaded to Database through engine as seperate tables.

Now its 2nd part, visualisation phase
### Execution with Streamlite
- with seperate pythone file import required lib's.
- First get data from database and add it to dataframe by making a connection engine again.
- Use pd.read_sql to read and asign it to Dataframes.
- These dataframes are directly used for plots and graphs without any processing which is already preprocessed as per our need.
- Here streamlit app is used for visualisation part like geo, bar, line
- Using Plotly, Scatter_geo, line graph, bar graphs are created.
You can see some snaps which I've made through streamlite.
![p1](https://user-images.githubusercontent.com/127252539/229164874-4bed6551-3852-4c44-9a9a-98998ca69433.jpg)
![p2](https://user-images.githubusercontent.com/127252539/229165105-e3b18e1d-2454-435b-899b-50b8c65d3128.jpg)
![p3](https://user-images.githubusercontent.com/127252539/229165159-7a098b47-c313-4205-abb1-d4e434d6eb4b.jpg)
![p4](https://user-images.githubusercontent.com/127252539/229165169-cb131582-315b-4660-9418-6b46766e4707.jpg)
