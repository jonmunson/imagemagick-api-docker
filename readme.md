# ImageMagick Docker Setup with Flask API

This project provides a Docker Compose setup for running an ImageMagick service alongside a Flask API wrapper. The API allows you to easily process images using ImageMagick through HTTP requests.

## Project Structure

```
imagemagick-docker/
├── docker-compose.yml
├── images/
│   └── (this folder will hold your input and output images)
├── scripts/
│   └── imagemagick_api.py
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic knowledge of how to use Docker commands.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/imagemagick-docker.git
   cd imagemagick-docker
   ```

2. **Set Up the Project**:
   Create the `images` directory for input and output images:

   ```bash
   mkdir images
   ```

3. **Run the Docker Compose**:
   Start the services by running:

   ```bash
   docker-compose up -d
   ```

4. **Access the API**:
   The API will be available at `http://localhost:5000/process-image`. You can use this endpoint to process images.

5. **Sending Requests**:
   To process an image, send a POST request with JSON data. Here’s an example using `curl`:

   ```bash
   curl -X POST http://localhost:5000/process-image \
   -H "Content-Type: application/json" \
   -d '{\
         "input_image": "input_image.png",\
         "text": "Your Custom Text Here",\
         "output_image": "output_image.png"\
       }'
   ```

   Ensure `input_image.png` exists in the `images` folder.

6. **Check Output**:
   After processing, the output image will be saved in the `images` directory with the name specified in the `output_image` field.

## Stopping the Services

To stop the services, run:

```bash
docker-compose down
```

## License

This project is licensed under the MIT License.
