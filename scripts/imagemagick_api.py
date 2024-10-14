from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    # Get parameters from the request
    data = request.json
    text = data.get('text', 'Test Text')
    font_size = data.get('font_size', 80)  # Default font size
    
    # Check if supplied_image is provided
    supplied_image = data.get('supplied_image')
    if not supplied_image:
        return jsonify({'error': 'No supplied image provided.'}), 400  # Bad Request
    
    # Paths for intermediate images
    background_path = '/images/background.png'
    text_image_path = '/images/text_image.png'
    resized_supplied_image_path = '/images/resized_supplied_image.png'  # Updated variable name
    final_output_path = '/images/final_output.jpg'
    
    # Step 1: Create the black background
    subprocess.run(['magick', '-size', '1920x1920', 'xc:black', background_path])

    # Step 2: Annotate text on the background
    subprocess.run([
        'magick', background_path, 
        '-gravity', 'North', 
        '-pointsize', str(font_size), 
        '-fill', 'lime', 
        '-font', 'Liberation-Sans', 
        '-annotate', '+0+30', text, 
        text_image_path
    ])

    # Step 3: Resize the supplied image
    subprocess.run(['magick', supplied_image, '-resize', '800x800', resized_supplied_image_path])  # Updated variable name

    # Step 4: Composite the images
    subprocess.run([
        'magick', text_image_path, 
        resized_supplied_image_path,  # Updated variable name
        '-gravity', 'Center', 
        '-compose', 'over', 
        '-composite', 
        final_output_path
    ])

    # Return the final output image path
    return jsonify({'output_image': final_output_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
