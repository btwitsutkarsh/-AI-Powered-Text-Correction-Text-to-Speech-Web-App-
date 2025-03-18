🎤 Text-to-Speech Web App with AI-Powered Text Correction

This is a Flask-based Text-to-Speech Web App that: ✅ Corrects spelling & grammar mistakes using Perplexity AI
✅ Converts text to speech using macOS system voices
✅ Supports Male/Female voices
✅ Allows age-based voice customization (Child, Teen, Adult, Old)
✅ Includes playback speed control

🚀 Features

AI-Powered Grammar Correction: Fixes spelling & grammar mistakes automatically.
Realistic Text-to-Speech: Uses macOS built-in voices (say command).
Age-Based Voice Selection: Different voices & speeds for Child, Teen, Adult, Old.
Male/Female Voice Selection: Choose between male (Alex, Daniel, Grandpa) or female (Samantha, Flo, Grandma).
Playback Speed Control: Adjust speech speed dynamically.
🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone 
cd text-to-speech

2️⃣ Create a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # For macOS/Linux

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Install ffmpeg (Required for Audio Processing)

brew install ffmpeg  # For macOS users



⸻

🎯 Usage

Run the Flask App

python app.py

	•	Open http://127.0.0.1:5000/ in your browser.

How to Use
	1.	Enter your Name (It personalizes the UI).
	2.	Type your Text (AI will fix spelling/grammar).
	3.	Select Voice (Male/Female).
	4.	Choose Age Group (Child/Teen/Adult/Old).
	5.	Click “Generate Speech” → It will fix text & generate audio.
	6.	Adjust Playback Speed & Listen! 🎧

⸻

📦 File Structure

📂 text-to-speech
 ┣ 📜 app.py              # Main Flask app
 ┣ 📜 requirements.txt    # Dependencies list
 ┣ 📂 static/             # Static files (CSS, JS, output audio)
 ┃ ┣ 📜 styles.css        # UI styling
 ┃ ┣ 📜 script.js         # Frontend logic
 ┣ 📂 templates/          # HTML templates
 ┃ ┣ 📜 index.html        # Main UI file
 ┣ 📜 README.md           # Project documentation



⸻

🔥 API Used: Perplexity AI

This app uses Perplexity AI to correct spelling & grammar.
To get an API key, visit: Perplexity AI

⸻

🏆 Contributors
	•	Utkarsh Tripathi – Developer 💻

⸻

🛠️ Future Improvements

🔹 Add multi-language support
🔹 Include custom voice tuning options
🔹 Convert audio to different formats (MP3, WAV, etc.)

⸻

⚡ License

MIT License - Feel free to use & modify! 🚀

---

