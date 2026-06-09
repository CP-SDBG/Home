## Modul 12: Vælg den rigtige model til opgaven

> **Målgruppe:** 10–15 år · Har prøvet flere AI-modeller
> **Illustration-filer:** modul12-ill1 til modul12-ill4 (PNG)

---

### Ikke alle modeller er ens

Du har nu mødt mange AI-modeller: GPT-4o, Claude, Llama, Qwen, Mistral, DeepSeek. De er alle LLM'er, men de er ikke ens gode til alle opgaver. Ligesom en hammer og en skruetrækker begge er værktøjer, men ikke udskiftelige — er det med AI-modeller.

I dette modul gennemgår vi hvilke modeller der er stærkest til hvilke opgaver, og giver dig en praktisk guide til at vælge.

📎 **Illustration:** `modul12-ill1-model-landskab.png`
**Titel:** Hele landskabet — cloud og lokal på ét overblik
*Oversigt over alle modeller fordelt på cloud/lokal og størrelse — visuelt landskab.*

---

### Kodning

Til kodning er specialiserede modeller markant bedre end generelle modeller af samme størrelse:

**Cloud:**
- **Claude Sonnet** — top til kompleks kode, arkitektur og fejlsøgning
- **GPT-4o** — god allrounder til kode på tværs af sprog

**Lokal:**
- **Qwen2.5-Coder 7B/14B** — stærkeste lokale kode-model, stærk til Python, JS og C#
- **DeepSeek-Coder-V2** — stærk til komplekse algoritmer
- **Gemma 3** — hurtig og overraskende god til simple kode-opgaver

Tommelfingerregel: brug altid en kode-specialiseret model til kodeopgaver, ikke en generel chat-model.

> 🔗 **Husk fra Modul 7:** `ollama pull qwen2.5-coder:7b` — download den bedste lokale kode-model.

---

### Skriving og kreativitet

**Cloud:**
- **Claude** — nuanceret, præcis, god til lange tekster og struktureret skrivning
- **GPT-4o** — kreativ og varieret, god til brainstorming og idéudvikling

**Lokal:**
- **Mistral 7B** — overraskende god til skriving for sin størrelse
- **Llama 3.2 8B** — god dansk og engelsk tekst
- Lokale modeller kæmper med lange, sammenhængende tekster over 1–2 sider

---

### Reasoning og kompleks analyse

Nogen modeller er specifikt trænet til at **tænke grundigt** — de bruger ekstra tid på at overveje svaret inden de svarer. Disse kaldes *reasoning-modeller*:

**Cloud:**
- **o3/o4 (OpenAI)** — designet til dyb reasoning, matematik og logik
- **Claude 3 Opus** — stærk til kompleks analyse og nuancerede svar

**Lokal:**
- **DeepSeek-R1 7B/14B** — open source reasoning-model, overraskende stærk
- Reasoning-modeller er langsommere — de skriver deres "tænkeproces" ud inden svaret

> 💬 **Ordforklaring:** *Reasoning* (ræsonnering) er evnen til at tænke logisk gennem et problem trin for trin. *Chain-of-thought* er en teknik hvor modellen skriver sin tænkeproces ud, hvilket forbedrer svarkvaliteten på komplekse opgaver.

---

### Multimodal — modeller der forstår billeder

Multimodale modeller kan tage imod både tekst og billeder som input:

**Cloud:**
- **GPT-4o** — tekst + billeder + lyd, meget kapabel
- **Claude 3** — tekst + billeder, særligt stærk til dokumentanalyse og diagrammer

**Lokal:**
- **LLaVA** — den klassiske lokale multimodale model
- **Qwen-VL** — stærk lokal model til billede-forståelse
- **Gemma 3** — Googles open source multimodale model

Brug cases: analyser et screenshot af en fejl, forklar et diagram fra en lærebog, beskriv hvad der er på et foto.

---

### Lange dokumenter — context window

Når du arbejder med lange PDF'er, store kode-filer eller lange samtaler, er context window afgørende:

| Model | Context window | Svarer til |
|-------|---------------|----------|
| Llama 3 (lokal) | 8.000 tokens | ~6.000 ord |
| GPT-4o | 128.000 tokens | ~96.000 ord |
| Claude | 200.000 tokens | ~150.000 ord (en roman) |
| Gemini 1.5 Pro | 1.000.000 tokens | ~750.000 ord |

Husk at jo mere du fylder i context window, jo langsommere og dyrere bliver svaret — brug det med omtanke.

> 🔗 **Husk fra Modul 4:** Context window — modellen kan kun se og tage hensyn til det der er inden for vinduet. Ældre dele af en lang samtale forsvinder ud af vinduet.

---

### Hastighed vs. kvalitet

Inden for hver udbyder er der typisk modeller i to kategorier:

**Hurtige/billige modeller** ("mini", "haiku", "flash"):
- Svar på under et sekund
- Billigere ved API-brug
- God nok til simple opgaver, korte svar, klassificering

**Kraftige/langsomme modeller** ("opus", "pro", "4o"):
- Svar på 3–15 sekunder
- Dyrere
- Nødvendige til kompleks reasoning, lange tekster, præcis kode

Tommelfingerregel: start med den hurtige model. Opgradér kun til den kraftige hvis resultatet ikke er godt nok.

---

### Benchmarks — hvordan måles modeller?

Benchmarks er standardiserede tests der måler modellers evner:

- **MMLU** — generel viden og reasoning på tværs af fag
- **HumanEval** — kodekvalitet, løsning af programmeringsopgaver
- **MATH** — matematisk reasoning
- **LMSYS Chatbot Arena** — menneskers præferencer i blinde tests

**Vigtig pointe:** benchmarks måler specifikke ting under specifikke betingelser. En model der scorer højt på MMLU er ikke nødvendigvis bedre til *din* opgave. Test altid selv på dine konkrete use cases.

📎 **Illustration:** `modul12-ill2-benchmarks.png`
**Titel:** Hvem vinder på hvad?
*Søjlediagram: top 6 modeller på tværs af 3 benchmarks (kodning, reasoning, generel viden).*

---

### Praktisk guide: vælg den rigtige model

Brug denne guide som udgangspunkt:

| Opgave | Cloud-valg | Lokal-valg |
|--------|-----------|----------|
| Generel chat og spørgsmål | Claude Sonnet eller GPT-4o | Qwen 2.5 7B |
| Kodning | Claude Sonnet | Qwen2.5-Coder 7B |
| Analyse af langt dokument | Claude (200K context) | Kræver cloud |
| Kreativ skriving | GPT-4o | Mistral 7B |
| Matematik og logik | o3/o4 eller Claude | DeepSeek-R1 7B |
| Billedanalyse | GPT-4o eller Claude 3 | LLaVA eller Qwen-VL |
| Hurtig og billig | GPT-4o mini eller Haiku | Qwen 2.5 3B |

**Fremgangsmåde:**
1. Definer opgaven klart
2. Vurder: kræver det cloud-kvalitet, eller klarer en lokal model det?
3. Vælg den billigste/hurtigste model der løser problemet
4. Test — hvis resultatet ikke er godt nok, opgradér

📎 **Illustration:** `modul12-ill3-valg-guide.png`
**Titel:** Trin-for-trin modelvalg
*Flowdiagram: opgave → spørgsmål → modelvalg — beslutningsguide.*

📎 **Illustration:** `modul12-ill4-model-sammenligning-tabel.png`
**Titel:** Alle modeller på én gang
*Komplet sammenligningstabel: alle modeller, cloud/lokal, stærke sider, pris, context window.*
  - Pakker kompleks model-opsætning i én simpel kommando
  - Kører som en lokal server — ingen internet nødvendigt
  - Standardiseret API der efterligner OpenAI's format
  - Fungerer som fundament for mange andre lokale værktøjer
- Installation (Linux, Windows, Mac)
  - Linux: `curl -fsSL https://ollama.com/install.sh | sh`
  - Windows: installer via .exe fra ollama.com
  - Mac: installer via .dmg eller Homebrew
  - Verifikation: `ollama --version`
- Download og kør din første model
  - `ollama pull llama3.2` — download model
  - `ollama run llama3.2` — start chat direkte i terminal
  - Første download kan tage tid afhængig af modellens størrelse
  - Modeller gemmes lokalt og kører offline bagefter
- Vigtige Ollama-kommandoer: pull, run, list, rm, show
  - `ollama pull <model>` — download en model
  - `ollama run <model>` — kør og chat med modellen
  - `ollama list` — se alle downloadede modeller
  - `ollama rm <model>` — slet en model og frigør diskplads
- Ollama som lokal API-server (port 11434)
  - Starter automatisk som baggrundstjeneste
  - REST API tilgængeligt på http://localhost:11434
  - Kompatibelt med OpenAI API-format
  - Andre programmer kan bruge Ollama som backend
