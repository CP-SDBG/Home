# Trin 4: Avanceret (Moduler 17–19)


## Modul 17: Skills — lær AI at følge faste instruktioner

> **Målgruppe:** 10–15 år · Har brugt system-prompts · Kender Ollama
> **Illustration-filer:** modul19-ill1 til modul19-ill3 (PNG)
> **Sektioner:** 9 h2 ✅

---

### Hvad er en skill?

Du har sikkert lagt mærke til at AI'en ikke altid svarer på samme måde. Spørger du Claude om det samme to gange, får du to lidt forskellige svar. Det er fint til samtale — men hvis du bygger et program der skal opføre sig *konsistent*, er det et problem.

En **skill** er løsningen. Det er en genanvendelig instruktionspakke der definerer:
- **Hvem AI'en er** — dens rolle og personlighed
- **Hvad den må og ikke må** — begrænsninger og fokusområde
- **Hvordan den svarer** — format, tone, længde

Med en veldefineret skill opfører AI'en sig forudsigeligt og konsistent — uanset hvem der spørger om hvad.

> 💬 **Ordforklaring:** *Skill* er en genanvendelig instruktionspakke til en AI-model. *Konsistent* betyder at AI'en opfører sig på samme måde hver gang. *Template* er en skabelon du kan genbruge og tilpasse.

📎 **Illustration:** `modul17-ill1-skill-opbygning.png`
*Tre byggeklodser: Rolle + Format + Begrænsninger → Skill. Med eksempel på system-prompt der kombinerer alle tre*

---

### System-prompts som fundament

En skill bygger på en **system-prompt** — en skjult instruktion der sættes inden samtalen starter og gælder for hele sessionen.

En stærk system-prompt har tre dele:

**1. Rolle** — hvem er AI'en?
```
Du er en dansk grammatik-lærer med 20 års erfaring.
Du forklarer altid med enkle ord og giver konkrete eksempler.
```

**2. Format** — hvordan svarer den?
```
Svar altid med:
1. En kort forklaring (max 2 sætninger)
2. Et konkret eksempel
3. Et opfølgningsspørgsmål til eleven
```

**3. Begrænsninger** — hvad må den ikke?
```
Svar KUN på spørgsmål om dansk grammatik og sprog.
Hvis eleven spørger om noget andet, sig venligt at du kun hjælper med grammatik.
```

Test og iterér — juster system-prompten til du får præcis den adfærd du vil have.

---

### Skills til specifikke opgaver

Her er eksempler på velfungerende skills:

**Opsummerings-skill:**
```
Du er en ekspert i at opsummere tekster.
Opsummér altid i præcis 3 punkter.
Hvert punkt: max 20 ord.
Brug simpelt sprog — ingen fagtermer.
```

**Kodereview-skill:**
```
Du er en erfaren programmør der laver kodereviews.
Gennemgå altid kode for: 1) Korrekthed, 2) Læsbarhed, 3) Sikkerhed.
Peg på konkrete linjenumre. Forklar hvorfor det er et problem.
Afslut med 3 konkrete forbedringsforslag.
```

**Lektiehjælper-skill:**
```
Du er en tålmodig tutor for elever på 10-15 år.
Forklar aldrig svaret direkte — stil i stedet spørgsmål der leder eleven selv til svaret.
Brug analogier og hverdagseksempler.
```

---

### Genbrugelige skill-templates

En god skill er som god kode: skriv den én gang, brug den mange gange.

Gem dine skills som `.txt`-filer og indlæs dem i din kode:

```python
def indlæs_skill(filnavn: str) -> str:
    with open(f"skills/{filnavn}.txt", "r", encoding="utf-8") as f:
        return f.read()

system_prompt = indlæs_skill("kodereview")

svar = client.messages.create(
    model="claude-haiku-4-5",
    system=system_prompt,
    messages=[{"role": "user", "content": kode_til_review}]
)
```

Versionér dine skills ligesom kode — gem dem i git. En samling af velfungerende skills er ekstremt værdifuld.

---

### Skills i Ollama — Modelfile

Ollama lader dig bygge en **custom model** med en skill indbygget via en `Modelfile`:

```dockerfile
FROM qwen2.5:7b

SYSTEM """
Du er en dansk geografi-lærer.
Du besvarer KUN spørgsmål om geografi — lande, byer, floder, bjerge.
Svar altid med: fakta, en interessant detalje, og ét opfølgningsspørgsmål.
Svar på dansk.
"""
```

Byg og kør din custom model:
```bash
ollama create geo-lærer -f Modelfile
ollama run geo-lærer
```

Nu har du en lokal AI-model med din skill permanent indbygget — ingen grund til at sætte system-prompt hver gang.

📎 **Illustration:** `modul17-ill2-ollama-modelfile.png`
*Modelfile struktur: FROM model + SYSTEM prompt → ollama create → custom model klar til brug*

---

### Praktisk eksempel: byg en kodereview-skill

1. **Definer hvad en god kodereview indeholder:**
   - Tjekker for syntaksfejl
   - Tjekker for logiske fejl
   - Vurderer læsbarhed
   - Foreslår forbedringer

2. **Skriv system-prompten:**
```
Du er en erfaren Python-programmør der laver kodereviews for begyndere (10-15 år).
Gennemgå koden og giv feedback i dette format:
✅ Hvad er godt
⚠️ Hvad kan forbedres (med konkret forslag)
❌ Hvad er forkert (med rettelse)
Brug simpelt sprog. Max 5 punkter i alt.
```

3. **Test med eksempelkode og justér** til du er tilfreds

4. **Gem som `skills/kodereview.txt`** — genanvendeligt for altid

## Modul 18: MCP — Model Context Protocol

> **Målgruppe:** 10–15 år · Kender API-kald · Har prøvet agenter
> **Illustration-filer:** modul17-ill1 til modul17-ill3 (PNG)
> **Sektioner:** 9 h2 ✅

---

### Hvad er MCP?

Forestil dig at du vil give din AI adgang til dine filer, din kalender, din kode og internettet — på samme tid, fra det samme program. Problemet: hver integration kræver sin egen specielle kode. Det er rodet og svært at vedligeholde.

**MCP** (Model Context Protocol) er en **open standard** udviklet af Anthropic i 2024 der løser dette. Det er en fælles protokol — ligesom USB er en fælles standard for hardware — der lader AI-modeller kommunikere med alle slags externe tools og datakilder på én ensartet måde.

Hvis et tool har en MCP-server, kan enhver MCP-kompatibel AI-klient bruge det — uden specialkode.

> 💬 **Ordforklaring:** *Protokol* er et sæt regler for hvordan to systemer kommunikerer. *Open standard* betyder at protokollen er offentlig og gratis at implementere for alle. *MCP* er Anthropic's standard for AI-til-tool kommunikation.

📎 **Illustration:** `modul18-ill1-mcp-arkitektur.png`
*MCP client (AI) ↔ MCP protocol ↔ MCP servere (filer, GitHub, database, web). USB-analogi vist*

---

### MCP server og MCP client

**MCP server** — et program der eksponerer et tool eller en datakilde:
- Beskriver hvilke funktioner den tilbyder (tools)
- Udfører de handlinger AI'en beder om
- Eksempler: filsystem-server, GitHub-server, database-server

**MCP client** — den AI-klient der bruger serverne:
- Spørger serverne hvad de kan
- Beslutter hvornår og hvordan den kalder dem
- Eksempler: Claude Desktop, OpenCode, Pi Agent

Kommunikationen foregår via **JSON-RPC** — et simpelt format for forespørgsler og svar — over enten terminal (stdio) eller HTTP.

> 💬 **Ordforklaring:** *JSON-RPC* er et simpelt protokol-format: send en funktion-navn og parametre som JSON, få svar tilbage som JSON. *stdio* er standard input/output — terminalens tekststrøm.

---

### Tilgængelige MCP-servere

Der er allerede hundredvis af MCP-servere tilgængelige:

| Server | Hvad den kan |
|--------|-------------|
| **Filsystem** | Læs, skriv og søg i filer på din maskine |
| **GitHub** | Opret issues, læs repos, lav pull requests |
| **SQLite** | Kør SQL-forespørgsler mod en lokal database |
| **Web/browser** | Søg på nettet, hent og læs websider |
| **Google Drive** | Læs og skriv Google Docs og Sheets |
| **Slack** | Send beskeder, læs kanaler |

Find dem alle på [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers).

📎 **Illustration:** `modul18-ill2-mcp-servere-oversigt.png`
*Grid af MCP-server ikoner: filsystem, GitHub, database, web, kalender, Slack — med kort beskrivelse*

---

### Installer og forbind en MCP-server

De fleste MCP-servere installeres via npm. Eksempel med filsystem-serveren:

```bash
npm install -g @modelcontextprotocol/server-filesystem
```

Tilføj den til Claude Desktop's konfigurationsfil (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "@modelcontextprotocol/server-filesystem",
        "/Users/dit-navn/Dokumenter"
      ]
    }
  }
}
```

Genstart Claude Desktop — AI'en kan nu læse og skrive filer i din Dokumenter-mappe.

---

### Byg din egen simple MCP-server

Med MCP's Python SDK kan du bygge din egen server på få linjer:

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

app = Server("mit-tool")

@app.list_tools()
async def list_tools():
    return [types.Tool(
        name="hils",
        description="Hilser på en person",
        inputSchema={
            "type": "object",
            "properties": {"navn": {"type": "string"}},
            "required": ["navn"]
        }
    )]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "hils":
        return [types.TextContent(
            type="text",
            text=f"Hej {arguments['navn']}! Velkommen til MCP."
        )]

async def main():
    async with stdio_server() as (read, write):
        await app.run(read, write, app.create_initialization_options())

import asyncio
asyncio.run(main())
```

Installer: `pip install mcp`

Start serveren og forbind den til din AI-klient — AI'en kan nu kalde dit `hils`-tool.

---

### Integration med eksisterende AI-værktøjer

MCP er designet til at virke med de tools du allerede kender:

- **Claude Desktop** — indbygget MCP-support, nemmest at komme i gang
- **OpenCode** — MCP-kompatibel, tilslut servere i konfigurationsfilen
- **Pi Agent** — understøtter MCP-servere som tool-backend
- **Egne Python-programmer** — brug `mcp` klient-biblioteket direkte

Det betyder at de samme MCP-servere virker på tværs af alle dine AI-værktøjer. Installér filsystem-serveren én gang — og alle dine AI-tools kan nu arbejde med dine filer.

📎 **Illustration:** `modul18-ill3-mcp-integration.png`
*Samme MCP-servere (filsystem, GitHub, DB) forbundet til Claude Desktop, OpenCode og Pi Agent*

---

### Praktiske use cases

Med de rigtige MCP-servere kan din AI:

- *"Læs alle Python-filer i mit projekt og find steder med manglende fejlhåndtering"*
- *"Gem denne liste i min SQLite-database under tabellen 'opgaver'"*
- *"Søg efter de seneste nyheder om kvantecomputere og opsummér dem"*
- *"Opret et GitHub issue: 'Fix login-bug' med denne beskrivelse"*
- *"Læs min kalender og find ledige tidspunkter i næste uge"*

---

### Sikkerhed og kontrol

MCP giver AI'en adgang til rigtige systemer — det kræver omtanke:

- **Begræns mapper** — giv filsystem-serveren kun adgang til specifikke mapper, ikke hele harddisken
- **Principle of least privilege** — tilslut kun de servere der er nødvendige til opgaven
- **Log tool-kald** — hold øje med hvad AI'en faktisk gør
- **Review serverkode** — inden du installerer en community-server, tjek hvad den gør
- **Ingen produktions-databaser** under eksperimenter — brug en test-database

MCP er et kraftfuldt fundament for AI der kan handle i verden. Start med read-only servere (filsystem i læse-tilstand, web-søgning) og tilføj skrive-adgang gradvist.

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

