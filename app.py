import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    job_description = data.get("job_description", "")
    skills = data.get("skills", "")
    rate = data.get("rate", "")
    experience = data.get("experience", "")

    prompt = f"""You are an elite Upwork freelancer who has earned over $500K on the platform with a 100% Job Success Score.

A client has posted this job:
---
{job_description}
---

The freelancer's skills and background:
---
{skills}
---

{f"Freelancer's rate: {rate}" if rate else ""}
{f"Years of experience: {experience}" if experience else ""}

Before writing, deeply analyse the client's job post for these signals:

TONE SIGNALS — Read how the client writes:
- Casual language, slang, emojis, relaxed phrasing = write in a warm, conversational, human tone
- Formal language, corporate terms, structured requirements = write in a polished, professional tone
- Urgent language, "ASAP", "immediately", "deadline" = write with urgency and decisiveness
- Detailed technical specs = write in a technical, precise, confident tone
- Vague or exploratory post = write in a collaborative, curious, idea-generating tone

LENGTH SIGNALS — Decide the right length:
- Simple, short job post with clear requirements = short proposal (80-120 words). Don't over-explain.
- Complex project with multiple requirements = medium proposal (150-200 words)
- Long detailed spec or enterprise-level project = detailed proposal (200-250 words)
- Quick task or micro-job = very short (50-80 words), be direct and punchy

STRUCTURE — Always follow this psychology:
1. First sentence: Mirror the client's biggest pain point or goal. Make them feel understood immediately.
2. Middle: Show you have done this exact thing before with a specific, believable result or example.
3. Rate/timeline: Weave it in naturally only if it strengthens the proposal.
4. Close: End with ONE specific question that is relevant to their project. This forces a reply.

STRICT RULES:
- Never start with "I", "Hello", "Dear", "Hi", or "My name is"
- Never use buzzwords: passionate, dedicated, hardworking, expert, guru, ninja, rockstar
- Never use placeholder text or brackets
- Never sound like AI — no perfect grammar-robot sentences
- Reference at least one specific detail from their job post to prove you read it
- Match the client's energy exactly — if they're excited, be excited. If they're serious, be serious.
- The proposal must feel like it was written specifically for this one client and no one else

Write only the proposal text. Nothing else. No labels, no explanations."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"cover_letter": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)