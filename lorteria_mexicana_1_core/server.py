from flask import Flask, render_template
import random

app = Flask(__name__)

cartas = [
    "1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas", "6  La sirena", "7  La escalera",
    "8  La botella", "9  El barril", "10 El árbol", "11 El melón", "12 El valiente", "13 El gorrito", "14 La muerte", "15 La pera",
    "16 La bandera", "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro", "21 La mano", "22 La bota", "23 La luna",
    "24 El cotorro", "25 El borracho", "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón", "31 Las jaras",
    "32 El músico", "33 La araña", "34 El soldado", "35 La estrella", "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal",
    "40 El alacrán", "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito", "45 El venado", "46 El sol", "47 La corona",   
    "48 La chalupa", "49 El pino", "50 El pescado", "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"
]

@app.route('/loteria') #nivel 1
def loteria():
    colores = ['#dda8c4', '#287fe4', '#eadb00']  #rosado, celeste, amarillo
    tablero = []

    for i in range(4):
        fila = []
        for j in range(4):
            fila.append(colores[(i+j) % len(colores)])
        tablero.append(fila)
    return render_template('loteria.html', tablero=tablero)

@app.route('/<int:x>') #nivel 2
def loteria_x(x): 
    colores = ['#dda8c4', '#287fe4', '#eadb00']  # rosado, celeste, amarillo
    tablero = []

    for i in range(x):  # Filas
        fila = []
        for j in range(4):  # Columnas
            fila.append(colores[(i + j) % len(colores)])
        tablero.append(fila)

    return render_template('loteria_x.html', tablero=tablero, filas=x)

#@app.route('/<int:x>/<int:y>') #nivel 3
#def loteria_xy(x,y) : 
    #colores = ['#dda8c4', '#287fe4', '#eadb00']  # rosado, celeste, amarillo
    #tablero = []

    #for i in range(x):  # Filas 
        #fila = []
        #for j in range(y):  # Columnas
        #fila.append(colores[(i + j) % len(colores)])
        #tablero.append(fila)

    #return render_template('loteria_xy.html', tablero=tablero, filas=x, columnas=y)

@app.route('/<int:x>/<int:y>')  # Nivel 4
def loteria_xy(x, y):
    colores = ['#dda8c4', '#287fe4', '#eadb00']  # Rosado, celeste, amarillo
    tablero = []

    for i in range(x):  # Filas
        fila = []
        for j in range(y):  # Columnas
            color = colores[(i + j) % len(colores)]
            carta = random.choice(cartas)  
            fila.append({'color': color, 'carta': carta})
        tablero.append(fila)


    return render_template('loteria_xy.html', tablero=tablero, filas=x, columnas=y)

@app.route('/loteria/bonus') #nivel 1 bonus
def loteriab():
    colores = ['#dda8c4', '#287fe4', '#eadb00']  #rosado, celeste, amarillo
    tablero = []

    for i in range(4):
        fila = []
        for j in range(4):
            color = colores[(i + j) % len(colores)]
            carta = random.choice(cartas)
            fila.append({'color': color, 'carta': carta})   
        tablero.append(fila)
    return render_template('loteriab.html', tablero=tablero)

@app.route('/bonus/<int:x>')  # Nivel 2 bonus
def loteria_x_bonus(x): 
    colores = ['#dda8c4', '#287fe4', '#eadb00']  # Rosado, celeste, amarillo
    tablero = []

    for i in range(x):  
        fila = []
        for j in range(4):  
            color = colores[(i + j) % len(colores)]
            carta = random.choice(cartas)  
            fila.append({'color': color, 'carta': carta})
        tablero.append(fila)

    return render_template('loteria_x_bonus.html', tablero=tablero, filas=x)

if __name__=="__main__":   

    app.run(debug=True)