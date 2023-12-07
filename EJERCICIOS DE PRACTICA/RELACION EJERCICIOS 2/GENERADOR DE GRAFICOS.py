import plotly.express as px
import pandas 

data={
    "Nombre": ["Juan","María","Carlos","Ana","Luis"],
    "Edad": [25,30,21,28,35],
    "Puntaje":[70,85,90,75,80]
}

df=pandas.DataFrame(data)

fig= px.scatter(df, x="Edad", y="Puntaje", text="Nombre",title="Puntaje vs Edad",
                labels={"Edad":"Edad(años)", "Puntaje":"Puntaje (%)"},
                hover_data={"Nombre": True, "Edad":True, "Puntaje":True})

fig.show()
                

