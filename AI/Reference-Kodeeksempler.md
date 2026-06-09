# Reference Eksempler

Samling af fungerende Python-programmer der understøtter modulernes teori.
Hvert eksempel er selvstændigt og kan køres direkte.

---

## Installation

De fleste eksempler bruger eksterne biblioteker. Installer med pip:

```bash
pip install opencv-python        # Eks. 01 — Ansigtsgenkendelse
pip install tiktoken             # Eks. 02 — Token-tæller
pip install requests             # Eks. 03–XX — API-kald (kommer senere)
```

---

## Oversigt

| Nr. | Fil | Modul | Emne |
|-----|-----|-------|------|
| 01 | `ansigtsgenkendelse.py` | Trin 1, Modul 2 | Deep learning i praksis |
| 02 | `token-taeller.py` | Trin 1, Modul 2 | Token-tæller |
| 03 | *(kommer)* | Trin 3, Modul 15 | Grundstof-gætter med Ollama |
| 04 | *(kommer)* | Trin 3, Modul 15 | Hovedstads-quiz med Ollama |
| 05 | *(kommer)* | Trin 3, Modul 14 | Simpel chatbot i terminalen |

---

## Eks. 01 — Ansigtsgenkendelse

**Fil:** `ansigtsgenkendelse.py`
**Understøtter:** Trin 1, Modul 2 — *Transformers og Deep Learning*
**Kræver:** `pip install opencv-python` + et billede ved navn `billede.jpg`

**Hvad det viser:**
En forud-trænet model genkender ansigter i et billede og tegner en grøn boks
rundt om hvert ansigt. Dette er deep learning i praksis — modellen er trænet
på tusindvis af ansigter og kan nu genkende nye ansigter den aldrig har set.
Præcis den mekanisme der beskrives i Modul 2.

```python
# reference-eksempler/ansigtsgenkendelse.py
# Understøtter Modul 2: Deep Learning og neurale netværk
#
# Installation:
#   pip install opencv-python
#
# Brug:
#   1. Læg et billede ved navn 'billede.jpg' i samme mappe som scriptet
#   2. Kør: python ansigtsgenkendelse.py
#   3. Et vindue åbner med grønne bokse rundt om ansigter
#   4. Tryk en vilkårlig tast for at lukke vinduet
#   5. Resultatet gemmes som 'resultat.jpg'

import cv2

# ── Indlæs den trænede model ──────────────────────────────────────────
# OpenCV har en indbygget model der er trænet til at genkende ansigter.
# Den hedder en "Haar Cascade" — et eksempel på machine learning der er
# trænet på tusindvis af billeder af ansigter (positive eksempler) og
# billeder uden ansigter (negative eksempler).
ansigts_model = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ── Indlæs billedet ───────────────────────────────────────────────────
billede = cv2.imread('billede.jpg')

if billede is None:
    print("Fejl: Kunne ikke finde 'billede.jpg'")
    print("Læg et billede ved navn 'billede.jpg' i samme mappe som scriptet")
    exit()

print(f"Billede indlæst: {billede.shape[1]}x{billede.shape[0]} pixels")

# Konverter til gråtoner — modellen arbejder bedre med gråtoner
graat = cv2.cvtColor(billede, cv2.COLOR_BGR2GRAY)

# ── Find ansigter ─────────────────────────────────────────────────────
# scaleFactor: hvor meget billedet skaleres ned for hvert trin (1.1 = 10%)
# minNeighbors: hvor mange "nabodetektioner" skal til før et ansigt godkendes
#               højere tal = færre falske positiver, men kan misse ansigter
ansigter = ansigts_model.detectMultiScale(
    graat,
    scaleFactor=1.1,
    minNeighbors=5
)

print(f"Fandt {len(ansigter)} ansigt(er) i billedet!")

# ── Tegn en grøn boks rundt om hvert ansigt ───────────────────────────
for (x, y, bredde, hoejde) in ansigter:
    cv2.rectangle(
        billede,
        (x, y),                      # øverste venstre hjørne
        (x + bredde, y + hoejde),    # nederste højre hjørne
        (0, 229, 160),               # farve i BGR-format (grøn)
        2                            # linjetykkelse i pixels
    )

# ── Vis og gem resultatet ─────────────────────────────────────────────
cv2.imshow('Ansigtsgenkendelse — tryk en tast for at lukke', billede)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('resultat.jpg', billede)
print("Resultatet er gemt som 'resultat.jpg'")
```

**Prøv selv:**
- Hvad sker der hvis du ændrer `minNeighbors` til 2? Eller til 10?
- Prøv med et billede med mange mennesker
- Prøv med en tegneserie — genkender den tegne-ansigter?

---

## Eks. 02 — Token-tæller

**Fil:** `token-taeller.py`
**Understøtter:** Trin 1, Modul 2 — *Tokenisering*
**Kræver:** `pip install tiktoken`

**Hvad det viser:**
En interaktiv terminal-app der viser præcis hvordan en LLM opdeler tekst i tokens.
Tokens fremhæves med skiftende farver, og man kan se statistik, context window
visualisering og estimeret cloud-API pris.

**De fire dele:**
1. Fast eksempel: "Kunstig intelligens er sejt!" tokeniseret med farver
2. Sprogsammenligning: dansk vs. engelsk vs. kode vs. tal vs. emoji
3. Context window: visualisering af hvor meget plads tokens fylder
4. Interaktiv: brugeren skriver selv sætninger og ser tokeniseringen live

**Prøv selv:**
- Skriv en lang dansk sætning — er der flere tokens end engelske ord?
- Prøv med kode: `for i in range(10): print(i)`
- Prøv med emojis — hvad sker der?
- Prøv med et enkelt langt ord som "Donaudampfschifffahrtsgesellschaft"

---

## Eks. 03 — Grundstof-gætter *(kommer)*

**Understøtter:** Trin 3, Modul 15 — *AI i dine egne programmer*
Beskriv et grundstofs egenskaber, AI gætter hvilket det er.

---

## Eks. 04 — Hovedstads-quiz *(kommer)*

**Understøtter:** Trin 3, Modul 15 — *AI i dine egne programmer*
Beskriv en hovedstads kendte attraktioner, AI gætter landet.

---

## Eks. 05 — Simpel chatbot i terminalen *(kommer)*

**Understøtter:** Trin 3, Modul 14 — *AI som co-pilot*
While-loop der holder samtalen kørende med Ollama API.
