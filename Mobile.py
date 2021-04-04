import plotly.figure_factory as ff
import pandas as pd 
import csv 
df=pd.read_csv("Mobile.csv")
rateList=df["Avg Rating"].tolist()
fig=ff.create_distplot([rateList], ["Rating"], show_hist=False)
fig.show()
