import streamlit as st
import sqlalchemy
import pymysql
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#Establishing DataBase connection through sqlalchemy-engine
#with cloud server using PlanetScale platform
ssl_args = {'ssl_ca':'/etc/ssl/certs/ca-certificates.crt'}
engine = sqlalchemy.create_engine("mysql+pymysql://j43ck51t16cz9g99gyx6:pscale_pw_qrlGS2uTl8SUpJRIhpkkYtU8TSrkl1KV8430JXlld74@aws.connect.psdb.cloud/pulse",connect_args=ssl_args)

#getting DataFrame from mysql DataBase
bar_users=pd.read_sql_table('bar_users',engine)
line_trans=pd.read_sql_table('line_trans',engine)
map_trans=pd.read_sql_table('map_trans',engine)
map_users=pd.read_sql_table('map_users',engine)
top_trans=pd.read_sql_table('top_trans',engine)
top_users=pd.read_sql_table('top_users',engine)

#page config
st.set_page_config(page_icon="🧊",page_title= "Phonepe Pulse Data Visualization",
                   layout= "wide")
st.title(':violet[_PhonePe Pulse_]')
st.caption('A FINTECH REPORT')

# creating tabs
tab1, tab2, tab3, tab4 = st.tabs(['Home', 'Map-plot','Aggregated_graph','Top_graph'])
with tab1:
  st.subheader(':violet[_Phonepe Pulse Data Visualization and Exploration_]')
  st.markdown(':red[Technologies used:] Github Cloning, Python, Pandas, MySQL, Sqlalchemy, Streamlit, and Plotly.')
  st.header(':grey[_Metric definitions_]')
  st.subheader(':violet[_App opens_]')
  st.write('App opens include in-app opens and out-of-app opens. In-app opens are the number of times the PhonePe app was opened by users, and the apps home page loaded successfully. Out-of-app opens are counted when a user initiates a payment, on a merchants website/app.')
  st.subheader(':violet[_Registered Users_]')
  st.write('The number of unique users who downloaded the PhonePe app, and accepted the Terms and Conditions displayed during the onboarding process, within a specific period. The user is identified by his/her mobile phone number - each mobile phone number is treated as a separate/unique user.')
  st.subheader(':violet[_Transaction_]')
  st.write('A payment, wherein a sender sends money to a receiver (can be a contact, a phone number, a merchant, etc.) In the PhonePe context, overall transactions are the total number of successful payments processed by PhonePe, net of payment reversals.')
  st.subheader(':violet[_Merchant transactions_]')
  st.write('The total number of successful payments made to merchants, net of reversals, made on the PhonePe app. The merchant can be one that has a purely digital presence (e.g. an e-commerce website), or one that has a physical presence as well (e.g. a supermarket).')
  st.subheader(':violet[_P2P transactions_]')
  st.write('Peer to peer payments, or the total number of successful money transfer transactions, on the UPI framework, wherein the sender transfers money to an existing phone contact, a phone number not stored as a contact, or directly to a bank account number.')
  st.subheader(':violet[_Recharges_]')
  st.write('In the context of this report, top up of talk time/buying data packs, by pre-paid mobile users.')
  st.header(':lightgrey[_About_]')
  st.write('Phonepe Pulse with streamlite is a report generation from PhonePe Pulse - Data (github) dataset with Aggregated - Aggregated values of various payment categories as shown under Categories section, Map - Total values at the State and District levels, Top - Totals of top States / Districts /Pin Codes  and extracted a required amount of data and made visualization using plotly line graph, bar graph and geo visualizations with animation scale.')

with tab2:
  st.subheader('National-level Scatter ploting with Plotly.Scatter_geo')
  st.write('Lets see the Map Transactions and Users datum report with Transaction_count, Amount, Registered_users and App_opens in year_wise representations individually in National level Representation states-wise ploting')
  col1,col2 = st.columns([2,2],gap="medium")
  with col1:
    fig = px.scatter_geo(data_frame=map_trans, 
                     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',title='National-level Transaction counts',
                     locations='state', 
                     size='count', 
                     color='count',
                     animation_frame='year')
    fig=fig.update_geos(showcountries=True,fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)
  with col2:
    fig = px.scatter_geo(data_frame=map_trans, 
                     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',title='National-level Money Flow',
                     locations='state', 
                     size='amount', 
                     color='amount',
                     animation_frame='year')
    fig=fig.update_geos(showcountries=True,fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)
  col3,col4 = st.columns([2,2],gap="medium")
  with col3:
    fig = px.scatter_geo(data_frame=map_users, 
                     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',title='National-level Registered_users',
                     locations='state', 
                     size='registeredusers', 
                     color='registeredusers',
                     animation_frame='year')
    fig=fig.update_geos(showcountries=True,fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)
  with col4:
    fig = px.scatter_geo(data_frame=map_users, 
                     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',title='National-level App_openings',
                     locations='state', 
                     size='appopens', 
                     color='appopens',
                     animation_frame='year')
    fig=fig.update_geos(showcountries=True,fitbounds="locations", visible=False)
    st.plotly_chart(fig,use_container_width=True)
with tab3:
  st.subheader('Line & Bar Graph')
  st.write('Lets see the Aggregated Transactions and Users datum report in Line graph with Payment-Instruments shows in Individual lines and Bar Graph with Registered_Users & App_opens in sub_plots')
  col1,col2 = st.columns([2,2],gap="medium")
  with col1:
    fig = px.line(line_trans, title='National-level Transaction counts', x="year", y="count", color='paymentinstrument')
    fig.update_layout(xaxis={'dtick': 1})
    st.plotly_chart(fig,use_container_width=True)
  with col2:
    fig = px.line(line_trans, title='National-level Money Flow', x="year", y="amount", color='paymentinstrument')
    fig.update_layout(xaxis={'dtick': 1})
    st.plotly_chart(fig,use_container_width=True)

  fig = make_subplots(rows=1, cols=2,subplot_titles=("Registered_Users","App_opens"))

  fig.add_trace(go.Bar(x=bar_users['year'], y=bar_users['registeredusers'],
                    marker=dict(color=[4, 5, 6,7,7], coloraxis="coloraxis")),1, 1)

  fig.add_trace(go.Bar(x=bar_users['year'], y=bar_users['appopens'],
                    marker=dict(color=[2, 3, 5,7,9], coloraxis="coloraxis")),1, 2)

  fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False,title_text="Title")
  st.plotly_chart(fig,use_container_width=True)
with tab4:
  st.subheader('Top States')
  st.write('Lets see the Top Transactions and Users datum report in Bar_graph with Transaction_count, Amount, Registered_users and App_opens with year_wise representations individually in National level Representation with top states')

  fig = px.bar(top_trans,title='Top-States with yearly high Transaction counts', x="state", y="count",text_auto='.2s',
             animation_frame='year',range_y=(0,6000000000))
  st.plotly_chart(fig,use_container_width=True)

  fig = px.bar(top_trans,title='Top-States with yearly high Money Flow', x="state", y="amount",text_auto='.2s',
             animation_frame='year',range_y=(0,10000000000000))
  st.plotly_chart(fig,use_container_width=True)

  fig = px.bar(top_users,title='Top-States with yearly high Registered-users', x="state", y="registeredusers",text_auto='.2s',
             animation_frame='year',range_y=(0,250000000))
  st.plotly_chart(fig,use_container_width=True)
