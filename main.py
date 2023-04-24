from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route("/saludar", methods=['GET', 'POST'])
def saludar():
    if (request.method=='GET'):
        return "Buenas Noches hace frio :C"
    else:
        body = request.get_json()
        print(body)
        return jsonify({
            "name":body['name'],
            "saludo": "buenas noches, hace frio"
        })
@app.route("/chayanne/<frase>",methods=['GET'])        
def verso (frase):
    cancion = [
        "De lunes a domingo voy desesperado"
        "tu dimde donde estas que yo no te he encontrado"
        "hay que ser torero, poner el alma en el ruedo"
    ]
    
    return cancion [frase]
@app.route('/', methods=['GET'])
def html():
    return render_template("index.html")       

app.run(port='3452')