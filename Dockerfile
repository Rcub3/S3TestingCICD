# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port that the app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
