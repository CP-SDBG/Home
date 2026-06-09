# SESSION_STATE.md - AI·KLAR

**Gemt:** 2026-06-09 (session 4)

---

## Mål

Bygge dansk/engelsk undervisningssite **AI·KLAR** - 19 moduler, 4 trin, målgruppe 10-15 år med let CS-baggrund. Standalone HTML-fil + PNG-billeder i samme mappe.

---

## Gennemført denne session

### Modul-udvidelse (HTML + MD synkroniseret)
- **Modul 14** (API co-pilot): 7 → 9 sektioner ✅
  - Tilføjet: "Token-forbrug og priser" (prissammenligningstabel + `usage`-kode), exponential backoff kode, "Praktisk eksempel: historiefortæller" (4 trin)
  - Do/don't-tabel for system-prompts
- **Modul 15** (Python + LLM API): 6 → 9 sektioner ✅
  - Tilføjet: "Lokal eller cloud?" (sammenligningstabel), "Byg genanvendelig AI-funktion" (Ollama + cloud switch), "Svar-parsing/JSON", "Fejlhåndtering" (ConnectionError/ResponseError)
  - Do/don't-tabel for prompts, praktiske eksempler udvidet med system-prompt
- **Modul 16** (RAG): 5 → 8 sektioner ✅
  - Tilføjet: "RAG vs. stor kontekst" (sammenligningstabel), "RAG-pipeline: installér og opsæt", "Søgekvalitet" (parametre-tabel), "Praktisk eksempel: pensum-assistent" (4 trin)
  - Kritisk detalje: "sig 'ved ikke' hvis ikke i kontekst"-instruks
- **Modul 17** (Agenter): 5 → 8 sektioner ✅
  - Tilføjet: "Chatbot eller agent?" (sammenligningstabel), komplet kørende ReAct agent-løkke (30 linjers Python), "Hukommelse og tilstand", "Sikkerhed" (bullet → tabel)
  - Manglede den fulde agent-løkke - nu tilføjet

### MD-filer synkroniseret med HTML
- `trin-2-interfaces-værktøjer.md`: verificeret i sync (modul 6-12) ✅
- `trin-3-byg-selv.md`: modul 13-17 alle opdateret ✅
- `trin-4-avanceret.md`: uberørt (modul 18-19 ikke udvidet endnu)

### PNG-filer uploadet og verificeret
- Modul 15: 3 PNG-filer uploadet ✅
- Modul 16: 3 PNG-filer uploadet ✅
- `illustrations-reference.md`: modul 13-16 alle ✅ (63 ✅, 8 🔲 tilbage)

### Illustrations-standard (understøt, ikke kopier)
Fastholdt og anvendt konsekvent på modul 14-17:
- **Visualisér kontrasten**: to tilstande/veje der leder til forskelligt resultat
- **Gør det konkret**: anatomisér protokol/flow der er usynlig i teksten
- **Skalérbarheds-perspektiv**: samme kode, vidt forskellig kontekst

---

## Filstruktur — arbejdsdokumenter

Hvert modul har sin egen MD-fil:
```
TrinXX-ModulYY-Titel.md        ← 19 modulfiler
Appendix-AXX-Titel.md          ← 3 appendix-filer
Reference-Kodeeksempler.md     ← 1 referencefil
illustrations-reference.md     ← illustrationsbeskrivelser
SESSION_STATE.md               ← dette dokument
```

Aeldre trin-MD-filer (trin-1 til trin-4) beholdes som backup indtil videre.

---

## Modulstruktur

| Trin | Moduler |
|------|---------|
| Trin 1: Grundlæggende | 1–5 |
| Trin 2: Interfaces & værktøjer | 6–12 |
| Trin 3: Byg selv | 13–16 |
| Trin 4: Avanceret | 17–19 |

---

## Indholdsstatus

| Modul | HTML-indhold | PNG-filer | Illustrations-koncepter |
|-------|-------------|-----------|------------------------|
| 01-05 | ✅ fuldt | ✅ alle | ✅ |
| 06-12 | ✅ fuldt | ✅ alle | ✅ |
| 13 | ✅ fuldt (9 h2) | ✅ alle | ✅ |
| 14 | ✅ fuldt (9 h2) | ✅ alle | ✅ |
| 15 | ✅ fuldt (9 h2) | ✅ alle | ✅ |
| 16 | ✅ fuldt (8 h2) | ✅ alle | ✅ |
| 17 | ✅ fuldt (8 h2) | ✅ alle | ✅ |
| 18 | ✅ fuldt (9 h2) | ✅ alle | ✅ |
| 19 | ✅ fuldt (9 h2) | ✅ alle | ✅ |
| Appendix 1-3 | 🔲 kun outline | - | - |

---

## Fastlagt arbejdsmetode - gælder fremadrettet

### Indholdsstandard for moduler
- **Minimum 7-9 sektioner** med `<h2>` overskrifter
- **Konkrete eksempler** - kode og prompts der kan kopieres direkte
- **Do/don't- eller sammenligningstabeller** frem for rene bullet-lister
- **Callouts** til ordforklaringer og cross-modul-referencer
- **Praktisk eksempel** som afsluttende sektion med nummererede trin

### Illustrations-standard
Illustrationer skal **understøtte** teksten - ikke kopiere den. Tre typer der virker:

1. **Visualisér kontrasten** - to veje/tilstande, forskelligt resultat (modul 14 ill2, modul 16 ill1)
2. **Gør det usynlige synligt** - anatomisér protokol/flow/kode (modul 15 ill2, modul 17 ill2)
3. **Skalerbarhed og komposabilitet** - samme arkitektur, forskellig skala (modul 15 ill1, modul 16 ill3)

**Format for illustrations-reference:**
- **Titel**: beskrivende navn
- **Indhold**: hvad der vises præcist
- **Formål**: hvad illustrationen tilføjer som teksten ikke siger

### Workflow ved ny modul-udvidelse
1. Læs eksisterende HTML-sektion + tilhørende MD-fil
2. Identificér mangler (sektioner, konkrethed, do/don't, praktisk eksempel)
3. Skriv udvidet HTML (Python-script til præcis replace)
4. Opdatér MD-arbejdsdokument tilsvarende
5. Opdatér `illustrations-reference.md` - Titel + Indhold + Formål
6. Opdatér `SESSION_STATE.md`

---

## PNG-filer der mangler

Alle PNG-filer modul 1–19 uploadet og verificeret ✅

**Workflow når PNG-filer uploades:**
1. Bruger dropper PNG-filer i mappen og giver besked
2. Verificér filnavne matcher HTML-referencer (`ls *.png | sort`)
3. Opdatér `illustrations-reference.md` - sæt 🔲 → ✅ (både `####`-headers og summary-tabel)

---

## Indhold der mangler

- **Modul 18** (Skills): ✅ udvidet til fuld standard (9 h2), ill3 tilføjet
- **Modul 19** (MCP): ✅ udvidet til fuld standard (9 h2)
- **Appendix 1** (Hvorfor Linux), **Appendix 2** (Linux cheatsheet), **Appendix 3** (CPU offloading): kun outline
- `overdragelsesdokument.md`: forældet - bør opdateres til nuværende tilstand

---

## Kendte problemer / blokkere

- Engelske oversættelser (`data-en`) kun på navigation, ikke brødtekst - laveste prioritet
- `overdragelsesdokument.md` forældet - beskriver gammel fejltilstand

---

## Vigtige beslutninger

- **Alle illustrationer er PNG** - ingen SVG inline
- **PNG-filnavngivning:** `modul[N]-ill[N]-[beskrivende-navn].png` - låst i HTML
- **illustrations-reference.md** er primær kilde til illustration-status og -koncepter
- **Én HTML-fil + PNG-mappe** - ingen multi-page konvertering planlagt
- **HTML er kilde til sandhed** - MD-filer synkroniseres med HTML (ikke omvendt)

---

## Næste skridt (i rækkefølge)

1. **Appendix 1–3** — skriv fuldt tekstindhold
2. **overdragelsesdokument.md** — opdatér til nuværende tilstand
3. **Upload PNG-filer** til modul 17-19 efterhånden → verificér + opdatér illustrations-reference
4. **Appendix 1-3** - skriv fuldt tekstindhold
5. **overdragelsesdokument.md** - opdatér til nuværende tilstand

---

## Valideringstatus

- HTML åbner uden fejl i browser ✅
- Alle PNG-referencer modul 1–19 matcher filer i mappen ✅
- 0 broken images ✅
- Alle udvidede moduler: 0 ulukkede divs ✅

---

## Vigtige stier og kommandoer

```
Projektmappe:
/mnt/c/Users/henri/OneDrive - etap.com/Desktop/AI Site/

Hoveddokument:
ai-læringssite.html

Arbejdsdokumenter:
trin-1-grundlaeggende.md
trin-2-interfaces-værktøjer.md
trin-3-byg-selv.md
trin-4-avanceret.md
appendix.md
illustrations-reference.md
reference-eksempler.md

Tjek PNG-filer i mappe:
ls *.png | sort

Tjek alle img-referencer i HTML:
grep -o 'src="modul[^"]*"' ai-læringssite.html | sort

Verificér modul-sektion i HTML:
python3 -c "
import re
with open('ai-læringssite.html', encoding='utf-8') as f: c = f.read()
for n in range(13,20):
    cid = str(n); nid = str(n+1)
    try:
        s = c.index(f'id=\"content-{cid}\"')
        e = c.index(f'id=\"content-{nid}\"')
        sec = c[s:e]
        h2s = re.findall(r'<h2>(.*?)</h2>', sec)
        print(f'Modul {n}: {len(h2s)} h2, {sec.count(\"<img\")} img, unclosed: {sec.count(\"<div\")-sec.count(\"</div\")}')
    except: pass
"

Status på illustrations-reference:
python3 -c "
import re
with open('illustrations-reference.md', encoding='utf-8') as f: c = f.read()
print(f'✅: {len(re.findall(r\"#### ✅\", c))}  🔲: {len(re.findall(r\"#### 🔲\", c))}')
"
```
