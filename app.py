from flask import Flask, abort, request, render_template
from calculo import calcularPotencial
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == "POST":
        potencial = request.form.get("diferenciaPotencial", "")
        cantidad = request.form.get("cantidadPuntos", "")
        precision = request.form.get("precision", "")
        resultado = calcularPotencial(potencial, cantidad, precision)
        return render_template("resultado.html", resultado=resultado , potencial=potencial, cantidad=cantidad, precision=precision)
    elif request.method == "GET":
        potencial = request.args.get("diferenciaPotencial", "")
        cantidad = request.args.get("cantidadPuntos", "")
        precision = request.args.get("precision", "")
        return render_template("index.html", potencial=potencial, cantidad=cantidad, precision=precision)
    

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
