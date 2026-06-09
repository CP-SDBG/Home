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
**Titel:** Spaghetti-integrationer vs. ét stik
*Split-screen*

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
**Titel:** Hvad MCP faktisk sender
*Tre-trins sekvens for ét enkelt tool-kald (zoomet ind på protokollen)*

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
**Titel:** Fra prompt til filsystem og tilbage — 7 trin
*Vandret tidslinje med 7 nummererede trin: 1) Bruger skriver prompt „Læs mine noter og opsummér" → 2) Claude spørger MCP-*

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
