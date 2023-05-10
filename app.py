from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_word():
    listaLetras = ['a','b','c']
    nombre_apellido = "Pablo Lemo"
    return render_template ("index.html",
           nombre= nombre_apellido,
           lista = listaLetras,
         )




if __name__=="__main__":
    app.run(debug=True)
    


'''@app.route("/bienvenido") 
def welcome():
    return "<h1>Riquelme pecho frio<h1>"

@app.route("/bienvenido/<nombre>") #lo que va entre <> es una variable
def welcome_nombre(nombre):
    return f"<h1>Hola {nombre}<h1>"

@app.route("/suma/<a>/<b>") 
def suma(a,b):
    try:
        result = int(a) + int(b)
        return f'<h1>La suma es: {result}<h1>'
    except:
        return {'No puedo realizar esa operacion'}

'''
