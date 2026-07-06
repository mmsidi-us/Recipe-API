recipe-api/
├── app/
│   ├── __init__.py          ← Makes 'app' a Python package
│   ├── main.py              ← FastAPI application entry point
│   ├── config.py            ← Settings and environment variables
│   ├── database.py          ← Database connection and session setup
│   ├── models/              ← SQLAlchemy database models
│   │   ├── __init__.py
│   │   └── recipe.py
│   ├── schemas/             ← Pydantic validation models
│   │   ├── __init__.py
│   │   └── recipe.py
│   ├── routers/             ← API endpoint definitions
│   │   ├── __init__.py
│   │   └── recipes.py
│   └── utils/               ← Helper functions
│       ├── __init__.py
│       └── security.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_users.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md﻿
