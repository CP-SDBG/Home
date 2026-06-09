## Modul 13: Byg med AI - vibe coding

> **Målgruppe:** 10-15 år · Let computer science baggrund · Har prøvet at skrive Python
> **Illustration-filer:** modul13-ill1 til modul13-ill3 (PNG)

---

### Hvad er vibe coding?

I januar 2025 opfandt AI-forskeren **Andrej Karpathy** begrebet *vibe coding* - og det beskriver en ny måde at bygge software på der er fundamentalt anderledes end klassisk programmering.

**Klassisk programmering:** du tænker på *hvordan* koden skal virke, skriver den linje for linje, og forstår hvert trin. Det kræver typisk måneder til år at lære ordentligt.

**Vibe coding:** du beskriver *hvad* du vil have, AI'en skriver koden, og du godkender og tester. Du er arkitekten - AI'en er bygmesteren.

Det åbner programmering for en helt ny gruppe mennesker. Med vibe coding kan du bygge ting som:
- En quiz-side om dit yndlingsemne
- Et simpelt spil (gæt et tal, ord-gætter, reaktions-spil)
- En lommeregner eller konverter (km til miles, celsius til fahrenheit)
- En hjemmeside til et projekt eller en klub
- Et lille Python-script der sorterer filer eller sender påmindelser

Du behøver ikke forstå hver linje - men du skal forstå *hvad* du vil have, og du skal kunne teste om det virker.

> 💬 **Ordforklaring:** *Vibe coding* er AI-assisteret kodning hvor du beskriver hvad du vil opnå frem for at skrive koden selv. *MVP* (Minimum Viable Product) er den mindste version af dit program der faktisk virker - ingen ekstra features, bare kernen.

📎 **Illustration:** `modul13-ill1-vibe-coding-tankegang.png`
**Titel:** Samme mål — to helt forskellige tankegange
*En færdig vejr-app i midten. To tankebobler fører hen til den: venstre = kode-syntax og tekniske begreber (klassisk), højre = naturligt sprog og resultatbeskrivelse (vibe coding). Under: “du bestemmer hvad — AI bygger hvordan”.*

---

### Tankegang: beskriv hvad, ikke hvordan

Det vigtigste skift er at tænke i *resultater* frem for *implementering*.

**Klassisk tankegang:** *"Jeg skal skrive en fetch-funktion der kalder et vejr-API og parser JSON-svaret til et objekt..."*

**Vibe coding tankegang:** *"Lav en webside der viser det aktuelle vejr for en by jeg skriver ind - med temperatur og et vejr-ikon."*

Begge fører til den samme kode. Forskellen er hvad du tænker på mens du formulerer opgaven.

Beskriv slutresultatet præcist ved at svare på:
- **Hvad skal brugeren kunne gøre?** - skrive ind, klikke, vælge, se?
- **Hvad skal vises på skærmen?** - tal, tekst, billeder, knapper?
- **Hvad sker der ved klik?** - ny side, opdatering, fejlbesked?
- **Hvilke begrænsninger er der?** - ingen login, kun dansk, virke på mobil?

Jo mere konkret du beskriver slutresultatet, jo bedre kode får du tilbage.

---

### Vælg dit vibe coding-miljø

Vibe coding kan foregå på tre måder - vælg ud fra hvad du er komfortabel med:

| Miljø | Hvordan | Bedst til |
|-------|---------|-----------|
| ☁️ Web chat (Claude.ai, ChatGPT) | Kopiér kode frem og tilbage manuelt | Begyndere, korte projekter |
| 🤖 Coding agent (OpenCode, Pi Agent) | Agenten læser og redigerer dine filer direkte | Projekter med flere filer |
| ✍️ Editor plugin (GitHub Copilot) | Kodeforslag mens du skriver | Når du vil lære kode sideløbende |

Start med web chat - det kræver ingen opsætning. Når du bygger projekter med mere end to-tre filer, er en coding agent (Modul 10-11) langt hurtigere.

> 🔗 **Forbindelser:** GitHub Copilot → Modul 9. OpenCode → Modul 10. Pi Agent → Modul 11.

---

### Prompt engineering til kodning

Et godt prompt er halvdelen af arbejdet:

| ✅ Gør dette | ❌ Undgå dette |
|-------------|---------------|
| "Brug HTML, CSS og vanilla JavaScript - ingen frameworks" | "Lav en hjemmeside" (for vagt) |
| "Brugeren skriver en by - siden viser temperatur og et ikon" | "Lav noget med vejr og AI og også et kort" (for meget) |
| "Start med ét spørgsmål og to svarmuligheder" | "Byg et fuldt quiz-spil med highscore, timer og 50 spørgsmål" |
| "Ingen eksterne biblioteker, skal virke i Chrome" | "Brug de bedste biblioteker" (uklart) |

**Tommelfingerregel:** hvis du kan teste om resultatet er rigtigt på under et minut, er prompten præcis nok.

> 💬 **Ordforklaring:** *Prompt engineering* er kunsten at formulere gode instruktioner til en AI-model. *Tech stack* er de teknologier du bruger i et projekt. *Vanilla JavaScript* betyder JavaScript uden ekstra biblioteker.

---

### Den iterative arbejdsproces

Den mest effektive metode er at bygge i meget små skridt - og teste efter hvert skridt:

1. **Start med MVP** - mindste fungerende version. Ingen styling, ingen ekstra features.
   → *"Lav en HTML-side med ét quiz-spørgsmål og to svarmuligheder"*
2. **Test straks** - åbn i browser, klik på alt. Gem en kopi af den fungerende version.
3. **Tilføj én ting** - én feature, ikke fem.
   → *"Tilføj en score-tæller der viser X af Y rigtige svar"*
4. **Test igen** - virker den nye feature? Virker resten stadig?
5. **Gentag** - styling, flere spørgsmål, afslutningsbesked, lyd...

**Gem arbejdende versioner undervejs.** Kald dem `quiz-v1.html`, `quiz-v2.html` osv. Hvis noget går galt i v4, kan du altid vende tilbage til v3.

Undgå at bede om alt på én gang. En lang kompleks prompt giver ofte rodet kode der er svær at rette efterfølgende.

📎 **Illustration:** `modul13-ill2-iterativ-tilgang.png`
**Titel:** Fra blank side til færdig quiz — 4 prompts, 25 minutter
*Filmstrimmel med 4 frames: blank HTML → grim men fungerende quiz → quiz med score → styled quiz → færdig quiz med afslutningsbesked. Gem-notationer under hvert trin.*

---

### Fejlhåndtering med AI

Du *vil* få fejl. Det er en del af processen - ikke et tegn på at noget er galt.

**Vigtigste regel:** kopiér hele fejlbeskeden fra terminalen eller browserkonsollen og indsæt den direkte i chatten - aldrig omformuler den med dine egne ord.

Tilføj kontekst om hvad du lavede da fejlen opstod:
```
Denne fejl opstår når jeg klikker på 'Start quiz'-knappen:

TypeError: Cannot read properties of undefined (reading 'length')
    at startQuiz (quiz.js:23:30)
    at HTMLButtonElement.onclick (quiz.html:15)
```

En fejlbesked som denne fortæller AI'en: **hvad** gik galt (TypeError), **hvor** (quiz.js linje 23), **hvornår** (ved klik på knap).

AI'en er særligt god til:
- Stack traces - fejlbeskeder med filnavne og linjenumre
- Syntaksfejl - forkert placeret parentes, manglende kolon
- TypeError og NameError i Python
- Konsolfejl i JavaScript (åbn med F12 i browser)

Hvis AI'en ikke kan løse det efter 2-3 forsøg: start en ny samtale fra bunden, prøv en anden model, eller gå tilbage til seneste fungerende version.

📎 **Illustration:** `modul13-ill3-fejlhaandtering.png`
**Titel:** Anatomien af en god fejlrapport
*To chat-vinduer side om side. Venstre (dårlig): “det virker ikke” → AI beder om mere info → spildt udveksling. Højre (god): fuld stack trace annoteret med pile der viser hvad = TypeError, hvor = quiz.js linje 23, hvornår = knapklik. Under: “F12 → Console → kopiér alt”.*

---

### Forstå koden du får

Du behøver ikke kunne skrive koden - men det er værd at forstå *hvad den gør*. Brug AI'en til at forklare den for dig:
- *"Forklar hvad denne funktion gør linje for linje"*
- *"Hvad sker der hvis jeg ændrer tallet 5 til 10 på linje 12?"*
- *"Hvilken del af koden håndterer brugerens klik?"*

Det giver dig to fordele: du kan træffe bedre beslutninger om hvad du vil ændre, og du opdager hurtigere hvis AI'en laver en fejl.

> ⚠️ **Vigtigt:** Kopiér aldrig kode til et system der håndterer persondata, login eller penge - uden at forstå hvad den gør.

---

### Begrænsninger - hvornår slår vibe coding fejl?

- **Kompleks forretningslogik** med mange edge cases - AI'en overser nemt specielle tilfælde
- **Systemer der kræver dyb domæneforståelse** - fx medicinsk software eller finansielle beregninger
- **Sikkerhedskritiske systemer** - autentificering, kryptering, betalinger
- **Store eksisterende codebases** - AI'en kender ikke konteksten og historikken
- **Langsigtede projekter** - AI-genereret kode kan blive rodet og svær at vedligeholde

Den største faldgrube: du forstår ikke koden du har fået. Vibe coding er et godt udgangspunkt, ikke en erstatning for grundlæggende forståelse.

---

### Praktisk eksempel: byg en quiz-side fra bunden

Konkret forløb der typisk tager 20-30 minutter:

1. **Prompt 1 - MVP:** *"Lav en HTML-fil med en quiz om danske byer. Vis ét spørgsmål ad gangen med 4 svarmuligheder som knapper. Vis om svaret var rigtigt eller forkert."*
   → Åbn filen, klik igennem alle spørgsmål
2. **Gem v1** - kopier filen som `quiz-v1.html`
3. **Prompt 2 - score:** *"Tilføj en score-tæller øverst der viser 'X af Y rigtige'. Nulstil scoren når quizzen startes forfra."*
   → Test at score tæller korrekt op og nulstiller
4. **Prompt 3 - styling:** *"Giv siden en mørk baggrund (#121212), hvid tekst, og grønne knapper (#00e5a0). Centrér alt og gør det pænt på mobil."*
   → Test på mobil (åbn Chrome devtools → mobilvisning)
5. **Prompt 4 - indhold:** *"Tilføj 10 spørgsmål mere og vis en afslutningsbesked med den samlede score og en 'Prøv igen'-knap."*

Slutresultat: et kørende quiz-program bygget uden at skrive en linje kode selv - men testet og godkendt ved hvert trin.
