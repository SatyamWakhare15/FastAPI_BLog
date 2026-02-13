# FastAPI_BLog
 As beginner level built a Blog Application using FastAPI with RESTful API endpoints and Jinja2 template rendering. The project demonstrates backend development concepts including routing, JSON responses, and dynamic HTML rendering. Implemented clean project structure and interactive API documentation using Swagger UI. 

 🚀 FastAPI Blog Application

A simple blog application built using FastAPI, Jinja2 Templates, and RESTful API principles.

This project demonstrates:

✅ FastAPI routing

✅ Jinja2 template rendering

✅ HTML & JSON responses

✅ REST API endpoints

✅ In-memory data storage

✅ Swagger UI documentation

✅ Clean project structure

🛠 Tech Stack

Python 3.x

FastAPI

Uvicorn

Jinja2

HTML

📂 Project Structure
fastapi_blog/
│
├── main.py
├── templates/
│     └── home.html
├── venv/
└── README.md

🔗 API Endpoints
Method	Endpoint	Description
GET	/	Render blog homepage (HTML)
GET	/posts	Render blog posts (HTML)
GET	/api/posts	Get all posts (JSON)

▶️ How to Run
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn jinja2
uvicorn main:app --reload


Then open:

http://127.0.0.1:8000

📘 Features

Dynamic template rendering using Jinja2

JSON API for frontend/backend integration

Swagger documentation at /docs

Beginner-friendly FastAPI structure

 
