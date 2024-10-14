# Use a base image that includes Python
FROM python:3.9.17-slim

# Install dependencies for building ImageMagick
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libfreetype6-dev \
    libmagickwand-dev \
    pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone and install ImageMagick from source
RUN git clone https://github.com/ImageMagick/ImageMagick.git && \
    cd ImageMagick && \
    git checkout tags/7.1.1-38 && \
    ./configure && make && make install && ldconfig && \
    cd .. && rm -rf ImageMagick

# Install Liberation Sans and other fonts
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    fonts-liberation \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your scripts into the container
COPY ./scripts /app

# Install Flask
RUN pip install flask

# Command to run your Flask app
CMD ["python", "imagemagick_api.py"]
