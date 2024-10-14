from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        data = request.json
        input_image = data.get('input_image')
        text = data.get('text')
        output_image = data.get('output_image', 'output_image.png')

        input_path = f"/images/{input_image}"
        output_path = f"/images/{output_image}"

        # Run ImageMagick command to annotate the image
        command = f"convert {input_path} -gravity North -pointsize 30 -fill green -annotate +0+10 '{text}' {output_path}"
        subprocess.run(command, shell=True, check=True)

        return jsonify({
            'message': 'Image processed successfully',
            'output_image': output_image
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
