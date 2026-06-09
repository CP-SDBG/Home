## Modul 4: Processen fra forespørgsel til svar

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul4-ill1 til modul4-ill5 (PNG)

---

### Følg en besked hele vejen

I Modul 2 lærte du *hvad* tokens, embeddings og attention er. Nu følger vi en enkelt besked hele vejen igennem modellen — fra du trykker Enter til svaret dukker op på skærmen.

Forestil dig at du skriver: **"Hvad er verdens højeste bjerg?"** — de næste sektioner følger denne besked trin for trin.

📎 **Illustration:** `modul4-ill1-pipeline-overblik.png`
**Titel:** Fra prompt til svar — 6 trin
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
**Titel:** Svaret vokser et token ad gangen
*Vertikal sekvens der viser svaret vokse token for token*

---

### Trin 5 — Temperature og sampling

Har du lagt mærke til at hvis du stiller det samme spørgsmål to gange, får du lidt forskellige svar? Det er ikke tilfældigt — det er **temperature**.

- **Lav temperature (0.0–0.3):** Modellen vælger næsten altid det mest sandsynlige token. Konsistente, forudsigelige svar. God til fakta og kodning.
- **Høj temperature (0.7–1.2):** Modellen vælger mere tilfældigt. Kreative og varierede svar. God til historier og brainstorming.

> 💬 **Ordforklaring:** *Temperature* styrer hvor "kreativ" eller "fokuseret" modellen er. *Sampling* er processen med at vælge det næste token.

📎 **Illustration:** `modul4-ill3-temperature.png`
**Titel:** Lav vs. høj temperature — to vidt forskellige AI'er
*To søjlediagrammer side om side med samme prompt*

---

### Trin 6 — Context window: hvad kan modellen huske?

Modellen har et **context window** — en grænse for hvor mange tokens den kan tage hensyn til på én gang. Tænk på det som en skrivebordslampe: den belyser kun det der er under den.

- Llama 3 (lokal): 8.000 tokens ≈ 6.000 ord
- GPT-4o: 128.000 tokens ≈ 96.000 ord
- Claude: 200.000 tokens ≈ 150.000 ord (en hel roman!)

> 💬 **Ordforklaring:** *Context window* er den mængde tekst modellen kan "se" på én gang — alt udenfor er usynligt.

📎 **Illustration:** `modul4-ill4-context-window.png`
**Titel:** Hukommelsesvinduet — hvad AI'en kan "se"
*Lang samtale-scroll med vindue der fremhæver de nyeste beskeder — ældre nedtonet og ude af vindue.*

---

### Trin 7 — Hallucinationer: når modellen gætter forkert

Modellen *forudsiger* det mest sandsynlige næste token — den *ved* ikke om det er sandt. Den kan producere tekst der lyder overbevisende og præcis, men som simpelthen er forkert.

Eksempler: opfinder referencer til bøger der ikke eksisterer, angiver forkerte årstal, beskriver en persons karriere med forkerte detaljer.

**Hvad gør du?** Tjek altid vigtige fakta i andre kilder. Bed modellen om at indrømme usikkerhed. Brug RAG (Modul 16) til at give modellen adgang til pålidelige dokumenter.

> 💬 **Ordforklaring:** *Hallucination* er når en AI producerer information der lyder rigtig men er forkert.

📎 **Illustration:** `modul4-ill5-hallucination.png`
**Titel:** Opdigtet med selvsikker stemme
*Chat-mockup med opdigtet bogtitel fremhævet med rød boks og ❌*
