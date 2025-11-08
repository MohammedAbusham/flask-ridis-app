# flask-ridis-app

This project demonstrates how to **build and run a Flask application connected to a Redis datebase** using docker.
It’s intended as a learning resource for understanding containerized development workflows.

---
## 🚀 Steps to Build and Run

Follow the steps below to build and run your Flask + Redis setup:

1. **Install Docker**  
   Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2. **Start the Docker Engine**  
   Ensure the Docker daemon is running before proceeding.

3. **Create Your Flask Application**  
   Write your Python application in a file named `app.py`.

4. **Create a Dockerfile**  
   Define your Flask app’s Docker image using a Dockerfile (see example below).

5. **Create Your docker-compose yml file**
   Write your docker-compose in a file named 'docker-compose.yml'.
   - In this file you need to declar the version of python and Redis DB you want to build, make the directory and copy the files in.
   - You will also assign the ports, map and mount the volume for persistent data storage.
