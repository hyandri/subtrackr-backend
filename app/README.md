

```markdown
# SubTrackr - Subscription Management API

A production-ready **FastAPI** backend for managing personal subscriptions (Netflix, Spotify, etc.).

Built while transitioning from basic CRUD to professional backend development.

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20Web%20Tokens)

---

## ✨ Features

- **User Authentication** (Register + Login with JWT)
- **Secure Password Hashing** (bcrypt)
- **Subscription Management** (Full CRUD)
- **Protected Routes** (Only authenticated users can access their data)
- **Async PostgreSQL** with SQLAlchemy 2.0
- **Pydantic v2** for request/response validation
- **CORS** enabled for frontend integration
- **Clean project structure**
- **Environment-based configuration**

---

## 🛠 Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL + SQLAlchemy (Async)
- **Authentication**: JWT + bcrypt
- **Validation**: Pydantic v2
- **ASGI Server**: Uvicorn

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/hyandri/subtrackr-backend.git
cd subtrackr-backend
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
```bash
cp .env.example .env
```
Then update `.env` with your PostgreSQL credentials.

### 5. Run the application
```bash
uvicorn app.main:app --reload
```

### 6. Open API Documentation
Go to: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📋 API Endpoints

| Method | Endpoint                | Description                  | Auth Required |
|--------|-------------------------|------------------------------|---------------|
| POST   | `/auth/register`        | Register new user            | No            |
| POST   | `/auth/login`           | Login and get JWT token      | No            |
| POST   | `/subscriptions/`       | Create new subscription      | Yes           |
| GET    | `/subscriptions/`       | Get all my subscriptions     | Yes           |
| GET    | `/subscriptions/{id}`   | Get single subscription      | Yes           |

---

## 📁 Project Structure

```
subtrackr/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routers/
│   └── utils/
├── .env
├── requirements.txt
└── README.md
```

---

## 🎯 Learning Objectives Achieved

- FastAPI project structure
- Async database with SQLAlchemy
- JWT Authentication
- Protected routes with dependencies
- Separation of Models vs Schemas
- Environment configuration
- Professional backend practices

---

## 🔮 Future Enhancements (Coming Soon)

- Email reminders using background tasks
- Rate limiting
- Global error handling
- Docker + Docker Compose
- Payment integration (Stripe)
- Unit & Integration tests
- Deployment to VPS

---

## ⭐ Show Your Support

If you like this project, please give it a star! ⭐

---




Would you like me to also create a `.env.example` file content for you?

Let me know when you’ve pushed it to GitHub, and we can continue with the next phase.
