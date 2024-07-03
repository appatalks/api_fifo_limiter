from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="api_gateway",
        # password="your_mysql_password",
        database="api_gateway_fifo"
    )
    return conn

# Endpoint to save data to the database
@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.json.get('data')
    if data:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO api_calls (data) VALUES (%s)', (data,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201
    else:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400

# Endpoint to retrieve and delete the oldest data (FIFO)
@app.route('/api/deliver', methods=['GET'])
def deliver_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM api_calls ORDER BY timestamp ASC LIMIT 1')
    row = cursor.fetchone()
    if row:
        cursor.execute('DELETE FROM api_calls WHERE id = %s', (row['id'],))
        conn.commit()
        conn.close()
        return jsonify({'data': row['data']}), 200
    else:
        conn.close()
        return jsonify({'status': 'error', 'message': 'No data available'}), 404

if __name__ == "__main__":
    app.run(debug=False)
