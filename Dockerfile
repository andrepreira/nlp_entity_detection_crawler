# Use the official Python image as a parent image
FROM python:3.10-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Run the unit tests
RUN python -m unittest discover

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Use uvicorn as the production ASGI server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
