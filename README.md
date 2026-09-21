FastAPI-CRUD-using-psycopg2
A simple CRUD (Create, Read, Update, Delete) API built using FastAPI and psycopg2 for direct PostgreSQL database interactions.

🚀 Features
	* Create, Read, Update, and Delete records via RESTful API endpoints
	* Direct PostgreSQL integration using psycopg2
	* Request/response validation with Pydantic schemas
	* Environment variable configuration using .env

🛠️ Tech Stack
	* FastAPI - Web framework for building APIs
	* psycopg2 - PostgreSQL database adapter for Python
	* Pydantic - Data validation and settings management
	* PostgreSQL - Relational database

📁 Project Structure
FastAPI-CRUD-using-psycopg2/
├── main.py          # Application entry point and API routes
├── schemas.py        # Pydantic models for request/response validation
├── sample.py          # Sample/reference code
├── .env               # Environment variables (not committed)
└── README.md

⚙️ Setup and Installation
	1. Clone the repository:

git clone https://github.com/ajimol960-blip/FastAPI-CRUD-using-psycopg2.git
cd FastAPI-CRUD-using-psycopg2

	1. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

	1. Install dependencies:

pip install fastapi uvicorn psycopg2 python-dotenv

	1. Create a .env file with your database credentials:

DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

	1. Run the application:

uvicorn main:app --reload

	1. Visit the interactive API docs at:

http://127.0.0.1:8000/docs

📌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/items` | Get all items |
| GET | `/items/{id}` | Get a single item |
| POST | `/items` | Create a new item |
| PUT | `/items/{id}` | Update an existing item |
| DELETE | `/items/{id}` | Delete an item |

