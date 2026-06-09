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
**Titel:** Tre lag — én lokal stak
*Lagdiagram: Grafisk interface (top) → Ollama (midt) → Model-fil (bund) — alt lokalt.*

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
**Titel:** LM Studio, Open WebUI, Msty — hvornår vælger du hvad?
*Tre kort side om side: LM Studio, Open WebUI, Msty — installation, krav og hvornår du vælger det.*

---

### Hardware-krav

Lokale interfaces stiller ikke ekstra krav ud over hvad modellen selv kræver:

- **Minimum:** 8 GB RAM — kør en 3B model på CPU (langsomt men muligt)
- **Anbefalet:** 16 GB RAM + GPU med 8 GB VRAM — kør 7B model hurtigt
- **Komfortabelt:** 32 GB RAM + GPU med 12–16 GB VRAM — kør 13–14B modeller

Uden GPU kører modellen på CPU — det virker, men er 5–20 gange langsommere. En 7B model genererer typisk 10–50 tokens/sekund på GPU mod 2–5 tokens/sekund på CPU.

> 🔗 **Husk fra Modul 3:** CPU offloading — hvis modellen er lidt for stor til VRAM, kan ekstra lag flyttes til RAM og CPU. Langsomt, men bedre end ingenting.

📎 **Illustration:** `modul8-ill3-hardware-krav.png`
**Titel:** Tre niveauer — hvad kan din maskine?
*Tre niveauer: minimum (CPU-only), anbefalet (8GB VRAM), komfortabelt (16GB VRAM) — med konkrete model-eksempler på hvert*

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
**Titel:** Hvornår vælger du lokal — og hvornår cloud?
*To kolonner: lokal AI (grøn) vs*
