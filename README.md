# NOTES.md — Task 1: Refactored User Management API

## 📌 Overview:
This project is a refactored version of a legacy Flask user management API. It supports creating users, logging in with JWT, and viewing/updating/deleting users.

---

## ✅ Features Implemented

- Modular folder structure using Flask Blueprints
- SQLite database connection via `models/db.py`
- Passwords are securely hashed using `werkzeug.security`
- JWT-based login and token generation (`utils/jwt_helper.py`)
- Clean error handling and JSON responses
- Tested endpoints using Postman

---

## 📁 Folder Structure
```
messy-migration/
├── app.py
├── users.db
├── init_db.py
├── models/
│   └── db.py
├── routes/
│   ├── create_user.py
│   ├── delete_user.py
│   ├── update_user.py
│   ├── login.py
│   ├── get_user.py
│   └── user_api.py
├── utils/
│   └── jwt_helper.py
```

---

## ⚙️ Step-by-Step to Test the App

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install flask werkzeug pyjwt
   ```

3. Initialize the DB:
   ```bash
   python init_db.py
   ```

4. Start the server:
   ```bash
   python app.py
   ```

5. Use Postman to test:
   - `POST /users/create`
   - `POST /users/login`
   - `GET /users/all`
   - `GET /users/<id>`
   - `PUT /users/update/<id>`
   - `DELETE /users/delete/<id>`

---

## 🔐 JWT Token
Add JWT token in Postman Headers:
```
Authorization: Bearer <your_token>
```

---

## 🧪 DB Testing Tips
To inspect the database:
```python
import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()
```



# 🧩 Refactored User Management API

A clean and modular Flask application to manage users with login, password hashing, JWT authentication, and SQLite database.

---

## 🚀 Features

- Create, retrieve, update, delete users
- Login with hashed password and JWT token
- SQLite database backend
- Modular folder structure using Blueprints

---

## 🛠️ Setup Instructions

### 1. Clone or download the repo

### 2. Create virtual environment and install dependencies:
```bash
pip install flask werkzeug pyjwt
```

### 3. Initialize database
```bash
python init_db.py
```

### 4. Run the application
```bash
python app.py
```

Server runs at:
```
http://localhost:5009
```

---

## 📬 API Endpoints

| Method | Endpoint              | Description        |
|--------|-----------------------|--------------------|
| POST   | /users/create         | Create a user      |
| POST   | /users/login          | Login with JWT     |
| GET    | /users/all            | Get all users      |
| GET    | /users/<id>           | Get user by ID     |
| PUT    | /users/update/<id>    | Update user        |
| DELETE | /users/delete/<id>    | Delete user        |

Add `Authorization: Bearer <token>` for protected routes.

---

## 📁 Folder Structure

```
messy-migration/
├── app.py
├── models/
│   └── db.py
├── routes/
├── utils/
├── init_db.py
├── users.db
```

---

## ✅ Task 1 Completed

All endpoints are tested and working in Postman.









