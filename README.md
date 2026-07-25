# 🤖 AI Agentic Pipeline | Neurofive

A multi-agent web application built with **Streamlit** and the **Groq API (Llama-3.3-70b)** that implements a dual-agent content creation and refinement pipeline—completely automated with no human intervention in between.

---

## ⚡ Overview

This application simulates a professional editorial workflow using two specialized AI agents:
1. **Agent 1 (Writer):** Acts as an expert technical researcher and content writer to draft comprehensive initial content based on a given topic.
2. **Agent 2 (Editor/Critic):** Acts as a strict Senior Technical Editor, reviewing the draft, fixing structural flaws, enhancing tone, and turning it into a publication-ready output.

---

## 🎨 Visual Identity & Theme
* **Dark Mode Aesthetic:** Custom-styled dark background (`#0b0f19`) for high readability.
* **Branding:** Dark green container header (`#0f291e`) featuring the **Neurofive** neon green badge (`#39ff14`).
* **Interactive Tabs:** Distinctive red-themed tabs that highlight actively selected views for seamless navigation.

---

## 🛠️ Tech Stack
* **Python** (Core logic)
* **Streamlit** (Frontend UI)
* **Groq API** (Llama-3.3-70b-versatile model for lightning-fast inference)
* **Python-Dotenv** (Environment variable management)

---

## 🚀 Local Installation & Setup

Follow these steps to run the application locally on your machine:

1. **Clone the repository:**

2. Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install dependencies:

Bash
pip install -r requirements.txt

Run the Streamlit application:

Bash
streamlit run app.py

   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME
