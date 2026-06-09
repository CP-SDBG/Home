## Modul 17: Skills — lær AI at følge faste instruktioner

> **Målgruppe:** 10–15 år · Har brugt system-prompts · Kender Ollama
> **Illustration-filer:** modul19-ill1 til modul19-ill3 (PNG)
> **Sektioner:** 9 h2 ✅

---

### Hvad er en skill?

Du har sikkert lagt mærke til at AI'en ikke altid svarer på samme måde. Spørger du Claude om det samme to gange, får du to lidt forskellige svar. Det er fint til samtale — men hvis du bygger et program der skal opføre sig *konsistent*, er det et problem.

En **skill** er løsningen. Det er en genanvendelig instruktionspakke der definerer:
- **Hvem AI'en er** — dens rolle og personlighed
- **Hvad den må og ikke må** — begrænsninger og fokusområde
- **Hvordan den svarer** — format, tone, længde

Med en veldefineret skill opfører AI'en sig forudsigeligt og konsistent — uanset hvem der spørger om hvad.

> 💬 **Ordforklaring:** *Skill* er en genanvendelig instruktionspakke til en AI-model. *Konsistent* betyder at AI'en opfører sig på samme måde hver gang. *Template* er en skabelon du kan genbruge og tilpasse.

📎 **Illustration:** `modul17-ill1-skill-opbygning.png`
**Titel:** Samme spørgsmål — to vidt forskellige AI'er
*To chat-vinduer side om side*

---

### System-prompts som fundament

En skill bygger på en **system-prompt** — en skjult instruktion der sættes inden samtalen starter og gælder for hele sessionen.

En stærk system-prompt har tre dele:

**1. Rolle** — hvem er AI'en?
```
Du er en dansk grammatik-lærer med 20 års erfaring.
Du forklarer altid med enkle ord og giver konkrete eksempler.
```

**2. Format** — hvordan svarer den?
```
Svar altid med:
1. En kort forklaring (max 2 sætninger)
2. Et konkret eksempel
3. Et opfølgningsspørgsmål til eleven
```

**3. Begrænsninger** — hvad må den ikke?
```
Svar KUN på spørgsmål om dansk grammatik og sprog.
Hvis eleven spørger om noget andet, sig venligt at du kun hjælper med grammatik.
```

Test og iterér — juster system-prompten til du får præcis den adfærd du vil have.

---

### Skills til specifikke opgaver

Her er eksempler på velfungerende skills:

**Opsummerings-skill:**
```
Du er en ekspert i at opsummere tekster.
Opsummér altid i præcis 3 punkter.
Hvert punkt: max 20 ord.
Brug simpelt sprog — ingen fagtermer.
```

**Kodereview-skill:**
```
Du er en erfaren programmør der laver kodereviews.
Gennemgå altid kode for: 1) Korrekthed, 2) Læsbarhed, 3) Sikkerhed.
Peg på konkrete linjenumre. Forklar hvorfor det er et problem.
Afslut med 3 konkrete forbedringsforslag.
```

**Lektiehjælper-skill:**
```
Du er en tålmodig tutor for elever på 10-15 år.
Forklar aldrig svaret direkte — stil i stedet spørgsmål der leder eleven selv til svaret.
Brug analogier og hverdagseksempler.
```

---

### Genbrugelige skill-templates

En god skill er som god kode: skriv den én gang, brug den mange gange.

Gem dine skills som `.txt`-filer og indlæs dem i din kode:

```python
def indlæs_skill(filnavn: str) -> str:
    with open(f"skills/{filnavn}.txt", "r", encoding="utf-8") as f:
        return f.read()

system_prompt = indlæs_skill("kodereview")

svar = client.messages.create(
    model="claude-haiku-4-5",
    system=system_prompt,
    messages=[{"role": "user", "content": kode_til_review}]
)
```

Versionér dine skills ligesom kode — gem dem i git. En samling af velfungerende skills er ekstremt værdifuld.

---

### Skills i Ollama — Modelfile

Ollama lader dig bygge en **custom model** med en skill indbygget via en `Modelfile`:

```dockerfile
FROM qwen2.5:7b

SYSTEM """
Du er en dansk geografi-lærer.
Du besvarer KUN spørgsmål om geografi — lande, byer, floder, bjerge.
Svar altid med: fakta, en interessant detalje, og ét opfølgningsspørgsmål.
Svar på dansk.
"""
```

Byg og kør din custom model:
```bash
ollama create geo-lærer -f Modelfile
ollama run geo-lærer
```

Nu har du en lokal AI-model med din skill permanent indbygget — ingen grund til at sætte system-prompt hver gang.

📎 **Illustration:** `modul17-ill2-ollama-modelfile.png`
**Titel:** Skill sendt med — vs. skill bagt ind
*To workflows side om side, begge til samme model*

---

### Praktisk eksempel: byg en kodereview-skill

1. **Definer hvad en god kodereview indeholder:**
   - Tjekker for syntaksfejl
   - Tjekker for logiske fejl
   - Vurderer læsbarhed
   - Foreslår forbedringer

2. **Skriv system-prompten:**
```
Du er en erfaren Python-programmør der laver kodereviews for begyndere (10-15 år).
Gennemgå koden og giv feedback i dette format:
✅ Hvad er godt
⚠️ Hvad kan forbedres (med konkret forslag)
❌ Hvad er forkert (med rettelse)
Brug simpelt sprog. Max 5 punkter i alt.
```

3. **Test med eksempelkode og justér** til du er tilfreds

4. **Gem som `skills/kodereview.txt`** — genanvendeligt for altid

📎 **Illustration:** `modul17-ill3-skill-bibliotek.png`
**Titel:** Én fil — ét ændringspunkt
*Én `skills/kodereview.txt`-fil i midten med pile ud til fire brugere: `main.py`, `web_server.py`, `test_runner.py` og `o*
