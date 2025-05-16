from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# MySQL Database Connection
connection = pymysql.connect(
    host='your-rds-endpoint',
    user='admin',
    password='your-password',
    database='flask_crud'
)

# ➡️ Fetch All Users
@app.route('/users', methods=['GET'])
def get_users():
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    return jsonify(users), 200

# ➡️ Add a User
@app.route('/users', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name, email, phone, address) VALUES (%s, %s, %s, %s)",
            (name, email, phone, address)
        )
        connection.commit()
    return "User Added Successfully", 201

# ➡️ Delete a User
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        connection.commit()
    return "User Deleted Successfully", 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
