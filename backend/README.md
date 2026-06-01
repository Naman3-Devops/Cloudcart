# CloudCart

CloudCart is an e-commerce backend application built while learning Backend Development, DevOps, and Cloud Engineering.

## Project Goal

The goal of this project is to learn and implement:

* Python Backend Development
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Git & GitHub
* DevOps Fundamentals
* Azure Cloud Services
* Docker
* CI/CD Pipelines

---

## Current Features

* FastAPI Backend
* PostgreSQL Database Integration
* SQLAlchemy ORM Models
* Product API Endpoints
* Swagger API Documentation
* Git Version Control
* GitHub Repository

---

## Tech Stack

### Backend

* Python
* FastAPI

### Database

* PostgreSQL
* SQLAlchemy

### Version Control

* Git
* GitHub

### Future Technologies

* Azure
* Docker
* GitHub Actions
* React
* Terraform

---

## Project Structure

backend/

├── app/

│ ├── models/

│ ├── routers/

│ ├── schemas/

│ ├── database.py

│ └── main.py

│

├── README.md

└── .gitignore

---

## API Endpoints

### Products

| Method | Endpoint       | Description                  |
| ------ | -------------- | ---------------------------- |
| GET    | /products      | Get all products             |
| GET    | /products/db   | Get products from PostgreSQL |
| GET    | /products/{id} | Get product by ID            |
| POST   | /products      | Create product               |
| PUT    | /products/{id} | Update product               |
| DELETE | /products/{id} | Delete product               |

---

## Running Locally

Activate virtual environment:

```bash
source venv/Scripts/activate
```

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Learning Journey

This project is being built from scratch while learning:

* Backend Architecture
* REST APIs
* Database Design
* ORM Concepts
* Version Control
* Cloud Engineering
* DevOps Practices

---

## Future Roadmap

* Complete PostgreSQL CRUD Operations
* Product Categories
* User Authentication
* Shopping Cart
* Orders
* Azure Deployment
* Docker Containers
* CI/CD Pipeline
* React Frontend

---

## Author

Naman Sharma

Learning Backend Development, DevOps, and Cloud Engineering through hands-on projects.
