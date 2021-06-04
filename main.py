import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("main.csv")

GRE_Score = df["GRE Score"].tolist()
Chance_of_Admit = df["Chance of Admit"].tolist()

fig = px.scatter(x=GRE_Score, y=Chance_of_Admit)

m = 0.01
c = -2.5
y = []

for x in GRE_Score:
     y_value = m*x+c
     y.append(y_value)

#x = height
#y =  m*x+c

fig.update_layout(shapes=[
    dict(
        type = 'line', 
        y0 = min(y), y1 = max(y),
        x0 = min(GRE_Score), x1 = max(GRE_Score),
    )
])
fig.show()

# Y = M (slope) M (magnitude of x-axis) + C (values to be intersected on y-axis)