# Overdragelsesdokument — AI Klar (ai-læringssite)

**Dato:** Juni 2026
**Status:** Aktivt projekt, pause påbegyndt

---

## 1. Projektets formål og status

### Formål
Bygge et dansk/engelsk undervisningssite kaldet **AI·KLAR** — en modulbaseret intro til AI rettet mod **unge 10–15 år** med let computer science baggrund (kan skrive simple Python-programmer, bruger Windows og browser). Siden bruges i undervisningssammenhæng, bl.a. relateret til Coding Pirates.

### Overordnet status
Siden er en **standalone HTML-fil** (`ai-læringssite.html`) der fungerer med tilhørende billedfiler i samme mappe. Den er mørk-tema med accordion-moduler der folder ud ved klik.

**Hvad er færdigt:**
- ✅ Design og struktur (mørkt tema, DA/EN-toggle, accordion)
- ✅ Komplet 19-modul struktur på siden (moduler 6–19 vises som "coming soon")
- ✅ Modul 1, 2 og 3 er fuldt udfyldt med tekst + illustrationer
- ✅ Modul 4 og 5 tekst er skrevet og klar — men HTML-indsætning fejlede (se sektion 4)
- ✅ Arbejdsdokumenter (MD-filer) for alle trin
- ✅ Illustrationsreference-dokument
- ✅ Reference-eksempler (Python-kode)

---

## 2. Det udførte arbejde

### 2a. Webside (`ai-læringssite.html`)
- Enkelt selvstændig HTML-fil, mørkt tech-tema
- Space Mono + Syne + Inter fonte
- Grøn accent `#00e5a0`, blå `#5b8fff`, rød `#ff6b6b`
- DA/EN toggle (data-da / data-en attributter på alle tekstelementer)
- 19 moduler opdelt i 4 trin, accordion-funktionalitet via `toggleModule(id)`
- **VIGTIGT:** HTML-filen er afhængig af PNG eller SVG-billedfilerne i SAMME mappe

### 2b. Modulindhold (fuldt udfyldt)

**Modul 1 — Introduktion til AI** ✅
Sektioner: Hvad er AI, Kort historie, Machine learning, Deep learning, Hvorfor nu, Hvad kan AI
Illustrationer: modul1-ill1 til ill6 (alle SVG, inline i HTML)

**Modul 2 — AI engine og LLM** ✅
Sektioner: AI engine, LLM, Tokenisering, Transformers, Embeddings, Model-sammenligning
Illustrationer: modul2-ill1 (SVG inline), ill2–ill6 (PNG, ekstern reference)
Cross-reference til Modul 1 Deep Learning
Kode-reference til `ansigtsgenkendelse.py`

**Modul 3 — Local vs Cloud** ✅
Sektioner: To veje, Lokal fordele/ulemper, Cloud fordele/ulemper, Hardware 101, Model størrelse, Quantization, CPU offloading
Illustrationer: modul3-ill1 til ill4 (PNG), ill5 (SVG inline)
Reference til Appendix 3 (CPU offloading)

**Modul 4 — Processen fra forespørgsel til svar** ⚠️ TEKST KLAR, HTML FEJLEDE
Sektioner: Pipeline-overblik, Tokenisering (ref Modul 2), Embeddings (ref Modul 2), Attention (ref Modul 2), Token-by-token generation, Temperature & sampling, Context window, Hallucinationer
Illustrationer: modul4-ill1 til ill5 (alle PNG, klar i outputs-mappe)

**Modul 5 — Prismodeller** ⚠️ TEKST KLAR, HTML FEJLEDE
Sektioner: Intro, Cloud API/token-priser, Abonnement, Open source/lokalt, ROI-betragtning
Illustrationer: modul5-ill1 til ill3 (alle PNG, klar i outputs-mappe)

### 2c. Arbejdsdokumenter (MD-filer)
Alle i `/mnt/user-data/outputs/`:

| Fil | Indhold |
|-----|---------|
| `trin-1-grundlaeggende.md` | Modul 1–5, fuldt tekst-indhold for modul 1–3, bullet-punkter for 4–5 |
| `trin-2-interfaces-værktøjer.md` | Modul 6–12, udvidede underpunkter |
| `trin-3-byg-selv.md` | Modul 13–18, udvidede underpunkter |
| `trin-4-avanceret.md` | Modul 19, underpunkter |
| `appendix.md` | Appendix 1 (Hvorfor Linux), Appendix 2 (Linux cheatsheet), Appendix 3 (CPU offloading) |
| `trin1-illustrations-reference.md` | Detaljeret beskrivelse af alle 24 illustrationer i Trin 1 + status |
| `reference-eksempler.md` | Oversigt over Python-kodeeksempler |

### 2d. Illustrationer — Trin 1

| Fil | Type | Status |
|-----|------|--------|
| modul1-ill1 til ill6 | SVG | ✅ Inline i HTML |
| modul2-ill1 | SVG | ✅ Inline i HTML |
| modul2-ill2 til ill6 | PNG | ✅ Ekstern, klar |
| modul3-ill1 til ill4 | PNG | ✅ Ekstern, klar |
| modul3-ill5 | SVG | ✅ Inline i HTML |
| modul4-ill1 til ill5 | PNG | ✅ Klar i outputs, IKKE i HTML endnu |
| modul5-ill1 til ill3 | PNG | ✅ Klar i outputs, IKKE i HTML endnu |

### 2e. Kodeeksempler (`reference-eksempler.md`)
- **Eks. 01:** `ansigtsgenkendelse.py` — OpenCV face detection (Modul 2, deep learning demo)
- **Eks. 02:** `token-taeller.py` — Interaktiv tokenisering med tiktoken (Modul 2)
- **Eks. 03–05:** Planlagt (grundstof-gætter, hovedstads-quiz, chatbot)

---

## 3. Fremtidige planer og næste skridt

### Højeste prioritet — Fix HTML-filen

**Problem:** Det sidste script-kørsel ødelagde modul 04-nummerering i HTML. Nuværende tilstand:
- Modul 01, 02, 03, 05 er til stede
- Modul 04 mangler i HTML (tal-div ikke fundet)
- Modul 06–19 er "coming soon" men mangler i output

**Løsning:** Byg HTML fra bunden med Python ved at samle alle dele fra MD-filerne, eller find og ret fejlen manuelt. Den sikreste fremgangsmåde er at:
1. Læse den nuværende HTML
2. Finde korrekt placering for modul 04 og 05
3. Indsætte dem korrekt med `<img src="...">` tags for PNG-filerne

### Trin 1 — Resterende (når HTML er fikset)
- Opdater `trin-1-grundlaeggende.md` med fuldt tekstindhold for Modul 4 og 5 (teksten er skrevet, bare ikke gemt i filen endnu)
- Opdater `trin1-illustrations-reference.md` — marker alle modul4 og modul5 illustrationer som ✅

### Trin 2–4 — Næste store opgave
Trin 2 (Modul 6–12) er næste trin at udfylde. Fremgangsmåde:
1. Lav indhold (forklarende tekst + illustration-beskrivelser) for hvert modul
2. Brugeren laver illustrationer og uploader PNG-filer
3. Indsæt i HTML og opdater MD-fil

**Moduler der mangler illustrationer (Trin 1):**
- modul5-ill-* er klar som PNG, mangler bare HTML-indsætning
- modul3-ill5-quantization.svg er allerede inline

### Planlagte kodeeksempler
- Eks. 03: Grundstof-gætter (Python + Ollama API)
- Eks. 04: Hovedstads-quiz (Python + Ollama API)
- Eks. 05: Simpel chatbot i terminalen

### Websiden — Fremtidige features
- Modul-fremgangsindikator ("du har gennemført X af 19")
- Responsivt design forbedringer til mobil
- Evt. mørkt/lyst tema-skift
- Navigation mellem moduler (forrige/næste)

---

## 4. Åbne spørgsmål og udfordringer

### Kritisk
- **HTML er i fejltilstand** — Modul 04 mangler, modul 05 er muligvis misplaceret. Skal fixes FØR ny indhold tilføjes. Anbefaling: Genbyg HTML fra de kendte gode dele.

### Uafklarede design-beslutninger
- **Hermes** — Hvad er det? Modulet er droppet for nu men ikke defineret.
- **Modul 4 og 5 tekst** er skrevet i chatten men ikke gemt i `trin-1-grundlaeggende.md` endnu.
- Skal siden distribueres som én HTML-fil + mappe med billeder, eller konverteres til et website med separate sider?

### Illustrationer der mangler
- `modul2-ill1-engine-vs-model` — kun SVG, ingen PNG-version
- `modul3-ill5-quantization` — kun SVG, ingen PNG-version
- Trin 2–4 illustrationer er endnu ikke lavet

### Afhængigheder
- HTML-filen er ikke selvstændig — den kræver alle PNG-filer i samme mappe
- Alternativ: Konverter PNG til base64 og embed direkte i HTML (øger filstørrelse kraftigt)

---

## 5. Specifikke retningslinjer og stil

### Målgruppe
- **Primær:** 10–15 år, let CS-baggrund, kan skrive simple Python-programmer
- **Sekundær:** Voksne nybegyndere, lærere
- Sprog: **Dansk** (primært), engelsk via DA/EN-toggle

### Tone og sprog
- Simpelt og direkte — ingen unødvendige fagord
- Ordforklaringer tilføjes altid (💬 callout-boks) ved tekniske termer
- Analogier bruges aktivt (rektor/klasse for CPU/GPU, restaurant for cloud osv.)
- Cross-referencer mellem moduler med 🔗 callout-boks
- Kode-referencer med 💻 callout-boks

### Illustrationsstil
- PNG-filer fra brugeren (lys baggrund, farverig, begynder-venlig)
- SVG-filer (genereret af AI): viewBox 720×variabel, font 'Segoe UI', farvepalette som ovenfor
- Alle illustrationer indlejres med `<div class="illustration-wrap"><img src="..."></div>`

### HTML-konventioner
- Modul-tekst struktur: `<h2>` for sektioner, `<p>` for brødtekst, `<ul>/<li>` for lister
- Callout-bokse: `<div class="callout"><span class="callout-icon">emoji</span><div>tekst</div></div>`
- Cross-reference callout: tilføj `style="border-left-color:#00e5a0; background:#e6fdf6;"` på callout
- Kode callout: tilføj `style="border-left-color:#f59e0b; background:#fff7ed;"` på callout
- Hvert modul-indhold afsluttes med `</div></div>` (mc-inner + module-content)

### Filnavngivning
- Illustrationer: `modul[N]-ill[N]-[beskrivende-navn].[svg|png]`
- Arbejdsdokumenter: `trin-[N]-[navn].md`
- Kodeeksempler: `[beskrivende-navn].py`

### Modulstruktur (19 moduler i 4 trin)
```
Trin 1 (01–05): Grundlæggende — Intro, AI engine/LLM, Local vs Cloud, Pipeline, Prismodeller
Trin 2 (06–12): Interfaces — Web-interfaces, Ollama, Lokale interfaces, Copilot, OpenCode, Pi Agent, Modelvalg
Trin 3 (13–18): Byg selv — Vibe coding, API co-pilot, AI i programmer, RAG, Skills, Agenter
Trin 4 (19):    Avanceret — MCP

Appendix: Hvorfor Linux, Linux kommandoer, CPU Offloading
```

---

## 6. Filer der skal medbringes

Alle filer ligger i `/mnt/user-data/outputs/`:

```
ai-læringssite.html          ← HOVEDDOKUMENT (i fejltilstand, se sektion 4)
trin-1-grundlaeggende.md     ← Arbejdsdokument Trin 1
trin-2-interfaces-værktøjer.md
trin-3-byg-selv.md
trin-4-avanceret.md
appendix.md
trin1-illustrations-reference.md
reference-eksempler.md
token-taeller.py
ansigtsgenkendelse.py        ← Ligger ikke i outputs, skal oprettes

modul1-ill[1-6].svg          ← Inline i HTML, men filer findes
modul2-ill1.svg              ← Inline i HTML
modul2-ill[2-6].png          ← Ekstern reference
modul3-ill[1-4].png          ← Ekstern reference
modul3-ill5.svg              ← Inline i HTML
modul4-ill[1-5].png          ← Klar, mangler HTML-indsætning
modul5-ill[1-3].png          ← Klar, mangler HTML-indsætning
```
