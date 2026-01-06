# ImageMagick Docker Setup with Flask API

This project provides a Docker Compose setup for running an ImageMagick service alongside a Flask API wrapper. The API allows you to process images using ImageMagick through HTTP requests.

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
         "supplied_image": "/images/input_image.png",\
         "text": "Your Custom Text Here",\
         "font_size": 80\
       }'
   ```

   Ensure `input_image.png` exists in the `images` folder (it is mounted as `/images` in the container).

6. **Check Output**:
   After processing, the output image will be saved in the `images` directory with a name like `final_output_<pid>.jpg`.
   This avoids filename collisions when multiple requests run at the same time.

## Stopping the Services

To stop the services, run:

```bash
docker-compose down
```

## License

This project is licensed under the MIT License.

### Who made this?

I’m **Jon Munson** - I like building simple things that solve real problems.

**Your support helps me keep shipping:** maintaining repos, fixing bugs, and adding features.  
<a href="https://buymeacoffee.com/jonmunson">
  <img src="https://cdn.simpleicons.org/buymeacoffee/FFDD00" alt="buy me a coffee" width="16" height="16">
  <b>&nbsp;Buy me a coffee</b>
</a>

More about me:
&nbsp;<a href="https://www.jonmunson.co.uk"><img src="https://cdn.simpleicons.org/googlechrome/ffffff" width="16" height="16"><b>&nbsp;Website</b></a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="https://x.com/jonmunson"><img src="https://s.magecdn.com/social/tc-x.svg" width="16" height="16"><b>&nbsp;@jonmunson</b></a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/jonmunson/"><img src="https://s.magecdn.com/social/tc-linkedin.svg" width="16" height="16"><b>&nbsp;LinkedIn</b></a>

---
