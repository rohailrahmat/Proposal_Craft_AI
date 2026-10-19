# ProposalCraft AI — Win More Upwork Jobs

An AI-powered web application that crafts high-converting, tailored Upwork proposals in seconds. Built with **Flask**, **Google Gemini GenAI**, and **TailwindCSS**.

---

## Features

- **Upwork-Optimized Proposals**: Eliminates buzzwords, robotic AI phrases, and cliches.
- **Smart Model Fallback**: Features automatic retries with exponential backoff across modern Gemini models (`gemini-3-flash-preview`, `gemini-flash-latest`, `gemini-3.8-flash`).
- **Interactive UI**: Responsive real-time interface with live word count, tone selector, and 1-click clipboard copy.
- **Production-Ready**: Clean error banner handling, health check endpoint (`/health`), and Vercel/Render compatibility.

---

## Setup & Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rohailrahmat/Proposal_Craft_AI.git
   cd Proposal_Craft_AI
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables:**
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Add your Gemini API key from [Google AI Studio](https://aistudio.google.com/):
   ```env
   GEMINI_API_KEY="your_api_key_here"
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Deployment (Vercel)

1. Import the repository into your [Vercel](https://vercel.com/) dashboard.
2. Under **Project Settings > Environment Variables**, add:
   - `GEMINI_API_KEY` = your Gemini API key.
3. Deploy!
