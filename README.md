# Recipe API

A production-ready, structured FastAPI application for managing recipes. Built with SQLAlchemy, Pydantic, and PostgreSQL/SQLite.

## 🚀 Features
* **CRUD Operations:** Create, read, update, and delete recipes.
* **Data Validation:** Robust request/response parsing via Pydantic.
* **Database Integration:** Async session management with SQLAlchemy.
* **Security:** Integrated password hashing and security utilities.
* **Testing:** Fully isolated testing environment utilizing Pytest.

---

## 📁 Project Structure

```text
recipe-api/
├── app/
│   ├── __init__.py         # Makes 'app' a Python package
│   ├── main.py             # FastAPI application entry point
│   ├── config.py           # Settings and environment variables
│   ├── database.py         # Database connection and session setup
│   ├── models/             # SQLAlchemy database models
│   │   ├── __init__.py
│   │   └── recipe.py
│   ├── schemas/            # Pydantic validation models
│   │   ├── __init__.py
│   │   └── recipe.py
│   ├── routers/            # API endpoint definitions
│   │   ├── __init__.py
│   │   └── recipes.py
│   └── utils/              # Helper functions
│       ├── __init__.py
│       └── security.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_users.py
├── .env                    # Local environment secrets (DO NOT COMMIT)
├── .gitignore
├── requirements.txt
└── README.md
