from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Prueba 3"

@app.route("/")
def index():
    if 'visitas' not in session:
        session['visitas'] = 0
    if 'reinicios' not in session:
        session['reinicios'] = 0
    session['visitas'] += 1
    return render_template("visitas.html", visitas=session['visitas'], reinicios=session['reinicios'])

@app.route("/destruir_sesion")
def destruir_sesion():
    session.clear()
    return redirect("/")

@app.route("/aumentar_visitas")
def aumentar_visitas():
    session['visitas'] += 2
    return redirect("/")

@app.route("/reiniciar_visitas")
def reiniciar_visitas():
    session['visitas'] = 0
    session['reinicios'] += 1
    return redirect("/")

@app.route("/formulario_cantidad", methods=["POST"])
def formulario_cantidad():
    cantidad = request.form.get("cantidad")
    if cantidad:
        session['visitas'] += int(cantidad)
    return redirect("/")


if __name__=="__main__":   

    app.run(debug=True)