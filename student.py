import csv 
import plotly.express as ps
with open("Student Marks vs Days Present.csv") as f:
    df=csv.DictReader(f)
    fig=ps.scatter(df,x="Marks In Percentage" , y="Days Present",color="Roll No")
    fig.show()