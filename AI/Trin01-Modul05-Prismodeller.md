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
**Titel:** Hvad koster én besked?
*Prisberegning pr*

---

### Abonnement — fast månedlig pris

- **ChatGPT Free** — gratis, begrænset adgang til GPT-4o
- **ChatGPT Plus** — $20/md, ubegrænset GPT-4o og nyeste modeller
- **Claude Free** — gratis, begrænset antal beskeder
- **Claude Pro** — $20/md, prioriteret adgang, større context window

Abonnement giver mening hvis du bruger AI dagligt. API er bedre hvis du bygger programmer eller bruger AI sporadisk.

📎 **Illustration:** `modul5-ill2-abonnement-vs-api.png`
**Titel:** Fast pris vs. betaling pr. brug
*To kort side om side: abonnement (fast månedspris, ubegrænset brug) vs*

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
**Titel:** Lokal vs. abonnement vs. API — hvad koster det over et år?
*Tre lodrette kort: lokal (engangsomkostning hardware), abonnement (månedlig fast), API (variabel, afh*
