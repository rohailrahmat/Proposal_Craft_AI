import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCOJwHdGezK6s-KZ5Akx9-WC5ZAJ4qWPXU"

client = genai.Client(api_key="AIzaSyCOJwHdGezK6s-KZ5Akx9-WC5ZAJ4qWPXU")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    job_description = data.get("job_description", "")
    skills = data.get("skills", "")

    prompt = f"""Write a professional, compelling cover letter for someone applying for the following job.

Job Description:
{job_description}

Applicant's Skills and Experience:
{skills}

Write a complete, ready-to-send cover letter. Make it sound human, confident and professional. Do not use placeholder text like [Your Name] - just write the body of the letter starting from 'Dear Hiring Manager'."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"cover_letter": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)