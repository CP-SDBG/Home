## Modul 19: Agenter - autonome AI-workflows

> **Målgruppe:** 10-15 år · Har fulgt Modul 14-16 · Kender Python-funktioner
> **Illustration-filer:** modul18-ill1 til modul18-ill3 (PNG)

---

### Hvad er en AI-agent?

En **chatbot** svarer på ét spørgsmål ad gangen. Du spørger, den svarer, du beslutter hvad der sker hærnest.

En **AI-agent** er fundamentalt anderledes. Du giver den et *mål* - og den planlægger selv, kalder de nødvendige funktioner, evaluerer resultater og fortsætter uden at du behøver at styre hvert trin.

En agent kombinerer tre ting: **LLM** (reasoning), **tools** (handlinger i verden) og **hukommelse** (kontekst på tværs af trin).

> 💬 **Ordforklaring:** *Agent* er en AI der selvstændigt planlægger og udfører en sekvens af handlinger for at nå et mål. *Tools* er Python-funktioner agenten kan kalde. *Orchestration* er koordineringen af hvilke tools der kaldes hvornår.

📎 **Illustration:** `modul19-ill1-agent-vs-chatbot.png`
**Titel:** 12 manuelle trin vs. ét agent-kald
*Opgaven „research 3 frameworks og gem fil" vist som manuel tjekliste med 12 nummererede bokse (åbn browser, google, klik* 12 manuelle trin vs. ét agent-kald
*Opgaven 'research 3 frameworks og gem fil' vist som manuel checkliste (12 bokse: åbn browser, søg, læs, noter, søg igen...) ved siden af agent-kaldet (1 linje kode). Gør MÆNGDEN AF ARBEJDE konkret - ikke et arkitekturdiagram.*

---

### Chatbot eller agent? Vælg rigtigt

| Brug chatbot når... | Brug agent når... |
|---------------------|------------------|
| Opgaven er ét trin: stil spørgsmål, få svar | Opgaven kræver flere trin og beslutninger |
| Alt information er allerede i prompten | AI skal hente information undervejs (søg, læs filer) |
| Output er ren tekst | Output inkluderer handlinger (gem fil, send besked) |
| Du ved præcis hvad der skal ske | Planen afhænger af hvad AI'en finder undervejs |

En agent er mere kompleks at bygge og fejlhåndtere end en chatbot. Brug den kun når opgaven faktisk kræver det.

---

### Tools - definer og implementér

Et tool har to dele: en **JSON-beskrivelse** som AI'en læser, og en **Python-funktion** som programmet kalder:

```python
# Del 1: JSON-beskrivelse (AI'en ser dette)
tools = [
    {
        "name": "søg_web",
        "description": "Søg efter faktuel information på internettet",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Søgeord eller spørgsmål"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "gem_fil",
        "description": "Gem tekst til en fil på disk",
        "input_schema": {
            "type": "object",
            "properties": {
                "filnavn": {"type": "string"},
                "indhold": {"type": "string"}
            },
            "required": ["filnavn", "indhold"]
        }
    }
]

# Del 2: Python-implementering (programmet kalder dette)
def udfør_tool(navn: str, args: dict) -> str:
    if navn == "søg_web":
        return f"[Søgeresultat for '{args['query']}': Django, Flask og FastAPI er populære]"
    elif navn == "gem_fil":
        with open(args["filnavn"], "w", encoding="utf-8") as f:
            f.write(args["indhold"])
        return f"Fil '{args['filnavn']}' gemt ({len(args['indhold'])} tegn)"
    return f"Ukendt tool: {navn}"
```

📎 **Illustration:** `modul19-ill2-tools-function-calling.png`
**Titel:** Det usynlige JSON-kald
*Sekvens i tre trin: 1) AI'en genererer JSON: `{"name": "søg_web", "input": {"query": "Python frameworks"}}` → 2) Python* Det usynlige JSON-kald
*Anatomien af et tool-kald: AI'en genererer `{"name": "søg_web", "input": {"query": "..."}}` → Python parser JSON → kalder `udfør_tool()` → returnerer string tilbage til AI. Gør DEN USYNLIGE PROTOKOL synlig.*

---

### ReAct-pattern og agent-løkken

Den mest udbredte agent-arkitektur hedder **ReAct** (Reasoning + Acting). AI'en skifter mellem at tænke og handle:

```
REASON:  "Jeg skal finde Python frameworks. Jeg har søg_web."
ACT:     søg_web("populære Python web-frameworks")
OBSERVE: "Django, Flask og FastAPI er de mest populære"
REASON:  "Jeg har information. Nu skal jeg gemme resultatet."
ACT:     gem_fil("frameworks.txt", "Django: ...\nFlask: ...")
OBSERVE: "Fil gemt"
REASON:  "Opgaven er løst."
SVAR:    "Sammenligningen er gemt i frameworks.txt"
```

Den fulde Python-løkke der kører dette mønster:

```python
import anthropic, os
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def kør_agent(mål: str, max_trin: int = 10) -> str:
    beskeder = [{"role": "user", "content": mål}]

    for trin in range(max_trin):
        svar = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            tools=tools,
            messages=beskeder
        )

        if svar.stop_reason == "end_turn":
            for blok in svar.content:
                if hasattr(blok, "text"):
                    return blok.text

        beskeder.append({"role": "assistant", "content": svar.content})
        tool_resultater = []

        for blok in svar.content:
            if blok.type == "tool_use":
                print(f"  Trin {trin+1}: {blok.name}({blok.input})")
                resultat = udfør_tool(blok.name, blok.input)
                tool_resultater.append({
                    "type": "tool_result",
                    "tool_use_id": blok.id,
                    "content": resultat
                })

        beskeder.append({"role": "user", "content": tool_resultater})

    return "Max trin nået"
```

📎 **Illustration:** `modul19-ill3-react-loop.png`
**Titel:** Agentens logbog
*Et konkret kørende transcript som terminal-output: `[THOUGHT] Jeg skal søge...` / `[ACTION] søg_web("Python frameworks")* Agentens logbog
*Et konkret transcript fra en kørende agent: linje for linje - timestamp, THOUGHT: "...", ACTION: søg_web(...), OBSERVATION: "...", THOUGHT: "...", FINAL: "...". Som debugger-output. Gør DET ABSTRAKTE LØP konkret og læseligt.*

---

### Multi-step planlægning

Agenten behøver ikke en step-by-step plan fra dig. Giv den et mål - den nedbryder det selv:

```python
kør_agent("Lav en liste over de 5 største danske byer, søg befolkningstal for hver, og gem en sorteret tabel i byer.csv")
```

Agenten vil: søge efter listen, søge befolkningstal for hver by, formatere som CSV, gemme filen - alt koordineret af AI'ens reasoning. Jo bedre målet er beskrevet, jo bedre planlægger agenten. Vær specifik om *format* og *output* - ikke om *fremgangsmåden*.

---

### Hukommelse og tilstand i agenter

Agenten husker alle trin i `beskeder`-listen - hver tool-handling og dens resultat tilføjes:

```python
# Beskeder-listen vokser for hvert trin:
beskeder = [
    {"role": "user",      "content": "Research Python frameworks..."},
    {"role": "assistant", "content": [tool_use: søg_web(...)]},
    {"role": "user",      "content": [tool_result: "Django, Flask..."]},
    {"role": "assistant", "content": [tool_use: gem_fil(...)]},
    {"role": "user",      "content": [tool_result: "Fil gemt"]},
    {"role": "assistant", "content": "Sammenligningen er gemt..."}
]
```

Agenten gentager ikke de samme tool-kald fordi den kan se hvad den allerede har gjort. Men listen vokser - lange agenter bruger mange tokens. Sæt altid `max_trin` for at undgå ukontrollerede kørsler.

---

### Sikkerhed og begrænsninger

Agenter med adgang til filsystem og internet kan gøre skade hvis de fejler. Byg disse sikkerhedslag ind fra start:

| Regel | Hvorfor | Implementering |
|-------|---------|----------------|
| Max trin | Loop kan køre evigt | `max_trin=10` i agent-løkken |
| Least privilege | Agenten gør kun hvad den må | Kun nødvendige tools i listen |
| Sandbox | Fejl ødelægger ikke rigtige filer | Test i separat testmappe |
| Log tool-kald | Se hvad agenten faktisk gjorde | `print(f"Kalder {blok.name}")` |
| Godkendelsestrin | Irreversible handlinger | `input("Bekræft? (j/n)")` |

---

### Praktisk eksempel: research-assistent

**1. Opsæt client og tools:**
```bash
pip install anthropic python-dotenv
```
Brug tool-definitionerne fra "Tools" sektionen ovenfor.

**2. Implementer tool-handler:**
```python
def udfør_tool(navn, args):
    if navn == "søg_web":
        return f"Mock resultat for: {args['query']}"  # erstat med rigtig API
    elif navn == "gem_fil":
        with open(args["filnavn"], "w", encoding="utf-8") as f:
            f.write(args["indhold"])
        return f"Gemt: {args['filnavn']}"
    return "Ukendt tool"
```

**3. Indsæt agent-løkken og kør:**
```python
resultat = kør_agent(
    "Find de 3 vigtigste forskelle mellem Django og FastAPI. Gem i sammenligning.txt"
)
print(resultat)
```

**4. Eksperimenter:** prøv korte mål vs. detaljerede, ændr `max_trin`, tilføj et tredje tool (`læs_fil`). Hvornår vælger agenten det forkerte tool? Hvornår løber den i loop?
