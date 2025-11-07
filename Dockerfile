# Use an official lightweight Python image
FROM python:3.11-slim

# Prevents Python from writing .pyc files and forces unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy your app files into the container
COPY . /app

# Install Python dependencies (Flask + MySQL client)
RUN pip install flask redis

# Expose port 5000 for Flask
EXPOSE 5000

# Default command to start the Flask app
CMD ["python", "app.py"]
