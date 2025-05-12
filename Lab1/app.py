# app.py
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# In-memory database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
        examples:
          application/json: [{"id":1,"name":"Alice"}]
    """
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
    responses:
      200:
        description: A user object
      404:
        description: User not found
    """
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: User
          required:
            - name
          properties:
            name:
              type: string
              description: Name of the user
              example: Charlie
    responses:
      201:
        description: User created
      400:
        description: Invalid input
    """
    data = request.get_json()
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
