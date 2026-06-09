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

📎 **Illustration:** `modul2-ill1-engine-vs-model.png`
**Titel:** DVD, afspiller og TV-skærm
*Tre bokse med pile: DVD'en = modellen (fx Llama 3), DVD-afspilleren = engineen (fx Ollama), TV-skærmen = output (AI's sv*

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

📎 **Illustration:** `modul2-ill2-token-forudsigelse.png`
**Titel:** Næste ord er en sandsynlighed — ikke et faktum
*En sætning med tomt felt: "Jeg går en tur i ___"*

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

📎 **Illustration:** `modul2-ill3-tokenisering.png`
**Titel:** Tekst klipt i stykker
*Papirstrimmel med teksten "Kunstig intelligens er sejt!" der klippes op*

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

📎 **Illustration:** `modul2-ill4-attention.png`
**Titel:** "Den" — hvem er det?
*Sætningen "Katten jagede musen fordi den var sulten" med hvert ord i boks*

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

📎 **Illustration:** `modul2-ill5-embeddings.png`
**Titel:** Ords "plads" i betydningsrummet
*2D-kort med fire klynger: Dyr (hund, kat, fugl), Transport (bil, tog, cykel), Mad (æble, brød, pizza), Sport (fodbold, t*

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

📎 **Illustration:** `modul2-ill6-model-sammenligning.png`
**Titel:** Cloud eller lokal — hvad er hvad?
*Fire kort i 2×2 grid*
