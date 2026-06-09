# AI·KLAR — Projektspecifikation

**Version:** 1.0 · **Dato:** 2026-06-09  
**Kilde til sandhed:** `ai-læringssite.html`

---

## 1. Projektbeskrivelse

**AI·KLAR** er en dansk/engelsk undervisningssite om AI og LLM til unge. Målet er at tage eleverne fra nul forståelse til at kunne bygge agenter — ét modul ad gangen.

**Tagline:** *"Forstå AI. Byg noget."*  
**Undertitel:** *"Fra nul til agent — et modul ad gangen. Du behøver ingen forudsætninger. Bare nysgerrighed og en computer."*

---

## 2. Målgruppe

| Parameter | Værdi |
|-----------|-------|
| Alder | 10–15 år |
| Baggrund | Let computer science baggrund — kan skrive små Python-programmer |
| Forudsætning | Ingen — nysgerrighed er nok til Trin 1 |
| Sprog | Dansk primært, engelsk sekundært |
| Hardware | Hvilken som helst computer med browser |

**Differentieringslogik:** Hvert modul angiver præcis målgruppe i frontmatter, fx:
> *"10–15 år · Har brugt system-prompts · Kender Ollama"*

---

## 3. Teknisk opbygning

| Parameter | Beslutning |
|-----------|------------|
| Format | Standalone HTML-fil — én fil, ingen server, ingen build |
| Billeder | PNG-filer i samme mappe som HTML |
| Hosting | Åbn direkte i browser — ingen deployment nødvendig |
| Sprog-toggle | DA/EN i navigation — brødtekst ikke oversat (lav prioritet) |
| Multi-page | Ikke planlagt — én HTML-fil er valgt |

**Filstruktur:**
```
ai-læringssite.html          ← hoveddokument (kilde til sandhed)
modul[N]-ill[N]-navn.png     ← illustrationer (samme mappe)
SPECIFIKATION.md             ← dette dokument
SESSION_STATE.md             ← sessionscheckpoint
Trin0X-Modul0Y-Titel.md      ← arbejdsdokumenter pr. modul
illustrations-reference.md   ← illustration-koncepter og status
```

---

## 4. Indholdsstruktur

### 4.1 Trin og moduler

| Trin | Titel | Moduler | Tag-farve |
|------|-------|---------|-----------|
| 1 | Grundlæggende | 1–5 | Grøn (Begynder) |
| 2 | Interfaces & Værktøjer | 6–12 | Blå (Tools) |
| 3 | Byg selv | 13–16 | Blå (Tools) |
| 4 | Avanceret | 17–19 | Rød (Avanceret) |
| — | Appendix | A1–A3 | Blå (Reference) |

**Total:** 19 moduler + 3 appendix + 1 reference-sektion

### 4.2 Modul-oversigt

| Modul | Titel |
|-------|-------|
| 01 | Introduktion til AI |
| 02 | AI engine og LLM — med eksempler |
| 03 | Local vs Cloud — hardware & privacy |
| 04 | Processen fra forespørgsel til svar |
| 05 | Prismodeller |
| 06 | Web-interfaces |
| 07 | Ollama |
| 08 | Lokale interfaces |
| 09 | GitHub Copilot |
| 10 | OpenCode |
| 11 | Pi Agent |
| 12 | Forskellige LLM til forskellige formål |
| 13 | Byg med AI — vibe coding |
| 14 | AI som co-pilot — API i din workflow |
| 15 | AI i dine egne programmer |
| 16 | RAG — giv AI adgang til din viden |
| 17 | Skills — lær AI at følge faste instruktioner |
| 18 | MCP — Model Context Protocol |
| 19 | Agenter — autonome AI-workflows |

### 4.3 Indholdsstandard pr. modul

- **7–9 sektioner** med `<h2>` overskrifter
- **Callout** til ordforklaring og cross-modul-referencer tidligt i modulet
- **Sammenligningstabel** eller **do/don't-tabel** — frem for rene bullet-lister
- **Konkrete kode-eksempler** der kan kopieres direkte
- **Cross-reference callout** til relaterede moduler
- **Praktisk eksempel** som afsluttende sektion — altid med nummererede trin

**Obligatorisk frontmatter i `<h2>`-sektion 1:**
```
Målgruppe: X–Y år · [forudsætning 1] · [forudsætning 2]
Illustration-filer: modulN-ill1 til modulN-illM (PNG)
```

---

## 5. Farvepalette

Alle farver defineret som CSS custom properties i `:root`:

| Variabel | Hex | Anvendelse |
|----------|-----|------------|
| `--bg` | `#0d0f14` | Sidebagggrund (mørk navy) |
| `--surface` | `#151820` | Modulkort og panel-baggrunde |
| `--border` | `#252a35` | Alle borders i dark-mode |
| `--accent` | `#00e5a0` | Primær accent — grøn/teal. Logo, hover, h2-understreg, Begynder-tag |
| `--accent2` | `#5b8fff` | Sekundær accent — blå. Callout-border, Tools-tag, links |
| `--accent3` | `#ff6b6b` | Tertiær accent — rød. Avanceret-tag, fejl/advarsel |
| `--text` | `#e8eaf0` | Primær tekst (dark-mode) |
| `--muted` | `#6b7280` | Sekundær tekst, labels, modul-num |

**Cloud-tag farve (kun CSS, ingen variabel):** `#c084fc` (lilla/violet)

**Indholdspanel (lys baggrund):**
| Element | Farve |
|---------|-------|
| Panel-baggrund | `#f8f9fc` |
| Panel-border | `1px solid #00e5a0` |
| Brødtekst | `#2d3748` |
| Stærk tekst `<strong>` | `#0d0f14` |
| H2 tekst | `#0d0f14` |
| H2 understreg | `2px solid #00e5a0` |
| Callout-baggrund | `#eef1ff` |
| Callout-border-left | `3px solid #5b8fff` |
| Callout-tekst | `#2d3748` |
| Inline code baggrund | `#eef1ff` |
| Inline code tekst | `#1e3a8a` |

**Gridbaggrund:** `rgba(0,229,160,0.03)` — subtile linjer, 40px × 40px

---

## 6. Typografi

### Fonte (Google Fonts)

| Variabel | Familie | Vægte | Anvendelse |
|----------|---------|-------|------------|
| `--mono` | Space Mono | 400, 700 | Logo, trin-labels, modul-numre, kode, tags, knapper |
| `--sans` | Syne | 400, 600, 800 | Hero H1, modul-overskrifter (h3), H2 i indhold |
| `--body` | Inter | 400, 500, 600 | Al brødtekst i indholdspaneler |

### Størrelser

| Element | Størrelse | Vægt | Font |
|---------|-----------|------|------|
| Hero H1 | `clamp(2.5rem, 6vw, 4.5rem)` | 800 | Syne |
| Hero manchet | `1.1rem` | 400 | Syne |
| Trin-label | `0.7rem` | 400 | Space Mono, uppercase, letter-spacing 0.2em |
| Modul-nummer | `0.7rem` | 400 | Space Mono |
| Modul-titel (h3) | `0.95rem` | 600 | Syne |
| Modul-beskrivelse | `0.8rem` | 400 | Space Mono, muted |
| Modul-tag | `0.65rem` | 400 | Space Mono |
| H2 i indhold | `1.3rem` | 700 | Syne |
| Brødtekst i indhold | `1rem` | 400 | Inter, line-height 1.75 |
| Inline kode | `0.85rem` | 400 | Space Mono |
| Tabelkode | `0.82rem` | 400 | Space Mono |
| Kodeblok | `0.82rem` | 400 | Space Mono, line-height 1.6 |

---

## 7. Layoutstruktur

### Overordnet layout
```
<header>          sticky, 60px, backdrop-blur, border-bottom
<body>
  .grid-bg        fast baggrundsgitter (pointer-events: none)
  .hero           max-width 900px, padding 5rem 2rem 3rem
  .modules-section max-width 900px, padding 1rem 2rem 6rem
    .trin-label   mono, uppercase, border-bottom
    .module-list  flex-column, gap 0.5rem
      .module-card  grid: 48px | 1fr | auto
      .module-content  lys panel, display:none → open
<footer>
```

### Modulkort grid
```
[48px modul-num] [1fr: h3 + p] [auto: tag + chevron]
```

### Indholdspanel
- Baggrund: `#f8f9fc` (lys — kontrast mod mørk side)
- Padding: `2.5rem 3rem`
- Border: `1px solid #00e5a0`
- Border-radius: `12px`

### Responsivt breakpoint: 640px
- Header padding: 1rem
- Hero padding: 3rem 1rem 2rem
- Modul-grid: `36px 1fr` (tag skjules)
- Indhold padding: `1.5rem 1.25rem`

---

## 8. Komponenter

### Callout
```html
<div class="callout">
  <span class="callout-icon">💬</span>
  <div><strong>Ordforklaring:</strong> ...</div>
</div>
```
Baggrund `#eef1ff`, venstre-border `3px solid #5b8fff`, font-size `0.9rem`.

Brug til: ordforklaringer, cross-referencer, vigtige pointer.

### Inline kode
```html
<code>ollama run qwen2.5</code>
```
Baggrund `#eef1ff`, tekst `#1e3a8a`, Space Mono, border-radius `4px`.

### Kodeblok
```html
<pre><code>
python kode her
</code></pre>
```
Arver `.mc-inner code` styling — lys blå baggrund, mørk blå tekst.

### Tabel (indhold)
Inline `style`-attributter — ingen separat CSS-klasse for indholtstabeller (undtagen `.cmd-table` til Linux-kommandoer).

Standard inline-tabel:
```html
<table style="width:100%;border-collapse:collapse;margin:1rem 0;font-size:0.93rem;">
  <thead><tr style="background:var(--accent-muted,#1a2a1a);">
    <th style="padding:0.5rem 0.75rem;text-align:left;">...</th>
  </tr></thead>
  <tbody>
    <tr style="border-bottom:1px solid #2a3a2a;">
      <td style="padding:0.45rem 0.75rem;">...</td>
    </tr>
  </tbody>
</table>
```

### Illustration-wrap
```html
<div class="illustration-wrap">
  <img src="modul[N]-ill[N]-navn.png"
       style="width:100%;height:auto;display:block;border-radius:8px;">
</div>
```
Border: `1px solid #e2e6f0`, border-radius `12px`, margin `1.75rem 0`.

### WIP-badge (appendix/outline)
```html
<div class="wip-badge">🚧 Under opbygning</div>
```
Amber farve, `#fff7ed` baggrund, `#d97706` tekst, `#f59e0b` border.

---

## 9. Modul-tags

| Tag-klasse | Farve | Anvendes til |
|------------|-------|--------------|
| `tag-beginner` | `#00e5a0` grøn | Trin 1 — grundlæggende moduler |
| `tag-tools` | `#5b8fff` blå | Trin 2–3 — interfaces og byg-selv |
| `tag-cloud` | `#c084fc` lilla | Cloud-specifikke moduler |
| `tag-advanced` | `#ff6b6b` rød | Trin 4 — avancerede moduler |
| `tag-soon` | `#6b7280` grå | Kommende moduler |

---

## 10. Illustrationsstandard

### Format
- **Alle illustrationer er PNG** — ingen SVG inline
- **Navngivning:** `modul[N]-ill[N]-[beskrivende-navn].png` — låst i HTML
- **Placering:** Samme mappe som HTML-filen
- **Størrelse:** Full-width i panel, `border-radius: 8px`

### Tre typer der virker

| Type | Princip | Eksempel |
|------|---------|---------|
| **Visualisér kontrasten** | To veje/tilstande → forskelligt resultat | Modul 14 ill2: nøgle i pengeskab vs. under dørmåtten |
| **Gør det usynlige synligt** | Anatomisér protokol/flow der er skjult i teksten | Modul 15 ill2: hvad sker der inde i `ollama.chat()`? |
| **Skalerbarhed og komposabilitet** | Samme arkitektur, vidt forskellig skala | Modul 16 ill3: 5 noter → 50.000 dokumenter |

### Regel
Illustrationer skal **understøtte** teksten — ikke kopiere den.  
✅ Vis noget teksten IKKE siger  
❌ Genvis det samme som teksten allerede forklarer

### Beskrivelsesformat (i illustrations-reference.md)
```
**Titel:** Beskrivende navn — hvad er kontrasten/pointen?
**Indhold:** Hvad vises præcist — elementer, pile, labels, farver
**Formål:** Hvad tilføjer illustrationen som teksten ikke siger
```

---

## 11. Sprogstil og tone

### Generelle principper
- **Direkte og konkret** — ingen akademisk omsvøb
- **Simpelt sprog** — målgruppen er 10–15 år
- **Eksempler frem for definitioner** — vis det, forklar det bagefter
- **"Du"-tiltale** — aldrig "man"
- **Imperativ i instruktioner** — "Skriv", "Kør", "Test"

### Tekst-hierarki i moduler
1. Kort intro-paragraf — hvad handler dette modul om?
2. Callout med ordforklaringer (tidligt)
3. Hoveddel med sektioner — tabeller, kode, eksempler
4. Afsluttende praktisk eksempel med nummererede trin

### Kodeeksempler
- **Altid kommenterede** med dansk forklaring
- **Kan køres direkte** — ingen placeholder-kode uden forklaring
- **Fejlhåndtering inkluderet** i avancerede moduler (trin 3–4)

### Ordforklaringer
Første gang et fagbegreb introduceres: altid forklaret i en callout.  
Cross-referencer bruger: *"Se modul X for mere om [emne]"*

---

## 12. Sprog-toggle (DA/EN)

Implementeret via `data-da` og `data-en` attributter på elementer + JavaScript.

```html
<span data-da="dansk tekst" data-en="english text">dansk tekst</span>
```

**Nuværende coverage:**
- Navigation og modul-kort: ✅ oversat
- Brødtekst i modulindhold: ❌ kun dansk (lav prioritet)

---

## 13. Vigtige designbeslutninger (låste valg)

| Beslutning | Begrundelse |
|------------|-------------|
| Lys indholdspanel på mørk side | Kodeeksempler læsbare, kontrast fra dark-mode shell |
| Space Mono til UI-elementer | Teknisk/terminal æstetik — signalerer "dette er et kodingssite" |
| Syne til overskrifter | Moderne, markant — skiller sig ud fra Inter-brødtekst |
| Standalone HTML | Nul deployment-kompleksitet — åbn og del som fil |
| PNG frem for SVG inline | Simplere at producere og vedligeholde illustrationer |
| Max-width 900px | Optimal læsbarhed for brødtekst + kode |
| Grøn (#00e5a0) som primær accent | Terminal/AI-kodningsæstetik — grøn cursor reference |
| Moduler accordion-style | Brugeren navigerer selektivt — ikke scroll-til-bunds |

---

## 14. Arbejdsmetode og vedligehold

### HTML er kilde til sandhed
MD-arbejdsdokumenter synkroniseres med HTML — ikke omvendt.

### Workflow ved ny modul-udvidelse
1. Læs eksisterende HTML-sektion
2. Identificér mangler (sektioner, do/don't, praktisk eksempel)
3. Skriv udvidet HTML
4. Opdatér tilhørende MD-arbejdsdokument
5. Opdatér `illustrations-reference.md`
6. Opdatér `SESSION_STATE.md`

### Valideringskommandoer
```bash
# Tjek modul-sektioner
python3 -c "
import re
with open('ai-læringssite.html', encoding='utf-8') as f: c = f.read()
for n in range(1,20):
    try:
        s = c.index(f'id=\"content-{n}\"')
        e = c.index(f'id=\"content-{n+1}\"') if n < 19 else c.index('<!-- APPENDIX -->')
        sec = c[s:e]
        h2s = re.findall(r'<h2>(.*?)</h2>', sec)
        print(f'Modul {n:02}: {len(h2s)} h2, {sec.count(\"<img\")} img, unclosed: {sec.count(\"<div\")-sec.count(\"</div\")}')
    except: pass
"

# Tjek PNG-filer matcher HTML
grep -o 'src=\"modul[^\"]*\"' ai-læringssite.html | sort > /tmp/html_imgs.txt
ls modul*.png | sed 's/^/src="/' | sed 's/$/"/' | sort > /tmp/disk_imgs.txt
diff /tmp/html_imgs.txt /tmp/disk_imgs.txt

# Illustrations-reference status
python3 -c "
import re
with open('illustrations-reference.md', encoding='utf-8') as f: c = f.read()
print(f'✅: {len(re.findall(r\"#### ✅\", c))}  🔲: {len(re.findall(r\"#### 🔲\", c))}')
"
```
