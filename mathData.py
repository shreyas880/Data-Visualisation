from numpy import less_equal
import pandas as pd
from plotly import graph_objs
import plotly.graph_objects as pg

import csv
# with open('mathData.csv',newline = '') as f:
    # reader = csv.reader(f)
    # list = 

dataFrame = pd.read_csv('mathData.csv')

mean = dataFrame.groupby('level')['attempt'].mean()

studentDataFrame = dataFrame.loc[dataFrame['student_id'] == 'TRL_zet']
studentMean = studentDataFrame.groupby('level')['attempt'].mean()

print(mean)
print(studentDataFrame)

levels = ['Level 1','Level 2','Level 3','Level 4']
graph = pg.Figure(pg.Bar(x=mean,y=levels,orientation='h'))

studentAttempts = pg.Figure(pg.Bar(x=levels,y=studentMean,orientation='v'))
studentAttempts.show()