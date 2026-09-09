from flask import Flask, render_template

# Creamos una NUEVA aplicación Flask (independiente de app.py)
app = Flask(__name__)

# ==========================================
# DATOS PARA EL PORTAL
# ==========================================
nombre = "Andres"
correo = "ajime@estudiante.com" 

# ==========================================
# RUTAS DEL PORTAL DE PERSONA
# ==========================================

# Ruta principal → Portal de Persona
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para el saludo original (reutilizamos el mismo index.html)
@app.route('/saludo')
def saludo():
    return render_template('index.html', person=nombre, email=correo)

# Ruta para la To-Do List (explica que está en to-do.py)
@app.route('/tareas')
def tareas():
    return """
    <h1>📋 To-Do List</h1>
    <p>La aplicación To-Do List está en el archivo <strong>to-do.py</strong>.</p>
    <p>Para usarla, abre una terminal y ejecuta:</p>
    <pre>python to-do.py</pre>
    <a href='/'>Volver al portal</a>
    """

# Ruta para juegos (placeholder)
@app.route('/juego')
def juego():
    return """
    <h1>🎮 Sección de Juegos</h1>
    <p>Próximamente...</p>
    <a href='/'>Volver al portal</a>
    """

# ==========================================
# EJECUCIÓN
# ==========================================
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Puerto diferente para no chocar con app.py