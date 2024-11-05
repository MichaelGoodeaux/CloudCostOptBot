# Dockerfile - Production

# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only production requirements
COPY python/requirements.txt .

# Install only production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY python/ python/

# Set PYTHONPATH to ensure imports work correctly
ENV PYTHONPATH=/app/python

# Command to run the application (replace with your application’s entry point)
CMD ["python", "your_app_entry.py"]
