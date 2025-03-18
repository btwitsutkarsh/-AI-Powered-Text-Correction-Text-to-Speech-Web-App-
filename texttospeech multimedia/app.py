from flask import Flask, render_template, request, jsonify
import requests
import os
import subprocess

app = Flask(__name__)

# Configure the Perplexity API
API_KEY = "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"
API_URL = "https://api.perplexity.ai/chat/completions"

def correct_text(user_text):
    """Uses Perplexity API to correct grammar and spelling mistakes ONLY, with no extra words."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "accept": "application/json",
        "content-type": "application/json"
    }
    
    data = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system", "content": "Fix the grammar and spelling mistakes ONLY. Return only the corrected sentence with no extra words."},
            {"role": "user", "content": user_text}
        ]
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()  # Ensure clean response
    else:
        return user_text  # Return original text if API fails

@app.route("/")
def index():
    return render_template("index.html")

def generate_speech(text, voice_type, age_group, speed, output_file):
    """Generates speech using a subprocess with realistic age-based voices."""

    # Ensure previous audio file is removed
    if os.path.exists(output_file):
        os.remove(output_file)

    # Select the correct voice based on gender & age
    if age_group == "child":
        voice_id = "Flo"  # More child-like voice
        rate = 280  # Higher speed for energetic tone
    elif age_group == "teen":
        voice_id = "Daniel" if voice_type == "male" else "Samantha"  # Natural youthful voice
        rate = 200
    elif age_group == "adult":
        voice_id = "Alex" if voice_type == "male" else "Samantha"  # Default stable voices
        rate = 150
    else:  # Old
        voice_id = "Grandpa" if voice_type == "male" else "Grandma"  # Older-sounding voices
        rate = 100  # Slower speech for realism

    # Apply user-selected speed multiplier
    final_rate = int(rate * speed)

    # Run macOS `say` command with adjusted parameters
    command = [
        "say",
        "-v", voice_id,
        "-r", str(final_rate),
        text,
        "-o", output_file.replace(".mp3", "")  # macOS saves as `.aiff`, we convert later
    ]
    
    subprocess.run(command, check=True)

    # Convert `.aiff` to `.mp3`
    aiff_file = output_file.replace(".mp3", ".aiff")
    if os.path.exists(aiff_file):
        subprocess.run(["ffmpeg", "-i", aiff_file, output_file], check=True)
        os.remove(aiff_file)  # Remove temporary file

@app.route("/process", methods=["POST"])
def process_text():
    """Handles text correction and speech synthesis."""
    user_text = request.form.get("text")
    voice_type = request.form.get("voice")  # Male/Female
    age_group = request.form.get("age")  # Child/Teen/Adult/Old
    speed = float(request.form.get("speed", 1.0))  # Playback speed

    # Correct the text using Perplexity API
    corrected_text = correct_text(user_text)
    audio_filename = "static/output.mp3"

    # Generate speech using subprocess (avoiding pyttsx3 issues)
    generate_speech(corrected_text, voice_type, age_group, speed, audio_filename)

    return jsonify({"corrected_text": corrected_text, "audio_url": audio_filename})

if __name__ == "__main__":
    app.run(debug=True)