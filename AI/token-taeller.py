# reference-eksempler/token-taeller.py
# Understøtter Modul 2: Tokenisering — hvordan forstår en LLM tekst?
#
# Installation:
#   pip install tiktoken
#
# Brug:
#   python token-taeller.py
#
# Hvad det viser:
#   - Hvordan en sætning splittes i tokens
#   - At tokens ikke er det samme som ord
#   - Context window og hvad det betyder
#   - Estimeret pris ved brug af cloud-API

import tiktoken

# ── Farver til terminalen ─────────────────────────────────────────────
# Giver farvelagt output så tokens er nemme at se
FARVER = [
    "\033[42m\033[30m",  # grøn baggrund, sort tekst
    "\033[44m\033[97m",  # blå baggrund, hvid tekst
    "\033[43m\033[30m",  # gul baggrund, sort tekst
    "\033[45m\033[97m",  # lilla baggrund, hvid tekst
    "\033[46m\033[30m",  # cyan baggrund, sort tekst
    "\033[41m\033[97m",  # rød baggrund, hvid tekst
]
RESET = "\033[0m"
FED   = "\033[1m"
GRØN  = "\033[92m"
BLÅ   = "\033[94m"
GUL   = "\033[93m"
GRÅ   = "\033[90m"

# ── Indlæs tokenizer ─────────────────────────────────────────────────
# GPT-4 og Claude bruger lignende tokenisering (begge baseret på BPE)
# Vi bruger GPT-4's tokenizer som er bredt tilgængeligt via tiktoken
tokenizer = tiktoken.encoding_for_model("gpt-4")

def tokeniser(tekst: str) -> list[str]:
    """Returnerer en liste af tokens som tekst-strenge."""
    token_ids = tokenizer.encode(tekst)
    return [tokenizer.decode([t]) for t in token_ids]

def vis_tokens(tekst: str) -> None:
    """Viser tokens med skiftende farver i terminalen."""
    tokens = tokeniser(tekst)
    antal_ord = len(tekst.split())
    
    print(f"\n{FED}Tekst:{RESET} {tekst}")
    print(f"\n{FED}Tokens (farvekodet):{RESET}")
    print("  ", end="")
    
    for i, token in enumerate(tokens):
        farve = FARVER[i % len(FARVER)]
        # Vis mellemrum tydeligt med understregning
        synlig = token.replace(" ", "·")
        print(f"{farve}{synlig}{RESET}", end="")
    
    print(f"\n\n{FED}Statistik:{RESET}")
    print(f"  Antal ord:   {GUL}{antal_ord}{RESET}")
    print(f"  Antal tokens:{GRØN}{FED} {len(tokens)}{RESET}")
    
    if antal_ord > 0:
        ratio = len(tokens) / antal_ord
        print(f"  Tokens pr. ord: {GRÅ}{ratio:.2f}{RESET}")
    
    # Vis token-liste
    print(f"\n{FED}Token-liste:{RESET}")
    for i, token in enumerate(tokens):
        synlig = repr(token)  # viser f.eks. ' hund' med anførselstegn
        print(f"  {GRÅ}[{i:2d}]{RESET} {synlig}")

def vis_context_window(tokens: int, model: str = "GPT-4o") -> None:
    """Visualiserer hvor meget af context window der er brugt."""
    max_tokens = {
        "GPT-4o": 128_000,
        "Claude": 200_000,
        "Llama 3 (lokal)": 8_000,
    }
    
    print(f"\n{FED}Context window visualisering:{RESET}")
    for navn, maks in max_tokens.items():
        brugt_pct = min(tokens / maks * 100, 100)
        bar_bredde = 40
        fyldt = int(brugt_pct / 100 * bar_bredde)
        tom = bar_bredde - fyldt
        
        bar = f"{GRØN}{'█' * fyldt}{RESET}{GRÅ}{'░' * tom}{RESET}"
        print(f"  {navn:<20} [{bar}] {tokens:,}/{maks:,} ({brugt_pct:.2f}%)")

def estimér_pris(tokens: int) -> None:
    """Estimerer hvad tokens koster ved cloud-API brug."""
    priser = {
        "Claude Haiku":  0.00025 / 1000,   # $ per token (input)
        "Claude Sonnet": 0.003   / 1000,
        "GPT-4o mini":   0.00015 / 1000,
        "GPT-4o":        0.005   / 1000,
    }
    
    print(f"\n{FED}Estimeret pris ved cloud-API (input-tokens):{RESET}")
    print(f"  {GRÅ}Baseret på {tokens:,} tokens{RESET}")
    for model, pris_per_token in priser.items():
        total = tokens * pris_per_token
        print(f"  {model:<18} ≈ ${total:.6f} USD")
    print(f"  {GRÅ}(1.000.000 tokens ≈ 1 lang roman){RESET}")

def sammenlign_sprog() -> None:
    """Viser at dansk bruger flere tokens end engelsk for samme tekst."""
    eksempler = [
        ("Dansk",   "Kunstig intelligens er virkelig fascinerende teknologi"),
        ("Engelsk", "Artificial intelligence is truly fascinating technology"),
        ("Kode",    "def hello(): print('Hello, World!')"),
        ("Tal",     "1234567890"),
        ("Emoji",   "😀🎉🤖💻🧠"),
    ]
    
    print(f"\n{FED}Sammenligning — tokens per tekst-type:{RESET}")
    print(f"  {'Type':<12} {'Tekst':<50} {'Tokens':>6}")
    print(f"  {GRÅ}{'─'*70}{RESET}")
    
    for sprog, tekst in eksempler:
        tokens = tokeniser(tekst)
        visning = tekst[:48] + ".." if len(tekst) > 48 else tekst
        print(f"  {GUL}{sprog:<12}{RESET} {visning:<50} {GRØN}{FED}{len(tokens):>6}{RESET}")

# ── MAIN ──────────────────────────────────────────────────────────────
def main():
    print(f"\n{FED}{'='*60}{RESET}")
    print(f"{FED}   TOKEN-TÆLLER — Modul 2: Tokenisering{RESET}")
    print(f"{FED}{'='*60}{RESET}")
    print(f"{GRÅ}   Lær hvordan en LLM opdeler tekst i tokens{RESET}")
    
    # ── Del 1: Fast eksempel ─────────────────────────────────────────
    print(f"\n{BLÅ}{FED}── DEL 1: Eksempel fra Modul 2 ──────────────────────────{RESET}")
    vis_tokens("Kunstig intelligens er sejt!")
    
    # ── Del 2: Sprogsammenligning ────────────────────────────────────
    print(f"\n{BLÅ}{FED}── DEL 2: Tokens varierer med sprog og indhold ──────────{RESET}")
    sammenlign_sprog()
    
    # ── Del 3: Interaktiv del ────────────────────────────────────────
    print(f"\n{BLÅ}{FED}── DEL 3: Prøv selv ─────────────────────────────────────{RESET}")
    
    while True:
        print(f"\n{FED}Skriv en sætning (eller 'stop' for at afslutte):{RESET}")
        bruger_input = input("  > ").strip()
        
        if bruger_input.lower() in ("stop", "exit", "quit", "q"):
            break
        
        if not bruger_input:
            print(f"  {GRÅ}Ingen tekst indtastet — prøv igen{RESET}")
            continue
        
        vis_tokens(bruger_input)
        
        tokens = tokeniser(bruger_input)
        vis_context_window(len(tokens))
        estimér_pris(len(tokens))
    
    print(f"\n{GRØN}{FED}Tak for at bruge token-tælleren! 👋{RESET}\n")

if __name__ == "__main__":
    main()
