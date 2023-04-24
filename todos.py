from flask import Flask, request, jsonify, json

app = Flask(__name__)

todos=[
    
   {
        "done": True,
        "label": "Sample Todo 1"
   },
   {
       "done": True,
       "label": "Sample Todo 2"
   }
]

@app.route("/todos", methods=['POST'])
def addTodos():
    tarea = request.json
    print(tarea)
    todos.append(tarea) 
    return jsonify(todos)

@app.route("/todos", methods=['GET'])
def getTodos():
    return jsonify(todos)

@app.route("/todos/<int:index>", methods=['DELETE'])
def deleteTodos(index):
    if index < len(todos):
        del todos[index]
        return jsonify(todos)
    else:
        return "Todo item does exist", 404

app.run(port='6969')