from flask import Flask

app=Flask(__name__)

@app.route("/hola")
def hola():
    return "hola mundo"
@app.route("/chau")
def adios():
    return "chau"

@app.route("/saludo/<nombre>")
def nose(nombre):
    return f"hola {nombre}" 

if __name__ == "__main__":
    app.run(debug=True)

app.run()