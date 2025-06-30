# Use a minimal Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Define the default command to run your API
CMD ["python", "predict_api.py"]
