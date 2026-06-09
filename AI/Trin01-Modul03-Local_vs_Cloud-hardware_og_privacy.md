## Modul 3: Local vs Cloud — hardware, privacy, GPU/CPU

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul3-ill1 til modul3-ill5 (SVG)

---

### To veje til AI

Når du vil bruge en AI-model, har du grundlæggende to valg: **Lokal** — modellen kører på din egen computer. **Cloud** — modellen kører på en virksomheds servere, du sender din besked over internettet og får svar tilbage.

> **Cloud** er som at bestille mad på restaurant — hurtigt, du behøver ikke lave noget selv, men restauranten ved hvad du bestilte.
> **Lokal** er som at lave mad hjemme — mere forberedelse og kræver et ordentligt køkken, men ingen ved hvad du laver.

📎 **Illustration:** `modul3-ill1-lokal-vs-cloud.png`
**Titel:** To veje til det samme svar
*Split-screen: lokal AI (data forbliver på maskinen, pil vender ind) vs*

---

### Lokal AI — fordele og ulemper

**✅ Fordele:**
- **Privacy** — dine data forlader aldrig din maskine
- **Ingen løbende omkostninger** — gratis efter download
- **Fungerer uden internet** — offline, i tog, på hytten
- **Fuld kontrol** — du vælger model og version

**❌ Ulemper:**
- Kræver hardware (GPU/CPU og nok RAM/VRAM)
- Langsommere end cloud på hjemme-hardware
- Sværere at sætte op end en hjemmeside

> 💬 **Ordforklaring:** *Privacy* handler om hvem der har adgang til dine informationer. Lokal AI betyder at kun du har adgang.

📎 **Illustration:** `modul3-ill2-privacy.png`
**Titel:** Hvad forlader din maskine?
*To scenarier: lokal AI (grøn lås, ingen pil ud) vs*

---

### Cloud AI — fordele og ulemper

**✅ Fordele:**
- Hurtigt og kraftfuldt — kører på enorme serverparker
- Altid opdateret — forbedringer sker automatisk
- Ingen hardware-krav — fungerer på en gammel laptop
- De absolutte topmodeller er kun tilgængelige her

**❌ Ulemper:**
- Dine data behandles af en tredjemand
- Koster penge ved højt forbrug via API
- Kræver internet
- Du er afhængig af andres beslutninger

> 💬 **Ordforklaring:** *API* er en måde at kommunikere med en tjeneste fra et program. *Tredjemand* er en anden virksomhed end dig selv.

---

### Hardware 101 — GPU, CPU, VRAM og RAM

**CPU** (Central Processing Unit) — computerens "hjerne". Alsidig, løser alle slags opgaver, men én ad gangen. Tænk: en meget klog rektor der behandler elever én for én.

**GPU** (Graphics Processing Unit) — grafikkortet. Designet til at beregne tusindvis af ting på én gang. Perfekt til AI. Tænk: en klasse med 3.000 elever der alle løser den samme simple opgave samtidig.

**RAM** — computerens arbejdshukommelse. Jo mere, jo flere ting kan du have i gang på én gang.

**VRAM** — det samme, men dedikeret til GPU'en. Modellen skal passe ind i VRAM for at køre hurtigt på GPU.

> 💬 **Ordforklaring:** *RAM* = hurtig midlertidig hukommelse. *VRAM* = samme koncept, men på GPU'en.

📎 **Illustration:** `modul3-ill3-cpu-gpu-ram-vram.png`
**Titel:** Hardwarens fire roller
*Computerkasse med fire annoterede dele: CPU, GPU, RAM, VRAM — med pil der viser hvilken del modellen kører på.*

---

### Modellens størrelse og hardware-krav

Modeller måles i milliarder parametre (B). Jo større model, jo bedre — men jo mere hardware kræves.

| Størrelse | Hvad kræves | Eksempel |
|-----------|-------------|---------|
| 1–3B | 4 GB RAM | Alt hardware, simple opgaver |
| 7–8B | 8 GB VRAM / 16 GB RAM | God allrounder ← start her |
| 13–14B | 12 GB VRAM / 32 GB RAM | Stærkere reasoning |
| 32–70B | 24+ GB VRAM | Næsten cloud-kvalitet |
| 405B+ | Mange GPU'er | Kun cloud |

📎 **Illustration:** `modul3-ill4-model-storrelse.png`
**Titel:** Størrelse vs. hvad der passer i dit VRAM
*Søjlediagram: 7B, 13B, 34B, 70B modeller vs*

---

### Quantization — større modeller på mindre hardware

Quantization reducerer præcisionen af tallene i modellen fra 16 bits til fx 4 bits (Q4). Som at komprimere et foto — fylder meget mindre, næsten samme kvalitet.

- Llama 3.1 70B original: ~140 GB VRAM
- Llama 3.1 70B Q4: ~40 GB — 75% mindre, ~95% kvalitet

Ollama og LM Studio downloader automatisk gode Q-versioner.

> 💬 **Ordforklaring:** *Quantization* reducerer præcisionen af tallene i en model for at spare plads. *Q4* = 4-bit quantization, *Q8* = 8-bit.

📎 **Illustration:** `modul3-ill5-quantization.png`
**Titel:** Præcision byttet for størrelse
*Samme model i tre størrelser: Q8 (stor, præcis) → Q4 (medio) → Q2 (lille, unøjagtig)*

---

### CPU offloading

Hvis modellen er lidt for stor til VRAM, kan de lag der ikke passer glide over til normal RAM og beregnes på CPU. Lidt langsommere — men giver mulighed for at køre større modeller end GPU ellers ville tillade.

→ Se **Appendix 3: CPU Offloading** for detaljer.
