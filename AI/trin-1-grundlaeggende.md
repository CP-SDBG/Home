# Trin 1: Grundlæggende

## Modul 1: Introduktion til AI

> **Målgruppe:** 10–15 år · Let computer science baggrund · Kan skrive små Python-programmer
> **Illustration-filer:** modul1-ill1 til modul1-ill6 (SVG)

---

### Hvad betyder AI egentlig?

AI står for **Artificial Intelligence** — eller på dansk: **kunstig intelligens**.

Men hvad betyder det? Tænk på det sådan her: Normalt er det kun levende væsener der kan "tænke" — altså løse problemer, genkende ting og finde på nye idéer. AI er programmer der kan gøre noget der *ligner* tænkning — uden at de er levende.

Din lommeregner er ikke AI. Den kan kun gøre præcis hvad den fik at vide. Men hvis du viser et program tusindvis af billeder af katte, og det bagefter selv kan genkende en kat på et nyt billede — det er AI.

> 💬 **Ordforklaring:** *Intelligens* betyder evnen til at lære, forstå og løse problemer. *Kunstig* betyder at det er lavet af mennesker, ikke opstået naturligt.

📎 **Illustration:** `modul1-ill1-ai-vs-ikke-ai.svg`
*Sammenligning: lommeregner (ikke AI) vs. kamera der genkender en kat (AI)*

---

### Kort historie — fra de tidlige idéer til i dag

AI er ikke nyt. Mennesker har drømt om tænkende maskiner i årtier.

**1950'erne:** Forskere begyndte at spørge: *"Kan maskiner tænke?"* De prøvede at kode regler direkte ind — fx *"hvis X, så gør Y"*. Det virkede til simple opgaver men slog hurtigt fejl på det virkelige verdens kompleksitet.

**1997:** Deep Blue slog verdensmesteren i skak. Imponerende! Men det kunne kun spille skak.

**2012–2017:** Alt ændrede sig. Med mere data, hurtigere computere og en ny teknik kaldet *deep learning* begyndte AI at kunne gøre ting der tidligere virkede umulige — genkende tale, oversætte sprog, generere billeder. I 2017 opfandt Google **Transformer-arkitekturen** — grundlaget for al moderne AI.

**2022–nu:** Nu er vi her. AI kan skrive tekst, kode programmer, lave musik og føre en samtale der næsten lyder menneskelig.

📎 **Illustration:** `modul1-ill2-tidslinje.svg`
*Vandret tidslinje: 1950 → 1997 → 2012–2017 → 2022–nu*

---

### Hvad er machine learning?

Normalt når du programmerer, fortæller du computeren *præcis* hvad den skal gøre — trin for trin. Det kalder vi klassisk programmering.

**Machine learning er anderledes.** I stedet for at give computeren reglerne, giver du den masser af eksempler — og den finder selv mønstrene.

Forestil dig du skal lære en robot at genkende spam-mails. Du *kunne* skrive hundredvis af regler: "hvis mailen indeholder 'vind en iPhone' er det spam". Men spammerne ville bare ændre ordene.

Med machine learning viser du i stedet robotten 10.000 spam-mails og 10.000 normale mails — og den lærer selv hvad der adskiller dem. Det er meget mere fleksibelt.

> 💬 **Ordforklaring:** *Mønster* betyder en regelmæssighed der gentager sig. Computeren leder efter sådanne regelmæssigheder i data.

📎 **Illustration:** `modul1-ill3-programmering-vs-ml.svg`
*To parallelle flowdiagrammer: klassisk programmering vs. machine learning med spam-eksempel*

---

### Hvad er deep learning?

Deep learning er en speciel slags machine learning — og det er den der har gjort AI så kraftfuld de seneste år.

Idéen er inspireret af din hjerne. Din hjerne er bygget af milliarder af nerveceller (*neuroner*) der sender signaler til hinanden. Deep learning efterligner det med kunstige neuroner i et **neuralt netværk**.

Forestil dig et net af lag. Hvert lag kigger på noget mere komplekst end laget før:
- **Lag 1** genkender måske bare kanter og linjer i et billede
- **Lag 2** kombinerer dem til former
- **Lag 3** genkender øjne, næse, mund
- **Lag 4** konkluderer: *"det er et ansigt"*

Jo dybere netværket er (jo flere lag), jo mere komplekse ting kan det lære. Deraf navnet: *deep* learning.

> 💬 **Ordforklaring:** *Neuron* er en nervecelle i hjernen. *Kunstig neuron* er en matematisk funktion der efterligner hvordan en nervecelle virker.

📎 **Illustration:** `modul1-ill4-neuralt-netvaerk.svg`
*Neuralt netværk med input-lag, skjulte lag og output-lag — pixels til "ansigt / ikke ansigt"*

---

### Hvorfor er AI blevet så populært nu?

AI har eksisteret i årtier — så hvorfor eksploderede det først nu?

Svaret er tre ting der skete på samme tid:

**1. Mere data**
Internettet har givet os ufattelige mængder data — tekster, billeder, videoer. AI lærer af data, så mere data = smartere AI.

**2. Hurtigere hardware**
Grafikkort (GPU'er) — de samme chips der bruges til computerspil — viste sig at være perfekte til at træne AI. De kan lave millioner af beregninger på samme tid.

**3. Bedre algoritmer**
Især én opfindelse ændrede alt: **Transformer-arkitekturen** fra 2017. Den er grundlaget for ChatGPT, Claude og næsten alle moderne AI-sprogmodeller. (Vi kigger nærmere på den i Modul 2.)

> 💬 **Ordforklaring:** *GPU* står for Graphics Processing Unit — et grafikkort. *Algoritme* er en opskrift computeren følger for at løse et problem.

📎 **Illustration:** `modul1-ill5-tre-grunde.svg`
*Tre kort side om side: Data + Hardware + Algoritmer med plus-tegn imellem*

---

### Hvad kan AI gøre — og hvad kan det ikke?

AI er imponerende, men det er vigtigt at forstå både hvad det er godt til og hvor det fejler.

**✅ AI er rigtig god til:**
- Genkende mønstre i store mængder data
- Generere tekst, billeder, kode og musik
- Oversætte sprog
- Besvare spørgsmål baseret på viden den har lært
- Finde fejl i kode

**❌ AI kæmper med:**
- Forstå verden som et menneske — den ved ikke hvad den siger, den *forudsiger* hvad der er sandsynligt at sige
- Holde styr på hvad der er sandt — den kan finde på fakta der lyder overbevisende men er forkerte
- Opgaver der kræver ægte kreativitet og følelser
- Ting den ikke har set eksempler på i sin træning

> 💬 **Ordforklaring:** *Hallucination* er når en AI opfinder information der ikke er sand — det sker fordi den er trænet til at lave sandsynlige svar, ikke nødvendigvis korrekte.

📎 **Illustration:** `modul1-ill6-styrker-svagheder.svg`
*To-kolonne oversigt: grøn kolonne (styrker) og rød kolonne (svagheder)*

## Modul 2: AI engine og LLM — med eksempler

> **Målgruppe:** 10–15 år · Let computer science baggrund · Kan skrive små Python-programmer
> **Illustration-filer:** modul2-ill1 til modul2-ill6 (SVG) — *skal oprettes*
> **Kode-eksempel:** `reference-eksempler/ansigtsgenkendelse.py` (se reference-eksempler.md)

---

### Hvad er en AI engine?

Når folk taler om AI, blander de ofte to ting sammen: **modellen** og **engineen** der kører den.

Tænk på det som et spil. Et computerspil er ikke det samme som motoren der kører det. *Minecraft* kører på Javas motor. *Fortnite* kører på Unreal Engine. Motoren er det der faktisk beregner alt — grafik, fysik, lyd. Spillet er indholdet.

På samme måde er en AI-model bare en stor fil fuld af tal. Den kan ikke gøre noget selv. Det er **engineen** der indlæser modellen og rent faktisk beregner svarene.

**Eksempler på AI engines:**
- **Ollama** — en engine der kører lokale modeller på din computer
- **llama.cpp** — den underliggende motor som mange værktøjer bruger
- **PyTorch** — et programmeringsframework brugt til at træne og køre modeller
- **OpenAI's servere / Anthropic's servere** — cloud-engines der kører ChatGPT og Claude

> 💬 **Ordforklaring:** *Engine* (motor) er den software der faktisk udfører beregningerne. *Runtime* er et andet ord for det — "det der kører når programmet er i gang".

📎 **Illustration 1 — Engine vs Model:**
Vis et DVD-afspiller-diagram. DVD'en = modellen (fx Llama 3). DVD-afspilleren = engineen (fx Ollama). TV-skærmen = output (AI's svar). Tre bokse med pile imellem. Simpel, farverig.

---

### Hvad er en Large Language Model (LLM)?

LLM står for **Large Language Model** — på dansk: en stor sprogmodel.

De tre ord fortæller præcis hvad det er:
- **Large** — modellen har milliarder af tal (parametre) indeni
- **Language** — den er trænet på tekst: bøger, websites, kode, artikler
- **Model** — det er en matematisk funktion der har lært mønstre fra al den tekst

Men hvad *gør* den egentlig? Svaret er overraskende simpelt:

**En LLM gætter hele tiden hvad det næste ord sandsynligvis er.**

Prøv det selv: "Jeg går en tur i ___" — din hjerne foreslår straks: *skoven*, *parken*, *haven*. Det er præcis hvad en LLM gør — bare med milliarder af eksempler at trække på, så gættet bliver meget præcist.

Det lyder simpelt. Men når du gør dette med nok data og nok parametre, opstår noget der ligner forståelse.

> 💬 **Ordforklaring:** *Parameter* er et tal indeni modellen der er justeret under træningen. En stor model har måske 70 milliarder parametre. *Træning* er processen hvor modellen læser enorme mængder tekst og justerer sine parametre, så den bliver bedre til at forudsige næste ord.

📎 **Illustration 2 — Næste token forudsigelse:**
Vis en sætning med et tomt felt til sidst: *"Jeg går en tur i ___"*. Ved siden af: søjlediagram der viser sandsynligheder: "skoven" 42%, "parken" 28%, "haven" 18%, "byen" 8%, "mørket" 4%. En pil der peger på det mest sandsynlige ord. Vis at næste ord tilføjes og processen gentager sig.

---

### Tokenisering — hvordan forstår en LLM tekst?

En LLM læser ikke bogstaver eller ord — den læser **tokens**.

Et token er et lille stykke tekst. Det kan være et helt ord, en del af et ord eller endda et tegn. Det er ikke det samme som et ord.

**Eksempel:**
Sætningen *"Kunstig intelligens er sejt!"* bliver måske splittet til:
```
["Kunst", "ig", " intel", "ligens", " er", " sejt", "!"]
```
Det er 7 tokens, selvom der kun er 4 ord.

Og det her ord: *"hund"* = 1 token. Men *"hundehvalp"* = måske 2-3 tokens.

**Hvorfor er det vigtigt?**
Fordi modeller har en grænse for hvor mange tokens de kan håndtere på én gang — det kaldes **context window**. En model med 128.000 tokens kan huske ca. 96.000 engelske ord på én gang. Og tokens koster penge ved cloud-API'er — prisen beregnes per token, ikke per ord.

> 💬 **Ordforklaring:** *Token* er den mindste enhed tekst som en LLM arbejder med. *Context window* er hvor meget tekst modellen kan "huske" og tage hensyn til på én gang.

📎 **Illustration 3 — Tokenisering:**
En papirstrimmel med teksten *"Kunstig intelligens er sejt!"* der bliver klippet op i stykker. Hvert stykke er et token i en farvet boks. Enkelt-token ord = grøn boks. Ord der er splittet = gule/orange bokse. Forneden: "7 tokens" tæller. Vis også context window som en lille "hukommelses-beholder".

---

### Transformers — arkitekturen bag moderne LLM'er

🔗 **Husk fra Modul 1:** I *Deep Learning*-afsnittet lærte vi at neurale netværk er bygget af lag — hvert lag genkender noget mere komplekst end det forrige. Transformer-arkitekturen er netop et sådant neuralt netværk, men med en særlig mekanisme ovenpå: *attention*. → [Modul 1 — Hvad er deep learning?](#modul-1)

I 2017 offentliggjorde Google-forskere en artikel med titlen *"Attention is All You Need"*. Den beskrev **Transformer-arkitekturen**, og den er grundlaget for næsten al moderne AI: ChatGPT, Claude, Gemini, Llama — alle bruger den.

Den store idé: **self-attention** (selv-opmærksomhed).

Tidligere AI-systemer læste tekst fra venstre til højre og glemte hvad der stod i starten. Transformeren gør noget anderledes: den kigger på **alle ord på samme tid** og regner ud hvilke ord der er relevante for hinanden.

**Et eksempel:**

*"Katten jagede musen fordi den var sulten"*

Hvem er "den"? Katten eller musen? Du ved det — katten er sulten, ikke musen. En transformer klarer det ved at lade hvert ord "kigge på" alle andre ord og regne ud hvilke der er vigtigst. Ordet "den" kigger på "sulten" og "jagede" og konkluderer: det er katten.

> 💬 **Ordforklaring:** *Arkitektur* er den måde et neuralt netværk er bygget op på. *Attention* er mekanismen der lader modellen fokusere på de vigtigste dele af teksten.

💻 **Kode-eksempel:** `reference-eksempler/ansigtsgenkendelse.py`
Ansigtsgenkendelse er et konkret eksempel på deep learning i praksis — en model der er trænet på tusindvis af ansigter kan nu genkende nye ansigter den aldrig har set. Præcis den mekanisme vi beskriver her.

📎 **Illustration 4 — Attention:**
Vis sætningen *"Katten jagede musen fordi den var sulten"* med hvert ord i sin egen boks. Fra ordet *"den"* trækkes linjer til alle andre ord — tyk linje til *"Katten"* (stærk attention), tynd linje til *"musen"* (svag attention). Linjernes tykkelse viser "hvor meget opmærksomhed" der er.

---

### Embeddings og vektorer — tal der betyder noget

Computere forstår ikke ord. De forstår tal. Så hvordan omsætter en LLM et ord til noget meningsfuldt?

Svaret er **embeddings**.

En embedding er en liste af tal der repræsenterer betydningen af et ord. Tænk på det som koordinater på et kort — men i stedet for 2 koordinater (x og y) har hvert ord måske 1.024 koordinater.

Det smarte er: ord med lignende betydning får lignende tal og havner tæt på hinanden på "kortet".

**Eksempler:**
- *"hund"* og *"kat"* havner tæt på hinanden (begge er kæledyr)
- *"bil"* og *"tog"* havner tæt (begge er transport)
- *"hund"* og *"bil"* er langt fra hinanden

Og her kommer noget fascinerende — man kan faktisk regne med ord:

> **Dronning ≈ Konge − Mand + Kvinde**

Hvis du tager vektoren for *"Konge"*, trækker *"Mand"* fra og lægger *"Kvinde"* til — får du noget der er meget tæt på *"Dronning"*. Sprogets logik er gemt i tallene!

> 💬 **Ordforklaring:** *Vektor* er en liste af tal der beskriver noget — fx position, retning eller her: betydning. *Embedding* er den specifikke vektor der repræsenterer et ords betydning i en model.

📎 **Illustration 5 — Embedding-kort:**
Et 2D "betydnings-kort" med fire klynger: Dyr (hund, kat, fugl), Transport (bil, tog, cykel), Mad (æble, brød, pizza), Sport (fodbold, tennis, svømning). Vis afstand med stiplede linjer. Vis pil-eksemplet: *"Konge − Mand + Kvinde ≈ Dronning"* som en lille vektor-illustration i hjørnet.

---

### Konkrete eksempler — de store modeller

**Claude** (lavet af Anthropic)
- Kører i cloud — tilgås via claude.ai eller API
- Meget god til analyse af lange tekster og kode
- Multimodal: kan forstå billeder
- Kendt for at være omhyggelig og præcis
- Det er den model du taler med her! 👋

**GPT-4o** (lavet af OpenAI)
- Kører i cloud — tilgås via ChatGPT eller API
- Meget alsidig — god til næsten alt
- Multimodal: tekst, billeder og lyd
- Den mest kendte AI-model i verden

**Llama 3** (lavet af Meta — Facebook's moderselskab)
- **Open source** — kildekoden og vægtene er frit tilgængelige
- Kan downloades og køres lokalt på din computer
- Næsten lige så god som de betalte cloud-modeller
- Bruges som fundament for mange andre lokale modeller

**Qwen 2.5** (lavet af Alibaba)
- Open source — gratis at bruge og modificere
- Særligt stærk til kodning
- Meget effektiv — kører godt på hardware med begrænset VRAM
- Et populært valg til lokal brug

> 💬 **Ordforklaring:** *Open source* betyder at koden og modellen er offentligt tilgængelig — alle kan downloade, bruge og bygge videre på den. *Cloud* betyder at modellen kører på en virksomheds servere og du sender dine beskeder derover.

📎 **Illustration 6 — Model-sammenligning:**
Fire kort i 2×2 grid. Hvert kort: modelnavn, afsender, sky-ikon ☁️ eller computer-ikon 💻, og to-tre nøgleord. Cloud-modeller i blå toner, lokale modeller i grønne toner. Forneden: "hvornår bruger du hvad"-guide i to kolonner.

## Modul 3: Local vs Cloud — hardware, privacy, GPU/CPU

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul3-ill1 til modul3-ill5 (SVG)

---

### To veje til AI

Når du vil bruge en AI-model, har du grundlæggende to valg: **Lokal** — modellen kører på din egen computer. **Cloud** — modellen kører på en virksomheds servere, du sender din besked over internettet og får svar tilbage.

> **Cloud** er som at bestille mad på restaurant — hurtigt, du behøver ikke lave noget selv, men restauranten ved hvad du bestilte.
> **Lokal** er som at lave mad hjemme — mere forberedelse og kræver et ordentligt køkken, men ingen ved hvad du laver.

📎 **Illustration 1 — To veje til AI:** `modul3-ill1-lokal-vs-cloud.svg`

---

### Lokal AI — fordele og ulemper

**✅ Fordele:**
- **Privacy** — dine data forlader aldrig din maskine
- **Ingen løbende omkostninger** — gratis efter download
- **Fungerer uden internet** — offline, i tog, på hytten
- **Fuld kontrol** — du vælger model og version

**❌ Ulemper:**
- Kræver hardware (GPU/CPU og nok RAM/VRAM)
- Langsommere end cloud på hjemme-hardware
- Sværere at sætte op end en hjemmeside

> 💬 **Ordforklaring:** *Privacy* handler om hvem der har adgang til dine informationer. Lokal AI betyder at kun du har adgang.

📎 **Illustration 2 — Privacy:** `modul3-ill2-privacy.svg`

---

### Cloud AI — fordele og ulemper

**✅ Fordele:**
- Hurtigt og kraftfuldt — kører på enorme serverparker
- Altid opdateret — forbedringer sker automatisk
- Ingen hardware-krav — fungerer på en gammel laptop
- De absolutte topmodeller er kun tilgængelige her

**❌ Ulemper:**
- Dine data behandles af en tredjemand
- Koster penge ved højt forbrug via API
- Kræver internet
- Du er afhængig af andres beslutninger

> 💬 **Ordforklaring:** *API* er en måde at kommunikere med en tjeneste fra et program. *Tredjemand* er en anden virksomhed end dig selv.

---

### Hardware 101 — GPU, CPU, VRAM og RAM

**CPU** (Central Processing Unit) — computerens "hjerne". Alsidig, løser alle slags opgaver, men én ad gangen. Tænk: en meget klog rektor der behandler elever én for én.

**GPU** (Graphics Processing Unit) — grafikkortet. Designet til at beregne tusindvis af ting på én gang. Perfekt til AI. Tænk: en klasse med 3.000 elever der alle løser den samme simple opgave samtidig.

**RAM** — computerens arbejdshukommelse. Jo mere, jo flere ting kan du have i gang på én gang.

**VRAM** — det samme, men dedikeret til GPU'en. Modellen skal passe ind i VRAM for at køre hurtigt på GPU.

> 💬 **Ordforklaring:** *RAM* = hurtig midlertidig hukommelse. *VRAM* = samme koncept, men på GPU'en.

📎 **Illustration 3 — CPU/GPU/RAM/VRAM:** `modul3-ill3-cpu-gpu-ram-vram.svg`

---

### Modellens størrelse og hardware-krav

Modeller måles i milliarder parametre (B). Jo større model, jo bedre — men jo mere hardware kræves.

| Størrelse | Hvad kræves | Eksempel |
|-----------|-------------|---------|
| 1–3B | 4 GB RAM | Alt hardware, simple opgaver |
| 7–8B | 8 GB VRAM / 16 GB RAM | God allrounder ← start her |
| 13–14B | 12 GB VRAM / 32 GB RAM | Stærkere reasoning |
| 32–70B | 24+ GB VRAM | Næsten cloud-kvalitet |
| 405B+ | Mange GPU'er | Kun cloud |

📎 **Illustration 4 — Model størrelse:** `modul3-ill4-model-storrelse.svg`

---

### Quantization — større modeller på mindre hardware

Quantization reducerer præcisionen af tallene i modellen fra 16 bits til fx 4 bits (Q4). Som at komprimere et foto — fylder meget mindre, næsten samme kvalitet.

- Llama 3.1 70B original: ~140 GB VRAM
- Llama 3.1 70B Q4: ~40 GB — 75% mindre, ~95% kvalitet

Ollama og LM Studio downloader automatisk gode Q-versioner.

> 💬 **Ordforklaring:** *Quantization* reducerer præcisionen af tallene i en model for at spare plads. *Q4* = 4-bit quantization, *Q8* = 8-bit.

📎 **Illustration 5 — Quantization:** `modul3-ill5-quantization.svg`

---

### CPU offloading

Hvis modellen er lidt for stor til VRAM, kan de lag der ikke passer glide over til normal RAM og beregnes på CPU. Lidt langsommere — men giver mulighed for at køre større modeller end GPU ellers ville tillade.

→ Se **Appendix 3: CPU Offloading** for detaljer.

## Modul 4: Processen fra forespørgsel til svar

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul4-ill1 til modul4-ill5 (PNG)

---

### Følg en besked hele vejen

I Modul 2 lærte du *hvad* tokens, embeddings og attention er. Nu følger vi en enkelt besked hele vejen igennem modellen — fra du trykker Enter til svaret dukker op på skærmen.

Forestil dig at du skriver: **"Hvad er verdens højeste bjerg?"** — de næste sektioner følger denne besked trin for trin.

📎 **Illustration:** `modul4-ill1-pipeline-overblik.png`
*Vandret pipeline med 6 nummererede trin fra input til output*

---

### Trin 1 — Input og tokenisering

Når du trykker Enter, sker der straks noget: din tekst splittes i tokens.

*"Hvad er verdens højeste bjerg?"* bliver til noget i stil med: `["Hvad", " er", " verdens", " høj", "este", " bjerg", "?"]`

Disse tokens er det modellen arbejder med — ikke bogstaver, ikke ord, men tokens.

> 🔗 **Husk fra Modul 2:** Vi gennemgik tokenisering i detaljer — se Illustration 3 i Modul 2.

---

### Trin 2 — Embeddings: fra tokens til tal

Hvert token omdannes til en **embedding** — en lang liste af tal der repræsenterer tokenets *betydning* i kontekst. "bjerg" i sætningen "verdens højeste bjerg" får en embedding der er påvirket af de omkringstående ord — modellen ved nu at vi taler om geografi.

> 🔗 **Husk fra Modul 2:** Embeddings som koordinater på et betydnings-kort — se Illustration 5 i Modul 2.

---

### Trin 3 — Attention: hvad kigger modellen på?

Med alle embeddings klar aktiveres **attention-mekanismen**. Hvert token kigger på alle andre tokens og beregner: *"Hvem er mest relevant for mig?"*

"bjerg" vil have høj attention til "højeste" og "verdens" — og lav attention til "Hvad" og "?". Modellen forstår nu at spørgsmålet handler om at finde det bjerg der er *højest* i *verden*.

> 🔗 **Husk fra Modul 2:** Attention-linjer fra "den" til "Katten" — se Illustration 4 i Modul 2.

---

### Trin 4 — Token-by-token generation

Nu sker det interessante: modellen genererer svaret **ét token ad gangen**. Den beregner: *"Givet alt hvad jeg ved — hvad er det mest sandsynlige næste token?"*

Det er derfor du ser tekst "dukke op" ord for ord i ChatGPT og Claude — hvert ord beregnes enkeltvis. Jo længere svar, jo flere beregninger.

📎 **Illustration:** `modul4-ill2-token-by-token-generation.png`
*Vertikal sekvens der viser svaret vokse token for token*

---

### Trin 5 — Temperature og sampling

Har du lagt mærke til at hvis du stiller det samme spørgsmål to gange, får du lidt forskellige svar? Det er ikke tilfældigt — det er **temperature**.

- **Lav temperature (0.0–0.3):** Modellen vælger næsten altid det mest sandsynlige token. Konsistente, forudsigelige svar. God til fakta og kodning.
- **Høj temperature (0.7–1.2):** Modellen vælger mere tilfældigt. Kreative og varierede svar. God til historier og brainstorming.

> 💬 **Ordforklaring:** *Temperature* styrer hvor "kreativ" eller "fokuseret" modellen er. *Sampling* er processen med at vælge det næste token.

📎 **Illustration:** `modul4-ill3-temperature.png`
*To søjlediagrammer side om side: lav vs høj temperature*

---

### Trin 6 — Context window: hvad kan modellen huske?

Modellen har et **context window** — en grænse for hvor mange tokens den kan tage hensyn til på én gang. Tænk på det som en skrivebordslampe: den belyser kun det der er under den.

- Llama 3 (lokal): 8.000 tokens ≈ 6.000 ord
- GPT-4o: 128.000 tokens ≈ 96.000 ord
- Claude: 200.000 tokens ≈ 150.000 ord (en hel roman!)

> 💬 **Ordforklaring:** *Context window* er den mængde tekst modellen kan "se" på én gang — alt udenfor er usynligt.

📎 **Illustration:** `modul4-ill4-context-window.png`
*Samtale-scroll med vindue der fremhæver de nyeste beskeder — ældre nedtonet*

---

### Trin 7 — Hallucinationer: når modellen gætter forkert

Modellen *forudsiger* det mest sandsynlige næste token — den *ved* ikke om det er sandt. Den kan producere tekst der lyder overbevisende og præcis, men som simpelthen er forkert.

Eksempler: opfinder referencer til bøger der ikke eksisterer, angiver forkerte årstal, beskriver en persons karriere med forkerte detaljer.

**Hvad gør du?** Tjek altid vigtige fakta i andre kilder. Bed modellen om at indrømme usikkerhed. Brug RAG (Modul 16) til at give modellen adgang til pålidelige dokumenter.

> 💬 **Ordforklaring:** *Hallucination* er når en AI producerer information der lyder rigtig men er forkert.

📎 **Illustration:** `modul4-ill5-hallucination.png`
*Chat-mockup med opdigtet bogtitel fremhævet med rød boks og ❌*

## Modul 5: Prismodeller

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul5-ill1 til modul5-ill3 (PNG)

---

### Hvad koster AI egentlig?

Alt fra gratis til meget dyrt — afhængigt af hvad du bruger. Der er tre overordnede modeller: **betal per token** (API), **fast abonnement** og **gratis/open source**.

---

### Cloud API'er — betal per token

Når du tilgår en LLM via API betaler du typisk per *token*. 1 million tokens ≈ 750.000 ord ≈ ca. 10 gennemsnitlige romaner.

- Claude Haiku: $0,25 / $1,25 per 1M tokens (input/output)
- Claude Sonnet: $3 / $15 per 1M tokens
- GPT-4o mini: $0,15 / $0,60 per 1M tokens
- GPT-4o: $5 / $15 per 1M tokens

**Output-tokens koster mere end input-tokens** — at generere tekst kræver mere beregning end at læse den. En typisk besked (~300 tokens) koster under en halv øre.

> 💬 **Ordforklaring:** *Input-tokens* er det du sender (spørgsmål + historik). *Output-tokens* er det modellen genererer (svaret).

📎 **Illustration:** `modul5-ill1-token-priser.png`
*Prisberegning pr. besked + søjlediagram over modeller*

---

### Abonnement — fast månedlig pris

- **ChatGPT Free** — gratis, begrænset adgang til GPT-4o
- **ChatGPT Plus** — $20/md, ubegrænset GPT-4o og nyeste modeller
- **Claude Free** — gratis, begrænset antal beskeder
- **Claude Pro** — $20/md, prioriteret adgang, større context window

Abonnement giver mening hvis du bruger AI dagligt. API er bedre hvis du bygger programmer eller bruger AI sporadisk.

📎 **Illustration:** `modul5-ill2-abonnement-vs-api.png`
*To kort side om side: abonnement vs API — hvornår vælger du hvad?*

---

### Open source og lokale modeller

Modeller som Llama 3, Qwen 2.5 og Mistral er **open source** — gratis at downloade. Den eneste løbende omkostning er elektricitet (~0,50–2 kr./time). Første gangs opsætning tager 30–60 minutter.

---

### Hvornår er hvad billigst?

**Vælg lokal** hvis du arbejder med private data eller allerede har gaming-hardware.
**Vælg abonnement** hvis du vil have de bedste modeller uden opsætning.
**Vælg API** hvis du bygger programmer eller har sporadisk brug.

Et år med 50 beskeder/dag: Claude Pro ≈ $240 · GPT-4o API ≈ $27 · Lokal ≈ $10–20 i strøm.

> 💬 **Ordforklaring:** *ROI* (Return on Investment) handler om hvad du får ud af en investering sammenlignet med hvad den koster.

📎 **Illustration:** `modul5-ill3-pris-sammenligning.png`
*Tre lodrette kort: lokal vs abonnement vs API — årlig pris og afvejning*
