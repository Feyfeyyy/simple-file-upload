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
- [Future Comments](#future-comments)

---

## Features
1. User File Upload
2. Admin Access
3. File Processing
4. Database Storage

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

## Future Comments

- Add more features
- Improve the UI
- Add logging for debugging
- Add Django tests so that the project can be tested
- Add User Authentication and Authorization with JWT
- Add a CI/CD pipeline for the project using Github Actions or Jenkins
- Add different environments for the project (Development, Staging, Production)
- Possibly more file types for upload if needed
- Possibly more file processing options
- Possibly a NO-SQL database for storage with the input of the data
- Possibly a front-end framework like React or Angular to improve the UI

---

## Contributors

- Feyaaz Chishty