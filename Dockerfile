# Use the official Python image as the base image
FROM python:3.11.6-alpine

WORKDIR /usr/src/app
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# Install system dependencies if needed (uncomment and add commands as necessary)
# RUN apt-get update && apt-get install -y ...

# Install system dependencies
# RUN apk update && \
#     apk add --no-cache \
#     bash \
#     chromium \
#     chromium-chromedriver \
#     curl \
#     unzip

RUN pip install --upgrade pip

# Copy the requirements file and install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the Django project files into the container
COPY . /usr/src/app/

# Expose the port your Django app will run on (if needed)
# EXPOSE 8000

# Default command to run when the container starts
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
