## Modul 11: Pi Agent — letvægts AI coding agent

> **Målgruppe:** 10–15 år · Kender terminalen · Har prøvet OpenCode eller Copilot
> **Illustration-filer:** modul11-ill1 til modul11-ill2 (PNG)

---

### Hvad er Pi Agent?

**Pi Agent** er det samme program du bruger til at læse og arbejde med dette site. Det er en open source AI coding agent der kører i terminalen og kan læse filer, skrive kode og udføre kommandoer — styret af dine instruktioner på naturligt sprog.

Ligesom OpenCode ser Pi Agent på hele dit projekt. Forskellen er at Pi Agent er designet til at være **letvægts og hurtig** — færre afhængigheder, enklere opsætning, og godt egnet til lokale modeller.

> 💬 **Ordforklaring:** *Letvægts* betyder at programmet er lille, hurtigt og kræver få ressourcer. *Afhængigheder* er andre programmer og biblioteker som et program kræver for at køre.

📎 **Illustration:** `modul11-ill1-pi-agent-oversigt.png`
**Titel:** Pi Agent som kodende agent med godkendelse
*Pi Agent i terminal: læser filer, skriver kode, kører kommandoer — bruger godkender hvert trin.*

---

### Sammenligning med OpenCode og Claude Code

Der er i dag tre populære terminal-baserede AI coding agents:

| | Pi Agent | OpenCode | Claude Code |
|---|---|---|---|
| Oprindelse | Open source | Open source | Officiel fra Anthropic |
| Model-support | Cloud + Ollama | Cloud + Ollama | Primært Claude |
| Opsætning | Meget simpel | Simpel | Simpel |
| Ressourcekrav | Lavt | Middel | Middel |
| Community | Lille | Voksende | Stor |
| Bedst til | Lokale modeller, simpel workflow | Bred model-support | Claude-integration |

Alle tre arbejder på samme måde: de læser dit projekt, foreslår ændringer og venter på din godkendelse.

📎 **Illustration:** `modul11-ill2-agent-sammenligning.png`
**Titel:** Pi Agent, OpenCode, Claude Code — hvornår vælger du hvad?
*Tre kort: Pi Agent, OpenCode, Claude Code — nøgleforskelle og hvornår du vælger det.*

---

### Installation og brug

Pi Agent installeres via npm:
```bash
npm install -g @earendil-works/pi-coding-agent
```

Start i dit projekt:
```bash
cd mit-projekt
pi
```

Forbind til Ollama (lokal, ingen API-nøgle):
```bash
# I Pi Agent config — vælg Ollama som provider
# og qwen2.5-coder som model
```

Derefter er arbejdsgangen den samme som OpenCode: skriv en instruktion på naturligt sprog, gennemgå forslaget, acceptér eller afvis.

---

### Hvornår vælger du Pi Agent?

- Du vil have noget **simpelt der bare virker** uden meget konfiguration
- Du arbejder primært med **lokale modeller** via Ollama
- Du er på en computer med **begrænsede ressourcer**
- Du eksperimenterer og vil prøve forskellige AI coding tools
- Du vil have et open source alternativ du selv kan læse koden i

Vil du have den bredeste model-support og mest aktive community, er OpenCode et bedre valg. Vil du have tæt integration med Claude og officiel support, er Claude Code det rigtige.
