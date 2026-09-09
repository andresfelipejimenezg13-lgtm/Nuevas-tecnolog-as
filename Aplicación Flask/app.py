from flask import Flask, render_template

app = Flask(__name__)

name = "Andres"
email = "ajime@estudiante.com"  # Tu correo

@app.route("/")
def hello_world():
    return render_template('index.html', person=name, contacto=email)

if __name__ == "__main__":
    app.run(debug=True)