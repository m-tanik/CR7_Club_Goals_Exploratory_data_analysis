import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt 
import seaborn as sns
from datetime import timedelta
import warnings
import os
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
#########################################################################################################
# st.set_page_config(page_title="CR7", layout="wide")
# css = '''
# <style>
#     [data-testid="stSidebar"]{
#         min-width: 700px;
#         max-width: 1200px;
#     }
# </style>
# '''
# st.markdown(css, unsafe_allow_html=True)

st.write("""
# Cristiano Ronaldo Exploritory Data Analysis of club Goals
         """)

# Data Loading
df = pd.read_csv('data.csv')

#########################################################################################################

st.write("""
# Basic Exploration
         """)

# Basic Exploration
df.head() 
print("Datasets Total Columns", df.columns) #columns list
df.shape #shape
df.describe(include=['object']).T
#########################################################################################################

st.write("""
### Goals In Different competition
         """)
# Exploritory Data Analysis of club Goals
### Goals In Different competition
fig1 = px.histogram(
    df,
    x='Competition',
    title="Goals in different competition",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Competition','Club'])
fig1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area background
)
st.plotly_chart(fig1)
# Show the Plotly plot
# fig.show()
#########################################################################################################

pd.DataFrame(df.Competition.value_counts()) # value count for every competition

#########################################################################################################

st.write("""
### Goals Per Season
         """)
### Goals Per Season
fig2 = px.histogram(
    df,
    x='Season',
    title="Goals per season",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Season','Club'])
fig2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area background
)
st.plotly_chart(fig2)

# Show the Plotly plot
# fig.show()
#########################################################################################################

st.write("""
### Goals Per Club
         """)
### Goals Per Club
fig3 = px.histogram(
    df,
    x='Club',
    title="Goals per Clubs - Seasons",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=600,
    color='Season',
    hover_name='Season',
    hover_data=['Competition','Season','Club'])
fig3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area background
)
st.plotly_chart(fig3)

# Show the Plotly plot
# fig.show()
#########################################################################################################

st.write("""
### Goals Per Club - Competition
         """)
### Goals Per Club - Competition
fig4 = px.histogram(
    df,
    x='Club',
    title="Goals per Clubs - Competition",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=500,
    color='Competition',
    hover_name='Competition',
    hover_data=['Competition','Season','Club'])
fig4.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area background
)
st.plotly_chart(fig4)

# Show the Plotly plot
# fig.show()
#########################################################################################################

st.write("""
### Goals Per Playing Position
         """)
### Goals per playing position
fig5 = px.histogram(
    df,
    x='Playing_Position',
    title="Goals per playing Position",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Playing_Position','Competition','Season','Club'])
fig5.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area background
)
st.plotly_chart(fig5)

# Show the Plotly plot
# fig.show()
#########################################################################################################

st.write("""
# Goals Per Game Minute
         """)
### Goals per game minute
mins=list(map(str, range(1,121)))
mins.insert(45,"1stE")
mins.insert(91,"2ndE")
mins.insert(122,"ExtE")
df.loc[df.Minute.str[:3]=='45+', 'Minute'] = '1stE'
df.loc[df.Minute.str[:3]=='90+', 'Minute'] = '2ndE'
df.loc[df.Minute.str[:4]=='120+', 'Minute'] = 'ExtE'
mins1=mins[:46]
mins2=mins[46:92]
mins3=mins[92:]


st.write("""
## Goals Per Game Minute (First Half)
         """)
sns.set(rc={'figure.figsize':(22,5)})
plt.xticks(fontsize=15)
p1=sns.countplot(df['Minute'],order=mins1)
p1.axes.set_title("Goals per Game Minute (First Half)",fontsize=30)
st.pyplot(p1.get_figure())
#########################################################################################################

st.write("""
## Goals Per Game Minute (Second Half With Extra Time)
         """)
p2=sns.countplot(df['Minute'],order=mins2)
p2.axes.set_title("Goals per Game Minute (Second Half With Extra time)",fontsize=30)
st.pyplot(p2.get_figure())

#########################################################################################################

st.write("""
## Goals Per Game Minute (91-Extra times)
         """)
p3=sns.countplot(df['Minute'],order=mins3)
p3.axes.set_title("Goals per Game Minute (91-Extra times)",fontsize=30)
st.pyplot(p3.get_figure())

#########################################################################################################
st.write("""
### Goals Per Type of Goals
         """)
### Goals Per Type of Goals
fig6 = px.histogram(
    df,
    x='Type',
    title="Goals per Type",
    log_x=False,
    log_y=False,
    #symbol='title',
    #markers=True,
    #width=800, 
    height=500,
    color='Club',
    hover_name='Club',
    hover_data=['Playing_Position','Competition','Season','Club'])

fig6.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area background
)
st.plotly_chart(fig6)
#########################################################################################################

st.write("""
### Scoreline After Goals
         """)
### Scoreline After Goals
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p4=sns.countplot(df['At_score'],hue_order=df.groupby('Competition'),order=df.At_score.value_counts().sort_values(ascending=False).index)
p4.axes.set_title("Scoresheet after scoring",fontsize=30)
st.pyplot(p4.get_figure())

#########################################################################################################
st.write("""
### Goals Against Opponents
         """)
### Goals Against Opponents
sns.set(rc={'figure.figsize':(30,5)})
plt.xticks(rotation='vertical')
p5=sns.countplot(df['Opponent'],hue_order=df.groupby('Competition'),order=df.Opponent.value_counts().sort_values(ascending=False).index)
p5.axes.set_title("Goals per Opponent",fontsize=30)
st.pyplot(p5.get_figure())
#########################################################################################################

mins=list(map(str, df.Opponent.value_counts().sort_values(ascending=False).index))
for min in df['Opponent']:
    if min not in mins:
        mins.append(min)
mins1=mins[:int(len(mins)/5)]
mins2=mins[int(len(mins)/5):int(2*len(mins)/5)]
mins3=mins[2*int(len(mins)/5):int(3*len(mins)/5)]
mins4=mins[3*int(len(mins)/5):int(4*len(mins)/5)]
mins5=mins[int(4*len(mins)/5):]

st.write("""
### Goals per Opponents -1
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p6=sns.countplot(df['Opponent'],order=mins1)
p6.axes.set_title("Goals per Opponents",fontsize=30)
st.pyplot(p6.get_figure())
#########################################################################################################
st.write("""
### Goals per Opponents -2
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p7=sns.countplot(df['Opponent'],order=mins2)
p7.axes.set_title("Goals per Opponents",fontsize=30)
st.pyplot(p7.get_figure())
#########################################################################################################
st.write("""
### Goals per Opponents -3
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p8=sns.countplot(df['Opponent'],order=mins3)
p8.axes.set_title("Goals per Opponents",fontsize=30)
st.pyplot(p8.get_figure())
#########################################################################################################
st.write("""
### Goals per Opponents -4
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p9=sns.countplot(df['Opponent'],order=mins4)
p9.axes.set_title("Goals per Opponents",fontsize=30)
st.pyplot(p9.get_figure())
#########################################################################################################
st.write("""
### Goals per Opponents -5
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p10=sns.countplot(df['Opponent'],order=mins5)
p10.axes.set_title("Goals per Opponents",fontsize=30)
st.pyplot(p10.get_figure())
#########################################################################################################

# st.write("""
# ### Most Favorite Opponents
#          """)
### Favorite Opponent
sns.set(rc={'figure.figsize':(12,5)})
opponents_df=df.groupby('Opponent').size().reset_index(name='count')
fav_opponents_df=opponents_df[opponents_df["count"]>15]
plt.xticks(fontsize=20,rotation='vertical')
# p=sns.countplot(fav_opponents_df['Opponent'],order=fav_opponents_df['count'])
# p.axes.set_title("Most Favorite Opponents",fontsize=30)

plt.bar(x=fav_opponents_df['Opponent'],height=fav_opponents_df['count'],color="#1ae5e1")
# st.pyplot(p.get_figure())

#########################################################################################################
st.write("""
### Goals Assisted BY
         """)
### Goals Assisted BY
sns.set(rc={'figure.figsize':(30,5)})
plt.xticks(rotation='vertical')
p11=sns.countplot(df['Goal_assist'],order=df.Goal_assist.value_counts().sort_values(ascending=False).index)
p11.axes.set_title("Goals Assist",fontsize=30)
st.pyplot(p11.get_figure())

#########################################################################################################

mins=list(map(str, df.Goal_assist.value_counts().sort_values(ascending=False).index))
for min in df['Goal_assist']:
    if min not in mins:
        mins.append(min)
mins1=mins[:int(len(mins)/5)]
mins2=mins[int(len(mins)/5):int(2*len(mins)/5)]
mins3=mins[2*int(len(mins)/5):int(3*len(mins)/5)]
mins4=mins[3*int(len(mins)/5):int(4*len(mins)/5)]
mins5=mins[int(4*len(mins)/5):]

st.write("""
### Goals Assisted BY -1
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p12=sns.countplot(df['Goal_assist'],order=mins1)
p12.axes.set_title("Goals Assisted by",fontsize=30)
st.pyplot(p12.get_figure())
#########################################################################################################

st.write("""
### Goals Assisted BY -2
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p13=sns.countplot(df['Goal_assist'],order=mins2)
p13.axes.set_title("Goals Assisted by",fontsize=30)
st.pyplot(p13.get_figure())
#########################################################################################################

st.write("""
### Goals Assisted BY -3
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p14=sns.countplot(df['Goal_assist'],order=mins3)
p14.axes.set_title("Goals Assisted by",fontsize=30)
st.pyplot(p14.get_figure())
#########################################################################################################

st.write("""
### Goals Assisted BY -4
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p15=sns.countplot(df['Goal_assist'],order=mins4)
p15.axes.set_title("Goals Assisted by",fontsize=30)
st.pyplot(p15.get_figure())
#########################################################################################################

st.write("""
### Goals Assisted BY -5
         """)
sns.set(rc={'figure.figsize':(20,5)})
plt.xticks(fontsize=15,rotation='vertical')
p16=sns.countplot(df['Goal_assist'],order=mins5)
p16.axes.set_title("Goals Assisted by",fontsize=30)
st.pyplot(p16.get_figure())
#########################################################################################################

st.write("""
### Home and Away Goals
         """)
### Home and Away Goals
fig, ax = plt.subplots(figsize=(8, 6))

plt.figure(figsize=(10,15))
plt.title('Goals per venue', fontsize=20)
df.Venue.value_counts().plot(kind='pie', labels=['Home', 'Away'], wedgeprops=dict(width=.7), autopct='%1.0f%%', startangle= -20,  textprops={'fontsize': 15}, ax= ax)
ax.set_ylabel('')  # Remove y-label
ax.set_title('Goals Distribution')

# Display the chart in Streamlit
st.pyplot(fig)
#########################################################################################################
