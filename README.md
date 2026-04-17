# 🚀 Job Tracker API

A production-ready backend API to track job applications with authentication, status tracking, and analytics.

---

## 🌐 Live API

👉 https://job-tracker-api-gjs9.onrender.com/

---

## 🧠 Overview

The **Job Tracker API** is a backend system designed to help users manage and track their job applications efficiently.

It allows users to:

* Register and authenticate securely
* Track job applications
* Update job status over time
* View complete status history
* Analyze job statistics

This project focuses on **real-world backend architecture**, **clean API design**, and **scalable structure**.

---

## ⚙️ Tech Stack

* **Python**
* **Flask**
* **PostgreSQL**
* **SQLAlchemy (ORM)**
* **Flask-JWT-Extended (JWT Auth)**
* **Flask-Migrate (Alembic)**
* **Flask-Limiter (Rate Limiting)**
* **Render (Deployment)**
* **Railway (Database Hosting)**
* **Postman (API Testing)**

---

## 🔐 Features

### 🔑 Authentication

* User Registration
* Login with JWT
* Access & Refresh Tokens
* Secure password hashing
* Token-based protected routes

---

### 💼 Job Management

* Create job applications
* Get all jobs (with filters & pagination)
* Get single job details
* Update job details
* Soft delete jobs

---

### 📊 Status Tracking

* Track status changes (applied → interview → offer / rejected)
* Maintain complete history of status transitions

---

### 📈 Dashboard

* Total jobs count
* Applied / Interview / Offer / Rejected stats

---

### 🛡️ Validation & Error Handling

* Consistent JSON response format
* Proper HTTP status codes (400, 401, 404, 429)
* Schema-based validation

---

## 📬 API Endpoints

### 🔑 Auth

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| POST   | `/auth/register` | Register user        |
| POST   | `/auth/login`    | Login user           |
| POST   | `/auth/refresh`  | Get new access token |
| POST   | `/auth/logout`   | Logout user          |

---

### 💼 Jobs

| Method | Endpoint     | Description                         |
| ------ | ------------ | ----------------------------------- |
| GET    | `/jobs`      | Get all jobs (filters + pagination) |
| POST   | `/jobs`      | Create new job                      |
| GET    | `/jobs/<id>` | Get single job                      |
| PUT    | `/jobs/<id>` | Update job                          |
| DELETE | `/jobs/<id>` | Soft delete job                     |

---

### 📊 Extra

| Method | Endpoint             | Description        |
| ------ | -------------------- | ------------------ |
| GET    | `/jobs/<id>/history` | Job status history |
| GET    | `/dashboard`         | Job statistics     |

---

## 🧪 API Testing (Postman)

A complete Postman collection is included covering:

* Auth flow (Register/Login)
* Job CRUD operations
* Status updates & history
* Full request lifecycle

📁 File:

```
/postman/job-tracker-api.postman_collection.json
```

👉 Import this file into Postman to test the API instantly.

---

## 🧱 Full Project Structure

```
Job_Tracker/
│
├── app/
│   ├── models/
│   │   ├── user.py
│   │   ├── job.py
│   │   ├── status_history.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── jobs.py
│   │   ├── dashboard.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── job_schema.py
│   │
│   ├── utils/
│   │   ├── errors.py
│   │
│   ├── __init__.py
│
├── migrations/
│
├── postman/
│   └── job-tracker-api.postman_collection.json
│
├── run.py
├── config.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🚀 Deployment

* Backend hosted on **Render**
* PostgreSQL database hosted on **Railway**
* Environment variables used for secure configuration

---

## ⚙️ Environment Variables

Required variables:

```
DATABASE_URL=your_postgresql_url
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
```

---

## 🧠 Key Learnings

* Designing scalable backend systems
* Implementing JWT authentication (access + refresh)
* Database modeling with relationships
* API design and best practices
* Handling real-world errors and edge cases
* Deployment and environment management

---

## 📌 Future Improvements

* Add automated testing (pytest)
* Add caching layer (Flask-Caching)
* Add background jobs (APScheduler)
* Build frontend (React)
* Add CI/CD pipeline

---

## 👨‍💻 Author

**Ibrahim**

* GitHub: https://github.com/Ibrahim-2005
* LinkedIn: https://www.linkedin.com/in/mohamed-ibrahim-y/

---

## ⭐ Support

If you found this useful, consider giving this repo a ⭐
