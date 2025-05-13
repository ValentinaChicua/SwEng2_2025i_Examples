# 🧾 Flask User API with Swagger Documentation

This is a simple RESTful API built with **Flask** and documented using **Swagger (Flasgger)**. It allows you to retrieve, create, and view user information.

---

## 📦 Features

- Get all users
- Get user by ID
- Create a new user
- Interactive API documentation via Swagger UI

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/camilonfs1/SwEng2_2025i.git
cd SwEng2_2025i
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> If you don't have a `requirements.txt`, install directly:
```bash
pip install flask flasgger
```

### 3. Run the API

```bash
python app.py
```

The server will run at:  
📍 **     **

---

## 📘 API Documentation

After running the server, you can access the Swagger UI here:  
👉 **http://localhost:5000/apidocs**

---

## 🔗 API Endpoints

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/users`         | Get all users          |
| GET    | `/users/<id>`    | Get user by ID         |
| POST   | `/users`         | Create a new user      |

---

## 📤 Example Requests

### GET `/users`
```bash
curl http://localhost:5000/users
```

### POST `/users`
```bash
curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Charlie"}'
```

### PUT `/users/<id>`
```bash
curl -X PUT http://localhost:5000/users/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice Updated"}'
```

### DELETE `/users/<id>`
```bash
curl -X DELETE http://localhost:5000/users/1
```
---

## 🧰 Tech Stack

- Python 3.x
- Flask
- Flasgger (Swagger for Flask)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## ✍️ Author

Made with ❤️ by camilo vargas 

