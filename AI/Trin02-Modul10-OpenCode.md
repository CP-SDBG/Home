## Modul 10: OpenCode — AI-assisteret kodning i terminalen

> **Målgruppe:** 10–15 år · Kender terminalen · Har prøvet at kode
> **Illustration-filer:** modul10-ill1 til modul10-ill3 (PNG)

---

### Hvad er OpenCode?

**OpenCode** er en AI coding agent der kører i terminalen. Mens Copilot sidder inde i din editor og hjælper linje for linje, tager OpenCode et skridt tilbage og ser på dit **hele projekt**.

Du beskriver en opgave på naturligt sprog — *"tilføj login-funktionalitet til dette projekt"* — og OpenCode læser alle relevante filer, planlægger hvad der skal laves, skriver koden og viser dig præcis hvad den vil ændre, inden du godkender.

Det er open source, understøtter mange modeller (cloud og lokale via Ollama) og er et populært alternativ til det officielle Claude Code.

> 💬 **Ordforklaring:** *Agent* er en AI der ikke bare svarer på spørgsmål, men selvstændigt planlægger og udfører opgaver — læser filer, skriver kode, kører kommandoer. *Codebase* er hele dit projekt med alle filer og mapper.

📎 **Illustration:** `modul10-ill1-opencode-oversigt.png`
**Titel:** Naturligt sprog ind — kodeændringer ud
*Terminal med OpenCode: naturligt sprog ind → filer læses → kodeændringer foreslås → bruger godkender/afviser.*

---

### Installation og opsætning

```bash
npm install -g opencode-ai
```

Konfigurér din model-forbindelse. Til cloud (Claude):
```bash
export ANTHROPIC_API_KEY=din-nøgle-her
```

Til lokal via Ollama (ingen nøgle nødvendig):
```bash
# I OpenCode config — peg på Ollama
model: ollama/qwen2.5-coder:7b
```

Navigér til dit projekt og start:
```bash
cd mit-projekt
opencode
```

> 💬 **Ordforklaring:** *npm* er Node.js's package manager — et program der installerer andre programmer. *Miljøvariabel* er en variabel der er tilgængelig for alle programmer på dit system — bruges til at gemme API-nøgler sikkert uden at skrive dem direkte i koden.

---

### Grundlæggende brug i terminalen

Når OpenCode starter, viser det en oversigt over dit projekt og venter på din instruktion:

```
> Tilføj en funktion der validerer email-adresser
```

OpenCode vil:
1. Scanne dit projekt for relevante filer
2. Foreslå hvilke filer der skal ændres
3. Vise dig en diff af de foreslåede ændringer
4. Vente på din godkendelse inden det skriver noget

Du kan altid afvise, bede om justeringer eller godkende. Du er aldrig tvunget til at acceptere et forslag.

```
> Fiks alle steder der mangler fejlhåndtering i utils.py
> Skriv docstrings til alle funktioner i api.py
> Refaktorér denne klasse til at bruge dataclasses
```

📎 **Illustration:** `modul10-ill2-opencode-workflow.png`
**Titel:** Diff-visning — se præcis hvad der ændres
*Terminal-session: instruktion → fil-scanning → diff-visning med grønt/rødt → godkend/afvis.*

---

### Cloud vs. lokal model

OpenCode kan bruges med begge:

**Cloud (Claude/GPT-4o):**
- Hurtigere og smartere resultater
- Koster penge per token
- Kræver internet
- Dine filer sendes til ekstern server

**Lokal (Ollama):**
- Gratis, ingen API-nøgle
- Fuld privacy — kode forlader ikke din maskine
- Langsommere, men fuldt funktionelt
- Bedste lokale kode-modeller: `qwen2.5-coder:7b`, `deepseek-coder-v2`

For privat eller fortrolig kode er lokal altid det rigtige valg. For hurtige resultater på åbne projekter er cloud-modeller stærkere.

📎 **Illustration:** `modul10-ill3-cloud-vs-lokal-kodning.png`
**Titel:** Hurtigt og dyrt vs. langsomt og privat
*To stier side om side: cloud-kodning (hurtig, koster penge, data ud) vs*

---

### Projektkontekst — hvordan forstår den din codebase?

OpenCode indekserer dit projekt: mappestruktur, filnavne, imports og afhængigheder. Det bruger denne kontekst til at forstå hvad din kode gør og hvordan delene hænger sammen.

Jo bedre struktureret dit projekt er, jo bedre resultater:
- **Gode filnavne** — `user_auth.py` er bedre end `utils2.py`
- **Kommentarer** — forklar hvad komplekse funktioner gør
- **Konsistent stil** — OpenCode følger den stil den ser i filen

---

### Praktiske use cases

- *"Refaktorér denne klasse til at følge single-responsibility princippet"*
- *"Find og fiks alle steder der mangler input-validering"*
- *"Tilføj logging til alle database-kald"*
- *"Skriv unit tests til funktionerne i auth.py"*
- *"Oversæt alle kommentarer fra dansk til engelsk"*

OpenCode er særligt stærk til opgaver der kræver at man forstår hele projektet — ikke kun én fil.
