## Modul 15: AI i dine egne programmer - Python + LLM API

> **Målgruppe:** 10-15 år · Kender Python · Har fulgt Modul 14
> **Illustration-filer:** modul15-ill1 til modul15-ill3 (PNG)

---

### Konceptet: AI som en funktion

AI er ikke kun chat. Fra dit programs perspektiv er en LLM bare en **funktion der tager tekst ind og giver tekst ud**. Det samme Python-kald kan løse radikalt forskellige opgaver:

```
spørg_ai("Hvad er Frankrigs hovedstad?")     →  "Paris"
spørg_ai("Omsæt 'hund' til spansk")          →  "perro"
spørg_ai("Er denne kode korrekt: ...")      →  "Nej, fejl på linje 3..."
spørg_ai("Opsummer denne tekst i 3 punkter") →  "1. ... 2. ... 3. ..."
```

Du behøver ikke bygge en ny AI til hvert problem. Én genanvendelig funktion er nok - opgaven defineres i prompten.

> 💬 **Ordforklaring:** *Funktion* er et genanvendeligt stykke kode der tager input og giver output. Når vi wrapper et AI-kald i en funktion, bliver LLM'en en byggeklods på linje med al anden Python-kode.

📎 **Illustration:** `modul15-ill1-ai-som-funktion.png`
**Titel:** Én funktion, uendelige muligheder
*`spørg_ai()` i centrum med 4 pile ud til 4 forskellige apps: grundstof-gætter, chatbot, quiz-generator, sentiment-analysator. Viser COMPOSABILITY - ikke flowdiagram.*

---

### Lokal eller cloud? Vælg din tilgang

Du har to måder at kalde en LLM fra Python. Valget påvirker pris, hastighed og hvad du kan i praksis:

| Egenskab | Ollama (lokal) | Cloud-API (Anthropic/OpenAI) |
|----------|---------------|-----------------------------|
| Pris | Gratis | Betalt per token |
| Internet | Ikke nødvendigt | Kræves |
| Modelkvalitet | God (7b-14b parametre) | State-of-the-art |
| Setup | `pip install ollama` | `pip install anthropic` + API-nøgle |
| Bedst til | Udvikling og test | Produktion og krævende opgaver |

Strategien: **byg med Ollama, deploy med cloud-API**. Koden er næsten identisk - du skifter blot bibliotek og model-navn når du er klar.

> 🔗 **Husk fra Modul 14:** Cloud-API'er bruger tokens - under udvikling med hundredvis af test-kald løber det hurtigt op. Ollama er gratis.

---

### Byg en genanvendelig AI-funktion

Wrap dit API-kald i en funktion én gang - brug den overalt i dit program:

```python
import ollama

def spørg_ai(spørgsmål: str, model: str = "qwen2.5:7b") -> str:
    svar = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": spørgsmål}]
    )
    return svar["message"]["content"]

print(spørg_ai("Hvad er Europas højeste bjerg?"))
```

Vil du skifte til cloud-API? Skift implementationen indeni - resten af koden røres ikke:

```python
import anthropic, os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def spørg_ai(spørgsmål: str, model: str = "claude-haiku-4-5") -> str:
    svar = client.messages.create(
        model=model, max_tokens=1024,
        messages=[{"role": "user", "content": spørgsmål}]
    )
    return svar.content[0].text

# Resten af dit program er uændret
```

📎 **Illustration:** `modul15-ill2-python-ollama-kode.png`
**Titel:** Hvad sker der indeni ollama.chat()?
*Den usynlige vej: Python → HTTP POST til port 11434 → Ollama-server-process → qwen-model i RAM → token-generering → HTTP response → Python får string. Gør black box synlig.*

---

### Strukturer prompts - do/don't

Kvaliteten af AI's output afhænger næsten udelukkende af promptens kvalitet:

| ❌ Undgå | ✅ Gør i stedet |
|---------|---------------|
| `f"Er {by} en dansk by?"` | `f"Svar KUN med ja eller nej. Er '{by}' en dansk by?"` |
| Lang tekst uden kontekst | Rolle først: `"Du er en [ekspert]. [opgave]."` |
| Ingen eksempler på format | Few-shot: vis 2-3 eksempler på hvad du forventer |
| "Opsummer det her" | "Opsummer i præcis 3 punkter, max 15 ord per punkt" |

**Few-shot eksempel - vis AI'en hvad du vil have:**
```python
prompt = f"""Kategorisér disse ord som DYR, PLANTE eller TING.
Eksempler:
- hund → DYR
- rose → PLANTE
- bord → TING

Nu kategorisér: {ord}"""
```

---

### Svar-parsing og struktureret output

Vil du bruge AI's svar som data i dit program - ikke bare printe det - skal du bede om **JSON-format** og parse svaret:

```python
import json

def analysér_sætning(sætning: str) -> dict:
    prompt = f"""Analysér sætningen og svar KUN med JSON. Ingen forklaring.
Sætning: "{sætning}"

Format:
{{"sentiment": "positiv/negativ/neutral",
  "emner": ["emne1", "emne2"],
  "resumé": "max 10 ord"}}"""

    svar_tekst = spørg_ai(prompt)
    svar_tekst = svar_tekst.strip().removeprefix("```json").removesuffix("```").strip()
    return json.loads(svar_tekst)

data = analysér_sætning("Klimaforandringer truer biodiversiteten i Arktis")
print(data["sentiment"])   # "negativ"
print(data["emner"])       # ["klimaforandringer", "biodiversitet", "Arktis"]
```

> 💬 **Ordforklaring:** *Parsing* er at omforme tekst til et brugbart dataformat. *JSON* er et tekstformat til strukturerede data - Python konverterer det til en `dict` med `json.loads()`.

---

### Fejlhåndtering - hvad når AI'en ikke svarer?

To typiske fejlscenarier: Ollama kører ikke, eller modellen er ikke downloadet:

```python
import ollama
from ollama import ResponseError

def spørg_ai_robust(spørgsmål: str, model: str = "qwen2.5:7b") -> str:
    try:
        svar = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": spørgsmål}]
        )
        return svar["message"]["content"]
    except ConnectionError:
        return "Fejl: Ollama kører ikke. Start den med: ollama serve"
    except ResponseError as e:
        return f"Model-fejl: {e}. Download modellen: ollama pull {model}"
    except Exception as e:
        return f"Ukendt fejl: {e}"
```

| Fejl | Årsag | Løsning |
|------|-------|----------|
| `ConnectionError` | Ollama kører ikke | `ollama serve` i terminal |
| `ResponseError` | Model ikke downloaded | `ollama pull qwen2.5:7b` |
| `json.JSONDecodeError` | AI svarede ikke valid JSON | Prøv igen eller justér prompt |

---

### Praktisk eksempel: Grundstof-gætter

Et interaktivt program der kombinerer en system-prompt med bruger-input:

```python
import ollama

def grundstof_gætter():
    print("=== GRUNDSTOF-GÆTTER ===")
    while True:
        beskrivelse = input("Beskriv grundstoffet (eller 'stop'): ")
        if beskrivelse.lower() == "stop":
            break
        prompt = f"""Du er en kemi-ekspert. En elev beskriver et grundstof:
"{beskrivelse}"
Gæt grundstoffet. Svar med: navn, kemisk symbol, og én sætning om hvorfor."""
        svar = ollama.chat(model="qwen2.5:7b",
            messages=[{"role": "user", "content": prompt}])
        print(f"AI's gæt: {svar['message']['content']}\n")

grundstof_gætter()
```

Prøv at ændre prompten: bed AI'en om hints i stedet for direkte svar, eller tilføj svarformat (`"Svar KUN med: [navn] ([symbol])"`). Hver ændring ændrer oplevelsen markant.

---

### Praktisk eksempel: Chatbot med historik

En chatbot der husker hele samtalen - og har en persona via system-prompt:

```python
import ollama

SYSTEM = "Du er en venlig dansk hjælper for elever på 10-15 år. Brug enkelt sprog."

def chatbot():
    historik = []
    print("Chatbot klar! Skriv 'stop' for at afslutte.\n")
    while True:
        bruger_input = input("Du: ")
        if bruger_input.lower() == "stop":
            break
        historik.append({"role": "user", "content": bruger_input})
        svar = ollama.chat(
            model="qwen2.5:7b",
            messages=[{"role": "system", "content": SYSTEM}] + historik
        )
        ai_tekst = svar["message"]["content"]
        historik.append({"role": "assistant", "content": ai_tekst})
        print(f"AI: {ai_tekst}\n")

chatbot()
```

📎 **Illustration:** `modul15-ill3-praktiske-eksempler.png`
**Titel:** Anatomien i en god prompt
*Tag grundstof-gætter-prompten og annotér dens dele med pile: [rolle: kemi-ekspert] → [kontekst: elevens beskrivelse] → [instruktion: gæt] → [outputformat: navn + symbol + sætning]. Viser HVORFOR prompten virker - ikke hvad den siger.*

---

### Hvad kan du bygge herfra?

Du har nu alle byggeklodser: en genanvendelig AI-funktion, strukturerede prompts og fejlhåndtering. Kombiner dem:

| Program | Prompt-tilgang | Output-type |
|---------|---------------|-------------|
| Lektiejælper | System-prompt: tålmodig tutor | Tekst |
| Tekst-opsummerer | Few-shot: eksempel på godt resumé | Tekst |
| Sentiment-analysator | Svar KUN med JSON | JSON → dict |
| Quiz-generator | Format: nøjagtigt 5 spørgsmål med svar | Struktureret tekst |

> 🔗 **Kommer i Modul 16:** RAG - giv din AI adgang til dine egne dokumenter og noter, så den kan svare baseret på specifik viden du har givet den.
