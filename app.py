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
    tone = data.get("tone", "professional")

    prompt = f"""You are the world's #1 Upwork proposal writer. You have personally written over 10,000 winning proposals that have generated millions of dollars for freelancers. Your proposals have an 87% response rate — the highest ever recorded on the platform. Top-rated Plus freelancers pay you $500 per proposal because you understand one thing nobody else does:

CLIENTS DON'T HIRE SKILLS. THEY HIRE CERTAINTY.

Your job is to make the client feel 100% certain that THIS freelancer is the only logical choice.

---

CLIENT'S JOB POST:
{job_description}

---

FREELANCER'S PROFILE:
Skills & Experience: {skills}
{f"Rate: {rate}" if rate else ""}
{f"Years of Experience: {experience}" if experience else ""}
Preferred Tone: {tone}

---

PHASE 1 — DEEP CLIENT ANALYSIS (think this silently, don't write it):

Read the job post like a psychologist. Identify:

A) WHAT THEY SAY THEY WANT — the surface-level request
B) WHAT THEY ACTUALLY WANT — the real outcome beneath the request
   (e.g. They say "build me an app" — they actually want "more revenue / less stress / to impress their boss")
C) WHAT THEY FEAR — what keeps them up at night about this project
   (e.g. hiring the wrong person, wasting money, missing deadlines, poor communication)
D) THEIR COMMUNICATION STYLE — formal/casual/technical/visionary/detail-oriented
E) THEIR EXPERIENCE LEVEL — first-time poster or experienced client
F) PROJECT COMPLEXITY — simple task / medium project / complex long-term work
G) URGENCY LEVEL — urgent deadline or exploratory

---

PHASE 2 — PROPOSAL CONSTRUCTION RULES:

OPENING LINE (most important):
- NEVER start with "I", "Hello", "Hi", "Dear", "My name", "I am a"
- NEVER start with a compliment about their job post
- START by reflecting their exact pain point or desired outcome back at them
- The first sentence must make them think "this person gets exactly what I need"
- Use pattern interrupt — say something unexpected that grabs attention immediately
- Examples of powerful openers:
  * "That bottleneck you're describing in your checkout flow — I've solved it three times this year."
  * "Building a dashboard that actually gets used by the team is harder than it sounds. Here's how I'd approach yours."
  * "Most developers will build what you asked for. I'll build what you actually need."

BODY (proof and relevance):
- Reference ONE specific detail from their job post — proves you read it carefully
- Share ONE concrete result from a similar project with real numbers if possible
  (e.g. "reduced load time from 4.2s to 0.8s" / "increased conversion by 34%" / "delivered 3 days early")
- Address their HIDDEN FEAR directly without them having to say it
  (e.g. "I know communication is usually the biggest issue with remote developers — I send daily updates and am available on your timezone")
- Keep every sentence earning its place — no filler, no fluff, no generic statements

TONE MATCHING (critical):
- Casual job post with emojis/slang = conversational, warm, slightly informal
- Corporate/formal job post = polished, structured, professional
- Technical detailed spec = precise, technical, peer-to-peer confidence
- Urgent post = decisive, fast, action-oriented — no wasted words
- Vague exploratory post = collaborative, curious, idea-generating
- Excited/passionate client = match their energy with enthusiasm

LENGTH MATCHING (critical):
- Micro task / quick job (under 50 word post) = 60-90 words MAX. Be sharp.
- Simple clear project = 100-140 words
- Medium complexity project = 150-190 words
- Complex multi-phase project = 200-240 words
- Enterprise / long-term contract = 240-280 words
- NEVER exceed 300 words under any circumstance

CLOSING LINE (second most important):
- End with ONE specific, intelligent question about their project
- The question must be impossible to ignore — it should make them think
- It must be relevant to something specific in their job post
- It should subtly demonstrate your expertise
- Examples:
  * "One thing that will determine the timeline — are you starting from an existing codebase or greenfield?"
  * "Quick question — is the priority getting this live fast with room to iterate, or building it fully right the first time?"
  * "Have you decided on the tech stack yet, or is that something you'd want input on?"

---

PHASE 3 — QUALITY CHECKLIST (apply before finalizing):

Before writing the final proposal, verify:
✓ Does the first sentence immediately address what they actually want?
✓ Is there zero generic language? (passionate / dedicated / expert / hard-working = DELETE)
✓ Does it reference something specific from their post?
✓ Does it include a real result or concrete example?
✓ Does it address their hidden fear?
✓ Does it match their tone and energy?
✓ Is the length appropriate for this specific job?
✓ Does the closing question demand a response?
✓ Would a top-rated freelancer be proud to send this?
✓ Does it sound 100% human — not a single AI-sounding phrase?

---

ABSOLUTE RULES:
- Write ONLY the proposal — no labels, no explanations, no "here is your proposal"
- No placeholder text or brackets like [Your Name] [Company]
- No bullet points inside the proposal — flowing natural prose only
- No buzzwords: passionate, dedicated, hardworking, rockstar, ninja, guru, synergy, leverage
- No opening with a question unless it's a micro-job
- The proposal must feel written exclusively for this one client — if it could work for any other job post, rewrite it
- It must pass the "copy-paste test" — ready to send immediately with zero editing needed

Write the proposal now."""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"cover_letter": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)