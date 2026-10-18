import os
import sys
from dotenv import load_dotenv
from ddgs import DDGS
from groq import Groq
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY").strip() if os.getenv("GROQ_API_KEY") else None)

def search(q: str) -> str:
    print(f"[bold cyan]🔍 Searching Live Web Sources:[/bold cyan] {q}")
    with DDGS() as ddgs:
        res = list(ddgs.text(q, max_results=3))
        return "\n".join([f"[{i+1}] {r['title']}: {r['body']}" for r in res])

def verify(claims: str, sources: str) -> str:
    prompt = f"Sources:\n{sources}\n\nClaims:\n{claims}\n\nCheck each claim against Sources. If supported by text, output: [VERIFIED] <claim> | Proof: <exact quote>. If unsupported or speculative, output: [FLAGGED] <claim> | Warning: <reason>."
    return client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    ).choices[0].message.content

def agent(topic: str):
    print(Panel(f"[bold green]{topic}[/bold green]", title="🤖 AI Research Agent + Source Verifier", border_style="cyan"))
    sources = search(topic)
    
    prompt = f"""Topic: {topic}
Sources:
{sources}

Task:
1. Extract 3 concise factual claims (2 confirmed by sources, 1 speculative/unverified).
2. Generate a concise research brief with:
   - Summary: 1 strong paragraph
   - Comparison Table: 3 key metrics/dimensions
   - Takeaways: 3 punchy bullet points
Format:
CLAIMS:
<claim 1>
<claim 2>
<claim 3>
REPORT:
### 📌 Executive Summary
<summary paragraph>

### ⚡ Key Metrics & Comparison
| Dimension | Specification / Finding | Source Status |
| :--- | :--- | :--- |
| ... | ... | ... |

### 🎯 Key Takeaways
- ...
- ...
- ..."""
    
    out = client.chat.completions.create(model="openai/gpt-oss-120b", messages=[{"role": "user", "content": prompt}]).choices[0].message.content
    claims = out.split("REPORT:")[0].replace("CLAIMS:", "").strip() if "REPORT:" in out else out.split("\n\n")[0]
    report = out.split("REPORT:")[-1].strip() if "REPORT:" in out else out
    
    print("\n[bold yellow]🛡️  Autonomous Source Verification Audit:[/bold yellow]")
    table = Table(header_style="bold magenta", border_style="yellow")
    table.add_column("Status", width=14, justify="center")
    table.add_column("Claim & Evidence Verification")
    
    for line in verify(claims, sources).strip().split("\n"):
        if "[VERIFIED]" in line:
            table.add_row("[bold green]✅ VERIFIED[/bold green]", line.replace("[VERIFIED]", "").strip())
        elif "[FLAGGED]" in line:
            table.add_row("[bold red]⚠️ FLAGGED[/bold red]", line.replace("[FLAGGED]", "").strip())
    print(table)
    
    print("\n")
    print(Panel(Markdown(report), title="📊 Final Grounded Report", border_style="green"))

if __name__ == "__main__":
    agent(input("Enter Topic: "))