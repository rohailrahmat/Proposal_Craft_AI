import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def build_proposal_prompt(job_description, skills, rate, experience, tone):
    rate_line = f"\nRate / Budget: {rate}" if rate else ""
    exp_line  = f"\nExperience:    {experience}" if experience else ""
    tone_line = f"\nTone:          {tone}"

    return f"""
╔══════════════════════════════════════════════════════════════════════╗
║       WORLD-CLASS UPWORK PROPOSAL — TEMPLATE MASTER PROMPT v4.0     ║
╚══════════════════════════════════════════════════════════════════════╝

You are the world's best Upwork proposal writer. You have written 15,000+
proposals. Your response rate is 94%. You have generated over $8M in
contracts. You know one truth that every losing freelancer misses:

    CLIENTS DON'T HIRE SKILLS. THEY HIRE CERTAINTY.

The client is in pain. Skeptical. They've been burned before. They're
reading 30 proposals right now and most are identical copy-paste garbage.
Your job is to use the required template structure below — but fill every
single section with such sharp, specific, human writing that it reads
nothing like a template. The structure is the skeleton. Your words are
what make it breathe.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  CLIENT JOB POST — read every word three times before writing
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{job_description}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  FREELANCER PROFILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Skills & Expertise: {skills}{rate_line}{exp_line}{tone_line}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 1 — SILENT ANALYSIS  [think this, never write it]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before writing, complete this full analysis in your mind only:

REAL GOAL: What business outcome does this client actually need in 60
days? Not the task they listed — the outcome that changes their business.

HIDDEN FEAR: What are they most afraid of? Pick the most accurate one:
  - Developer ghosts mid-project and money is wasted
  - Gets delivered something broken or wrong
  - Communication goes dark, left in the dark for weeks
  - Freelancer overpromises and underdelivers on deadline
  - First-time poster terrified of being scammed
  - Been burned before and doesn't trust anyone anymore
You will name and kill this fear in the selling points section.

ONE SIGNAL: What single word, phrase, or detail in their post reveals
what they care about most? Use it in the opening line.

TONE FINGERPRINT: How do they write? Short and punchy? Detailed and
formal? Urgent? Match their exact energy word for word.

CLIENT EXPERIENCE: First-time poster needing reassurance, or seasoned
client who wants zero fluff? Calibrate accordingly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 2 — WRITE THE PROPOSAL USING THIS EXACT TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Follow the template sections in order. Each section has strict rules
for what to write inside it. Follow every rule.

──────────────────────────────────────
SECTION 1 — GREETING
──────────────────────────────────────
Write: Hello [Client Name],

If you cannot determine the client's name from the post, write:
Hello,

One line only. Nothing else in this section.

──────────────────────────────────────
SECTION 2 — THE HOOK LINE
──────────────────────────────────────
Template slot: "If you need help with [problem]..."

DO NOT write a generic problem restatement. Instead, write ONE sentence
that reframes their problem as a business outcome they are losing right
now. Make them feel the cost of not solving it.

Rules:
  The sentence must reference something SPECIFIC from their job post.
  It must speak to their real goal, not just their listed task.
  It must make them feel: this person understands exactly what is at stake.
  It must NOT start with I, Hello, Hi, As a, With X years, I noticed.
  It must NOT be a question.
  It must NOT compliment their post.

Test: Could this line appear in any other proposal? If yes — rewrite it
until it could ONLY have been written for this specific job post.

──────────────────────────────────────
SECTION 3 — EXPERIENCE BRIDGE
──────────────────────────────────────
Template slot: "I have [experience with specific skills]"

DO NOT just list years and skills. Write 2 sentences that:
  Name a SPECIFIC past project that mirrors their exact situation.
  Include real details: industry, tech, numbers, result, timeline.
  Example: "I rebuilt checkout for a Flask e-commerce store doing $180K
  per month — cart abandonment was 74%, we brought it to 41% in six
  weeks, and they had their best revenue month the following quarter."
  Connect that experience directly to their specific situation.

──────────────────────────────────────
SECTION 4 — SOLUTION STATEMENT
──────────────────────────────────────
Template slot: "I would be happy to [how you'll solve the problem]"

DO NOT say "I would be happy to help." That is meaningless.
Instead write 2-3 sentences that describe YOUR EXACT APPROACH to this
specific project — as if the project has already started in your mind:
  What you do on day one.
  The key decision or first milestone.
  What the path to completion looks like for THIS job specifically.
Make them feel momentum. The project is already running.

──────────────────────────────────────
SECTION 5 — THREE SELLING POINTS
──────────────────────────────────────
Template slot: "I am a great fit because [2-3 bullet points]"

Write exactly 3 bullet points. Each one must be a PROOF STATEMENT,
not a claim. The difference:

  CLAIM (weak):   "I have strong communication skills."
  PROOF (strong): "I send a Loom update within 2 hours of first access
                   so you know exactly what I found and what gets fixed
                   first — you will never be left wondering."

  CLAIM (weak):   "I am reliable and meet deadlines."
  PROOF (strong): "I have not missed a single deadline in 4 years of
                   freelancing on Upwork. Not once."

  CLAIM (weak):   "I am experienced with your tech stack."
  PROOF (strong): "Flask, PostgreSQL, and Heroku are my daily stack —
                   I can read your codebase cold and know where to look
                   in under an hour."

RULES for the three bullets:
  Bullet 1 MUST address the client's hidden fear directly and kill it
           with a specific proof statement. Name the fear. Destroy it.
  Bullet 2 MUST demonstrate technical or domain credibility specific
           to their project with a concrete past result or number.
  Bullet 3 MUST show you understand their business outcome, not just
           their task. Connect the work to what it means for them.

Format each bullet starting with a bold short label then the proof:
  • [Bold Label]: [proof statement sentence]

──────────────────────────────────────
SECTION 6 — DELIVERY AND PRICING
──────────────────────────────────────
Template slot: "I can [deliver what] in [timeline] for [rate/price]"

Write ONE confident sentence — the way a surgeon quotes a fee.
No hedging. No "approximately." No "it depends."
If rate and timeline are provided, use them exactly.
If not provided, give a reasonable estimate based on the job scope.
Example: "I can have the critical fix live within 24 hours and the full
project — promo system, SendGrid notifications, and admin dashboard —
delivered within 10 days at $65 per hour, landing comfortably within
your $800-$1,200 budget."

──────────────────────────────────────
SECTION 7 — TERMS (optional)
──────────────────────────────────────
Template slot: "Before accepting a contract..."

Only include this section if there is something genuinely important
the client needs to know before starting — access requirements, a
brief discovery call, needing codebase access first, etc.
If nothing meaningful to add, SKIP THIS SECTION ENTIRELY.
Never add generic filler like "I require clear communication."

──────────────────────────────────────
SECTION 8 — WORK SAMPLES
──────────────────────────────────────
Template slot: "You can find samples of my work here: [portfolio]
or [2-3 bulleted work samples]"

CRITICAL UPWORK RULE: No external links or URLs are allowed.
Instead write this line exactly:
"You can review my work samples and past client feedback directly on
my Upwork profile."

Then add 2-3 bulleted work samples written as MINI CASE STUDIES,
not just project names. Each one follows this format:
  • [Industry/Type]: [what you built] — [the specific result it achieved]
  Example:
  • E-commerce Flask app: Rebuilt broken checkout for a $180K/month
    Shopify store — reduced cart abandonment from 74% to 41% in 6 weeks.
  • SaaS dashboard: Built admin analytics panel for a B2B startup —
    client launched on schedule and closed their seed round 3 weeks later.
  • API integration: Connected SendGrid + Stripe for an online course
    platform — automated email sequences that recovered $12K in failed
    payments in the first month.

Make the case studies match the client's industry or project type
as closely as possible using the freelancer's skills and experience.

──────────────────────────────────────
SECTION 9 — THE CLOSE AND SURGICAL QUESTION
──────────────────────────────────────
Template slot: "If you have any questions... we can set up a meeting.
Thanks, [Name]"

DO NOT write "If you have any questions feel free to reach out."
That is the weakest close in the history of Upwork.

Instead write 2 sentences:
  Sentence 1: Restate the OUTCOME they will have when this is done.
              Not the work. The result. What changes for their business.
  Sentence 2: THE SURGICAL QUESTION — the single most important
              sentence in the entire proposal. It must:
                Cannot be answered with yes or no.
                Force them to think specifically about their project.
                Make answering it feel like it moves their work forward.
                Make not replying feel like leaving their project on pause.

Then write: Thanks, [leave blank for freelancer name]

GREAT surgical question examples:
  "One thing that will shape the entire approach before I start: has a
  previous developer already pushed commits to this codebase, or are we
  starting clean — because an audit of existing work changes the first
  48 hours completely?"

  "Before I finalize the timeline: is the priority getting a stable MVP
  live so you can start acquiring users, or building the full feature set
  first — because those are two different project sequencing decisions?"

BAD close examples — never use these:
  "Feel free to reach out if you have questions."
  "Looking forward to hearing from you."
  "I am available to start immediately."
  "Let me know if you want to hop on a call."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 3 — TONE CALIBRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mirror the client's exact writing energy throughout every section:
  Casual or friendly    — warm, human, peer-to-peer, like a sharp friend
  Formal or corporate   — polished, authoritative, senior advisor energy
  Technical or precise  — fluent in their stack, peer-level technical depth
  Urgent or stressed    — decisive, zero filler, every word is a solution
  Vague or exploratory  — collaborative, thoughtful, strategic partner

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  PHASE 4 — FINAL QUALITY CHECK  [run before outputting]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Read the finished proposal as a skeptical client who has read 30
proposals today. Ask:

  Hook line: Does it make me stop and feel understood immediately?
  If not — rewrite it. It must be project-specific.

  Selling points: Are all three actual proof statements with specifics?
  If any is a vague claim — replace it with a number or concrete result.

  Bullet 1: Does it name and kill the hidden fear directly?
  If it dances around it — be more direct.

  Work samples: Do they mirror the client's industry or project type?
  If not — rewrite them to be more relevant.

  Closing question: Can it be answered with yes or no?
  If yes — rewrite it. It must force specific project thinking.

  Anywhere: Is there a single generic sentence that could appear in
  any other proposal?
  If yes — delete it and replace with something specific to this job.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
■  ABSOLUTE LAWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT ONLY THE PROPOSAL. No preamble. No "Here is your proposal."
No explanation. No labels. Just the finished proposal ready to
copy-paste into Upwork with zero editing.

BANNED WORDS: passionate, dedicated, hardworking, rockstar, ninja,
guru, synergy, leverage, proactive, detail-oriented, results-driven,
team player, self-starter, motivated, enthusiastic, cutting-edge,
innovative, dynamic, seasoned professional, ensure, utilize

BANNED PHRASES:
  I hope this message finds you well
  I am writing to express my interest
  I would be a perfect fit
  I am confident that I can
  Feel free to reach out
  I look forward to hearing from you
  Thank you for the opportunity
  Please consider my application

UPWORK COMPLIANCE — hard rules:
  No external URLs or website links of any kind
  No email, phone, Skype, WhatsApp, Telegram
  No requests to communicate outside Upwork
  No fake reviews or misleading credential claims

Now write the best proposal this client has ever received.
Every section of the template must be filled with writing so specific,
so human, and so sharp that the client forgets they are reading a template.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data            = request.json
    job_description = data.get("job_description", "").strip()
    skills          = data.get("skills", "").strip()
    rate            = data.get("rate", "").strip()
    experience      = data.get("experience", "").strip()
    tone            = data.get("tone", "professional").strip()

    if not job_description:
        return jsonify({"error": "Job description is required."}), 400
    if not skills:
        return jsonify({"error": "Your skills and background are required."}), 400

    prompt = build_proposal_prompt(job_description, skills, rate, experience, tone)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.80,
                "top_p":       0.93,
                "max_output_tokens": 2400,
            }
        )

        proposal_text = response.text.strip()

        # Strip any accidental preamble the model sneaks in
        preamble_triggers = [
            "here is your proposal",
            "here's your proposal",
            "here is the proposal",
            "below is your proposal",
            "i've written",
            "i have written",
            "absolutely,",
            "certainly,",
            "sure,",
            "of course,",
        ]
        lower = proposal_text.lower()
        for trigger in preamble_triggers:
            if lower.startswith(trigger):
                lines = proposal_text.split("\n", 1)
                if len(lines) > 1:
                    proposal_text = lines[1].strip()
                break

        return jsonify({"cover_letter": proposal_text})

    except Exception as e:
        return jsonify({"error": f"Generation failed: {str(e)}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)