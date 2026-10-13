# 🤖 AI Research Agent

> An ultra-fast, autonomous **Deep Research AI Agent** built from scratch in ~40 lines of pure Python using **Groq** and **DuckDuckGo Search**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-Ultra--Fast%20LPU-orange?logo=fastapi)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/vaibhavv-labs/AI-Research-Agent?style=social)](https://github.com/vaibhavv-labs/AI-Research-Agent)

---

## 📸 Demo Preview

![AI Research Agent Terminal Demo](assets/demo.png)

---

## 📌 Overview

**AI Research Agent** implements the **ReAct (Reasoning + Acting)** pattern to autonomously conduct in-depth web research on any topic. Instead of relying solely on pre-trained LLM knowledge, it queries the live web, analyzes the latest sources, and compiles a comprehensive research brief with structured tables and strategic takeaways.

---

## ✨ Features

- **⚡ Lightning-Fast Inference**: Runs on Groq's LPUs for near-instant responses.
- **🔍 Live Web Scraping & Search**: Autonomously formulates search queries and scrapes DuckDuckGo without requiring expensive Google/Bing API keys.
- **🧠 ReAct Loop**: Seamless cycle of *Thought → Action (Search) → Observation (Read) → Synthesis (Report)*.
- **📊 Rich Terminal UI**: Beautiful formatted markdown reports, status panels, and styled tables powered by `rich`.
- **🎥 Built-in Typing Simulator**: Includes `type_simulator.py` to simulate realistic character-by-character human typing for screen recording demos.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A([User Input: Research Topic]) --> B[Agent Prompt]
    B --> C{Groq LLM: Reasoning}
    C -- "Needs Data: SEARCH <query>" --> D[DuckDuckGo Search]
    D -- Live Search Results --> C
    C -- "Has Sufficient Data: REPORT" --> E[Rich Terminal Markdown Panel]
    E --> F([Final Structured Report])
```

---

## 📂 Project Structure

```text
AI-Research-Agent/
│
├── assets/
│   ├── demo.png         # VS Code terminal output screenshot
│   └── demo.svg         # Vector terminal recording
│
├── research_agent.py    # Core AI research agent logic (~40 lines)
├── type_simulator.py    # Automation tool for live human-typing demo recordings
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment configuration
├── .gitignore           # Ignores sensitive keys and cache files
└── README.md            # Project documentation
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/vaibhavv-labs/AI-Research-Agent.git
cd AI-Research-Agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup API Key
Create a `.env` file from the template:
```bash
cp .env.example .env
```
Add your free **[Groq API Key](https://console.groq.com/keys)** inside `.env`:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 4. Run the Agent
```bash
python research_agent.py
```
Enter any topic (e.g., `Future of AI Agents in 2026`, `Quantum Computing Breakthroughs`) and watch the agent autonomously search and compile the report!

---

## 🎬 Live Typing Simulator (For Video Creators)

Want to record a clean coding video for LinkedIn, Twitter, or YouTube?

1. Open `research_agent.py` in your code editor and clear the file.
2. Run the simulator script:
   ```bash
   python type_simulator.py
   ```
3. Start your screen recording software.
4. Press **`F8`** — the script will realistically type out the entire code with natural human pauses and zero indentation bugs!
*(Press `ESC` anytime to immediately cancel).*

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Vaibhav Bhoyate**  
- GitHub: [@vaibhavv-labs](https://github.com/vaibhavv-labs)  
- Project Repository: [AI-Research-Agent](https://github.com/vaibhavv-labs/AI-Research-Agent)