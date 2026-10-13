import os
import sys
from dotenv import load_dotenv
from duckduckgo_search import DDGS
from groq import Groq
from rich import print
from rich.markdown import Markdown
from rich.panel import Panel

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY").strip() if os.getenv("GROQ_API_KEY") else None)

def search(q: str) -> str:
    print(f"[bold cyan]Searching:[/bold cyan] {q}")
    with DDGS() as ddgs:
        res = ddgs.text(q, max_results=3)
        return "\n".join([f"- {r['title']}: {r['body']}" for r in res])

def agent(topic: str):
    print(Panel(f"[bold green]{topic}[/bold green]", title="AI Research Agent"))
    prompt = f"Write a research report on: {topic}. Output: SEARCH <query> if needed. Then output: REPORT <text summary, markdown table, takeaways. NO python code>."
    msgs = [{"role": "user", "content": prompt}]

    for _ in range(3):
        out = client.chat.completions.create(model="openai/gpt-oss-120b", messages=msgs).choices[0].message.content
        if "SEARCH " in out:
            q = out.split("SEARCH ")[1].strip().split("\n")[0]
            msgs += [{"role": "assistant", "content": out}, {"role": "user", "content": f"Data:\n{search(q)}\nGive written REPORT now (no code blocks)."}]
        else:
            rep = out.split("REPORT")[-1].strip()
            print(Panel(Markdown(rep), title="Final Report", border_style="green"))
            return

if __name__ == "__main__":
    agent(input("Enter Topic: "))
    