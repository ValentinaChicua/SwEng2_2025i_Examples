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
    user = [u for u in users if u["id"] == user_id]
    if user:
        return jsonify(user[0])
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
      - in: body
        name: body
        required: true
        schema:
          id: UserUpdate
          required:
            - name
          properties:
            name:
              type: string
              description: New name of the user
              example: Alice Updated
    responses:
      200:
        description: User updated
        examples:
          application/json: {"id": 1, "name": "Alice Updated"}
      404:
        description: User not found
        examples:
          application/json: {"error": "User not found"}
    """
    data = request.get_json()
    user = [u for u in users if u["id"] == user_id]
    if user:
        user[0]["name"] = data["name"]
        return jsonify(user[0])
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user
    responses:
      200:
        description: User deleted
        examples:
          application/json: {"message": "User deleted"}
      404:
        description: User not found
        examples:
          application/json: {"error": "User not found"}
    """
    global users
    user = [u for u in users if u["id"] == user_id]
    if user:
        users = [u for u in users if u["id"] != user_id]
        return jsonify({"message": "User deleted"})
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

@app.route('/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    """
    Partially update a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user to update
      - in: body
        name: body
        required: true
        schema:
          id: UserPatch
          properties:
            name:
              type: string
              description: New name of the user
              example: Alice Updated
    responses:
      200:
        description: User updated successfully
        examples:
          application/json: {"id": 1, "name": "Alice Updated"}
      404:
        description: User not found
        examples:
          application/json: {"error": "User not found"}
      400:
        description: Invalid input
        examples:
          application/json: {"error": "No update data provided"}
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No update data provided"}), 400
        
    user = [u for u in users if u["id"] == user_id]
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    if "name" in data:
        user[0]["name"] = data["name"]
        
    return jsonify(user[0])

if __name__ == '__main__':
    app.run(debug=True)
