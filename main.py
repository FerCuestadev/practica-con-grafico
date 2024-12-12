import os
import json
from flask import Flask, send_file
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')


@app.route("/guardarestudio/<titulo>/<entidad>/<fecha>")
def guardarestudio(titulo,entidad,fecha):
    registro={
        "titulo":titulo,
        "entidad":entidad,
        "fecha":fecha
    }
    with open("estudios.txt","a") as archivo:
        archivo.write(json.dumps(registro)+"\n")
        return "Estudio guardado satisfactoriamente"


@app.route("/listadoestudios")
def listadoEstudios():
    with open("estudios.txt","r") as archivo:
        contenido=""
        for linea in archivo:
            elemento=json.loads(linea)

            contenido=contenido+"<div class= 'alert alert-success'>"
            contenido=contenido+"<strong>"+elemento["titulo"]+"</strong><br> "
            contenido=contenido+"<em>"+elemento["entidad"]+" <br>"+elemento["fecha"]+" </em></div>"
        return contenido


@app.route("/cargarfuentedatos")
def cargarfuentedatos():
    with open("modernrenewableprod.csv","r") as archivo:
        mitabla="<table id= 't_datos' class='table table-hover'>"
        mitabla=mitabla+"<thead>"
        mitabla=mitabla+"   <tr>"
        mitabla=mitabla+"      <th>País</th>"
        mitabla=mitabla+"      <th>codigo</th>"
        mitabla=mitabla+"      <th>año</th>"
        mitabla=mitabla+"      <th>data</th>"
        mitabla=mitabla+"   <tr>"
        mitabla=mitabla+"</thead"
        mitabla=mitabla+"<tdody>"
        paises =set() #Conjunto para evitar duplicados
        for linea in archivo:
            elemento=linea.split(",")
            mitabla=mitabla+"<tr>"
            mitabla=mitabla+"      <td>"+elemento[0]+"</td>"
            mitabla=mitabla+"      <td>"+elemento[1]+"</td>"
            mitabla=mitabla+"      <td>"+elemento[2]+"</td>"
            mitabla=mitabla+"      <td>"+elemento[3]+"</td>"
            mitabla=mitabla+"</tr>"
        mitabla+"</tbody></table>"

        select_paises = "<select id='sl_paises' class='form-control'>"
        for pais in paises: #ordenaanr lospaises alfabeticamente
            select_paises=select_paises+ "<option value='"+ pais +"'>" + pais + "</option>"
        select_paises = select_paises + "</select>"

        select_grafico = "<select id='sl_grafico' class= 'from-control'>"
        select_grafico =select_grafico+ "<>" 




#funciones para graficar

@app.route('/graficar')
def graficar():
    #grafico torta
    df = pd.DataFrame({'Categoria': ['Automoviles', 'Motocicletas', 'Barcos', 'Submarino', 'Bicicleta', 'Cohete'], 'Porcentaje': [100, 30, 20, 30, 70, 200]})

    fig = px.pie(df, names='Categoria', values='Porcentaje', title='GRAFICO PASTEL')
    graph_html = fig.to_html(full_html=False)

    return graph_html



@app.route('/linea')
def lineas():
    #grafico linea
    df = pd.DataFrame({'X':[1,2,3,4,5,6,7], 'Y':[40,35,85,65,10,90,52]})

    fig = px.line(df,x='X', y='Y', title='GRAFICO LINEAS')
    graph_html = fig.to_html(full_html=False)

    return graph_html


@app.route('/barras')
def barras():
    #grafico barra
    df = pd.DataFrame({'Categoria':['Pan', 'Arroz', 'Azucar', 'Cafe', 'Frijol', 'Sal', 'Carne', 'Lentejas'],'Valores': [70,10,20,40,15,35,90,50]})

    fig = px.bar(df, x='Categoria', y='Valores', title='GRAFICO BARRAS')
    graph_html = fig.to_html(full_html=False)

    return graph_html


@app.route('/ScartterPlot')
def ScartterP():
    #grafico barra
    df = pd.DataFrame({'X': [1,2,3,4,5], 'Y': [10,20,15,25,30]})

    fig = px.scatter(df, x='X', y='Y', title='GRAFICO DE DISPERSIÓN')
    graph_html = fig.to_html(full_html=False)

    return graph_html



@app.route('/Histogramas')
def Histogramas():
    #grafico barra
    df = pd.DataFrame({'Datos': [1,2,2,3,3,3,4,4,5,6,6,6,7,7,8,8,9,9]})

    fig = px.histogram(df, x='Datos', title='HISTOGRAMA')
    graph_html = fig.to_html(full_html=False)

    return graph_html




@app.route('/BoxPlot')
def BoxPlot():
    #grafico 
    df = pd.DataFrame({'Grupo': ['A', 'A','B','B','C','C'], 'Valores': [10,20,15,25,30,40]})

    fig = px.box(df, x='Grupo', y='Valores', title='CAJA')
    graph_html = fig.to_html(full_html=False)

    return graph_html




@app.route('/Heatmap')
def Heatmap():
    #grafico 
    df =go.Figure(data=go.Heatmap(
        z=[[1, 20, 30],
           [20, 1, 60],
           [30, 60, 1]],
        X=['X1', 'X2', 'X3'],
        Y=['Y1', 'Y2', 'Y3']
    ))
    fig.update_layout(title='MAPA DE CALOR')
    graph_html = fig.to_html(full_html=False)

    return graph_html




@app.route('/Area')
def Area():
    #grafico 
    df = pd.DataFrame({'X': [1,2,3,4,5], 'Y': [10,20,15,25,30]})

    fig =px.area(df, x='X', y='Y', title='GRAFICO AREA')
    graph_html = fig.to_html(full_html=False)

    return graph_html



@app.route('/Densidad')
def Densidad1():
    #grafico 
    df = pd.DataFrame({
        'X' :np.random.raandn(1000),
        'Y' :np.random.raandn(1000)
    })

    fig =px.density_contour(df, x='X', y='Y', title='GRAFICO DE CONTORNO DE DENSIDAD')
    graph_html = fig.to_html(full_html=False)

    return graph_html



@app.route('/3D')
def G3D():
    #grafico 
    df = pd.DataFrame({
        'X' : [1, 2, 3, 4, 5],
        'Y' : [10, 20, 15, 25, 30],
        'Z' : [5, 10, 15, 20, 25],
    })

    fig =px.scatter_3d(df, x='X', y='Y', z='Z', title='GRAFICO 3D')
    graph_html = fig.to_html(full_html=False)

    return graph_html




@app.route('/Violin')
def Violin():
    #grafico 
    df = px.data.tips()

    fig =px.violin(df, y='total_bill', box=True, points=all, title='GRAFICO VIOLIN')
    graph_html = fig.to_html(full_html=False)

    return graph_html



def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
