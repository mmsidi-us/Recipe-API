# Recipe API Challenge

A modular, properly structured FastAPI application tracking Recipes and Ingredients using separated routers, Pydantic data schemas, and in-memory storage.

## 📁 Project Structure

```text
recipe-api/
├── app/
│   ├── __init__.py         # Makes 'app' a Python package
│   ├── main.py             # FastAPI entry point & Router wiring
│   ├── config.py           # Application configurations (Pydantic Settings)
│   ├── schemas/            # Pydantic validation models
│   │   ├── __init__.py
│   │   ├── recipe.py
│   │   └── ingredient.py
│   └── routers/            # Endpoint route handlers
│       ├── __init__.py
│       ├── recipes.py
│       └── ingredients.py
├── .env                    # Local environment secrets
├── .gitignore              # Git ignored assets
└── requirements.txt        # Third-party dependencies
