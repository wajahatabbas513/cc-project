from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_data():
    conn = sqlite3.connect('/app/data.db')  # Use the mounted path
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()  # Fetch all data from the 'users' table
    conn.close()
    return render_template('display.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
