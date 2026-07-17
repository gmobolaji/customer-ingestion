# Customer Ingestion V1 – Build Notes

## Goal

Build a containerized ETL pipeline that extracts customer data from a REST API, transforms it using Python, and loads it into PostgreSQL using Docker Compose.

Final Architecture

REST API
    │
    ▼
Extract (Python)
    │
    ▼
Transform
    │
    ▼
Load
    │
    ▼
PostgreSQL (Docker)

---

## Technologies

- Docker
- Docker Compose
- Python 3.12
- PostgreSQL 17
- psycopg2
- requests
- Git/GitHub

---

## Project Structure

customer-ingestion/

├── app/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── db.py
│
├── sql/
│   └── create_tables.sql
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore

---

## Build Order

### 1. Create GitHub Repository

Create empty repository.

Clone locally.

Initialize project structure.

---

### 2. Create Project Files

Dockerfile

docker-compose.yml

requirements.txt

app/

sql/

.gitignore

---

### 3. Configure PostgreSQL

Docker Compose

- postgres container
- warehouse database
- exposed port 5432
- persistent Docker volume

Important

Docker containers communicate using service names.

Example

host="postgres"

NOT

host="localhost"

---

### 4. Build Python Container

Dockerfile

- python:3.12-slim
- install requirements
- copy application
- execute main.py

---

### 5. Extract Layer

Source

https://jsonplaceholder.typicode.com/users

requests.get()

response.raise_for_status()

Return JSON list.

---

### 6. Transform Layer

Extract required columns

customer_id

customer_name

email

Return cleaned dictionary.

---

### 7. Database Layer

db.py

Create PostgreSQL connection

psycopg2.connect()

Connection values

host="postgres"

database="warehouse"

user="postgres"

password="password"

---

### 8. SQL Schema

create_tables.sql

CREATE TABLE IF NOT EXISTS customers
(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    email TEXT
);

Schema stored separately from Python.

---

### 9. Load Layer

INSERT INTO customers

ON CONFLICT (customer_id)
DO NOTHING

Purpose

Idempotent loads.

Pipeline can be executed multiple times safely.

---

### 10. Main Pipeline

initialize_database()

↓

Extract

↓

Transform

↓

Load

↓

Pipeline completed successfully

---

## Validation

Verify data loaded

docker exec -it ingestion-postgres \
psql -U postgres -d warehouse

Run

SELECT COUNT(*) FROM customers;

Expected

10

Verify

SELECT * FROM customers;

---

## Docker Commands

Validate Compose

docker compose config

Build

docker compose up --build

Detached Mode

docker compose up -d

Stop

docker compose down

Running Containers

docker ps

Container Logs

docker compose logs

---

## Git Workflow

git add .

git commit -m "message"

git push

If remote already contains commits

git pull origin main --rebase

Resolve conflicts

git add .

git rebase --continue

Push

git push

---

## Major Errors Encountered

### YAML syntax

Incorrect indentation

Duplicate keys

Incorrect depends_on formatting

---

### Port Conflict

Bind for 5432 failed

Cause

Local PostgreSQL already using port.

---

### PostgreSQL 18 Data Directory

Mount path changed.

Resolved by using PostgreSQL 17.

---

### Docker Networking

Incorrect

localhost

Correct

postgres

---

### Missing Python Files

main.py path incorrect.

Docker COPY path corrected.

---

### Import Errors

Incorrect function names

Incorrect module imports

Resolved by matching filenames and functions.

---

### REST API

jsonplaceholder.org

Returned HTTP 403.

Changed to

jsonplaceholder.typicode.com

---

### Python Errors

SyntaxError

Missing comma

NameError

Variable mismatch

ImportError

Incorrect function names

---

### Git Errors

Merge conflicts

Remote ahead of local

Resolved using

git pull --rebase

Conflict resolution

---

## Production Concepts Introduced

Docker Networking

Containerized PostgreSQL

REST API Extraction

ETL Architecture

SQL Schema Management

Database Initialization

Idempotent Loads

Separation of Concerns

Git Version Control

Container Orchestration

---

## Lessons Learned

Never trust the application.

Always validate the database.

SELECT COUNT(*)

before assuming data loaded successfully.

Read stack traces from top to bottom.

Build incrementally.

Validate after every feature.

Commit frequently.

Separate schema from application code.

Docker services communicate using service names rather than localhost.

---

## Final Result

Successfully built a Dockerized ETL pipeline that

- extracts customer data from a REST API
- transforms data into a warehouse schema
- initializes PostgreSQL automatically
- loads records into PostgreSQL
- prevents duplicate inserts
- validates successful ingestion using SQL
