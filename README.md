# SafeSpaceAI

SafeSpaceAI is a powerful web-based tool that uses **Gemini LLM** to analyze user-generated content (text and images) for harmful elements such as **threats**, **cyberbullying**, and **illegal material**. Built with **Flask** and **Tailwind CSS**, it provides a simple UI and integrates advanced prompt engineering techniques to ensure responsible AI usage.

---

## 🔍 Features

- ✅ Analyze Text
- ✅ Analyze Images
- ✅ Dual Input (Text + Image)
- ✅ Ratings for Threat, Cyberbullying, Illegal Content (scale of 0–10)
- ✅ Beautiful UI using TailwindCSS
- ✅ Gemini LLM Integration via Google API

---

## 💻 Technologies Used

- **Flask** – Backend server
- **HTML/CSS** – Frontend templates
- **Tailwind CSS** – UI framework
- **JavaScript (Vanilla)** – AJAX for async interaction
- **Gemini API** – Core analysis engine (Generative AI)
- **Base64** – Image encoding

---

## ⚙️ Installation

### Prerequisites

- Python 3.8+
- pip

### Steps

```bash
# Clone the repository
git clone https://github.com/pratikcse/SafeSpaceAI.git
cd SafeSpaceAI

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 📦 Requirements

```txt
Flask
google-generativeai
Werkzeug
```

Create a file `requirements.txt`:

```txt
Flask==2.3.3
google-generativeai==0.3.1
Werkzeug==2.3.7
```

---

## 🤖 LLM API Integration

This app uses **Gemini 1.5 Flash** from Google via `google-generativeai`.

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_GOOGLE_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')
```

Prompts like:

```
"Analyze this text and image for threat level (0–10), cyberbullying (0–10), and illegal content (0–10). Format response as: Threat: X, Cyberbullying: Y, Illegal: Z"
```

---

## 📜 Prompt Engineering

We use a **static prompt** enriched with user input. Based on what’s provided (text, image, or both), the Gemini model evaluates content and responds with clear, quantifiable results.

Example format:
```
Threat: 6, Cyberbullying: 2, Illegal: 0
```

This is displayed back in the UI as a bot message.



## 🧩 How to Integrate into Social Media Platforms

SafeSpaceAI can be integrated into social media platforms via:

1. **API-Based Moderation**  
   Plug our analysis function into your existing comment/image submission pipeline.
   
2. **Webhook Integration**  
   On every post or upload, send content to SafeSpaceAI’s endpoint, receive a threat report instantly.
   
3. **Content Flagging**  
   Use the score output to flag or warn users before they post something harmful.

---

## 📷 Screenshots

> Upload or paste screenshots here:
- Interface view
- Chat interaction example
- Analysis result

---

## 📄 License

MIT License. Free for educational and personal use.

---

## ✨ Author

Made with ❤️ by [@pratikcse](https://github.com/pratikcse)

---
