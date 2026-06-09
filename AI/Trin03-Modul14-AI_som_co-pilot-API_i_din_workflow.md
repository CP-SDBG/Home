## Modul 14: AI som co-pilot - API i din workflow

> **Målgruppe:** 10-15 år · Kender Python-grundlag · Har brugt terminal
> **Illustration-filer:** modul14-ill1 til modul14-ill3 (PNG)

---

### Hvad er en API?

**API** står for *Application Programming Interface* - og det er grundlaget for at få AI ind i dine egne programmer.

Tænk på det som en restaurant med et drive-through vindue. Du (dit program) kører op til vinduet, bestiller (sender en forespørgsel), og får maden (svaret) tilbage. Du ved ikke hvad der sker i køkkenet - du behøver bare at kende menuen og formatet.

En LLM-API fungerer præcis sådan: du sender en tekstbesked (**HTTP-request**), modellen behandler den på udbyderens servere, og du får tekst tilbage (**HTTP-response**). Det hele sker via REST API over HTTP - den samme protokol din browser bruger til at hente hjemmesider.

> 💬 **Ordforklaring:** *API* er et sæt regler for hvordan to programmer kommunikerer. *REST API* er en bestemt stil for HTTP-baserede API'er. *HTTP-request* er en besked sendt over internettet - som at spørge en server om noget.

📎 **Illustration:** `modul14-ill1-api-hvad-er-det.png`
**Titel:** To veje ind i køkkenet
*Split-screen: venstre viser manuel brug af claude.ai i browser, højre viser Python-fil med `client.messages.create(...)`. Begge peger på samme AI-sky i midten - visualisér kontrasten: to veje, samme model.*

---

### API-nøgler - sikkerhed er vigtigt

For at bruge en cloud LLM-API skal du bruge en **API-nøgle** - et langt unikt token der identificerer dig og dit forbrug. Hvis nogen får din nøgle, kan de bruge den i dit navn og koste dig penge.

**Regel nummer ét: del aldrig din API-nøgle.** Gem den i en `.env`-fil:

```
# .env fil (aldrig commit denne til git!)
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxx
```

```python
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
```

Tilføj `.env` til din `.gitignore`-fil så den aldrig uploades til GitHub:
```
# .gitignore
.env
```

> 💬 **Ordforklaring:** *API-nøgle* er et hemmeligt token der identificerer dig som bruger af en API. *.env-fil* er en fil der gemmer miljøvariabler lokalt - aldrig commit den til git. *Miljøvariabel* er en variabel der er tilgængelig for alle programmer på dit system.

📎 **Illustration:** `modul14-ill2-api-noegle-sikkerhed.png`
**Titel:** Nøglen i pengeskabet vs. nøglen under dørmåtten
*To scenarier: venstre (rød ramme) viser `api_key="sk-ant-xxx"` direkte i kode, hacker kan se den på GitHub. Højre (grøn ramme) viser `.env` + `.gitignore` blokerer upload. Gør sikkerhedsreglen konkret.*

---

### Første API-kald i Python

Installer biblioteket: `pip install anthropic python-dotenv`

```python
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hvad er Danmarks længste flod?"}
    ]
)
print(message.content[0].text)
```

Til OpenAI er strukturen næsten identisk: `pip install openai` og brug `openai.OpenAI()` i stedet for `anthropic.Anthropic()`.

> 🔗 **Husk fra Modul 13:** Du kan vibe-code hele dette program - beskriv hvad du vil bygge til AI'en og lad den generere kode-skelettet. Skriv derefter dine egne API-kald ind.

---

### System-prompts og roller

En **system-prompt** sættes én gang og gælder for hele samtalen. Uden system-prompt er AI'en generalist - med system-prompt er den specialist der opfører sig konsistent og forudsigeligt.

```python
message = client.messages.create(
    model="claude-haiku-4-5",
    system="Du er en dansk matematik-lærer der altid forklarer trin for trin.",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hvad er 2+2?"}]
)
```

| ❌ Undgå | ✅ Gør i stedet |
|---------|---------------|
| "Du er en hjælper" | "Du er en dansk fysik-lærer for 12-årige der forklarer med hverdagseksempler" |
| Ingen format-krav | "Svar altid i 3 punkter, max 2 sætninger per punkt" |
| "Svar på alt" | "Svar kun på spørgsmål om matematik - afvis andet venligt" |
| Lang, rodet prompt uden struktur | Rolle → Format → Begrænsninger - i den rækkefølge |

En god system-prompt giver konsistente og forudsigelige svar - det er grundlaget for en *skill* (Modul 18).

---

### Konversationshistorik

LLM'er er **statsløse** - de husker ingenting mellem kald. Vil du have en rigtig samtale, skal du sende hele historikken med hver gang:

```python
historik = []

def chat(bruger_besked):
    historik.append({"role": "user", "content": bruger_besked})
    svar = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=historik
    )
    ai_svar = svar.content[0].text
    historik.append({"role": "assistant", "content": ai_svar})
    return ai_svar
```

Jo længere samtalen bliver, jo flere tokens bruges per kald - og jo dyrere bliver det. Ved meget lange samtaler kan du trunkere de ældste beskeder og beholde kun de seneste.

📎 **Illustration:** `modul14-ill3-konversationshistorik.png`
**Titel:** Den voksende pakke
*Tre HTTP-kald som pakker: kald 1 (1 besked), kald 2 (3 beskeder), kald 3 (5 beskeder). Pakkestørrelse og token-tæller vokser visuelt. Konkretisér konsekvensen: større historik = flere tokens = højere pris.*

---

### Token-forbrug og priser

Cloud LLM-API'er koster penge baseret på **tokens** - ikke tegn eller ord, men de brudstykker sproget opdeles i indeni modellen. "Hej verden" er ~3 tokens. En hel roman er ~200.000 tokens.

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Typisk til |
|-------|-----------------------|------------------------|------------|
| Claude Haiku 4.5 | ~$0.80 | ~$4 | Hurtige svar, chatbots |
| Claude Sonnet | ~$3 | ~$15 | Komplekse opgaver, kode |
| Ollama (lokal) | Gratis | Gratis | Udvikling og test |

Kontrollér dit forbrug direkte i svar-objektet:

```python
svar = client.messages.create(...)
print(f"Input tokens:  {svar.usage.input_tokens}")
print(f"Output tokens: {svar.usage.output_tokens}")
print(f"Total:         {svar.usage.input_tokens + svar.usage.output_tokens}")
```

Sæt altid et realistisk `max_tokens` - det sætter et loft for output og forhindrer overraskende store regninger.

> 💡 **Tip:** Start altid med Ollama lokalt under udvikling. Skift til cloud-API når du er klar til at deploye - det sparer penge og giver hurtigere feedback-loops.

---

### Fejlhåndtering og rate limits

Cloud-API'er kan fejle - for mange kald på kort tid giver fejlkode 429 (rate limit). Byg altid **exponential backoff** ind:

```python
import time
from anthropic import RateLimitError, APIConnectionError

def robust_kald(besked, max_forsøg=3):
    for forsøg in range(max_forsøg):
        try:
            return client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=1024,
                messages=[{"role": "user", "content": besked}]
            )
        except RateLimitError:
            vent = 2 ** forsøg  # 1s, 2s, 4s
            print(f"Rate limit - venter {vent}s...")
            time.sleep(vent)
        except APIConnectionError as e:
            print(f"Forbindelsesfejl: {e}")
            break
    return None
```

| Fejlkode | Årsag | Løsning |
|----------|-------|----------|
| 429 | Rate limit nået | Exponential backoff (se kode ovenfor) |
| 401 | Ugyldig API-nøgle | Tjek .env - er variabelnavnet korrekt? |
| 500 | Server-fejl hos udbyderen | Prøv igen om lidt - ikke din fejl |

---

### Lokalt alternativ: Ollama API

Ollama eksponerer samme API-format som OpenAI - du kan bruge OpenAI-biblioteket til at tale med Ollama:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # kræves men ignoreres af Ollama
)

svar = client.chat.completions.create(
    model="qwen2.5:7b",
    messages=[{"role": "user", "content": "Hej!"}]
)
print(svar.choices[0].message.content)
```

Ingen API-nøgle, ingen token-pris, kører offline. Skift fra Ollama til cloud-API ved blot at ændre `base_url` og `api_key` - resten af koden er identisk.

> 🔗 **Husk fra Modul 7:** Ollama kører på `localhost:11434` og starter automatisk som baggrundstjeneste. Kør `ollama list` for at se dine installerede modeller.

---

### Praktisk eksempel: lav en historiefortæller

Vi bygger et program der genererer korte historier baseret på brugerens input - kombinerer system-prompt, konversationshistorik og token-tracking i ét samlet program.

**1. Opsæt miljø og client:**
```bash
pip install anthropic python-dotenv
```
```python
import anthropic, os
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
```

**2. Definer system-prompten - specialist, ikke generalist:**
```python
SYSTEM = """Du er en kreativ historiefortæller for børn på 10-15 år.
Skriv altid historier der:
- Er max 150 ord lange
- Har en overraskende vending i slutningen
- Slutter med ét spørgsmål der inviterer til næste kapitel
Brug enkelt sprog. Ingen vold eller skræmmende indhold."""
```

**3. Byg chat-løkken med historik og token-tracking:**
```python
historik = []
total_tokens = 0

def fortæl_videre(bruger_input):
    global total_tokens
    historik.append({"role": "user", "content": bruger_input})
    svar = client.messages.create(
        model="claude-haiku-4-5",
        system=SYSTEM,
        max_tokens=300,
        messages=historik
    )
    tekst = svar.content[0].text
    historik.append({"role": "assistant", "content": tekst})
    total_tokens += svar.usage.input_tokens + svar.usage.output_tokens
    print(f"[tokens dette kald: {svar.usage.input_tokens + svar.usage.output_tokens} | total: {total_tokens}]")
    return tekst
```

**4. Test og iterér - justér system-prompten efter hvert forsøg:**
```python
# Start historien
print(fortæl_videre("Start en historie om en robot der finder en gammel nøgle"))

# Fortsæt historien med brugerens valg
print(fortæl_videre("Robotten åbner en hemmelig dør - hvad sker der?"))

# Prøv en anden genre: skift SYSTEM til sci-fi, detektiv eller eventyr
# Sammenlign output - system-prompten er den stærkeste kontrol du har
```

Næste skridt: gem historierne til en fil (`open("historier.txt", "a")`), tilføj en brugergrænseflade med `input()`, eller skift model fra Haiku til Sonnet og sammenlign kvaliteten.
