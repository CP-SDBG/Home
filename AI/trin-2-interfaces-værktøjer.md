# Trin 2: Interfaces & værktøjer

## Modul 6: Web-interfaces — ChatGPT, Claude, OpenRouter

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul6-ill1 til modul6-ill5 (PNG)

---

### Hvad er et web-interface til en LLM?

Den nemmeste måde at komme i gang med AI er via et **web-interface** — en hjemmeside du åbner i din browser, logger ind på og begynder at skrive til med det samme. Ingen installation, ingen kode, ingen konfiguration.

Du kender sikkert allerede konceptet fra Gmail eller Google Docs: software der kører i browseren, gemmer dine data i skyen og altid er opdateret. Web-interfaces til LLM'er fungerer på samme måde — du skriver en besked, modellen svarer, og historikken gemmes automatisk på udbyderens servere.

Det betyder også at udbyderen kan se dine beskeder. Det er vigtigt at huske: alt du skriver til ChatGPT eller Claude sendes over internettet og behandles af en virksomheds servere. Del aldrig adgangskoder, personlige oplysninger eller fortrolige dokumenter via et web-interface.

> 💬 **Ordforklaring:** *Web-interface* er en brugerflade der kører i din browser — som en hjemmeside der reagerer på dine input. *Cloud* betyder at beregningerne sker på en virksomheds servere langt væk, ikke på din computer.

📎 **Illustration:** `modul6-ill1-web-interface-oversigt.png`
*Oversigt: browser → internet → AI-server → svar tilbage — med login og historik*

---

### ChatGPT — den mest kendte

**ChatGPT** er lavet af OpenAI og er det web-interface de fleste tænker på når de hører "AI". Det blev lanceret i november 2022 og satte gang i den store AI-bølge vi er midt i nu.

**Hvad kan det?**
Standardmodellen i dag er **GPT-4o** (udtales "four-oh") — en *multimodal* model, hvilket betyder den kan forstå både tekst, billeder og lyd. Du kan indsætte et billede og spørge om det, vedhæfte en PDF og få den opsummeret, eller bede om hjælp til kode.

ChatGPT har også en **websøgning**-funktion der lader den finde aktuelle informationer — nyttigt når du spørger om noget der er sket for nylig, for modellens træningsdata stopper på et bestemt tidspunkt.

**Vigtigt at vide:**
OpenAI kan bruge dine samtaler til at træne fremtidige modeller. Du kan slå det fra under indstillinger — gør det, hvis du ikke vil have dine tekster brugt på den måde.

**Styrker:** generelle opgaver, kreativ skrivning, kode, brainstorming, websøgning
**Begrænsninger:** prisen stiger hurtigt ved højt API-forbrug, data kan bruges til træning

> 💬 **Ordforklaring:** *Multimodal* betyder at modellen kan arbejde med flere slags input — tekst, billeder og lyd — ikke kun tekst. *Træningsdata* er de eksempler modellen har lært fra.

📎 **Illustration:** `modul6-ill2-chatgpt-interface.png`
*ChatGPT-interface med eksempel på samtale, filupload og websøgning markeret*

---

### Claude.ai — præcis og omhyggelig

**Claude** er lavet af Anthropic og er den model du taler med her. Den er designet med et særligt fokus på præcision, sikkerhed og ærlighed — Claude vil hellere sige "det ved jeg ikke" end opfinde et svar der lyder godt men er forkert.

**Hvad kan det?**
Claude er særligt stærk til **analyse af lange tekster**. Hvor mange modeller kæmper når dokumentet bliver langt, håndterer Claude op til **200.000 tokens** — svarende til en hel roman. Det gør den ideel til at læse store PDF'er, gennemgå lange kode-filer eller følge en lang og kompleks samtale.

Claude er også multimodal og kan analysere billeder. Den gratis plan giver et begrænset antal beskeder per dag. Claude Pro til $20/md giver prioriteret adgang og større context window.

**Styrker:** lange dokumenter, præcise og ærlige svar, kode, nuanceret analyse
**Begrænsninger:** ingen native websøgning i gratis plan, beskedbegrænsning på gratis tier

> 🔗 **Husk fra Modul 2:** Context window — den mængde tekst modellen kan "huske" på én gang. Claudes 200K tokens er markant større end de fleste lokale modellers 8–32K.

📎 **Illustration:** `modul6-ill3-claude-interface.png`
*Claude.ai-interface med eksempel på lang dokument-analyse og 200K context window vist*

---

### OpenRouter — ét sted, alle modeller

**OpenRouter** er anderledes end ChatGPT og Claude. Det er ikke en model — det er et **aggregator-interface** der samler adgang til hundredvis af modeller fra mange forskellige udbydere på ét sted.

Tænk på det som en streamingtjeneste der samler Netflix, Disney+ og HBO på én skærm — du betaler kun for det du bruger, og du kan skifte "kanal" med ét klik. Via OpenRouter kan du teste GPT-4o, Claude, Llama, Mistral, Gemini og mange andre med ét enkelt login og ét API-key.

Det er praktisk når du vil:
- Sammenligne to modeller på den samme opgave
- Finde den billigste model der løser dit problem godt nok
- Bygge et program der kan bruge mange forskellige modeller

Prisen er pay-per-token — du køber credits og betaler kun for det du faktisk bruger. Mange modeller er tilgængelige gratis eller meget billigt.

> 💬 **Ordforklaring:** *Aggregator* samler mange tjenester på ét sted. *API-key* er en unik kode der identificerer dig når du tilgår en tjeneste via kode — som et kørekort til API'et.

📎 **Illustration:** `modul6-ill4-openrouter-model-valg.png`
*OpenRouter: ét interface med mange modeller — prissammenligning og model-skift vist*

---

### Sammenligning — hvornår bruger du hvad?

De tre interfaces løser ikke det samme problem — vælg det der passer til opgaven:

| Situation | Bedste valg |
|-----------|-------------|
| Generel hjælp, ideer, skriving, kode | ChatGPT eller Claude |
| Analysere et langt dokument eller en stor fil | Claude (200K context) |
| Aktuelle nyheder eller websøgning | ChatGPT (med søgning slået til) |
| Teste og sammenligne mange modeller | OpenRouter |
| Bygge et program der kalder en LLM | OpenRouter API eller direkte API |
| Privacy vigtigst — data må ikke forlade maskinen | Lokal model (Modul 7–8) |

Alle tre har **gratis tiers** — et godt sted at starte. Når du rammer grænserne, kan du vurdere om et betalt abonnement giver mening for dig.

---

### Gratis vs. betalte planer

Ingen af de store AI-tjenester er fuldt ud gratis — men alle tilbyder en gratis pakke der er god nok til at komme i gang.

**Gratis tier:**
- Adgang til modellen, men begrænset antal beskeder per dag
- Ældre eller mindre modeller (fx GPT-4o mini i stedet for GPT-4o)
- Kan være langsom i myldretiden når mange bruger tjenesten

**Betalt abonnement (~$20/md):**
- Ubegrænset eller markant højere antal beskeder
- Adgang til de nyeste og kraftigste modeller
- Højere prioritet i køen — hurtigere svar
- Ekstra features som avanceret billedgenerering og stemme-mode

**API (pay-per-token):**
- Bedst til programmering — du betaler kun for det du bruger
- Kræver teknisk opsætning (se Modul 14)
- For moderat brug ofte billigere end abonnement

Tommelfingerregel: start gratis. Hvis du bruger AI dagligt og rammer begrænsningerne jævnligt, er $20/md et overkommeligt beløb. Til programmering er API næsten altid det rigtige valg.

> 💬 **Ordforklaring:** *Tier* betyder niveau — fx gratis niveau, standard niveau, premium niveau. *Abonnement* er en fast månedlig betaling uanset hvor meget du bruger.

---

### Hvad er forskellen på web-interface og API-adgang?

Du kan tænke på det sådan her:

**Web-interface** er som at gå på restaurant — du sætter dig ned, bestiller, og får maden serveret. Alt er klar, men du kan kun vælge fra menuen og må bruge restaurantens åbningstider.

**API** er som at have et professionelt køkken derhjemme — du får adgang til de samme ingredienser, men kan lave præcis den ret du vil, når du vil, og i den mængde du vil. Kræver lidt mere setup.

| | Web-interface | API |
|---|---|---|
| Adgang | Browser, klik og skriv | Kode (Python, JS osv.) |
| Setup | Ingen — bare log ind | Kræver API-nøgle og kode |
| Automatisering | Manuel — du skriver selv | Kan køres automatisk |
| Pris | Gratis tier eller abonnement | Pay-per-token |
| Bedst til | Lære, eksperimentere, daglig brug | Bygge programmer |

I dette modul arbejder vi med web-interfaces. API-adgang gennemgår vi i Modul 14.

> 🔗 **Kommer i Modul 14:** Første API-kald i Python — send en besked til en LLM fra din egen kode og få svaret tilbage.

📎 **Illustration:** `modul6-ill5-web-vs-api.png`
*To kolonner: web-interface (browser, klik) vs API (kode, automatisering) — hvornår hvert giver mening*

## Modul 7: Ollama — kør AI-modeller lokalt

> **Målgruppe:** 10–15 år · Let computer science baggrund · Kræver adgang til terminal
> **Illustration-filer:** modul7-ill1 til modul7-ill4 (PNG)

---

### Hvad er Ollama og hvad løser det?

At køre en AI-model lokalt på din computer lyder måske kompliceret — og det *var* det engang. Du skulle selv finde den rigtige fil, konfigurere GPU-drivere, installere Python-biblioteker og håbe at det hele virkede sammen. Det tog timer og fejlede halvdelen af gangene.

**Ollama løser det problem.** Det er et program der pakker al den kompleksitet ind i én simpel kommando. Du skriver `ollama run llama3.2`, og Ollama finder modellen, downloader den, sætter den op og starter en chat — alt i ét.

Bag kulisserne kører Ollama som en **lokal server** på din computer. Det betyder at andre programmer — fx din browser, et Python-script eller en editor — kan tale med AI-modellen via et standard API, præcis som de ville tale med ChatGPT i skyen. Bare lokalt, privat og gratis.

> 💬 **Ordforklaring:** *Server* er et program der venter på forespørgsler og svarer på dem. En lokal server kører på din egen computer — ikke på internettet. *API* er en standardiseret måde for programmer at tale med hinanden.

📎 **Illustration:** `modul7-ill1-ollama-arkitektur.png`
*Ollama som lag mellem model-filer og bruger/programmer — terminal, browser og Python alle forbundet*

---

### Installation

Ollama virker på Windows, Mac og Linux.

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Hent installationsfilen fra [ollama.com](https://ollama.com) og kør den. Ollama installeres og starter automatisk som en baggrundstjeneste.

**Mac:**
Hent `.dmg`-filen fra ollama.com eller installer via Homebrew: `brew install ollama`

Tjek at det virker:
```bash
ollama --version
```

Hvis du får et versionsnummer tilbage, er Ollama klar.

> 💬 **Ordforklaring:** *curl* er et terminal-kommando der downloader filer fra internettet. *Baggrundstjeneste* er et program der kører stille i baggrunden uden et synligt vindue.

---

### Download og kør din første model

```bash
ollama pull qwen2.5:7b
```

Dette downloader Qwen 2.5 7B-modellen — en god allrounder på ~4 GB. Første download tager lidt tid afhængig af din internetforbindelse. Modellen gemmes lokalt og kører offline bagefter.

Start en chat direkte i terminalen:
```bash
ollama run qwen2.5:7b
```

Du kan nu skrive til modellen og få svar — uden internet, uden abonnement, uden at dine beskeder forlader din computer. Skriv `/bye` for at afslutte.

> 🔗 **Husk fra Modul 3:** Vi gennemgik hardware-krav til lokale modeller. En 7B model kræver ~8 GB VRAM eller ~16 GB RAM. Har du mindre, prøv en 3B model: `ollama pull qwen2.5:3b`

---

### Vigtige kommandoer

```bash
ollama pull <model>    # Download en model
ollama run <model>     # Start chat med modellen
ollama list            # Se alle downloadede modeller
ollama rm <model>      # Slet en model og frigør diskplads
ollama show <model>    # Vis info om modellen (størrelse, parametre)
```

Modeller fylder fra ~1 GB (lille 1B model) til ~80 GB (70B model). Brug `ollama list` jævnligt for at holde styr på hvad du har liggende.

📎 **Illustration:** `modul7-ill2-ollama-kommandoer.png`
*De 5 vigtigste Ollama-kommandoer med eksempler og hvad de gør*

---

### Ollama som lokal API-server

Når Ollama kører, starter det automatisk en lokal webserver på **port 11434**. Det betyder du kan sende HTTP-forespørgsler til `http://localhost:11434` — præcis som du ville kalde OpenAI's API, bare lokalt.

Det vigtige her: Ollama's API-format er **kompatibelt med OpenAI's format**. Det betyder at programmer der er skrevet til at tale med ChatGPT, ofte kan skiftes om til at bruge Ollama med én linje kode — bare skift adressen fra `api.openai.com` til `localhost:11434`.

Dette er grunden til at Ollama er blevet så populært: det er ikke bare et chat-program, det er et fundament som mange andre værktøjer kan bygge på.

> 💬 **Ordforklaring:** *Port* er som et husnummer på internettet — port 11434 er den "dør" Ollama lytter på. *localhost* er din computers adresse til sig selv — trafik der går til localhost forlader aldrig din maskine.

📎 **Illustration:** `modul7-ill3-lokal-api-server.png`
*Ollama på port 11434 — terminal, Python-script, Open WebUI og browser alle forbundet til den samme lokale server*

---

### Integration med andre værktøjer

Fordi Ollama kører som en lokal server med standardiseret API, kan mange andre programmer bruge det som AI-backend:

- **Open WebUI** — grafisk chat-interface i browseren, forbinder automatisk til Ollama (Modul 8)
- **LM Studio** — kan bruge Ollama som backend eller køre egne modeller
- **Python** — kald via `requests`-biblioteket eller det dedikerede `ollama`-bibliotek
- **VS Code extensions** — flere AI-coding extensions kan pege på Ollama i stedet for cloud
- **Pi Agent og OpenCode** — begge kan konfigureres til at bruge Ollama (Modul 10–11)

```python
# Simpelt Python-kald til Ollama
import ollama
response = ollama.chat(model='qwen2.5:7b',
    messages=[{'role': 'user', 'content': 'Hvad er verdens højeste bjerg?'}])
print(response['message']['content'])
```

---

### Model library — hvad findes der, og hvad vælger du?

På [ollama.com/library](https://ollama.com/library) finder du hundredvis af modeller. Her er de vigtigste kategorier:

| Model | Størrelse | Bedst til |
|-------|-----------|----------|
| Llama 3.2 | 3B, 8B | God allrounder, hurtig |
| Qwen 2.5 | 3B, 7B, 14B | Stærk til kodning og dansk tekst |
| Mistral | 7B | Hurtig, god til instruktioner |
| Qwen2.5-coder | 7B, 14B | Specifikt til kode |
| DeepSeek-R1 | 7B, 14B | Reasoning og komplekse opgaver |
| Gemma 3 | 4B, 12B | Googles open source model |

Tommelfingerregel: **start med Qwen 2.5 7B** til generel brug. Til kodning: **Qwen2.5-coder 7B**.

📎 **Illustration:** `modul7-ill4-model-library.png`
*Oversigt over populære Ollama-modeller med størrelse, styrker og anbefalede use cases*

## Modul 8: Lokale interfaces — LM Studio, Open WebUI, Msty

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul8-ill1 til modul8-ill4 (PNG)

---

### Hvad er et lokalt interface?

At chatte med en AI i terminalen via `ollama run` virker fint til hurtige tests — men det er ikke særlig komfortabelt til daglig brug. Du kan ikke se en pæn samtalehistorik, skifte model med et klik eller vedhæfte filer.

Det er her **lokale interfaces** kommer ind. Det er programmer der giver dig en grafisk brugerflade — ligesom ChatGPT eller Claude.ai — men som kører på din egen computer og taler med Ollama (eller en anden lokal model-engine) i baggrunden.

Resultatet: du får en oplevelse der ligner de kendte cloud-interfaces, men med en afgørende forskel — **dine data forlader aldrig din maskine**.

> 💬 **Ordforklaring:** *Grafisk brugerflade* (GUI) er et program med knapper, menuer og vinduer — i modsætning til en terminal der kun bruger tekst. *Frontend* er det du ser og klikker på. *Backend* er det der kører i baggrunden og laver det egentlige arbejde.

📎 **Illustration:** `modul8-ill1-lokal-interface-oversigt.png`
*Lagdiagram: Grafisk interface (top) → Ollama (midt) → Model-fil (bund) — alt lokalt på din computer*

---

### LM Studio — fuld kontrol

**LM Studio** er en desktop-app til Windows, Mac og Linux der kombinerer model-browser, downloader og chat-interface i ét program. Du behøver ikke Ollama — LM Studio har sin egen model-engine indbygget.

**Hvad kan det:**
- **Model browser** — søg efter og download modeller direkte fra Hugging Face
- **Chat-interface** med system-prompt editor (skriv en personlighed til din AI)
- **Parameter-justering** — skru på temperature, context length og andre indstillinger
- **Lokal API-server** — eksponér modellen som OpenAI-kompatibelt API til andre programmer

LM Studio er den bedste løsning hvis du vil have fuld kontrol og mulighed for at eksperimentere med avancerede indstillinger.

> 💬 **Ordforklaring:** *System-prompt* er en skjult instruktion du giver AI'en inden samtalen starter — fx "du er en hjælpsom lærer der forklarer alt simpelt". *Hugging Face* er det største open source-arkiv for AI-modeller.

---

### Open WebUI — ChatGPT-oplevelsen, lokalt

**Open WebUI** er et browser-baseret interface der kører oven på Ollama. Du installerer det én gang, og bagefter åbner du bare din browser og har en oplevelse der ligner ChatGPT meget — komplet med samtalehistorik, model-skift og filupload.

**Hvad kan det:**
- Kører i din browser — ingen desktop-app nødvendig
- Understøtter model-skift på sekunder
- Samtalehistorik gemmes lokalt
- Kan håndtere **multiple brugere** — god til familier eller et lille klasseværelse
- Understøtter billedmodeller (multimodal) og RAG

Installation via Docker:
```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```
Åbn derefter `http://localhost:3000` i din browser.

> 💬 **Ordforklaring:** *Docker* er et program der pakker software i isolerede "containere" — det gør installation nemmere fordi alt hvad programmet kræver er inkluderet. *RAG* gennemgås i Modul 16.

---

### Msty — simpelt og hurtigt

**Msty** er en desktop-app designet til at være så nem som muligt. Den forbinder automatisk til Ollama og giver dig en ren, hurtig chat-oplevelse uden avancerede indstillinger der forvirrer.

God til: dem der vil have noget der bare virker uden at rode med indstillinger. Ikke god til: avancerede brugere der vil justere parametre eller sætte en API-server op.

---

### Sammenligning — hvornår bruger du hvad?

| | LM Studio | Open WebUI | Msty |
|---|---|---|---|
| Installation | Download .exe/.dmg | Docker | Download .exe/.dmg |
| Kræver Ollama | Nej (egen engine) | Ja | Ja |
| Interface | Desktop-app | Browser | Desktop-app |
| Sværhedsgrad | Middel | Lidt teknisk | Nem |
| Bedst til | Eksperimenter, API | Server, flere brugere | Hurtig daglig brug |
| Avancerede indstillinger | ✅ Mange | ✅ Mange | ❌ Få |

📎 **Illustration:** `modul8-ill2-sammenligning.png`
*Tre kort side om side: LM Studio, Open WebUI, Msty — installation, krav og hvornår du bruger hvert*

---

### Hardware-krav

Lokale interfaces stiller ikke ekstra krav ud over hvad modellen selv kræver:

- **Minimum:** 8 GB RAM — kør en 3B model på CPU (langsomt men muligt)
- **Anbefalet:** 16 GB RAM + GPU med 8 GB VRAM — kør 7B model hurtigt
- **Komfortabelt:** 32 GB RAM + GPU med 12–16 GB VRAM — kør 13–14B modeller

Uden GPU kører modellen på CPU — det virker, men er 5–20 gange langsommere. En 7B model genererer typisk 10–50 tokens/sekund på GPU mod 2–5 tokens/sekund på CPU.

> 🔗 **Husk fra Modul 3:** CPU offloading — hvis modellen er lidt for stor til VRAM, kan ekstra lag flyttes til RAM og CPU. Langsomt, men bedre end ingenting.

📎 **Illustration:** `modul8-ill3-hardware-krav.png`
*Tre niveauer: minimum (CPU-only), anbefalet (8GB VRAM), komfortabelt (16GB VRAM) — med model-størrelser og hastigheder*

---

### Fordele ved lokal AI

Alt dette opsummerer hvorfor lokale interfaces er værd at sætte op:

- **Privacy** — ingen beskeder forlader din maskine, ingen logging, ingen brug til træning
- **Offline** — virker uden internet, i tog, på hytten, på skolens netværk
- **Ingen løbende omkostninger** — download én gang, kør for evigt
- **Fuld kontrol** — vælg selv model, version og indstillinger
- **Ingen censur** — open source modeller er typisk mindre begrænsede end cloud-modeller

Ulempen er stadig hardware-kravet og initial opsætning. Men når det kører, er det en kraftfuld og privat AI-arbejdsplads.

📎 **Illustration:** `modul8-ill4-lokal-vs-cloud-fordele.png`
*To kolonner: lokal AI (grøn) vs cloud AI (blå) — fordele og ulemper for begge*

## Modul 9: GitHub Copilot — AI i din editor

> **Målgruppe:** 10–15 år · Kender VS Code · Har skrevet Python eller andet kode
> **Illustration-filer:** modul9-ill1 til modul9-ill4 (PNG)

---

### Hvad er GitHub Copilot?

Forestil dig at have en meget erfaren programmør siddende ved siden af dig mens du koder — en der kender alle sprog, har læst millioner af kode-eksempler og altid er klar til at foreslå næste linje. Det er præcis hvad **GitHub Copilot** er.

Copilot er en AI-assistent der er bygget direkte ind i din kodeeditor. Den kigger på hvad du skriver og foreslår kode i realtid — hele funktioner, loops, fejlhåndtering — baseret på konteksten i din fil og dine kommentarer.

Den er udviklet af GitHub (ejet af Microsoft) og bruger OpenAI's modeller i baggrunden. Det er den mest udbredte AI-coding-assistent i verden med over 1 million aktive brugere.

> 💬 **Ordforklaring:** *Editor* er det program du skriver kode i — VS Code, PyCharm, Vim osv. *Extension* er et tilføjelsesprogram der udvider editorens funktioner.

📎 **Illustration:** `modul9-ill1-copilot-i-vscode.png`
*VS Code med Copilot aktiv — autocomplete-forslag vist som nedtonet tekst, chat-panel i sidebar*

---

### Installation i VS Code

1. Åbn VS Code
2. Gå til Extensions (Ctrl+Shift+X)
3. Søg efter "GitHub Copilot" og installer
4. Log ind med din GitHub-konto
5. Acceptér Copilot-licensen

**Pris og studerende:**
Copilot koster normalt ~$10/md. Men hvis du er studerende med en `.edu`-mailadresse eller aktivt bidragyder til open source, kan du få det **gratis** via GitHub Education. Det er værd at tjekke.

Der er også et gratis tier med begrænsede completions per måned — nok til at komme i gang.

---

### Autocomplete — kodeforslag mens du skriver

Det mest basale — og mest brugte — feature er **autocomplete**. Mens du skriver, vises Copilots forslag som nedtonet grå tekst:

- **Tab** — acceptér forslaget
- **Esc** — afvis forslaget
- **Alt+]** — se næste alternative forslag

Copilot er særligt god til:
- Boilerplate-kode du altid skriver på samme måde
- At fortsætte et mønster du har påbegyndt
- At skrive kode ud fra en kommentar der beskriver hvad du vil

```python
# Funktion der beregner gennemsnittet af en liste tal
# Copilot foreslår resten automatisk:
def beregn_gennemsnit(tal: list) -> float:
    if not tal:
        return 0.0
    return sum(tal) / len(tal)
```

Jo mere kontekst der er i filen (variabelnavne, kommentarer, eksisterende funktioner), jo bedre bliver forslagene.

📎 **Illustration:** `modul9-ill2-autocomplete-eksempel.png`
*Kode-editor med Copilot-forslag vist som nedtonet tekst — Tab/Esc/Alt-pil forklaret*

---

### Copilot Chat — stil spørgsmål om din kode

Ud over autocomplete har Copilot et **chat-panel** i VS Code's sidebar. Her kan du stille spørgsmål på naturligt sprog om din kode:

- *"Hvad gør denne funktion?"*
- *"Fiks denne fejl for mig"*
- *"Skriv en test til denne klasse"*
- *"Forklar hvad en rekursiv funktion er"*

Copilot Chat forstår hele filen du har åben som kontekst — du behøver ikke kopiere koden ind, det ved det allerede.

Brug `@workspace` for at give Copilot adgang til hele dit projekt på tværs af filer: *"@workspace find alle steder der kalder denne funktion"*.

---

### Inline edits — ret kode direkte

Markér et stykke kode og tryk **Ctrl+I** (eller Cmd+I på Mac) for at åbne inline-editoren. Beskriv hvad du vil lave om:

- *"Gør denne funktion mere effektiv"*
- *"Tilføj fejlhåndtering"*
- *"Oversæt kommentarerne til engelsk"*

Copilot viser forslaget som en **diff** — ændringer markeret med grønt (tilføjet) og rødt (fjernet) — inden du accepterer. Du er altid den der beslutter om ændringen gennemføres.

---

### Copilot vs. manuel kodning

Copilot er et kraftfuldt værktøj, men det er vigtigt at forstå hvad det er:

**Copilot er en co-pilot — ikke en pilot.** Du bestemmer retningen. Copilot hjælper med at skrive hurtigere.

**✅ Copilot vinder til:**
- Gentagne mønstre og boilerplate
- Kendte biblioteker og standard-operationer
- Hurtig prototyping

**⚠️ Vær forsigtig med:**
- Forslag du ikke forstår — acceptér aldrig blind kode
- Sikkerhedskritisk kode — tjek altid selv
- Copilot kan foreslå forældet eller forkert kode

Tommelfingerreglen: **forstå koden inden du accepterer den.** Copilot skal gøre dig hurtigere, ikke erstatte din forståelse.

> 💬 **Ordforklaring:** *Boilerplate* er den gentagne standardkode du skriver på samme måde gang på gang — fx fil-åbning, fejlhåndtering, class-definitioner. *Diff* er en visning der viser præcis hvad der er ændret mellem to versioner.

📎 **Illustration:** `modul9-ill3-copilot-workflow.png`
*Workflow: skriv kommentar → Copilot foreslår → gennemgå → acceptér/afvis — med Tab og Esc markeret*

---

### Pris og licens

| Plan | Pris | Inkluderer |
|------|------|----------|
| Gratis | $0 | Begrænsede completions og chat per måned |
| Individual | ~$10/md | Ubegrænset completions og chat |
| Business | ~$19/bruger/md | Team-features, policy-kontrol |
| Studerende | Gratis | Via GitHub Education — tjek om du er berettiget |

For de fleste unge og studerende er det gratis tier eller GitHub Education den rigtige indgang.

📎 **Illustration:** `modul9-ill4-pris-oversigt.png`
*Tre plan-kort: Gratis, Individual, Studerende — med hvad hvert indeholder*

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
*Terminal med OpenCode: naturligt sprog ind → filer læses → kodeændringer foreslås → godkend/afvis*

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
*Terminal-session: instruktion → fil-scanning → diff-visning → godkend/afvis*

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
*To stier: cloud (hurtig, koster penge, data ud) vs lokal (langsom, gratis, privat) med use cases for hver*

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

## Modul 11: Pi Agent — letvægts AI coding agent

> **Målgruppe:** 10–15 år · Kender terminalen · Har prøvet OpenCode eller Copilot
> **Illustration-filer:** modul11-ill1 til modul11-ill2 (PNG)

---

### Hvad er Pi Agent?

**Pi Agent** er det samme program du bruger til at læse og arbejde med dette site. Det er en open source AI coding agent der kører i terminalen og kan læse filer, skrive kode og udføre kommandoer — styret af dine instruktioner på naturligt sprog.

Ligesom OpenCode ser Pi Agent på hele dit projekt. Forskellen er at Pi Agent er designet til at være **letvægts og hurtig** — færre afhængigheder, enklere opsætning, og godt egnet til lokale modeller.

> 💬 **Ordforklaring:** *Letvægts* betyder at programmet er lille, hurtigt og kræver få ressourcer. *Afhængigheder* er andre programmer og biblioteker som et program kræver for at køre.

📎 **Illustration:** `modul11-ill1-pi-agent-oversigt.png`
*Pi Agent i terminal: læser filer, skriver kode, kører kommandoer — bruger godkender hvert trin*

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
*Tre kort: Pi Agent, OpenCode, Claude Code — nøgleforskelle og hvornår du vælger hvert*

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

## Modul 12: Vælg den rigtige model til opgaven

> **Målgruppe:** 10–15 år · Har prøvet flere AI-modeller
> **Illustration-filer:** modul12-ill1 til modul12-ill4 (PNG)

---

### Ikke alle modeller er ens

Du har nu mødt mange AI-modeller: GPT-4o, Claude, Llama, Qwen, Mistral, DeepSeek. De er alle LLM'er, men de er ikke ens gode til alle opgaver. Ligesom en hammer og en skruetrækker begge er værktøjer, men ikke udskiftelige — er det med AI-modeller.

I dette modul gennemgår vi hvilke modeller der er stærkest til hvilke opgaver, og giver dig en praktisk guide til at vælge.

📎 **Illustration:** `modul12-ill1-model-landskab.png`
*Oversigt over alle modeller fordelt på cloud/lokal og størrelse — visuelt landskab*

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
*Søjlediagram: top 6 modeller på tværs af 3 benchmarks (kodning, reasoning, generel viden)*

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
*Flowdiagram: opgave → spørgsmål → modelvalg — trin-for-trin beslutningsguide*

📎 **Illustration:** `modul12-ill4-model-sammenligning-tabel.png`
*Komplet sammenligningstabel: alle modeller, cloud/lokal, stærke sider, pris, context window*
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
