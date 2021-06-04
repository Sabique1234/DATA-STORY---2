import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")

height = df["Height"].tolist()
weight = df["Weight"].tolist()

fig = px.scatter(x=height,y=weight)

# Y = M (slope) M (magnitude of x-axis) + C (values to be intersected on y-axis)

#m = 1
#c = 0

m = 0.95
c = -93

y = []
for x in height:
     y_value = m*x+c
     y.append(y_value)


#x = height
#y =  m*x+c

fig.update_layout(shapes=[
    dict(
        type = 'line', 
        y0 = min(y), y1 = max(y),
        x0 = min(height), x1 = max(height),
    )
])

fig.show()