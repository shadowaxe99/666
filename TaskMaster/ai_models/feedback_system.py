```python
import sqlite3
from sqlite3 import Error

class FeedbackSystem:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        return conn

    def submit_feedback(self, feedback_id, user_id, feedback_content):
        conn = self.create_connection()
        with conn:
            feedback = (feedback_id, user_id, feedback_content)
            sql = ''' INSERT INTO feedbacks(feedback_id, user_id, feedback_content)
                      VALUES(?,?,?) '''
            cur = conn.cursor()
            cur.execute(sql, feedback)
            return cur.lastrowid

    def get_feedback(self, feedback_id):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM feedbacks WHERE feedback_id=?", (feedback_id,))
            rows = cur.fetchall()
            for row in rows:
                print(row)

    def update_feedback(self, feedback_id, feedback_content):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("UPDATE feedbacks SET feedback_content = ? WHERE feedback_id = ?", (feedback_content, feedback_id))
            conn.commit()

    def delete_feedback(self, feedback_id):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM feedbacks WHERE feedback_id=?", (feedback_id,))
            conn.commit()
```