from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows React to connect to Flask

# Linked list muna for database
tasks = []

# GET all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "name": data['name'],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# PATCH to mark as done
@app.route('/api/tasks/<int:task_id>', methods=['PATCH'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# DELETE a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"result": "success"})

if __name__ == '__main__':
    app.run(debug=True)
