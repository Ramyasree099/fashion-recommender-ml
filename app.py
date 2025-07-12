from flask import Flask, request, jsonify, render_template
from PIL import Image
import os

app = Flask(__name__)

# Simulated ML model: return style based on mood (placeholder for real model)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form.get('mood', '')
    image = request.files.get('image')

    # Save and optionally analyze image (placeholder for ML model)
    if image:
        image_path = os.path.join("static", "upload.jpg")
        image.save(image_path)
        # Future: load image and run ML prediction

    # Mood-based logic
    suggestions = {
        "happy": "Bright colors like yellow or orange, floral dresses.",
        "sad": "Comfort wear — soft hoodies and relaxed fit jeans.",
        "calm": "Earth tones — beige, sage green, or linen fabrics.",
        "confident": "Bold colors — red blazers, statement outfits.",
    }

    recommendation = suggestions.get(mood, "Classic casual — jeans, t-shirt, and neutral tones.")

    return jsonify({"recommendation": recommendation})

if __name__ == '__main__':
    app.run(debug=True)