import time
import random
import sys
import pyautogui
import pyperclip
import keyboard

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.005

# ────────────────────────────────────────────
# YEH CODE TYPING SIMULATOR TYPE KAREGA
# Har line EXACTLY jaise likhi hai waise hi type hogi
# ────────────────────────────────────────────
AGENT_CODE = [
    'import os',
    'import sys',
    'from dotenv import load_dotenv',
    'from duckduckgo_search import DDGS',
    'from groq import Groq',
    'from rich import print',
    'from rich.markdown import Markdown',
    'from rich.panel import Panel',
    '',
    'if sys.platform == "win32":',
    '    sys.stdout.reconfigure(encoding="utf-8")',
    '',
    'load_dotenv()',
    'client = Groq(api_key=os.getenv("GROQ_API_KEY").strip() if os.getenv("GROQ_API_KEY") else None)',
    '',
    'def search(q: str) -> str:',
    '    print(f"[bold cyan]Searching:[/bold cyan] {q}")',
    '    with DDGS() as ddgs:',
    '        res = ddgs.text(q, max_results=3)',
    '        return "\\n".join([f"- {r[\'title\']}: {r[\'body\']}" for r in res])',
    '',
    'def agent(topic: str):',
    '    print(Panel(f"[bold green]{topic}[/bold green]", title="AI Research Agent"))',
    '    prompt = f"Write a research report on: {topic}. Output: SEARCH <query> if needed. Then output: REPORT <text summary, markdown table, takeaways. NO python code>."',
    '    msgs = [{"role": "user", "content": prompt}]',
    '',
    '    for _ in range(3):',
    '        out = client.chat.completions.create(model="openai/gpt-oss-120b", messages=msgs).choices[0].message.content',
    '        if "SEARCH " in out:',
    '            q = out.split("SEARCH ")[1].strip().split("\\n")[0]',
    '            msgs += [{"role": "assistant", "content": out}, {"role": "user", "content": f"Data:\\n{search(q)}\\nGive written REPORT now (no code blocks)."}]',
    '        else:',
    '            rep = out.split("REPORT")[-1].strip()',
    '            print(Panel(Markdown(rep), title="Final Report", border_style="green"))',
    '            return',
    '',
    'if __name__ == "__main__":',
    '    agent(input("Enter Topic: "))',
]


def check_abort():
    if keyboard.is_pressed('esc'):
        print("\n STOPPED by user (ESC).")
        sys.exit(0)


def type_one_char(ch):
    """Ek character type karo"""
    check_abort()
    if ord(ch) > 127:
        pyperclip.copy(ch)
        pyautogui.hotkey('ctrl', 'v')
    else:
        pyautogui.write(ch, interval=0)
    delay = random.uniform(0.025, 0.055)
    if ch in (':', '(', ')', '[', ']', '=', ',', '.', '"', "'"):
        delay += random.uniform(0.03, 0.06)
    time.sleep(delay)


def type_line(text):
    """Puri line character-by-character type karo"""
    for ch in text:
        type_one_char(ch)


def press_enter():
    check_abort()
    pyautogui.press('enter')
    time.sleep(0.08)


def kill_auto_indent():
    """VS Code ke auto-indent ko maarke cursor ko col 0 pe laao,
    phir Shift+End se auto-indent select karo.
    Jab agle character type hoga, woh selection replace ho jayegi."""
    pyautogui.press('escape')       # autocomplete popup band karo
    time.sleep(0.03)
    pyautogui.press('home')         # first non-whitespace pe jao
    time.sleep(0.02)
    pyautogui.press('home')         # col 0 pe jao (2nd press)
    time.sleep(0.02)
    pyautogui.hotkey('shift', 'end')  # select everything (auto-indent)
    time.sleep(0.02)


# ────────────────────────────────────────────
# MAIN SCRIPT
# ────────────────────────────────────────────
print("=" * 60)
print("  HUMAN TYPING SIMULATOR v3 (Anti-AutoIndent)")
print("=" * 60)
print()
print("Instructions:")
print("  1. VS Code me 'research_agent.py' kholo")
print("  2. File ka SAARA content delete karo (Ctrl+A, Delete)")
print("  3. Cursor Line 1, Column 1 pe hona chahiye")
print("  4. Screen recorder ON karo")
print("  5. F8 dabao — typing shuru ho jayegi")
print()
print("  Emergency stop: ESC dabao kisi bhi time")
print()
print("  F8 ka wait kar raha hoon...")

keyboard.wait('f8')
time.sleep(0.8)

start_time = time.time()
print("\n  TYPING STARTED!\n")

for i, line in enumerate(AGENT_CODE):
    check_abort()

    if line == '':
        # ─── BLANK LINE ───
        # Pehle auto-indent hatao (agar hai), phir Enter
        if i > 0:
            kill_auto_indent()
            pyautogui.press('delete')   # selection delete karo (agar thi)
            time.sleep(0.03)
        press_enter()
        time.sleep(random.uniform(0.15, 0.30))

    else:
        # ─── NON-EMPTY LINE ───
        if i > 0:
            # Auto-indent select karke rakho — pehla character replace kar dega
            kill_auto_indent()

        # Type the line — pehla char auto-indent ki selection replace karega
        type_line(line)
        press_enter()

        # Natural "thinking" pause
        pause = random.uniform(0.12, 0.30)
        if line.startswith('def ') or line.startswith('for ') or line.startswith('if __'):
            pause += random.uniform(0.25, 0.50)
        elif line.startswith('import ') or line.startswith('from '):
            pause += random.uniform(0.08, 0.15)
        time.sleep(pause)

elapsed = round(time.time() - start_time, 1)
print()
print("=" * 60)
print(f"  DONE! Typed in {elapsed} seconds. Zero indentation errors.")
print("=" * 60)
