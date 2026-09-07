<div align="center">
  
# 🚀 Job Tracker API

[![Run Tests](https://github.com/Ibrahim-2005/job-tracker-api/actions/workflows/test.yml/badge.svg)](https://github.com/Ibrahim-2005/job-tracker-api/actions/workflows/test.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?logo=postgresql)
![JWT](https://img.shields.io/badge/JWT-Authentication-success)
![Pytest](https://img.shields.io/badge/Tested-Pytest-success)
![Render](https://img.shields.io/badge/Render-Deployed-success)
![Railway](https://img.shields.io/badge/Database-Railway-purple)

A production-ready Flask REST API for tracking job applications with JWT authentication, analytics, caching, background jobs, and automated testing.

---
</div>

## 🌐 Live API

👉 https://job-tracker-api-gjs9.onrender.com/

---

## 🧠 Overview

The **Job Tracker API** is a backend system designed to help users manage and track their job applications efficiently.
This API is designed with production-ready practices including caching, background jobs, and CI/CD.

It allows users to:

* Register and authenticate securely  
* Track job applications  
* Update job status over time  
* View complete status history  
* Analyze job statistics  
* Improve performance using caching  

This project focuses on **real-world backend architecture**, **clean API design**, and **scalable structure**.

---

## ⚙️ Tech Stack

* **Python**
* **Flask**
* **PostgreSQL**
* **SQLite (for testing)**
* **SQLAlchemy (ORM)**
* **Flask-JWT-Extended (Authentication)**
* **Flask-Migrate (Alembic)**
* **Flask-Caching (Performance)**
* **Flask-Limiter (Rate Limiting)**
* **APScheduler (Background Jobs)**
* **Pytest (Testing)**  
* **GitHub Actions (CI)**  
* **Render (Deployment)**
* **Railway (Database Hosting)**
* **Postman (API Testing)**

---

## 🏛 Architecture

```text
                   Client
                     │
                     ▼
             Flask REST API
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Authentication   Job Routes   Dashboard
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              Service Layer
                     ▼
              SQLAlchemy ORM
                     ▼
               PostgreSQL
                     ▲
                     │
        APScheduler Background Jobs

        Flask-Caching (Dashboard)

```
---

## 🔐 Features

### 🔑 Authentication

* User Registration  
* Login with JWT  
* Access & Refresh Tokens  
* Secure password hashing  
* Token-based protected routes  
* Logout with token blocklist  

---

### 💼 Job Management

* Create job applications  
* Get all jobs (with filters & pagination)  
* Get single job details  
* Update job details  
* Soft delete jobs  
* Duplicate job prevention  

---

### 📊 Status Tracking

* Track status changes (applied → interview → offer → rejected)  
* Maintain complete history of status transitions  

---

### 📈 Dashboard

* Total jobs count  
* Applied / Interview / Offer / Rejected stats  
* Response rate calculation  
* Stale job detection (based on inactivity, not creation time)  

---

### ⚡ Performance Optimization

* User-specific dashboard caching  
* Manual cache control using:
  - `X-Cache: HIT`
  - `X-Cache: MISS`

---

### 🔄 Background Jobs

* Daily job: identify stale applications  
* Weekly job: clear cached data  

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

### 📊 History

| Method | Endpoint             | Description             |
| ------ | -------------------- | ----------------------- |
| GET    | `/jobs/<id>/history` | Job status history      |
| GET    | `/dashboard`         | Job statistics          |
| GET    | `/dashboard/stale`   | Stale job detection     |

---

## 📖 Example API Request

### Login

```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

### Response

```json
{
  "access_token": "...",
  "refresh_token": "..."
}
```

---

## ⚡ Caching Strategy

Dashboard responses are cached per user.

Cache key format:


```
dashboard_<user_id>
```


Response header shows cache behavior:


```
X-Cache: HIT / MISS
```
---

## 🧠 Stale Job Logic

A job is considered stale if:
- Status = applied  
- AND no activity in the last 7 days  

Uses:
StatusHistory.changed_at (latest activity), NOT created_at.

---

### 🧪 Testing & CI

* Pytest-based test suite  
* GitHub Actions CI pipeline  
* In-memory database for isolated testing  

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
│   │   ├── scheduler.py
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
* Performance optimization using caching  
* Handling real-world errors and edge cases  
* Deployment and CI integration  

---

## 📌 Future Improvements

* Redis-based caching  
* Persistent JWT blocklist  
* Expanded test coverage  
* Frontend (React)  
* Docker support

---

## ⚠️ Known Limitations

* JWT blocklist is stored in-memory and resets when the server restarts  
* SimpleCache is not suitable for multi-instance production  
* Scheduler runs inside the app (can be separated in production)  

---

## 👨‍💻 Author

**Mohamed Ibrahim**

Backend Developer

Python • Flask • PostgreSQL

* GitHub: https://github.com/Ibrahim-2005
* LinkedIn: https://www.linkedin.com/in/mohamed-ibrahim-y/

---

## ⭐ Support

If you found this useful, consider giving this repo a ⭐

---
