import csv 
import plotly.express as ps
with open("cups of coffee vs hours of sleep.csv") as f:
    df=csv.DictReader(f)
    fig=ps.scatter(df,x="Coffee in ml" , y="sleep in hours",color="week")
    fig.show()