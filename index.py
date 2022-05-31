#1 Importar la biblioteca de flask
from glob import escape
from os import abort
from flask import Flask, redirect, render_template, request, url_for, flash

# 2 Instanciar la aplicacion
app = Flask(__name__)

# 3 Definicion de las rutas -- no olvidar crear el archivo html...
@app.route('/')
def index():
    return render_template('index.html')
# 3 Definicion de las rutas -- no olvidar crear el archivo html...
@app.route('/evaluar')
def evaluar():
    return render_template('evaluar.html')

# Definicion de rutas
# lo que va entre "<>" se ingresa por teclado en el browser
@app.route('/capitalize/<word>/')
# Llamar a ruta
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))


# Definicion de rutas----para ejecutar ingreso en el browser los datos a sumar con los /
# lo que va entre "<>" se ingresa por teclado en el browser
@app.route('/suma/<int:num1>/<int:num2>/')
# Llamar a ruta
def suma(num1, num2):
    return '<h1>{}</h1>'.format(num1+num2)

############ mostrar string concatenado#######
@app.route('/concatenar/<string:pal1>/<string:pal2>/')
# Llamar a ruta
def concatenar(pal1, pal2):
    return '<h1>{}</h1>'.format(pal1 + pal2)


####### Definicion de rutas por id ######
@ app.route('/usuario/<int:user_id>/')
# Llamar a ruta
def greet_users(user_id):
    usuario=['Bob', 'Jane', 'Adam']
    try:
        return '<h2>{}</h2>'.format(usuario[user_id])
    except IndexError:
        abort(404)



#esto es una prieba 


# 4 Metodo para correr la aplicacion (main)
if __name__ == '__main__':
    app.run(debug=True)