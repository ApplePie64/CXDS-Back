# CXDS-BACK

This repository contains the backend server for the CXDS project, built using **FastAPI** and designed to serve a React Native mobile app.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
   - [Clone the Repository](#clone-the-repository)
   - [Setup the Virtual Environment](#setup-the-virtual-environment)
   - [Install Dependencies](#install-dependencies)
3. [Environment Variables](#environment-variables)
4. [Run the Application](#run-the-application)
5. [Database Migrations](#database-migrations)
6. [Testing](#testing)

---

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10+
- pip (Python package manager)
- Git
- MongoDB Atlas Account (for MongoDB setup)
- Supabase Account (for PostgreSQL setup)

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/cxds-back.git
cd cxds-back
```

### 2. Setup the Virtual Environment
Create a virtual environment to isolate the project dependencies:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows:
```bash
.venv\Scripts\activate
```

Mac/Linux:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
Install all required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables
Create a .env file in the root directory and set the required environment variables. An example .env file:

```env
Copy code
# MongoDB
MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>
MONGODB_DB_NAME=<dbname>

# PostgreSQL
SUPABASE_URL=https://<supabase_url>
SUPABASE_API_KEY=<supabase_api_key>
SUPABASE_DB_URL=postgresql://<username>:<password>@<host>/<dbname>

# Other
SECRET_KEY=your_secret_key
```

Replace \<username>, \<password>, \<dbname>, and other placeholders with your actual credentials.

## Run the Application
To start the backend server, run:

```bash
uvicorn src.main:app --reload
```

The server will be accessible at http://127.0.0.1:8000.

Database Migrations
If you make changes to the database schema, use Alembic for migrations:

Generate a new migration script:

```bash
alembic revision --autogenerate -m "Migration message"
```

Apply the migrations:

```bash
alembic upgrade head
```
## Testing
Run tests to ensure everything is working correctly:

```bash
pytest
```

## Folder Structure
The src directory contains the modular endpoint structure. Each endpoint (e.g., address_management) includes:

constants.py
dependencies.py
exceptions.py
models.py
router.py
schemas.py
service.py
utils.py
Modify or add to these files as needed for your endpoint-specific logic.