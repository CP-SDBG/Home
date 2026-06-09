## Modul 9: GitHub Copilot — AI i din editor

> **Målgruppe:** 10–15 år · Kender VS Code · Har skrevet Python eller andet kode
> **Illustration-filer:** modul9-ill1 til modul9-ill4 (PNG)

---

### Hvad er GitHub Copilot?

Forestil dig at have en meget erfaren programmør siddende ved siden af dig mens du koder — en der kender alle sprog, har læst millioner af kode-eksempler og altid er klar til at foreslå næste linje. Det er præcis hvad **GitHub Copilot** er.

Copilot er en AI-assistent der er bygget direkte ind i din kodeeditor. Den kigger på hvad du skriver og foreslår kode i realtid — hele funktioner, loops, fejlhåndtering — baseret på konteksten i din fil og dine kommentarer.

Den er udviklet af GitHub (ejet af Microsoft) og bruger OpenAI's modeller i baggrunden. Det er den mest udbredte AI-coding-assistent i verden med over 1 million aktive brugere.

> 💬 **Ordforklaring:** *Editor* er det program du skriver kode i — VS Code, PyCharm, Vim osv. *Extension* er et tilføjelsesprogram der udvider editorens funktioner.

📎 **Illustration:** `modul9-ill1-copilot-i-vscode.png`
**Titel:** Copilot som ekstra programmør i editoren
*VS Code med Copilot aktiv — autocomplete-forslag vist som nedtonet tekst, chat-panel og inline suggestions markeret.*

---

### Installation i VS Code

1. Åbn VS Code
2. Gå til Extensions (Ctrl+Shift+X)
3. Søg efter "GitHub Copilot" og installer
4. Log ind med din GitHub-konto
5. Acceptér Copilot-licensen

**Pris og studerende:**
Copilot koster normalt ~$10/md. Men hvis du er studerende med en `.edu`-mailadresse eller aktivt bidragyder til open source, kan du få det **gratis** via GitHub Education. Det er værd at tjekke.

Der er også et gratis tier med begrænsede completions per måned — nok til at komme i gang.

---

### Autocomplete — kodeforslag mens du skriver

Det mest basale — og mest brugte — feature er **autocomplete**. Mens du skriver, vises Copilots forslag som nedtonet grå tekst:

- **Tab** — acceptér forslaget
- **Esc** — afvis forslaget
- **Alt+]** — se næste alternative forslag

Copilot er særligt god til:
- Boilerplate-kode du altid skriver på samme måde
- At fortsætte et mønster du har påbegyndt
- At skrive kode ud fra en kommentar der beskriver hvad du vil

```python
# Funktion der beregner gennemsnittet af en liste tal
# Copilot foreslår resten automatisk:
def beregn_gennemsnit(tal: list) -> float:
    if not tal:
        return 0.0
    return sum(tal) / len(tal)
```

Jo mere kontekst der er i filen (variabelnavne, kommentarer, eksisterende funktioner), jo bedre bliver forslagene.

📎 **Illustration:** `modul9-ill2-autocomplete-eksempel.png`
**Titel:** Tab, Esc eller Alt+pil — tre reaktioner
*Kode-editor med Copilot-forslag vist som nedtonet tekst*

---

### Copilot Chat — stil spørgsmål om din kode

Ud over autocomplete har Copilot et **chat-panel** i VS Code's sidebar. Her kan du stille spørgsmål på naturligt sprog om din kode:

- *"Hvad gør denne funktion?"*
- *"Fiks denne fejl for mig"*
- *"Skriv en test til denne klasse"*
- *"Forklar hvad en rekursiv funktion er"*

Copilot Chat forstår hele filen du har åben som kontekst — du behøver ikke kopiere koden ind, det ved det allerede.

Brug `@workspace` for at give Copilot adgang til hele dit projekt på tværs af filer: *"@workspace find alle steder der kalder denne funktion"*.

---

### Inline edits — ret kode direkte

Markér et stykke kode og tryk **Ctrl+I** (eller Cmd+I på Mac) for at åbne inline-editoren. Beskriv hvad du vil lave om:

- *"Gør denne funktion mere effektiv"*
- *"Tilføj fejlhåndtering"*
- *"Oversæt kommentarerne til engelsk"*

Copilot viser forslaget som en **diff** — ændringer markeret med grønt (tilføjet) og rødt (fjernet) — inden du accepterer. Du er altid den der beslutter om ændringen gennemføres.

---

### Copilot vs. manuel kodning

Copilot er et kraftfuldt værktøj, men det er vigtigt at forstå hvad det er:

**Copilot er en co-pilot — ikke en pilot.** Du bestemmer retningen. Copilot hjælper med at skrive hurtigere.

**✅ Copilot vinder til:**
- Gentagne mønstre og boilerplate
- Kendte biblioteker og standard-operationer
- Hurtig prototyping

**⚠️ Vær forsigtig med:**
- Forslag du ikke forstår — acceptér aldrig blind kode
- Sikkerhedskritisk kode — tjek altid selv
- Copilot kan foreslå forældet eller forkert kode

Tommelfingerreglen: **forstå koden inden du accepterer den.** Copilot skal gøre dig hurtigere, ikke erstatte din forståelse.

> 💬 **Ordforklaring:** *Boilerplate* er den gentagne standardkode du skriver på samme måde gang på gang — fx fil-åbning, fejlhåndtering, class-definitioner. *Diff* er en visning der viser præcis hvad der er ændret mellem to versioner.

📎 **Illustration:** `modul9-ill3-copilot-workflow.png`
**Titel:** Kommentar → forslag → godkend
*Workflow: skriv kommentar → Copilot foreslår → gennemgå → acceptér/afvis*

---

### Pris og licens

| Plan | Pris | Inkluderer |
|------|------|----------|
| Gratis | $0 | Begrænsede completions og chat per måned |
| Individual | ~$10/md | Ubegrænset completions og chat |
| Business | ~$19/bruger/md | Team-features, policy-kontrol |
| Studerende | Gratis | Via GitHub Education — tjek om du er berettiget |

For de fleste unge og studerende er det gratis tier eller GitHub Education den rigtige indgang.

📎 **Illustration:** `modul9-ill4-pris-oversigt.png`
**Titel:** Gratis, Individual, Studerende — hvad får du?
*Tre plan-kort: Gratis, Individual, Studerende — med hvad hvert indeholder og pris.*
