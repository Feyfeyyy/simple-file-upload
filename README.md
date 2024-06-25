# My Simple File Upload

Welcome to the simple-file-upload wiki!

This is a simple file upload project using Python Django. The project is a simple web application that allows users to upload files that contains data. The uploaded files are then processed and the data is stored in a database. 

The project is built using Python Django and uses Postgres as the database.

---

## Table of Contents

- [Features](#features)
- [List of Requirements Needed For Project Before Installation](#list-of-requirements-needed-for-project-before-installation)
- [Installation Using Docker](#installation-using-docker)
- [Installation Without Docker](#installation-without-docker)
- [How to Use](#how-to-use)
- [Future Comments](#future-comments)

---

## Features
1. User File Upload
2. Admin Access
3. File Processing
4. Database Storage
5. Query Engine

---

## List of Requirements Needed For Project Before Installation

- Python 3.11
- Django ^5.0
- Postgres 13.4
- Docker
- Poetry
- IDE (VSCode, PyCharm (**recommended**), etc)

## Installation Using Docker

The docker file is already created and the docker-compose file is already created. The docker-compose file will build the image and run the container. The docker-compose file will also create the database and the superuser.

1. Clone the repository
```bash
git clone
```
2. Run the following command to build the docker image and to run the docker container
```bash
docker-compose up
```


## Installation Without Docker

Manually install the project without using Docker.

1. Clone the repository
```bash
git clone
```
2. Run the following command to initialize the virtual environment
```bash
poetry shell
```
3. Run the following command to install the dependencies
```bash
poetry install
```
4. Run the following command to initialize the database
```python
python manage.py makemigrations
python manage.py migrate
```
5. Run the following command to create the superuser
```python
python manage.py createsuperuser
```
6. Run the following command to start the server
```python
python manage.py runserver
```

---

## How to Use

Once the project is installed, you can access the project by going to the following URL:
    
```bash
http://localhost:8000
```

To access the admin panel, you can go to the following URL:

If you have used the Docker installation, the superuser credentials are:

- Username: admin
- Password: admin
    
```bash
http://localhost:8000/admin
```

To access the file upload page, you can go to the following URL:

You will be presented with a minimalistic UI that allows you to upload a file. The file will be processed and the data will be stored in the database.
    
```bash
http://localhost:8000/data/upload
```

To access the query engine, here are some examples of how to query the data:

a data example.
```json
[
    {"name": "John Doe", "age": 30, "city": "New York"},
    {"name": "Jane Smith", "age": 25, "city": "Los Angeles"},
    {"name": "John Smith", "age": 25, "city": "Los Angeles"},
    {"name": "Jane Doe", "age": 30, "city": "New York"}
]
```

If looking to see all the data that has been stored in the database, you can go to the following URL:
    
```bash
http://localhost:8000/data/query
```

results will be:
```json
{
    "status": "success",
    "message": "Data retrieved successfully",
    "data": [
        {
            "data": {"name": "John Doe", "age": 30, "city": "New York"},
            "file_name": "test.csv",
            "file_id": 1
        },
        {
            "data": {"name": "Jane Smith", "age": 25, "city": "Los Angeles"},
            "file_name": "test.json",
            "file_id": 2
        },
        {
            "data": {"name": "John Smith", "age": 25, "city": "Los Angeles"},
            "file_name": "test.csv",
            "file_id": 3
        },
        {
            "data": {"name": "Jane Doe", "age": 30, "city": "New York"},
            "file_name": "test.json",
            "file_id": 4
        }
    ]
```

If looking to filter the data by file type, you can go to the following URL:
    
```bash
http://localhost:8000/data/query?type=csv
```

results will be:
```json
{
    "status": "success",
    "message": "Data retrieved successfully",
    "data": [
        {
            "data": {"name": "John Doe", "age": 30, "city": "New York"},
            "file_name": "test.csv",
            "file_id": 1
        },
        {
            "data": {"name": "John Smith", "age": 25, "city": "Los Angeles"},
            "file_name": "test.csv",
            "file_id": 3
        }
    ]
}
```


If looking to filter by exact match of the data, you can go to the following URL:

```bash
http://localhost:8000/data/query?name=John
```

results will be:
```json
{
    "status": "success",
    "message": "Data retrieved successfully",
    "data": [
        {
            "data": {"name": "John Doe", "age": 30, "city": "New York"},
            "file_name": "test.csv",
            "file_id": 1
        },
        {
            "data": {"name": "John Smith", "age": 25, "city": "Los Angeles"},
            "file_name": "test.csv",
            "file_id": 3
        }
    ]
}
```

or you are able to combine the query by file type and exact match of the data, you can go to the following URL:

```bash
http://localhost:8000/data/query?type=csv&name=John
```

results will be:
```json
{
    "status": "success",
    "message": "Data retrieved successfully",
    "data": [
        {
            "data": {"name": "John Doe", "age": 30, "city": "New York"},
            "file_name": "test.csv",
            "file_id": 1
        },
        {
            "data": {"name": "John Smith", "age": 25, "city": "Los Angeles"},
            "file_name": "test.csv",
            "file_id": 3
        }
    ]
}
```

lastly, if you are looking to partial search of the data, you can go to the following URL:

```bash
http://localhost:8000/data/query/?type=json&match=partial&name=Jane
```

results will be:
```json
{
    "status": "success",
    "message": "Data retrieved successfully",
    "data": [
        {
            "data": {"name": "Jane Smith", "age": 25, "city": "Los Angeles"},
            "file_name": "test.json",
            "file_id": 2
        },
        {
            "data": {"name": "Jane Doe", "age": 30, "city": "New York"},
            "file_name": "test.json",
            "file_id": 4
        }
    ]
}
```

---
## Future Comments

- Add more features
- Add ENV variables for security
- Improve the UI
- Add logging for debugging
- Add Django tests so that the project can be tested
- Add User Authentication and Authorization with JWT
- Add a CI/CD pipeline for the project using Github Actions or Jenkins
- Add different environments for the project (Development, Staging, Production)
- Possibly add Django Rest Framework for API endpoints, so that the project can be used as a REST API
- Possibly more file types for upload if needed
- Possibly more file processing options
- Possibly a NO-SQL database for storage with the input of the data
- Possibly a front-end framework like React or Angular to improve the UI

---

## Contributors

- Feyaaz Chishty