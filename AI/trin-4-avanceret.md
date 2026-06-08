# Trin 4: Avanceret

## Modul 18: Skills — lær AI at følge faste instruktioner

> **Målgruppe:** 10–15 år · Har brugt system-prompts · Kender Ollama
> **Illustration-filer:** modul18-ill1 til modul18-ill2 (PNG)

---

### Hvad er en skill?

Du har sikkert lagt mærke til at AI'en ikke altid svarer på samme måde. Spørger du Claude om det samme to gange, får du to lidt forskellige svar. Det er fint til samtale — men hvis du bygger et program der skal opføre sig *konsistent*, er det et problem.

En **skill** er løsningen. Det er en genanvendelig instruktionspakke der definerer:
- **Hvem AI'en er** — dens rolle og personlighed
- **Hvad den må og ikke må** — begrænsninger og fokusområde
- **Hvordan den svarer** — format, tone, længde

Med en veldefineret skill opfører AI'en sig forudsigeligt og konsistent — uanset hvem der spørger om hvad.

> 💬 **Ordforklaring:** *Skill* er en genanvendelig instruktionspakke til en AI-model. *Konsistent* betyder at AI'en opfører sig på samme måde hver gang. *Template* er en skabelon du kan genbruge og tilpasse.

📎 **Illustration:** `modul18-ill1-skill-opbygning.png`
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

📎 **Illustration:** `modul18-ill2-ollama-modelfile.png`
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

## Modul 19: MCP — Model Context Protocol

> **Målgruppe:** 10–15 år · Kender API-kald · Har prøvet agenter
> **Illustration-filer:** modul19-ill1 til modul19-ill3 (PNG)

---

### Hvad er MCP?

Forestil dig at du vil give din AI adgang til dine filer, din kalender, din kode og internettet — på samme tid, fra det samme program. Problemet: hver integration kræver sin egen specielle kode. Det er rodet og svært at vedligeholde.

**MCP** (Model Context Protocol) er en **open standard** udviklet af Anthropic i 2024 der løser dette. Det er en fælles protokol — ligesom USB er en fælles standard for hardware — der lader AI-modeller kommunikere med alle slags externe tools og datakilder på én ensartet måde.

Hvis et tool har en MCP-server, kan enhver MCP-kompatibel AI-klient bruge det — uden specialkode.

> 💬 **Ordforklaring:** *Protokol* er et sæt regler for hvordan to systemer kommunikerer. *Open standard* betyder at protokollen er offentlig og gratis at implementere for alle. *MCP* er Anthropic's standard for AI-til-tool kommunikation.

📎 **Illustration:** `modul19-ill1-mcp-arkitektur.png`
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

📎 **Illustration:** `modul19-ill2-mcp-servere-oversigt.png`
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

📎 **Illustration:** `modul19-ill3-mcp-integration.png`
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
