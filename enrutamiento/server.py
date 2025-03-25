from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_flask():
    return '¡Hola Flask!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/ruta')      # Nueva ruta '/ruta'
def ruta_busqueda():
    return '¿Qué ruta estás buscando?'  # Respuesta para la nueva ruta

@app.route('/bienvenido/<nombre>')  # Nueva ruta '/bienvenido/<nombre>'
def bienvenido(nombre):
    return f'Bienvenid@ a esta ruta, {nombre}!'  # Devuelve un mensaje de bienvenida personalizado
#cambio nombre por Python, Miyagi, Taquito

@app.route('/repite/<nombre>/<int:num>')
def repite_cantidad(nombre, num):
    return f'Repite después de mi: {nombre}'*num

#BONUS

#BONUS DE PLATA: En la 3ra tarea de la asignación, asegúrate que lo recibido como nombre sea cadena

@app.route('/bbienvenido/<string:nombre>')
def bbienvenido(nombre):
    return f'Bienvenid@ a esta ruta, {nombre}!'

#BONUS PLATA 2: En la 4ta tarea de la asignación, asegúrate que se reciba un número y una cadena respectivamente

@app.route('/repiteb/<string:nombre>/<int:num>')
def repiteb_cantidad(nombre, num):
    return f'Repite después de mi: {nombre}'*num

#BONUS ORO: Asegúrate de que si el usuario intenta ingresar a alguna ruta no especificada se muestra el mensaje:
# “¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo.”
@app.errorhandler(404)
def not_found(error):
    return '¡Sobrecarga de rutas! No encontramos a donde quieres ir, inténtalo de nuevo.', 404

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente   

    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración/debug para detectar cualquier cambio y recargarlo

