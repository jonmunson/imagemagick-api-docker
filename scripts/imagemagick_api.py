from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    # Get data from request
    data = request.json
    input_path = data['input_image']
    output_path = data['output_image']
    text = data['text']
    font = data.get('font', 'Liberation Sans')  # Default to Liberation Sans if no font is specified

    # Construct the command to annotate the image
    command = f"magick {input_path} -gravity North -pointsize 30 -fill green -font '{font}' -annotate +0+10 '{text}' {output_path}"

    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        return jsonify({'success': True, 'message': 'Image processed successfully.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
