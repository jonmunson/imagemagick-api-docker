# Use a base image that includes Python
FROM python:3.9.17-slim

# Install ImageMagick
RUN apt-get update && apt-get install -y \
    imagemagick \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your scripts into the container
COPY ./scripts /app

# Install Flask
RUN pip install flask

# Command to run your Flask app
CMD ["python", "imagemagick_api.py"]
