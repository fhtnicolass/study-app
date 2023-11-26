from flask import Flask, request, jsonify

import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def connect_db():
    return sqlite3.connect("myapp.db")

# Rota para iniciar o timer
@app.route('/api/timer/start', methods=['POST'])
def start_timer():
    # Implemente a lógica para iniciar o timer aqui
    return jsonify({"message": "Timer started"})

# Rota para adicionar uma atividade ao cronograma
@app.route('/api/schedule/add', methods=['POST'])
def add_to_schedule():
    data = request.json
    date = data['date']
    activity = data['activity']

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO schedule (date, activity) VALUES (?, ?)", (date, activity))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Activity added to schedule"})

# Rota para listar atividades do cronograma
@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM schedule")
    schedule_data = cursor.fetchall()
    
    conn.close()

    schedule = [{'id': row[0], 'date': row[1], 'activity': row[2]} for row in schedule_data]

    return jsonify(schedule)

# Rota para adicionar uma tarefa à lista de tarefas
@app.route('/api/tasks/add', methods=['POST'])
def add_task():
    task = request.json['task']

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added"})

# Rota para listar tarefas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks_data = cursor.fetchall()
    
    conn.close()

    tasks = [{'id': row[0], 'task': row[1], 'completed': bool(row[2])} for row in tasks_data]

    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
