# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Copy Dependencies
COPY requirements.txt /code

# Install dependencies
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . /code

EXPOSE 8000

RUN python manage.py migrate --noinput

CMD python manage.py runserver 0.0.0.0:8000

