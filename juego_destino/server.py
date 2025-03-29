from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'destino'

@app.route('/')
def index():
      return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
   session['nombre'] = request.form['nombre']
   session['numero'] = request.form['numero']
   session['lugar'] = request.form['lugar']
   session['comida'] = request.form['comida']
   session['profesion'] = request.form['profesion']
   
   session['mensaje'] = random.choice(['bueno', 'malo'])
   return redirect('/futuro')

@app.route('/futuro')
def futuro():
   mensaje_tipo = session.get('mensaje', 'bueno')
   if session['mensaje'] == 'bueno':
      mensaje = f"Soy el adivino del Dojo, {session['nombre']} tendrá un viaje muy largo dentro de {session['numero']} años a {session['lugar']} y estará el resto de sus días preparando {session['comida']} para todas las personas que quiere. Cambio de profesión y ahora es {session['profesion']}."
   else:
      mensaje = f"Soy el adivino del Dojo, {session['nombre']} tendrá {session['numero']} años de mala suerte, nunca conocerá {session['lugar']} y jamás volvió a comer {session['comida']}."
   return render_template('futuro.html', nombre=session['nombre'], numero=session['numero'], lugar=session['lugar'],
         comida=session['comida'], profesion=session['profesion'], mensaje=mensaje)

if __name__=="__main__":   

   app.run(debug=True)