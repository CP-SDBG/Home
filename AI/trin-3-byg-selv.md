# Trin 3: Byg selv

## Modul 13: Byg med AI — vibe coding

> **Målgruppe:** 10–15 år · Let computer science baggrund · Har prøvet at skrive Python
> **Illustration-filer:** modul13-ill1 til modul13-ill3 (PNG)

---

### Hvad er vibe coding?

I januar 2025 opfandt AI-forskeren **Andrej Karpathy** begrebet *vibe coding* — og det beskriver en ny måde at bygge software på der er fundamentalt anderledes end klassisk programmering.

**Klassisk programmering:** du tænker på *hvordan* koden skal virke, skriver den linje for linje, og forstår hvert trin. Det kræver typisk måneder til år at lære ordentligt.

**Vibe coding:** du beskriver *hvad* du vil have, AI'en skriver koden, og du godkender og tester. Du er arkitekten — AI'en er bygmesteren.

Det åbner programmering for en helt ny gruppe mennesker. Med vibe coding kan du bygge ting som:
- En quiz-side om dit yndlingsemne
- Et simpelt spil (gæt et tal, ord-gætter, reaktions-spil)
- En lommeregner eller konverter (km til miles, celsius til fahrenheit)
- En hjemmeside til et projekt eller en klub
- Et lille Python-script der sorterer filer eller sender påmindelser

Du behøver ikke forstå hver linje — men du skal forstå *hvad* du vil have, og du skal kunne teste om det virker.

> 💬 **Ordforklaring:** *Vibe coding* er AI-assisteret kodning hvor du beskriver hvad du vil opnå frem for at skrive koden selv. *MVP* (Minimum Viable Product) er den mindste version af dit program der faktisk virker — ingen ekstra features, bare kernen.

📎 **Illustration:** `modul13-ill1-vibe-coding-tankegang.png`
*En færdig vejr-app i midten. To tankebobler fører hen til den: venstre = kode-syntax og tekniske begreber (klassisk), højre = naturligt sprog og resultatbeskrivelse (vibe coding). Under: "du bestemmer hvad — AI bygger hvordan".*

---

### Tankegang: beskriv hvad, ikke hvordan

Det vigtigste skift er at tænke i *resultater* frem for *implementering*.

**Klassisk tankegang:** *"Jeg skal skrive en fetch-funktion der kalder et vejr-API og parser JSON-svaret til et objekt..."*

**Vibe coding tankegang:** *"Lav en webside der viser det aktuelle vejr for en by jeg skriver ind — med temperatur og et vejr-ikon."*

Begge fører til den samme kode. Forskellen er hvad du tænker på mens du formulerer opgaven.

Beskriv slutresultatet præcist ved at svare på:
- **Hvad skal brugeren kunne gøre?** — skrive ind, klikke, vælge, se?
- **Hvad skal vises på skærmen?** — tal, tekst, billeder, knapper?
- **Hvad sker der ved klik?** — ny side, opdatering, fejlbesked?
- **Hvilke begrænsninger er der?** — ingen login, kun dansk, virke på mobil?

Jo mere konkret du beskriver slutresultatet, jo bedre kode får du tilbage.

---

### Vælg dit vibe coding-miljø

Vibe coding kan foregå på tre måder — vælg ud fra hvad du er komfortabel med:

| Miljø | Hvordan | Bedst til |
|-------|---------|-----------|
| ☁️ Web chat (Claude.ai, ChatGPT) | Kopiér kode frem og tilbage manuelt | Begyndere, korte projekter |
| 🤖 Coding agent (OpenCode, Pi Agent) | Agenten læser og redigerer dine filer direkte | Projekter med flere filer |
| ✍️ Editor plugin (GitHub Copilot) | Kodeforslag mens du skriver | Når du vil lære kode sideløbende |

Start med web chat — det kræver ingen opsætning. Når du bygger projekter med mere end to-tre filer, er en coding agent (Modul 10–11) langt hurtigere.

> 🔗 **Forbindelser:** GitHub Copilot → Modul 9. OpenCode → Modul 10. Pi Agent → Modul 11.

---

### Prompt engineering til kodning

Et godt prompt er halvdelen af arbejdet:

| ✅ Gør dette | ❌ Undgå dette |
|-------------|---------------|
| "Brug HTML, CSS og vanilla JavaScript — ingen frameworks" | "Lav en hjemmeside" (for vagt) |
| "Brugeren skriver en by — siden viser temperatur og et ikon" | "Lav noget med vejr og AI og også et kort" (for meget) |
| "Start med ét spørgsmål og to svarmuligheder" | "Byg et fuldt quiz-spil med highscore, timer og 50 spørgsmål" |
| "Ingen eksterne biblioteker, skal virke i Chrome" | "Brug de bedste biblioteker" (uklart) |

**Tommelfingerregel:** hvis du kan teste om resultatet er rigtigt på under et minut, er prompten præcis nok.

> 💬 **Ordforklaring:** *Prompt engineering* er kunsten at formulere gode instruktioner til en AI-model. *Tech stack* er de teknologier du bruger i et projekt. *Vanilla JavaScript* betyder JavaScript uden ekstra biblioteker.

---

### Den iterative arbejdsproces

Den mest effektive metode er at bygge i meget små skridt — og teste efter hvert skridt:

1. **Start med MVP** — mindste fungerende version. Ingen styling, ingen ekstra features.
   → *"Lav en HTML-side med ét quiz-spørgsmål og to svarmuligheder"*
2. **Test straks** — åbn i browser, klik på alt. Gem en kopi af den fungerende version.
3. **Tilføj én ting** — én feature, ikke fem.
   → *"Tilføj en score-tæller der viser X af Y rigtige svar"*
4. **Test igen** — virker den nye feature? Virker resten stadig?
5. **Gentag** — styling, flere spørgsmål, afslutningsbesked, lyd...

**Gem arbejdende versioner undervejs.** Kald dem `quiz-v1.html`, `quiz-v2.html` osv. Hvis noget går galt i v4, kan du altid vende tilbage til v3.

Undgå at bede om alt på én gang. En lang kompleks prompt giver ofte rodet kode der er svær at rette efterfølgende.

📎 **Illustration:** `modul13-ill2-iterativ-tilgang.png`
*Filmstrimmel med 4 frames: blank HTML → grim men fungerende quiz → quiz med score → styled quiz → færdig quiz med afslutningsbesked. Gem-notationer under hvert trin.*

---

### Fejlhåndtering med AI

Du *vil* få fejl. Det er en del af processen — ikke et tegn på at noget er galt.

**Vigtigste regel:** kopiér hele fejlbeskeden fra terminalen eller browserkonsollen og indsæt den direkte i chatten — aldrig omformuler den med dine egne ord.

Tilføj kontekst om hvad du lavede da fejlen opstod:
```
Denne fejl opstår når jeg klikker på 'Start quiz'-knappen:

TypeError: Cannot read properties of undefined (reading 'length')
    at startQuiz (quiz.js:23:30)
    at HTMLButtonElement.onclick (quiz.html:15)
```

En fejlbesked som denne fortæller AI'en: **hvad** gik galt (TypeError), **hvor** (quiz.js linje 23), **hvornår** (ved klik på knap).

AI'en er særligt god til:
- Stack traces — fejlbeskeder med filnavne og linjenumre
- Syntaksfejl — forkert placeret parentes, manglende kolon
- TypeError og NameError i Python
- Konsolfejl i JavaScript (åbn med F12 i browser)

Hvis AI'en ikke kan løse det efter 2–3 forsøg: start en ny samtale fra bunden, prøv en anden model, eller gå tilbage til seneste fungerende version.

📎 **Illustration:** `modul13-ill3-fejlhaandtering.png`
*To chat-vinduer side om side. Venstre (dårlig): "det virker ikke" → AI beder om mere info → spildt udveksling. Højre (god): fuld stack trace annoteret med pile der viser hvad = TypeError, hvor = quiz.js linje 23, hvornår = knapklik. Under: "F12 → Console → kopiér alt".*

---

### Forstå koden du får

Du behøver ikke kunne skrive koden — men det er værd at forstå *hvad den gør*. Brug AI'en til at forklare den for dig:
- *"Forklar hvad denne funktion gør linje for linje"*
- *"Hvad sker der hvis jeg ændrer tallet 5 til 10 på linje 12?"*
- *"Hvilken del af koden håndterer brugerens klik?"*

Det giver dig to fordele: du kan træffe bedre beslutninger om hvad du vil ændre, og du opdager hurtigere hvis AI'en laver en fejl.

> ⚠️ **Vigtigt:** Kopiér aldrig kode til et system der håndterer persondata, login eller penge — uden at forstå hvad den gør.

---

### Begrænsninger — hvornår slår vibe coding fejl?

- **Kompleks forretningslogik** med mange edge cases — AI'en overser nemt specielle tilfælde
- **Systemer der kræver dyb domæneforståelse** — fx medicinsk software eller finansielle beregninger
- **Sikkerhedskritiske systemer** — autentificering, kryptering, betalinger
- **Store eksisterende codebases** — AI'en kender ikke konteksten og historikken
- **Langsigtede projekter** — AI-genereret kode kan blive rodet og svær at vedligeholde

Den største faldgrube: du forstår ikke koden du har fået. Vibe coding er et godt udgangspunkt, ikke en erstatning for grundlæggende forståelse.

---

### Praktisk eksempel: byg en quiz-side fra bunden

Konkret forløb der typisk tager 20–30 minutter:

1. **Prompt 1 — MVP:** *"Lav en HTML-fil med en quiz om danske byer. Vis ét spørgsmål ad gangen med 4 svarmuligheder som knapper. Vis om svaret var rigtigt eller forkert."*
   → Åbn filen, klik igennem alle spørgsmål
2. **Gem v1** — kopier filen som `quiz-v1.html`
3. **Prompt 2 — score:** *"Tilføj en score-tæller øverst der viser 'X af Y rigtige'. Nulstil scoren når quizzen startes forfra."*
   → Test at score tæller korrekt op og nulstiller
4. **Prompt 3 — styling:** *"Giv siden en mørk baggrund (#121212), hvid tekst, og grønne knapper (#00e5a0). Centrér alt og gør det pænt på mobil."*
   → Test på mobil (åbn Chrome devtools → mobilvisning)
5. **Prompt 4 — indhold:** *"Tilføj 10 spørgsmål mere og vis en afslutningsbesked med den samlede score og en 'Prøv igen'-knap."*

Slutresultat: et kørende quiz-program bygget uden at skrive en linje kode selv — men testet og godkendt ved hvert trin.

## Modul 14: AI som co-pilot — API i din workflow

> **Målgruppe:** 10–15 år · Kender Python-grundlag · Har brugt terminal
> **Illustration-filer:** modul14-ill1 til modul14-ill3 (PNG)

---

### Hvad er en API?

**API** står for *Application Programming Interface* — og det er grundlaget for at få AI ind i dine egne programmer.

Tænk på det som en restaurant med et drive-through vindue. Du (dit program) kører op til vinduet, bestiller (sender en forespørgsel), og får maden (svaret) tilbage. Du ved ikke hvad der sker i køkkenet — du behøver bare at kende menuen og formatet.

En LLM-API fungerer præcis sådan: du sender en tekstbesked (**HTTP-request**), modellen behandler den på udbyderens servere, og du får tekst tilbage (**HTTP-response**). Det hele sker via REST API over HTTP — den samme protokol din browser bruger til at hente hjemmesider.

> 💬 **Ordforklaring:** *API* er et sæt regler for hvordan to programmer kommunikerer. *REST API* er en bestemt stil for HTTP-baserede API'er. *HTTP-request* er en besked sendt over internettet — som at spørge en server om noget.

📎 **Illustration:** `modul14-ill1-api-hvad-er-det.png`
**Titel:** To veje ind i køkkenet
*Split-screen: venstre viser manuel brug af claude.ai i browser, højre viser Python-fil med `client.messages.create(...)`. Begge peger på samme AI-sky i midten — visualisér kontrasten: to veje, samme model.*

---

### API-nøgler — sikkerhed er vigtigt

For at bruge en cloud LLM-API skal du bruge en **API-nøgle** — et langt unikt token der identificerer dig og dit forbrug. Hvis nogen får din nøgle, kan de bruge den i dit navn og koste dig penge.

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

> 💬 **Ordforklaring:** *API-nøgle* er et hemmeligt token der identificerer dig som bruger af en API. *.env-fil* er en fil der gemmer miljøvariabler lokalt — aldrig commit den til git. *Miljøvariabel* er en variabel der er tilgængelig for alle programmer på dit system.

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

> 🔗 **Husk fra Modul 13:** Du kan vibe-code hele dette program — beskriv hvad du vil bygge til AI'en og lad den generere kode-skelettet. Skriv derefter dine egne API-kald ind.

---

### System-prompts og roller

En **system-prompt** sættes én gang og gælder for hele samtalen. Uden system-prompt er AI'en generalist — med system-prompt er den specialist der opfører sig konsistent og forudsigeligt.

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
| „Du er en hjælper“ | „Du er en dansk fysik-lærer for 12-årige der forklarer med hverdagseksempler“ |
| Ingen format-krav | „Svar altid i 3 punkter, max 2 sætninger per punkt“ |
| „Svar på alt“ | „Svar kun på spørgsmål om matematik — afvis andet venligt“ |
| Lang, rodet prompt uden struktur | Rolle → Format → Begrænsninger — i den rækkefølge |

En god system-prompt giver konsistente og forudsigelige svar — det er grundlaget for en *skill* (Modul 18).

---

### Konversationshistorik

LLM'er er **statsløse** — de husker ingenting mellem kald. Vil du have en rigtig samtale, skal du sende hele historikken med hver gang:

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

Jo længere samtalen bliver, jo flere tokens bruges per kald — og jo dyrere bliver det. Ved meget lange samtaler kan du trunkere de ældste beskeder og beholde kun de seneste.

📎 **Illustration:** `modul14-ill3-konversationshistorik.png`
**Titel:** Den voksende pakke
*Tre HTTP-kald som pakker: kald 1 (1 besked), kald 2 (3 beskeder), kald 3 (5 beskeder). Pakkestørrelse og token-tæller vokser visuelt. Konkretisér konsekvensen: større historik = flere tokens = højere pris.*

---

### Token-forbrug og priser

Cloud LLM-API'er koster penge baseret på **tokens** — ikke tegn eller ord, men de brudstykker sproget opdeles i indeni modellen. „Hej verden“ er ~3 tokens. En hel roman er ~200.000 tokens.

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

Sæt altid et realistisk `max_tokens` — det sætter et loft for output og forhindrer overraskende store regninger.

> 💡 **Tip:** Start altid med Ollama lokalt under udvikling. Skift til cloud-API når du er klar til at deploye — det sparer penge og giver hurtigere feedback-loops.

---

### Fejlhåndtering og rate limits

Cloud-API'er kan fejle — for mange kald på kort tid giver fejlkode 429 (rate limit). Byg altid **exponential backoff** ind:

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
            print(f"Rate limit — venter {vent}s...")
            time.sleep(vent)
        except APIConnectionError as e:
            print(f"Forbindelsesfejl: {e}")
            break
    return None
```

| Fejlkode | Årsag | Løsning |
|----------|-------|----------|
| 429 | Rate limit nået | Exponential backoff (se kode ovenfor) |
| 401 | Ugyldig API-nøgle | Tjek .env — er variabelnavnet korrekt? |
| 500 | Server-fejl hos udbyderen | Prøv igen om lidt — ikke din fejl |

---

### Lokalt alternativ: Ollama API

Ollama eksponerer samme API-format som OpenAI — du kan bruge OpenAI-biblioteket til at tale med Ollama:

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

Ingen API-nøgle, ingen token-pris, kører offline. Skift fra Ollama til cloud-API ved blot at ændre `base_url` og `api_key` — resten af koden er identisk.

> 🔗 **Husk fra Modul 7:** Ollama kører på `localhost:11434` og starter automatisk som baggrundstjeneste. Kør `ollama list` for at se dine installerede modeller.

---

### Praktisk eksempel: lav en historiefortæller

Vi bygger et program der genererer korte historier baseret på brugerens input — kombinerer system-prompt, konversationshistorik og token-tracking i ét samlet program.

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

**2. Definer system-prompten — specialist, ikke generalist:**
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

**4. Test og iterér — justér system-prompten efter hvert forsøg:**
```python
# Start historien
print(fortæl_videre("Start en historie om en robot der finder en gammel nøgle"))

# Fortsæt historien med brugerens valg
print(fortæl_videre("Robotten åbner en hemmelig dør — hvad sker der?"))

# Prøv en anden genre: skift SYSTEM til sci-fi, detektiv eller eventyr
# Sammenlign output — system-prompten er den stærkeste kontrol du har
```

Næste skridt: gem historierne til en fil (`open("historier.txt", "a")`), tilføj en brugergrænseflade med `input()`, eller skift model fra Haiku til Sonnet og sammenlign kvaliteten.

## Modul 15: AI i dine egne programmer — Python + LLM API

> **Målgruppe:** 10–15 år · Kender Python · Har fulgt Modul 14
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

Du behøver ikke bygge en ny AI til hvert problem. Én genanvendelig funktion er nok — opgaven defineres i prompten.

> 💬 **Ordforklaring:** *Funktion* er et genanvendeligt stykke kode der tager input og giver output. Når vi wrapper et AI-kald i en funktion, bliver LLM'en en byggeklods på linje med al anden Python-kode.

📎 **Illustration:** `modul15-ill1-ai-som-funktion.png`
**Titel:** Én funktion, uendelige muligheder
*`spørg_ai()` i centrum med 4 pile ud til 4 forskellige apps: grundstof-gætter, chatbot, quiz-generator, sentiment-analysator. Viser COMPOSABILITY — ikke flowdiagram.*

---

### Lokal eller cloud? Vælg din tilgang

Du har to måder at kalde en LLM fra Python. Valget påvirker pris, hastighed og hvad du kan i praksis:

| Egenskab | Ollama (lokal) | Cloud-API (Anthropic/OpenAI) |
|----------|---------------|-----------------------------|
| Pris | Gratis | Betalt per token |
| Internet | Ikke nødvendigt | Kræves |
| Modelkvalitet | God (7b–14b parametre) | State-of-the-art |
| Setup | `pip install ollama` | `pip install anthropic` + API-nøgle |
| Bedst til | Udvikling og test | Produktion og krævende opgaver |

Strategien: **byg med Ollama, deploy med cloud-API**. Koden er næsten identisk — du skifter blot bibliotek og model-navn når du er klar.

> 🔗 **Husk fra Modul 14:** Cloud-API'er bruger tokens — under udvikling med hundredvis af test-kald løber det hurtigt op. Ollama er gratis.

---

### Byg en genanvendelig AI-funktion

Wrap dit API-kald i en funktion én gang — brug den overalt i dit program:

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

Vil du skifte til cloud-API? Skift implementationen indeni — resten af koden røres ikke:

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

### Strukturer prompts — do/don't

Kvaliteten af AI's output afhænger næsten udelukkende af promptens kvalitet:

| ❌ Undgå | ✅ Gør i stedet |
|---------|---------------|
| `f"Er {by} en dansk by?"` | `f"Svar KUN med ja eller nej. Er '{by}' en dansk by?"` |
| Lang tekst uden kontekst | Rolle først: `"Du er en [ekspert]. [opgave]."` |
| Ingen eksempler på format | Few-shot: vis 2–3 eksempler på hvad du forventer |
| "Opsummer det her" | "Opsummer i præcis 3 punkter, max 15 ord per punkt" |

**Few-shot eksempel — vis AI'en hvad du vil have:**
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

Vil du bruge AI's svar som data i dit program — ikke bare printe det — skal du bede om **JSON-format** og parse svaret:

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

> 💬 **Ordforklaring:** *Parsing* er at omforme tekst til et brugbart dataformat. *JSON* er et tekstformat til strukturerede data — Python konverterer det til en `dict` med `json.loads()`.

---

### Fejlhåndtering — hvad når AI'en ikke svarer?

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

En chatbot der husker hele samtalen — og har en persona via system-prompt:

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
*Tag grundstof-gætter-prompten og annotér dens dele med pile: [rolle: kemi-ekspert] → [kontekst: elevens beskrivelse] → [instruktion: gæt] → [outputformat: navn + symbol + sætning]. Viser HVORFOR prompten virker — ikke hvad den siger.*

---

### Hvad kan du bygge herfra?

Du har nu alle byggeklodser: en genanvendelig AI-funktion, strukturerede prompts og fejlhåndtering. Kombiner dem:

| Program | Prompt-tilgang | Output-type |
|---------|---------------|-------------|
| Lektiejælper | System-prompt: tålmodig tutor | Tekst |
| Tekst-opsummerer | Few-shot: eksempel på godt resumé | Tekst |
| Sentiment-analysator | Svar KUN med JSON | JSON → dict |
| Quiz-generator | Format: nøjagtigt 5 spørgsmål med svar | Struktureret tekst |

> 🔗 **Kommer i Modul 16:** RAG — giv din AI adgang til dine egne dokumenter og noter, så den kan svare baseret på specifik viden du har givet den.

## Modul 16: RAG — giv AI adgang til din egen viden

> **Målgruppe:** 10–15 år · Kender Python og LLM-kald · Har fulgt Modul 15
> **Illustration-filer:** modul16-ill1 til modul16-ill3 (PNG)

---

### Hvad er RAG?

**RAG** står for *Retrieval-Augmented Generation* — og det løser et af AI's største problemer: modellen kender kun det den er trænet på. Den kender ikke dine noter, din skoles regler eller gårsdagens nyheder.

Med RAG giver du AI'en adgang til et "bibliotek" af dine egne dokumenter. Når du stiller et spørgsmål, finder systemet først de relevante dokumentstykker og lægger dem ind i prompten — så AI'en svarer baseret på din faktiske viden, ikke bare sin træning.

**RAG løser tre problemer på én gang:** hallucination (AI'en ser de rigtige fakta), forældet viden (du kan give de nyeste dokumenter), og specifik viden (din AI kender dine interne dokumenter).

> 💬 **Ordforklaring:** *RAG* kombinerer søgning i et dokumentarkiv med AI-generering. *Retrieval* = hentning. *Augmented* = forbedret. *Generation* = AI's tekstgenerering. Det er ikke en model — det er en *arkitektur*.

📎 **Illustration:** `modul16-ill1-rag-pipeline.png`
**Titel:** Låsen der åbnes
*Samme spørgsmål, to versioner: UDEN RAG → AI hallucinerer et forkert svar. MED RAG → relevant chunk hentes, AI svarer korrekt fra dokumentet. Viser det KONKRETE PROBLEM RAG løser.*

---

### RAG vs. „bas bare al tekst ind i prompten“

Kan du ikke bare paste hele dit dokument ind i prompten? Teknisk ja — men det skalerer ikke:

| ❌ Al tekst i prompten | ✅ RAG |
|--------------------|-------|
| Max ~200.000 tokens — så er context-vinduet fyldt | Ubegrænset antal dokumenter i databasen |
| Koster mange tokens per kald — dyrt ved gentagne spørgsmål | Kun relevante chunks sendes — typisk 3–5 stykker |
| AI'en fortaber sig i lang tekst — kvaliteten falder | AI får præcis det relevante — koncentreret svar |
| Virker ikke med 1.000+ siders PDF-arkiv | Virker med millioner af dokumenter |

Tommelfingerregel: under 5 sider og ét enkelt dokument — paste det ind. Over det — brug RAG.

---

### Embeddings og semantisk søgning

RAG søger på *mening*, ikke nøgleord. Det sker via **embeddings** — hvert tekststykke omdannes til en lang liste tal der repræsenterer dets betydning:

```
# Keyword-søgning finder intet:
søg("bil")  →  ingen hits  # dokumentet siger "køretøj"

# Semantisk søgning finder det:
vektor_søg("bil")  →  "Et køretøj med fire hjul..."  # ens betydning
```

Dine dokumenter får hver sin embedding-vektor og gemmes i en **vektor-database**. Når du spørger, omdannes dit spørgsmål også til en vektor — databasen finder de dokumentstykker der er tættest på.

Populære vektor-databaser: **ChromaDB** (lokal, perfekt til begyndere), **Pinecone** (cloud, skalerbar), **Weaviate** (open source).

> 🔗 **Husk fra Modul 2:** Embeddings som koordinater på et betydningskort — ord med ens mening havner tæt på hinanden. RAG bruger præcis den mekanisme.

---

### Chunking — opdel dokumenter smart

Inden du kan søge i dine dokumenter, skal de opdeles i passende bidder — **chunks**. Typisk 200–500 ord med et overlap på 50–100 ord.

```python
def chunk_tekst(tekst: str, chunk_størrelse: int = 400, overlap: int = 50) -> list:
    ord = tekst.split()
    chunks = []
    i = 0
    while i < len(ord):
        chunk = " ".join(ord[i:i + chunk_størrelse])
        chunks.append(chunk)
        i += chunk_størrelse - overlap
    return chunks
```

| ❌ Dårlig chunking | ✅ God chunking |
|----------------|----------------|
| Hele dokumentet som ét chunk | 200–500 ord per chunk |
| Ingen overlap — grænse-information går tabt | 50–100 ords overlap mellem chunks |
| Sætninger klippes midt over | Klip ved naturlige grænser (afsnit, punktum) |

📎 **Illustration:** `modul16-ill2-chunking-overlap.png`
**Titel:** Nøglesætningen der går tabt
*Viser en tekst med en vigtig sætning der falder præcis på chunk-grænsen: UDEN overlap → sætningen splittes, begge chunks er ubrugelige. MED overlap → sætningen er hel i begge chunks. Viser PROBLEMET overlap løser.*

---

### RAG-pipeline: installér og opsæt

Du skal bruge to pakker:

```bash
pip install chromadb ollama
```

ChromaDB kan køre midlertidigt (nulstilles ved genstart) eller persistent på disk:

```python
import chromadb

# Midlertidigt (nulstilles ved genstart)
client = chromadb.Client()

# Persistent (gemmes på disk)
client = chromadb.PersistentClient(path="./min-rag-db")

# Opret eller hent samling
samling = client.get_or_create_collection("pensum-biologi")
```

---

### RAG i praksis med ChromaDB

Det fulde mønster: tilføj dokumenter én gang, søg og svar mange gange:

```python
import chromadb, ollama

client = chromadb.Client()
samling = client.create_collection("mine-noter")

# 1. Indlæs dokumenter (én gang)
samling.add(
    documents=[
        "Fotosyntese er den proces hvor planter omdanner sollys til sukker.",
        "Klorofyl er det grønne stof i planter der absorberer sollys.",
        "Planter frigiver oxygen som biprodukt af fotosyntese.",
    ],
    ids=["dok1", "dok2", "dok3"]
)

# 2. Søg og svar (gentages for hvert spørgsmål)
def rag_svar(spørgsmål: str, antal_resultater: int = 2) -> str:
    resultater = samling.query(query_texts=[spørgsmål], n_results=antal_resultater)
    kontekst = "\n".join(resultater["documents"][0])
    prompt = f"""Svar baseret KUN på denne kontekst. Siger konteksten ikke svaret, sig 'Det ved jeg ikke ud fra de givne dokumenter.'\n\nKontekst:\n{kontekst}\n\nSpørgsmål: {spørgsmål}"""
    svar = ollama.chat(model="qwen2.5:7b", messages=[{"role": "user", "content": prompt}])
    return svar["message"]["content"]

print(rag_svar("Hvad er klorofyl?"))
print(rag_svar("Hvad er Danmarks hovedstad?"))  # "Det ved jeg ikke..."
```

Bemærk instruksen *„Sig 'ved ikke' hvis ikke i konteksten“* — den er kritisk. Uden den gætter AI'en og hallucinerer.

---

### Søgekvalitet — hvad påvirker resultatet?

Tre parametre gør størst forskel:

| Parameter | Påvirker | Anbefaling |
|-----------|----------|------------|
| `n_results` | Antal chunks i kontekst | Start med 2–3. For mange = forvirret AI |
| Chunk-størrelse | Præcision vs. kontekst | 200–400 ord til fakta, 400–600 til analyse |
| Prompt-instruks | Om AI hallucinerer | Altid: „sig 'ved ikke' hvis ikke i kontekst“ |

Fejlfinding: får du dårlige svar? Print `resultater["documents"][0]` og se hvilke chunks der faktisk hentes. Henter den de forkerte — juster chunk-størrelse eller øg overlap.

📎 **Illustration:** `modul16-ill3-rag-use-cases.png`
**Titel:** Samme arkitektur, al fra 5 noter til 50.000 dokumenter
*Venstre: en elev med 5 noter → ChromaDB lokal → AI svarer. Højre: en virksomhed med 50.000 dokumenter → ChromaDB/Pinecone → AI svarer. Samme kode-mønster begge steder. Viser SKALERBARHEDEN, ikke use cases.*

---

### Praktisk eksempel: byg en pensum-assistent

Vi bygger et program der læser dine egne noter og svarer på spørgsmål om dem.

**1. Forbered noter som Python-liste:**
```python
noter = [
    "Andenskoloven: F = m * a. Kraft er lig masse gange acceleration.",
    "Newton's tredjelov: For enhver kraft er der en modsat og lige stor reaktionskraft.",
    "Energibevarelse: Energi kan ikke skabes eller forsvinde, kun omdannes.",
    "Kinetisk energi: Ek = 0.5 * m * v^2. Afhænger af masse og hastighed.",
    "Potentiel energi: Ep = m * g * h. Afhænger af højde og masse.",
]
```

**2. Indlæs i ChromaDB:**
```python
import chromadb
samling = chromadb.Client().create_collection("fysik-noter")
samling.add(documents=noter, ids=[f"note{i}" for i in range(len(noter))])
```

**3. Byg spørgsmåls-løkken:**
```python
import ollama

print("Pensum-assistent klar! (stop for at afslutte)\n")
while True:
    q = input("Spørgsmål: ")
    if q.lower() == "stop": break
    hits = samling.query(query_texts=[q], n_results=2)
    kontekst = "\n".join(hits["documents"][0])
    svar = ollama.chat(model="qwen2.5:7b", messages=[{"role": "user",
        "content": f"Baseret KUN på disse noter:\n{kontekst}\n\nSvar kort: {q}"}])
    print(f"\nSvar: {svar['message']['content']}\n")
```

**4. Udvid med dine egne noter:** skift listen ud med indhold fra dine undervisningsbøger. Jo flere og bedre noter, jo præcisere svar. Prøv at tilføje modstridende information og se om AI'en håndterer det korrekt.

## Modul 17: Agenter — autonome AI-workflows

> **Målgruppe:** 10–15 år · Har fulgt Modul 14–16 · Kender Python-funktioner
> **Illustration-filer:** modul17-ill1 til modul17-ill3 (PNG)

---

### Hvad er en AI-agent?

En **chatbot** svarer på ét spørgsmål ad gangen. Du spørger, den svarer, du beslutter hvad der sker hærnest.

En **AI-agent** er fundamentalt anderledes. Du giver den et *mål* — og den planlægger selv, kalder de nødvendige funktioner, evaluerer resultater og fortsætter uden at du behøver at styre hvert trin.

En agent kombinerer tre ting: **LLM** (reasoning), **tools** (handlinger i verden) og **hukommelse** (kontekst på tværs af trin).

> 💬 **Ordforklaring:** *Agent* er en AI der selvstændigt planlægger og udfører en sekvens af handlinger for at nå et mål. *Tools* er Python-funktioner agenten kan kalde. *Orchestration* er koordineringen af hvilke tools der kaldes hvornår.

📎 **Illustration:** `modul17-ill1-agent-vs-chatbot.png`
**Titel:** 12 manuelle trin vs. ét agent-kald
*Opgaven 'research 3 frameworks og gem fil' vist som manuel checkliste (12 bokse: åbn browser, søg, læs, noter, søg igen...) ved siden af agent-kaldet (1 linje kode). Gør MÆNGDEN AF ARBEJDE konkret — ikke et arkitekturdiagram.*

---

### Chatbot eller agent? Vælg rigtigt

| Brug chatbot når… | Brug agent når… |
|---------------------|------------------|
| Opgaven er ét trin: stil spørgsmål, få svar | Opgaven kræver flere trin og beslutninger |
| Alt information er allerede i prompten | AI skal hente information undervejs (søg, læs filer) |
| Output er ren tekst | Output inkluderer handlinger (gem fil, send besked) |
| Du ved præcis hvad der skal ske | Planen afhænger af hvad AI'en finder undervejs |

En agent er mere kompleks at bygge og fejlhåndtere end en chatbot. Brug den kun når opgaven faktisk kræver det.

---

### Tools — definer og implementér

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

📎 **Illustration:** `modul17-ill2-tools-function-calling.png`
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

📎 **Illustration:** `modul17-ill3-react-loop.png`
**Titel:** Agentens logbog
*Et konkret transcript fra en kørende agent: linje for linje — timestamp, THOUGHT: "...", ACTION: søg_web(...), OBSERVATION: "...", THOUGHT: "...", FINAL: "...". Som debugger-output. Gør DET ABSTRAKTE LØP konkret og læseligt.*

---

### Multi-step planlægning

Agenten behøver ikke en step-by-step plan fra dig. Giv den et mål — den nedbryder det selv:

```python
kør_agent("Lav en liste over de 5 største danske byer, søg befolkningstal for hver, og gem en sorteret tabel i byer.csv")
```

Agenten vil: søge efter listen, søge befolkningstal for hver by, formatere som CSV, gemme filen — alt koordineret af AI'ens reasoning. Jo bedre målet er beskrevet, jo bedre planlægger agenten. Vær specifik om *format* og *output* — ikke om *fremgangsmåden*.

---

### Hukommelse og tilstand i agenter

Agenten husker alle trin i `beskeder`-listen — hver tool-handling og dens resultat tilføjes:

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

Agenten gentager ikke de samme tool-kald fordi den kan se hvad den allerede har gjort. Men listen vokser — lange agenter bruger mange tokens. Sæt altid `max_trin` for at undgå ukontrollerede kørsler.

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

