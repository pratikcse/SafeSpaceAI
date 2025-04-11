from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)

GOOGLE_API_KEY = "AIzaSyC_ODe9ZKgt2JXUNyIF6iG35kvpseOPjdg"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def analyze_content(text=None, image_path=None):
    try:
        if image_path and text:
            with open(image_path, 'rb') as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
                response = model.generate_content([
                    "Analyze this text and image for threat level (0-10), cyberbullying (0-10), and illegal content (0-10). "
                    "Format response as: Threat: X, Cyberbullying: Y, Illegal: Z",
                    text,
                    {"mime_type": "image/jpeg", "data": image_data}
                ])
        elif image_path:
            with open(image_path, 'rb') as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
                response = model.generate_content([
                    "Analyze this image for threat level (0-10), cyberbullying (0-10), and illegal content (0-10). "
                    "Format response as: Threat: X, Cyberbullying: Y, Illegal: Z",
                    {"mime_type": "image/jpeg", "data": image_data}
                ])
        else:
            response = model.generate_content([
                "Analyze this text for threat level (0-10), cyberbullying (0-10), and illegal content (0-10). "
                "Format response as: Threat: X, Cyberbullying: Y, Illegal: Z",
                text
            ])
        return response.text
    except Exception as e:
        return f"Error analyzing content: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.form.get('text', '')
        file = request.files.get('image')
        
        image_path = None
        if file and file.filename:
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)
        
        result = analyze_content(text if text.strip() else None, image_path)
        
        if image_path and os.path.exists(image_path):
            os.remove(image_path)
            
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
