from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Get JSON data from the request
        data = request.json
        input_image = data.get('input_image')
        text = data.get('text', '')  # Default to empty string if not provided
        output_image = data.get('output_image', 'output_image.png')

        # Validate input image
        if not input_image:
            return jsonify({'error': 'input_image is required'}), 400
        
        input_path = f"/images/{input_image}"
        output_path = f"/images/{output_image}"

        # Check if the input image exists
        if not os.path.isfile(input_path):
            return jsonify({'error': f'Input image {input_image} not found'}), 404

        # Run ImageMagick command to annotate the image
        command = f"/usr/local/bin/convert {input_path} -gravity North -pointsize 30 -fill green -annotate +0+10 '{text}' {output_path}"
        print(f"Running command: {command}")  # For debugging
        subprocess.run(command, shell=True, check=True)

        return jsonify({
            'message': 'Image processed successfully',
            'output_image': output_image
        }), 200

    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'ImageMagick command failed: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
