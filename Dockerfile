# Dockerfile
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run the celery worker
CMD ["celery", "-A", "your_project_name", "worker", "-l", "info"]