# Use the official Python image as the base image
FROM python:3.9.5

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE djangoproject.settings

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the project files into the container
COPY . /code/

# Install project dependencies
RUN pip install -r requirements.txt

# Expose the port the application will run on
EXPOSE 8000

# Use the custom wait script to wait for the PostgreSQL database and start the Gunicorn server
CMD ["gunicorn", "djangoproject.wsgi:application", "--bind", "0.0.0.0:8000"]
