```python
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('TaskMaster/database/db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/status_update/<int:task_id>', methods=['GET'])
def update_task_status(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task is None:
        return jsonify({"message": "Task not found"}), 404
    else:
        return jsonify({"task_status": task['status']})

if __name__ == "__main__":
    app.run(debug=True)
```