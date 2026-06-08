# Illustrations Reference — AI·KLAR

Oversigt over alle illustrationer til AI·KLAR (alle trin og moduler).

**Formatkonvention:**
- **PNG (ekstern):** Alle illustrationer er PNG-filer refereret via `<img src="...">` i HTML — filer skal ligge i samme mappe som HTML

---

## Generelle designretningslinjer

### PNG (bruger-lavet)
- Lys baggrund, farverig, begynder-venlig
- Bredt format foretrukket (landscape)

### HTML-indsætning
```html
<div class="illustration-wrap"><img src="filnavn.png" style="width:100%;height:auto;display:block;border-radius:8px;"></div>
```

---

## Trin 1: Grundlæggende (Moduler 1–5)

### Modul 1: Introduktion til AI

#### ✅ modul1-ill1-ai-vs-ikke-ai.png — PNG ekstern
**Titel:** Hvad er AI — og hvad er det ikke?
**Indhold:** To kolonner adskilt af en stiplet linje.
- Venstre (IKKE AI): lommeregner med "2+2=4", tekst "Følger kun præcis de regler den fik", "Intet nyt, ingen læring"
- Højre (AI ✓): kamera der scanner en kat, AI-boble "Det er en kat!", tekst "Lærte selv at genkende katte fra eksempler", "Finder mønstre selv"

#### ✅ modul1-ill2-tidslinje.png — PNG ekstern
**Titel:** AI's historie — fra drøm til virkelighed
**Indhold:** Vandret tidslinje med 4 punkter:
- 1950'erne: "?" ikon, "Kan maskiner tænke?", "Regler kodes i hånden"
- 1997: skakbrik ikon, "Deep Blue slår verdensmester i skak"
- 2012–2017: neural netværk prikker, "Deep learning gennembruddet", "Transformer-arkitektur opfindes"
- 2022–nu: chat-boble ikon (grøn fyldt cirkel), "ChatGPT, Claude og AI for alle", "Du er her! 🎉"

#### ✅ modul1-ill3-programmering-vs-ml.png — PNG ekstern
**Titel:** To måder at lære en computer noget
**Indhold:** To vandrette rækker med flowdiagram (4 bokse + pile):
- Øverst (KLASSISK PROGRAMMERING, grå): Menneske → Regler → Computer → Problem: spammere ændrer ordene 😤
- Nederst (MACHINE LEARNING, grøn): Eksempler (5000 spam + 5000 normal) → AI træner → Model → Virker stadig ✅

#### ✅ modul1-ill4-neuralt-netvaerk.png — PNG ekstern
**Titel:** Sådan ser et neuralt netværk ud
**Indhold:** Klassisk neural network diagram, venstre til højre:
- Input (pixels): 5 cirkler med pixel-ikoner
- Lag 1 (kanter og linjer): 4 cirkler
- Lag 2 (former): 3 cirkler (større)
- Lag 3 (ansigtstræk): 3 cirkler
- Output: 2 cirkler (grønne) "Ansigt 😊" og "Ikke ansigt"
- Linjer mellem alle lag, tykkere mod output
- Bundtekst: "Hvert lag lærer noget mere komplekst end laget før"

#### ✅ modul1-ill5-tre-grunde.png — PNG ekstern
**Titel:** Hvorfor eksploderede AI nu? — Tre grunde
**Indhold:** Tre lodrette kort side om side med + tegn imellem:
- Kort 1 (blå top): Database-ikon, "Mere Data", "Internettet har skabt milliarder af tekster, billeder og videoer", "AI lærer fra data"
- Kort 2 (grøn top): GPU-chip ikon med 🎮, "Hurtigere Hardware", "Grafikkort (GPU) kan lave millioner af beregninger på én gang", "Samme chip som i spil!"
- Kort 3 (rød top): Tandhjul med "T", "Bedre Algoritmer", "Transformer-arkitekturen fra 2017", "Grundlag for ChatGPT m.fl."

#### ✅ modul1-ill6-styrker-svagheder.png — PNG ekstern
**Titel:** Hvad kan AI — og hvad kan det ikke?
**Indhold:** To store kort side om side:
- Venstre (grøn header ✅): 4 rækker med ikon + titel + undertekst: 🔍 Genkende mønstre, ✍️ Generere tekst/billeder/kode, 🌍 Oversætte sprog, 💬 Besvare spørgsmål
- Højre (rød header ⚠️): 4 rækker: 🤔 Forstå verden som menneske, 🎭 Holde styr på hvad der er sandt, 💡 Ægte kreativitet/følelser, 🆕 Ting den ikke er trænet på
- Midten: Lille cirkel med "VS ⚖️"

---

### Modul 2: AI engine og LLM

#### ✅ modul2-ill1-engine-vs-model.png — PNG ekstern
**Titel:** Model og Engine — hvad er forskellen?
**Indhold:** Tre bokse vandret med pile imellem:
- Venstre (blå top): DVD-ikon (cirkel med hul), "Modellen", "fx Llama 3, Qwen 2.5", "En stor fil med tal"
- Pil med tekst "indlæses i"
- Midten (grøn top): DVD-afspiller med knapper og PLAY-display, "Engineen", "fx Ollama, PyTorch", "Kører modellen"
- Pil med tekst "producerer"
- Højre (rød top): TV-skærm med chat-boble "Hej! Jeg er klar til at hjælpe!", "Output", "AI's svar til dig"
- Bundtekst: "Modellen = opskriften · Engineen = køkkenet · Output = maden"

#### ✅ modul2-ill2-token-forudsigelse.png — PNG ekstern
**Titel:** En LLM gætter hele tiden næste ord
**Indhold:** Tre zoner ovenfra:
- Top: Ord-bokse "Jeg går en tur i [?]" — de kendte ord i blå bokse, spørgsmålstegn i stiplet grøn boks
- Midten: Hjerne-ikon 🧠 med pile ned fra spørgsmålstegn og op fra søjlerne
- Bund: Sandsynligheds-søjler: "skoven 42%" (grøn, størst, "← vælges!"), "parken 28%" (blå), "haven 18%", "byen 8%", "mørket 4%"
- Stiplet pil fra "vælges" tilbage til den tomme boks der nu viser "skoven"

#### ✅ modul2-ill3-tokenisering.png — PNG ekstern
**Titel:** Tokenisering — tekst splittes i bidder
**Indhold:** Tre sektioner:
- Top: "INPUT:" — hvid boks med teksten "Kunstig intelligens er sejt!" og en saks ✂️
- Pil ned med tekst "splittes til tokens"
- Midten "TOKENS:" — 7 farvede bokse:
  - Orange (del af ord): "Kunst", "ig", " intel", "ligens"
  - Grøn (helt ord): " er", " sejt"
  - Blå (tegn): "!"
  - Sort boks til højre: "I alt: 7 tokens" (grøn tekst)
- Bund: Farvelegend + context window-bar (7 tokens brugt af 128.000)

#### ✅ modul2-ill4-attention.png — PNG ekstern
**Titel:** Attention — hvad fokuserer "den" på?
**Indhold:** Sætningens ord i individuelle bokse øverst:
- "Katten" (grøn border), "jagede" (grå), "musen" (rød border), "fordi" (grå), "den" (gul border, fremhævet), "var" (grå), "sulten" (grøn border)
- Attention-linjer fra "den":
  - Tyk grøn linje til "Katten" (92%)
  - Medium grøn linje til "sulten" (78%)
  - Tynd rød stiplet linje til "musen" (6%)
  - Meget tynd grå linje til "jagede" (3%)
- Bundforklaring i mørk boks: "Ordet 'den' kigger på alle andre ord... → 'den' = Katten ✓"
- Legend: tyk linje = stærk forbindelse, stiplet = svag

#### ✅ modul2-ill5-embeddings.png — PNG ekstern
**Titel:** Embeddings — ord med ens betydning bor tæt på hinanden
**Indhold:** 2D koordinatsystem med 4 farvede ordklynger:
- 🐾 DYR (grøn zone): hund, kat, fugl, fisk
- 🚗 TRANSPORT (blå zone): bil, tog, cykel, fly
- 🍎 MAD (orange zone): æble, brød, pizza, mælk
- 👑 ROYALT (lilla zone): Konge, Dronning, Mand, Kvinde
- Stiplet linje ml. hund og bil med tekst "langt fra hinanden"
- Mørk formel-boks i hjørnet: "Konge − Mand + Kvinde ≈ Dronning ✓"

#### ✅ modul2-ill6-model-sammenligning.png — PNG ekstern
**Titel:** De store modeller — hvem er hvem?
**Indhold:** 2×2 grid med fire modell-kort:
- Øverste venstre (grøn border): C-cirkel, "Claude / af Anthropic", ☁️ Cloud badge, ✦ 200K tokens, ✦ Analyse og lange tekster, ✦ Multimodal
- Øverste højre (blå border): GPT-cirkel, "GPT-4o / af OpenAI", ☁️ Cloud badge, ✦ Den mest kendte, ✦ Alsidig, ✦ Multimodal
- Nederste venstre (orange border): 🦙 Llama 3 / af Meta, 💻 Lokal badge, 🔓 Open Source badge, ✦ Gratis lokalt, ✦ Næsten cloud-kvalitet
- Nederste højre (rød border): Q-cirkel, "Qwen 2.5 / af Alibaba", 💻 Lokal badge, 🔓 Open Source badge, ✦ Stærk til kodning, ✦ Effektiv hardware-brug
- Bundlinje: "Cloud → hurtigt, kraftfuldt" | "Lokal → privat, gratis"

---

### Modul 3: Local vs Cloud

#### ✅ modul3-ill1-lokal-vs-cloud.png — PNG ekstern
**Titel:** To veje til AI — hvilken vælger du?
**Indhold:** Central computer-boks i midten. To stier:
- Venstre (grøn pil): "Ingen internet" label, lokal PC-boks med 🔒 badge, grøn nøgleords-boks: ✅ Privat, ✅ Gratis drift, ✅ Offline, ⚠️ Kræver hardware
- Højre (blå pil): "via internet" label, sky-boks med ☁️, blå nøgleords-boks: ✅ Hurtigt, ✅ Ingen opsætning, ✅ De bedste modeller, ⚠️ Data til tredjemand
- Bundforklaring i mørk boks: madlavnings-analogien (restaurant vs hjemmelavet)

#### ✅ modul3-ill2-privacy.png — PNG ekstern
**Titel:** Privacy — hvor rejser dine data?
**Indhold:** To store sektioner side om side:
- Venstre "🔒 Lokal AI" (grøn): Flowdiagram Person → Computer → Model, alt inde i grøn stiplet boble "Alt foregår inde i din computer", Hvid boks med ✅ eksempler på hvad man trygt kan spørge om
- Højre "☁️ Cloud AI" (rød): Flowdiagram Person → internet → 🏢 Virksomhedens servere → Model, rød advarsel "⚠️ Dine beskeder kan logges og analyseres", Hvid boks med ❌ ting man skal være forsigtig med

#### ✅ modul3-ill3-cpu-gpu-ram-vram.png — PNG ekstern
**Titel:** Hardware 101 — CPU, GPU, RAM og VRAM
**Indhold:** 2×2 grid:
- Øverste venstre (blå): CPU chip-ikon, 👨‍💼 rektor-analogi, "Meget klog, løser alle slags opgaver — men behandler én ad gangen", "Typisk 8–32 kerner"
- Øverste højre (grøn): GPU med mange små kerner-grid, 👩‍🎓👨‍🎓 klasse-analogi, "Tusindvis af kerner der løser simple opgaver alle på samme tid", "Typisk 3.000–16.000 kerner"
- Nederste venstre (lilla): Skrivebords-ikon med papirer, RAM, "Jo større bord, jo mere kan du have fremme", "Typisk 8–64 GB"
- Nederste højre (orange): Lille skrivebord inde i GPU med "AI MODEL" blok, VRAM, "Modellen SKAL passe ind her for at køre hurtigt", "Typisk 4–24 GB"

#### ✅ modul3-ill4-model-storrelse.png — PNG ekstern
**Titel:** Modellens størrelse og hvad du skal bruge
**Indhold:** Lodret thermometer/søjle til venstre (farvet fra grøn bund til orange top). Fem vandrette rækker:
- 1–3B (grøn): "Lille og hurtig", "4 GB RAM (CPU) · Kører på alt"
- 7–8B (grøn, fremhævet med "⭐ sweet spot"): "God allrounder ← Anbefalet start", "8 GB VRAM / 16 GB RAM · Qwen2.5 7B, Llama 3.1 8B"
- 13–14B (blå): "Stærkere reasoning", "12 GB VRAM / 32 GB RAM"
- 32–70B (orange): "Næsten cloud-kvalitet", "24+ GB VRAM"
- 405B+ (rød): "Kun realistisk i cloud"
- Bundtekst i mørk boks: "Tommelfingerregel: start med 7–8B"

#### ✅ modul3-ill5-quantization.png — PNG ekstern
**Titel:** Quantization — større modeller på mindre hardware
**Indhold:** To søjler side om side med pil imellem:
- Venstre "Original model (16-bit / FP16)": Stort grid af præcise decimaltal, "Hvert tal: 16 bits = høj præcision", filstørrelse-bar: "~140 GB" (fuld blå bar)
- Pil med "Q4 quantize" i mørk boks
- Højre "Q4 model (4-bit)": Grovere tal, "Hvert tal: 4 bits = lidt lavere præcision", filstørrelse-bar: "~40 GB" (kort grøn bar), "75% mindre! Kører på RTX 4090"
- Bund: Kvalitets-sammenligning: "Original 100%" vs "Q4 ~95%"

---

### Modul 4: Processen fra forespørgsel til svar

#### ✅ modul4-ill1-pipeline-overblik.png — PNG ekstern
**Titel:** Fra spørgsmål til svar — hele rejsen
**Indhold:** Vandret pipeline med 6 nummererede trin, forbundet med pile:
1. **Input** (tastatur-ikon): "Din tekst: Hvad er verdens højeste bjerg?"
2. **Tokenisering** (saks-ikon): teksten opdeles i tokens
3. **Embeddings** (koordinat-ikon): tokens → tal/vektorer
4. **Attention** (øje-ikon): alle tokens kigger på hinanden
5. **Generering** (tandhjul-ikon): token-for-token output
6. **Output** (chat-ikon): "Mount Everest er verdens højeste bjerg..."
Under hele pipelinen: en lang grøn pil venstre til højre. Farver: trin 1–2 = blå, trin 3–4 = lilla, trin 5–6 = grøn.

#### ✅ modul4-ill2-token-by-token-generation.png — PNG ekstern
**Titel:** Svaret bygges op ét token ad gangen
**Indhold:** Vertikal sekvens der viser svar der vokser token for token:
- "Mount" → "Mount Everest" → "Mount Everest er" → osv.
- Hvert nyt token markeret grønt
- Pile fra nyt token tilbage til alle tidligere tokens — viser kontekst-opslag
- Bundtekst: "Hvert token = én beregning · Længere svar = flere beregninger"

#### ✅ modul4-ill3-temperature.png — PNG ekstern
**Titel:** Temperature — kreativ eller fokuseret?
**Indhold:** To sektioner side om side:
- Venstre "🌡️ Lav temperature (0.1)": Søjlediagram ét ord dominerer (85%). Output: "Mount Everest er 8.849 meter højt." (faktuel)
- Højre "🎨 Høj temperature (1.0)": Søjlediagram jævn fordeling. Output: "Tænk på bjerget som et svar på universets største spørgsmål..." (kreativ)
- Bundtekst: "Lav = præcis og forudsigelig · Høj = kreativ og overraskende"

#### ✅ modul4-ill4-context-window.png — PNG ekstern
**Titel:** Context window — hvad kan modellen huske?
**Indhold:** Lang samtale-scroll, vindue fremhæver kun de nyeste beskeder. Øverste beskeder nedtonet: "Modellen ser ikke dette længere". Til højre: tre modeller med bar for vinduesstørrelse:
- Llama 3 (lokal): "8.000 tokens"
- GPT-4o: "128.000 tokens"
- Claude: "200.000 tokens ≈ en hel roman"

#### ✅ modul4-ill5-hallucination.png — PNG ekstern
**Titel:** Hallucination — når AI gætter forkert
**Indhold:** Chat-mockup:
- Bruger: "Hvornår udgav Astrid Lindgren bogen 'Brødrene Bjørnedal'?"
- AI svarer selvsikkert med opdigtet svar — fremhævet med rød boks og ❌ "Denne bog eksisterer ikke! AI opfandt den."
- Forklarings-boks: "AI genererer sandsynlig tekst — ikke nødvendigvis sand tekst"
- Grøn boks: "✅ Tjek altid vigtige fakta i andre kilder"

---

### Modul 5: Prismodeller

#### ✅ modul5-ill1-token-priser.png — PNG ekstern
**Titel:** Hvad koster et token?
**Indhold:**
- Top: Besked sendes (200 input tokens) og svar returneres (150 output tokens)
- Midten: Prisberegning: 200 × $0.000003 = $0.0006, 150 × $0.000015 = $0.0023, total ~$0.003
- Bund: Søjlediagram input vs output priser for 4 modeller (Haiku, Sonnet, GPT-4o mini, GPT-4o)
- Bundtekst: "1 kop kaffe ≈ pris for ~50.000 GPT-4o mini beskeder"

#### ✅ modul5-ill2-abonnement-vs-api.png — PNG ekstern
**Titel:** Abonnement eller API — hvornår vælger du hvad?
**Indhold:** To kort side om side:
- Venstre "📅 Abonnement": Fast pris, check-liste med hvornår det giver mening. Pris-badge: "$20/md"
- Højre "🔌 API (pay-per-use)": Betaler pr. brug, check-liste. Pris-badge: "Fra $0.0002/besked"
- Bund: "Ny bruger? Start med gratis tier → opgrader kun hvis du har brug for det"

#### ✅ modul5-ill3-pris-sammenligning.png — PNG ekstern
**Titel:** Hvad koster et år med AI?
**Indhold:** Tre lodrette kort:
- Lokal (grøn): 🖥️ "~$10–20/år (kun strøm)", ✅ Gratis modeller, ⚠️ Kræver hardware
- Cloud abonnement (blå): ☁️ "~$240/år ($20/md)", ✅ Bedste modeller, ⚠️ Fast udgift
- Cloud API (lilla): 🔌 "~$5–50/år (typisk brug)", ✅ Fleksibel, ⚠️ Kræver programmering
- Gratis tier fremhævet som startpunkt for unge/studerende

---

## Trin 2: Interfaces og værktøjer (Moduler 6–12)

### Modul 6: Web-interfaces — ChatGPT, Claude, OpenRouter

#### ✅ modul6-ill1-web-interface-oversigt.png
**Titel:** Hvad sker der når du skriver til en LLM?
**Indhold:** Browser → internet-pil → AI-server-boks → svar-pil tilbage til browser. Vis login-symbol og historik-symbol på serverens side. Under: lille advarsel-boks “dine beskeder sendes over internettet”.

#### ✅ modul6-ill2-chatgpt-interface.png
**Titel:** ChatGPT — hvad kan det?
**Indhold:** Mockup af ChatGPT-interface med: tekstboks, filupload-ikon, websøgnings-ikon og GPT-4o label. Pile der peger på de vigtigste features med korte labels.

#### ✅ modul6-ill3-claude-interface.png
**Titel:** Claude.ai — hvad kan det?
**Indhold:** Mockup af Claude-interface. Fremhæv 200K context window som en lang bar sammenlignet med andre modellers kortere bar. Label: “svarende til en hel roman”.

#### ✅ modul6-ill4-openrouter-model-valg.png
**Titel:** OpenRouter — ét sted, alle modeller
**Indhold:** Ét interface i midten med pile til mange model-logoer rundt om (GPT, Claude, Llama, Mistral, Gemini). Prissammenligning-tabel under. Label: “ét API-key til dem alle”.

#### ✅ modul6-ill5-web-vs-api.png
**Titel:** Web-interface vs. API — hvornår bruger du hvad?
**Indhold:** To kolonner. Venstre (browser-ikon): klik og skriv, ingen kode, manuel. Højre (kode-ikon): Python/JS, automatisk, skalerbar. Under hver: checkmarks for hvornår det giver mening.

---

### Modul 7: Ollama — kør AI-modeller lokalt

#### ✅ modul7-ill1-ollama-arkitektur.png
**Titel:** Ollama — hvad er det og hvad løser det?
**Indhold:** Tre lag lodret stablet:
- Top: Programmer der bruger AI (terminal, browser, Python-script)
- Midt: Ollama-server (grøn boks) med label “lokal server på port 11434”
- Bund: Model-filer (Qwen, Llama, Mistral som filbokse)
- Pile op og ned der viser data-flow. Til venstre: “før Ollama — kompleks opsætning” (rod af pile og fejl-ikoner). Til højre: “med Ollama — én kommando” (enkelt pil ned).

#### ✅ modul7-ill2-ollama-kommandoer.png
**Titel:** De vigtigste Ollama-kommandoer
**Indhold:** 5 vandrette rækker, hver med:
- Kommando i monospace grøn kode-boks (fx `ollama pull qwen2.5:7b`)
- Ikon der illustrerer handlingen (download-pil, play-knap, liste, skraldespand, info-i)
- Kort forklaring (fx “Download en model til din computer”)
- Eksempel på output i grå boks under
Bundlinje: “Brug `ollama list` jævnligt for at holde styr på plads”

#### ✅ modul7-ill3-lokal-api-server.png
**Titel:** Ollama som lokal API-server
**Indhold:** Central boks “Ollama :11434” i midten. Fire klienter forbundet med pile:
- Terminal (sort vindue-ikon)
- Python-script (Python-logo)
- Open WebUI (browser-ikon)
- VS Code extension (editor-ikon)
Over pilen: “HTTP request”. Under: “HTTP response”. Mørk boks i hjørnet: “localhost — trafik forlader aldrig din maskine 🔒”

#### ✅ modul7-ill4-model-library.png
**Titel:** Model library — hvad vælger du?
**Indhold:** Tabel-layout med 6 rækker (en per model-familie):
- Kolonne 1: Model-navn + logo/farve-ikon
- Kolonne 2: Størrelse (fx 3B / 7B / 14B som farvede badges)
- Kolonne 3: Bedst til (fx “God allrounder”, “Kodning”, “Reasoning”)
- Fremhæv “Qwen 2.5 7B” med ⭐ “Anbefalet start” badge
- Bundlinje: “Start med 7B — opgrader kun hvis du skal bruge mere”

---

### Modul 8: Lokale interfaces — LM Studio, Open WebUI, Msty

#### ✅ modul8-ill1-lokal-interface-oversigt.png
**Titel:** Lokalt interface — hvad er det?
**Indhold:** Lagdiagram med tre niveauer (top til bund):
- Top (lys baggrund): Grafisk interface — tre ikoner side om side: LM Studio (desktop), Open WebUI (browser), Msty (desktop)
- Midt (grøn baggrund): Ollama / model-engine med gear-ikon
- Bund (blå baggrund): Model-filer (Qwen, Llama, Mistral)
- Pile ned og op. Højre side: stor grøn boks “Alt foregår på din computer 🔒”

#### ✅ modul8-ill2-sammenligning.png
**Titel:** LM Studio vs Open WebUI vs Msty — hvornår bruger du hvad?
**Indhold:** Tre kort side om side, hvert med farvet header:
- LM Studio (blå): “Fulld kontrol” — ikon: desktop-app, ✅ Model browser, ✅ Parameter-justering, ✅ Lokal API-server, Target: avancerede brugere
- Open WebUI (grøn): “ChatGPT-følelsen, lokalt” — ikon: browser, ✅ Historik, ✅ Flere brugere, ✅ Model-skift, Target: server / homelab
- Msty (lilla): “Bare kom i gang” — ikon: desktop-app, ✅ Auto-forbinder til Ollama, ✅ Ingen konfiguration, Target: begyndere

#### ✅ modul8-ill3-hardware-krav.png
**Titel:** Hardware-krav til lokale modeller
**Indhold:** Vandret bjælke-diagram — tre niveauer markeret med farver:
- Rød zone: “Minimum — 8 GB RAM, CPU-kørsel” — ikon: gammel laptop — “3B model, langsomt”
- Gul zone: “Anbefalet — 16 GB RAM + 8 GB VRAM” — ikon: gaming-PC — “7B model, hurtigt”
- Grøn zone: “Komfortabelt — 32 GB RAM + 12–16 GB VRAM” — ikon: workstation — “13–14B model”
Bundtekst: “Uden GPU: 5–20x langsommere — muligt men ikke ideelt”

#### ✅ modul8-ill4-lokal-vs-cloud-fordele.png
**Titel:** Lokal AI — fordele og ulemper
**Indhold:** To kolonner:
- Venstre “🔒 Lokal AI” (grøn header): ✅ Privacy — data forlader ikke maskinen, ✅ Offline, ✅ Ingen løbende omkostninger, ✅ Fuld kontrol, ⚠️ Kræver hardware, ⚠️ Initial opsætning
- Højre “☁️ Cloud AI” (blå header): ✅ Hurtigt og kraftfuldt, ✅ Ingen hardware-krav, ✅ Altid opdateret, ⚠️ Data til tredjemand, ⚠️ Koster penge ved højt forbrug

---

### Modul 9: GitHub Copilot — AI i din editor

#### ✅ modul9-ill1-copilot-i-vscode.png
**Titel:** GitHub Copilot i VS Code
**Indhold:** Mockup af VS Code-editor:
- Venstre: kode med nedtonet grå autocomplete-forslag synligt
- Højre sidebar: Copilot Chat-panel åbent med en samtale
- Pile og labels der peger på: “Autocomplete”, “Chat-panel”, “Inline edit (Ctrl+I)”
- Bundlinje: “Copilot er en co-pilot — ikke en pilot”

#### ✅ modul9-ill2-autocomplete-eksempel.png
**Titel:** Autocomplete — kodeforslag mens du skriver
**Indhold:** Kode-editor-udsnit med:
- Kommentar øverst (grøn): `# Funktion der beregner gennemsnittet af en liste tal`
- Første linje skrevet af bruger: `def beregn_gennemsnit(`
- Resten af funktionen vist som nedtonet grå Copilot-forslag
- Tre pile med labels: `Tab → acceptér`, `Esc → afvis`, `Alt+] → næste forslag`

#### ✅ modul9-ill3-copilot-workflow.png
**Titel:** Copilot-workflow fra kommentar til færdig kode
**Indhold:** Vandret sekvens med 4 trin og pile imellem:
1. “Skriv kommentar” — ikon: tastatur — eksempel: `# Sorter liste og fjern dubletter`
2. “Copilot foreslår” — ikon: gul lysære — nedtonet kode dukker op
3. “Gennemgå forslaget” — ikon: øje — “Forstå inden du acceptérer!”
4. “Acceptér eller afvis” — ikon: grøn flueben / rød kryds — Tab / Esc
Bundlinje: “Gennemgå altid koden inden accept” (rød fremhævning)

#### ✅ modul9-ill4-pris-oversigt.png
**Titel:** GitHub Copilot — pris og licens
**Indhold:** Tre plan-kort vandret:
- Grå kort “Gratis”: $0, begrænsede completions per måned, godt til at prøve
- Blå kort “Individual”: ~$10/md, ubegrænset, alle features
- Grøn kort “Studerende”: GRATIS badge i rødt, “Via GitHub Education”, “tjek om du er berettiget →”
Bundlinje: “Studerende med .edu-mail — tjek GitHub Education inden du betaler”

---

### Modul 10: OpenCode — AI-assisteret kodning i terminalen

#### ✅ modul10-ill1-opencode-oversigt.png
**Titel:** OpenCode — AI agent der ser hele dit projekt
**Indhold:** To sider:
- Venstre “Copilot”: editor med én fil åben, pil markerer “ser kun denne fil”
- Højre “OpenCode”: terminal med mappetrae vist, pile ud til mange filer, label “forstår hele projektet”
Under: workflow-pile → “Naturligt sprog ind” → “Filer læses” → “Diff vises” → “Du godkender”

#### ✅ modul10-ill2-opencode-workflow.png
**Titel:** OpenCode — workflow fra instruktion til kørende kode
**Indhold:** Lodret sekvens — 4 trin med terminal-mockup:
1. Bruger skriver: `> Tilføj email-validering til auth.py`
2. OpenCode: “Scanner projekt...” + mappetræ vist
3. Diff-visning: grønne linjer (tilføjet) og røde linjer (fjernet)
4. Prompt: “Godkend ændringer? [j/n]” — grøn j-knap fremhævet

#### ✅ modul10-ill3-cloud-vs-lokal-kodning.png
**Titel:** Cloud vs. lokal model til kodning
**Indhold:** To stier fra “OpenCode”-boksen i midten:
- Venstre sti (blå): “Cloud” — ikon: sky — ✅ Hurtigst og smartest, ✅ Komplekse opgaver, ⚠️ Koster penge, ⚠️ Kode sendes til ekstern server
- Højre sti (grøn): “Lokal (Ollama)” — ikon: computer — ✅ Gratis, ✅ Fuldt privat 🔒, ⚠️ Langsommere, ⚠️ Kræver god hardware
Bundlinje: “Fortrolig kode? Altid lokal.”

---

### Modul 11: Pi Agent — letvægts AI coding agent

#### ✅ modul11-ill1-pi-agent-oversigt.png
**Titel:** Pi Agent — letvægts terminal-agent
**Indhold:** Terminal-vindue med Pi Agent i gang:
- Øverst: projekt-mappe vises (`/mit-projekt`)
- Bruger skriver: `> Tilføj docstrings til alle funktioner i utils.py`
- Pi Agent: “Læser utils.py...”, “Forslår 3 ændringer”
- Diff vist med grønne tilføjelser
- Prompt: “Godkend? [j/n]”
Højre side: tre labels med pile — “Laser-fokus”, “Letvægts”, “Virker med Ollama”

#### ✅ modul11-ill2-agent-sammenligning.png
**Titel:** Pi Agent vs OpenCode vs Claude Code
**Indhold:** Tre kort side om side:
- Pi Agent (lilla): “Letvægts” — ✅ Simpel opsætning, ✅ Lokal-model fokus, ✅ Få afhængigheder, ❌ Færre features
- OpenCode (grøn): “Bred support” — ✅ Mange modeller, ✅ Aktivt community, ✅ Fuld feature-set, ❌ Mere kompleks
- Claude Code (blå): “Officiel” — ✅ Tæt Claude-integration, ✅ Officiel support, ✅ Stor community, ❌ Primært cloud
Bund: “Alle tre: terminal-baserede, arbejder med hele projekter, naturligt sprog”

---

### Modul 12: Vælg den rigtige model til opgaven

#### ✅ modul12-ill1-model-landskab.png
**Titel:** AI-model landskabet — overblik
**Indhold:** 2D diagram med to akser:
- X-akse: Lokal ↔ Cloud
- Y-akse: Lille/hurtig ↔ Stor/kraftfuld
Modeller placeret som farvede cirkler:
- Lokal/lille: Qwen 2.5 3B, Gemma 3 4B (grøn)
- Lokal/stor: Qwen 2.5 14B, DeepSeek-R1 14B (blå)
- Cloud/hurtig: GPT-4o mini, Claude Haiku (gul)
- Cloud/kraftfuld: Claude Sonnet, GPT-4o, o3 (rød)
Farve-legend og “sweet spot” markeret

#### ✅ modul12-ill2-benchmarks.png
**Titel:** Benchmarks — sådan måles modeller
**Indhold:** Gruperet søjlediagram — 6 modeller på X-aksen, tre farvede søjler per model:
- Grøn søjle: MMLU (generel viden)
- Blå søjle: HumanEval (kodning)
- Orange søjle: MATH (matematik)
Advarsel-boks under: “⚠️ Benchmarks måler specifikke ting — test altid på dine egne use cases”

#### ✅ modul12-ill3-valg-guide.png
**Titel:** Vælg den rigtige model — step by step
**Indhold:** Flowdiagram (top til bund):
- Start: “Hvad er opgaven?”
- Forgrening 1: Kodning → “Cloud: Claude Sonnet / Lokal: Qwen2.5-Coder”
- Forgrening 2: Skriving → “Cloud: GPT-4o / Lokal: Mistral 7B”
- Forgrening 3: Langt dokument → “Claude (200K)”
- Forgrening 4: Matematik/logik → “Cloud: o3 / Lokal: DeepSeek-R1”
- Forgrening 5: Hurtigt og billigt → “GPT-4o mini / Qwen 2.5 3B”
Farve-kode: grøn = lokal, blå = cloud

#### ✅ modul12-ill4-model-sammenligning-tabel.png
**Titel:** Komplet model-sammenligning
**Indhold:** Tabel med 7 rækker (en per model) og 5 kolonner:
- Model-navn + ikon
- Cloud ☁️ eller Lokal 💻 badge
- Bedst til (2–3 nøgleord)
- Context window
- Pris (gratis / $/md / $/token)
Fremhæv “Anbefalet start” badge på Claude Sonnet og Qwen 2.5 7B

| Fil | Modul | Status |
|-----|-------|--------|
| modul6-ill1-web-interface-oversigt.png | 6 | ✅ |
| modul6-ill2-chatgpt-interface.png | 6 | ✅ |
| modul6-ill3-claude-interface.png | 6 | ✅ |
| modul6-ill4-openrouter-model-valg.png | 6 | ✅ |
| modul6-ill5-web-vs-api.png | 6 | ✅ |
| modul7-ill1-ollama-arkitektur.png | 7 | ✅ |
| modul7-ill2-ollama-kommandoer.png | 7 | ✅ |
| modul7-ill3-lokal-api-server.png | 7 | ✅ |
| modul7-ill4-model-library.png | 7 | ✅ |
| modul8-ill1-lokal-interface-oversigt.png | 8 | ✅ |
| modul8-ill2-sammenligning.png | 8 | ✅ |
| modul8-ill3-hardware-krav.png | 8 | ✅ |
| modul8-ill4-lokal-vs-cloud-fordele.png | 8 | ✅ |
| modul9-ill1-copilot-i-vscode.png | 9 | ✅ |
| modul9-ill2-autocomplete-eksempel.png | 9 | ✅ |
| modul9-ill3-copilot-workflow.png | 9 | ✅ |
| modul9-ill4-pris-oversigt.png | 9 | ✅ |
| modul10-ill1-opencode-oversigt.png | 10 | ✅ |
| modul10-ill2-opencode-workflow.png | 10 | ✅ |
| modul10-ill3-cloud-vs-lokal-kodning.png | 10 | ✅ |
| modul11-ill1-pi-agent-oversigt.png | 11 | ✅ |
| modul11-ill2-agent-sammenligning.png | 11 | ✅ |
| modul12-ill1-model-landskab.png | 12 | ✅ |
| modul12-ill2-benchmarks.png | 12 | ✅ |
| modul12-ill3-valg-guide.png | 12 | ✅ |
| modul12-ill4-model-sammenligning-tabel.png | 12 | ✅ |

---

## Trin 3: Byg selv (Moduler 13–17)

### Modul 13: Vibe coding

#### ✅ modul13-ill1-vibe-coding-tankegang.png
**Titel:** Samme mål — to helt forskellige tankegange
**Indhold:** En færdig vejr-app på en skærm står i midten. To tankebobler fører hen til den:
- Venstre boble (klassisk programmering): fyldt med kode-syntax, funktionsnavne, pile og tekniske begreber — en rodet mentalt landkort
- Højre boble (vibe coding): kun naturligt sprog “lav en side der viser vejret— temperatur og et ikon”, rød/grøn feedback-boks, mobilvisning
Under midterbilledet: lille arkitekt-ikon + bygmester-ikon med tekst “du bestemmer hvad — AI bygger hvordan”
**Formål:** Visualiserer at resultatet er det samme, men den mentale model er fundamentalt forskellig — understøtter pointe om resultattænkning frem for implementation

#### ✅ modul13-ill2-iterativ-tilgang.png
**Titel:** Fra blank side til færdig quiz — 4 prompts, 25 minutter
**Indhold:** Vandret filmstrimmel med 4 frames, forbundet med pile:
- Frame 1: Blank HTML → chat-boble “Lav quiz med ét spørgsmål” → mini-browser: grim men fungerende quiz
- Frame 2: chat-boble “Tilføj score-tæller” → mini-browser: quiz + “2 af 5 rigtige” øverst
- Frame 3: chat-boble “mørk baggrund, grønne knapper” → mini-browser: styled quiz
- Frame 4: chat-boble “10 spørgsmål mere + afslutningsbesked” → mini-browser: færdig quiz
Under strimlen: “Gem quiz-v1.html efter frame 1 — quiz-v2.html efter frame 2” med lille diskette-ikon
**Formål:** Gør den iterative arbejdsproces konkret og håndgribelig — tekstens punktliste føles abstrakt, illustrationen viser det faktiske resultat af hvert trin

#### ✅ modul13-ill3-fejlhaandtering.png
**Titel:** Anatomien af en god fejlrapport
**Indhold:** To chat-vinduer side om side:
- Venstre (rød header “Dårlig fejlrapport”): Bruger skriver “det virker ikke når jeg klikker”. AI svarer: “Kan du give mere information om hvad der sker?”. Spildt udveksling markeret med rød pil.
- Højre (grøn header “God fejlrapport”): Bruger indsætter fuld stack trace med kontekst. Stack trace annoteret med pile der peger på:
  - “HVAD gik galt: TypeError”
  - “HVOR i koden: quiz.js linje 23”
  - “HVORNÅR: ved klik på knap”
Bunder med lille guide: “F12 i Chrome → Console → kopiér alt”
**Formål:** Viser hvad en fejlbesked indeholder og hvorfor hver del hjælper — understøtter pointe om at omformulering mister information

### Modul 14: API co-pilot

#### ✅ modul14-ill1-api-hvad-er-det.png
**Titel:** To veje ind i køkkenet
**Indhold:** Split-screen: venstre side viser en person der manuelt tasker på claude.ai i en browser. Højre side viser en Python-fil med `client.messages.create(...)` der sender en request over internettet. Begge sider peger på den samme AI-sky i midten — to veje, samme model.
**Formål:** Visualisér kontrasten — teksten forklarer hvad en API *er*, illustrationen viser at det er *den samme AI* som du allerede kender, bare tilgået på en anden måde.

#### ✅ modul14-ill2-api-noegle-sikkerhed.png
**Titel:** Nøglen i pengeskabet vs. nøglen under dørmåtten
**Indhold:** To scenarier side om side. Venstre (rød ramme): kode med `api_key="sk-ant-xxx"` direkte i Python-fil, en figur med "hacker" kan se den på GitHub. Højre (grøn ramme): `.env`-fil med nøglen, `.gitignore` blokerer upload, kun dit program kan læse den.
**Formål:** Gør sikkerhedsreglen konkret — ikke bare "del ikke nøglen" men *hvad der konkret sker* hvis du gør det forkert vs. rigtigt.

#### ✅ modul14-ill3-konversationshistorik.png
**Titel:** Den voksende pakke
**Indhold:** Tre HTTP-kald vist som pakker der sendes. Kald 1: pakke med 1 besked. Kald 2: pakke med 3 beskeder (de 2 fra kald 1 + ny). Kald 3: pakke med 5 beskeder. Pakkestørrelse vokser visuelt. Token-tæller ved siden af viser stigende tal.
**Formål:** Konkretisér processen — teksten forklarer at historik sendes med, illustrationen viser *konsekvensen*: pakken vokser, tokens stiger, pris stiger.

### Modul 15: Python + LLM API

#### ✅ modul15-ill1-ai-som-funktion.png
**Titel:** Én funktion, uendelige muligheder
**Indhold:** `spørg_ai()` i centrum med 4 pile ud til 4 forskellige apps: grundstof-gætter, chatbot, quiz-generator, sentiment-analysator. Hvert app-navn i en lille boks med et enkelt ikon.
**Formål:** Teksten forklarer HVAD en AI-funktion er. Illustrationen viser HVAD DER BLIVER MULIGT — composability: ét tool, fire programmer.

#### ✅ modul15-ill2-python-ollama-kode.png
**Titel:** Hvad sker der indeni ollama.chat()?
**Indhold:** Den usynlige vej annoteret trin for trin: Python-kode → HTTP POST til port 11434 → Ollama-process → qwen-model i RAM → token-generering (lille loop-pil) → HTTP response → Python modtager string. Hvert trin har en kort label.
**Formål:** Teksten viser HVORDAN man kalder funktionen. Illustrationen viser HVAD DER SKER INDENI — gør black box synlig for begyndere.

#### ✅ modul15-ill3-praktiske-eksempler.png
**Titel:** Anatomien i en god prompt
**Indhold:** Grundstof-gætter-prompten vist som en tekstblok med farvede annoterings-pile: grøn pil → "Rolle: kemi-ekspert", blå pil → "Kontekst: elevens beskrivelse", gul pil → "Instruktion: gæt", lilla pil → "Outputformat: navn + symbol + sætning".
**Formål:** Teksten viser kode-eksemplet. Illustrationen forklarer DESIGNBESLUTNINGERNE i prompten — hvorfor hver del er der.

### Modul 16: RAG

#### ✅ modul16-ill1-rag-pipeline.png
**Titel:** Låsen der åbnes
**Indhold:** To versioner af samme spørgsmål side om side. UDEN RAG: bruger spørger → AI hallucinerer et forkert svar (rød ramme). MED RAG: bruger spørger → chunk hentes fra dokumentarkiv → AI svarer korrekt fra dokumentet (grøn ramme).
**Formål:** Teksten forklarer HVAD RAG er. Illustrationen viser det KONKRETE PROBLEM det løser — fejl vs. korrekt svar.

#### ✅ modul16-ill2-chunking-overlap.png
**Titel:** Nøglesætningen der går tabt
**Indhold:** En tekstblok med en vigtig sætning der falder præcis på grænsen mellem chunk A og chunk B. Øverst (rød): ingen overlap → sætningen er klippet midt over i begge chunks, AI kan ikke bruge den. Nederst (grøn): med overlap → sætningen er hel i begge chunks.
**Formål:** Teksten forklarer overlap-parameter. Illustrationen viser KONSEKVENSEN af at undlade overlap — tabt information.

#### ✅ modul16-ill3-rag-use-cases.png
**Titel:** Samme arkitektur, fra 5 noter til 50.000 dokumenter
**Indhold:** Venstre: en elev med 5 noter → ChromaDB lokal → Ollama → AI svarer. Højre: en virksomhed med 50.000 dokumenter → ChromaDB/Pinecone → cloud-API → AI svarer. Kode-mønstret er identisk begge steder — vist med "samme kode" label.
**Formål:** Teksten viser use cases. Illustrationen viser SKALERBARHEDEN — at det samme mønster virker fra hobbyprojekt til produktion.

### Modul 17: Agenter

#### 🔲 modul17-ill1-agent-vs-chatbot.png
**Titel:** 12 manuelle trin vs. ét agent-kald
**Indhold:** Opgaven „research 3 frameworks og gem fil“ vist som manuel tjekliste med 12 nummererede bokse (åbn browser, google, klik, læs, noter...) på venstre side. Højre side: én linje kode `kør_agent("...")`. Antallet 12 vs 1 fremhævet.
**Formål:** Teksten forklarer HVAD en agent er. Illustrationen gør MÆNGDEN AF ARBEJDE konkret — ikke et arkitekturdiagram.

#### 🔲 modul17-ill2-tools-function-calling.png
**Titel:** Det usynlige JSON-kald
**Indhold:** Sekvens i tre trin: 1) AI'en genererer JSON: `{"name": "søg_web", "input": {"query": "Python frameworks"}}` → 2) Python parser og kalder `udfør_tool("søg_web", {"query": "..."})` → 3) Python returnerer string „Django, Flask...“ tilbage til AI. Hvert trin annoteret med hvad der sker.
**Formål:** Teksten viser tool-definitioner og -implementering. Illustrationen viser DEN USYNLIGE PROTOKOL imellem dem — hvad AI'en faktisk sender og modtager.

#### 🔲 modul17-ill3-react-loop.png
**Titel:** Agentens logbog
**Indhold:** Et konkret kørende transcript som terminal-output: `[THOUGHT] Jeg skal søge...` / `[ACTION] søg_web("Python frameworks")` / `[OBSERVATION] Django, Flask...` / `[THOUGHT] Nu skal jeg gemme...` / `[ACTION] gem_fil(...)` / `[FINAL] Færdig`. Ligner debugger-output.
**Formål:** Teksten viser ReAct-mønsteret abstrakt. Illustrationen gør LØKKENS KONKRETE FORLØB læseligt — hvad agenten faktisk tænker og gør.

| Fil | Modul | Status |
|-----|-------|--------|
| modul13-ill1-vibe-coding-tankegang.png | 13 | ✅ Uploadet |
| modul13-ill2-iterativ-tilgang.png | 13 | ✅ Uploadet |
| modul13-ill3-fejlhaandtering.png | 13 | ✅ Uploadet |
| modul14-ill1-api-hvad-er-det.png | 14 | ✅ Uploadet |
| modul14-ill2-api-noegle-sikkerhed.png | 14 | ✅ Uploadet |
| modul14-ill3-konversationshistorik.png | 14 | ✅ Uploadet |
| modul15-ill1-ai-som-funktion.png | 15 | ✅ Uploadet |
| modul15-ill2-python-ollama-kode.png | 15 | ✅ Uploadet |
| modul15-ill3-praktiske-eksempler.png | 15 | ✅ Uploadet |
| modul16-ill1-rag-pipeline.png | 16 | ✅ Uploadet |
| modul16-ill2-chunking-overlap.png | 16 | ✅ Uploadet |
| modul16-ill3-rag-use-cases.png | 16 | ✅ Uploadet |
| modul17-ill1-agent-vs-chatbot.png | 17 | 🔲 Mangler |
| modul17-ill2-tools-function-calling.png | 17 | 🔲 Mangler |
| modul17-ill3-react-loop.png | 17 | 🔲 Mangler |

---

## Trin 4: Avanceret (Moduler 18–19)

### Modul 18: Skills

#### 🔲 modul18-ill1-skill-opbygning.png
**Indhold:** Tre byggeklodser: Rolle + Format + Begrænsninger → Skill. Eksempel på system-prompt der kombinerer alle tre.

#### 🔲 modul18-ill2-ollama-modelfile.png
**Indhold:** Modelfile struktur: FROM model + SYSTEM prompt → ollama create → custom model klar til brug.

### Modul 19: MCP

#### 🔲 modul19-ill1-mcp-arkitektur.png
**Indhold:** MCP client (AI) ↔ MCP protocol ↔ MCP servere (filer, GitHub, database, web). USB-analogi vist.

#### 🔲 modul19-ill2-mcp-servere-oversigt.png
**Indhold:** Grid af MCP-server ikoner: filsystem, GitHub, database, web, kalender, Slack — med kort beskrivelse.

#### 🔲 modul19-ill3-mcp-integration.png
**Indhold:** Samme MCP-servere (filsystem, GitHub, DB) forbundet til Claude Desktop, OpenCode og Pi Agent.

| Fil | Modul | Status |
|-----|-------|--------|
| modul18-ill1-skill-opbygning.png | 18 | 🔲 Mangler |
| modul18-ill2-ollama-modelfile.png | 18 | 🔲 Mangler |
| modul19-ill1-mcp-arkitektur.png | 19 | 🔲 Mangler |
| modul19-ill2-mcp-servere-oversigt.png | 19 | 🔲 Mangler |
| modul19-ill3-mcp-integration.png | 19 | 🔲 Mangler |

---

## Samlet oversigt — Trin 1

| Fil | Format | Modul | Status |
|-----|--------|-------|--------|
| modul1-ill1-ai-vs-ikke-ai.png | PNG ekstern | 1 | ✅ |
| modul1-ill2-tidslinje.png | PNG ekstern | 1 | ✅ |
| modul1-ill3-programmering-vs-ml.png | PNG ekstern | 1 | ✅ |
| modul1-ill4-neuralt-netvaerk.png | PNG ekstern | 1 | ✅ |
| modul1-ill5-tre-grunde.png | PNG ekstern | 1 | ✅ |
| modul1-ill6-styrker-svagheder.png | PNG ekstern | 1 | ✅ |
| modul2-ill1-engine-vs-model.png | PNG ekstern | 2 | ✅ |
| modul2-ill2-token-forudsigelse.png | PNG ekstern | 2 | ✅ |
| modul2-ill3-tokenisering.png | PNG ekstern | 2 | ✅ |
| modul2-ill4-attention.png | PNG ekstern | 2 | ✅ |
| modul2-ill5-embeddings.png | PNG ekstern | 2 | ✅ |
| modul2-ill6-model-sammenligning.png | PNG ekstern | 2 | ✅ |
| modul3-ill1-lokal-vs-cloud.png | PNG ekstern | 3 | ✅ |
| modul3-ill2-privacy.png | PNG ekstern | 3 | ✅ |
| modul3-ill3-cpu-gpu-ram-vram.png | PNG ekstern | 3 | ✅ |
| modul3-ill4-model-storrelse.png | PNG ekstern | 3 | ✅ |
| modul3-ill5-quantization.png | PNG ekstern | 3 | ✅ |
| modul4-ill1-pipeline-overblik.png | PNG ekstern | 4 | ✅ |
| modul4-ill2-token-by-token-generation.png | PNG ekstern | 4 | ✅ |
| modul4-ill3-temperature.png | PNG ekstern | 4 | ✅ |
| modul4-ill4-context-window.png | PNG ekstern | 4 | ✅ |
| modul4-ill5-hallucination.png | PNG ekstern | 4 | ✅ |
| modul5-ill1-token-priser.png | PNG ekstern | 5 | ✅ |
| modul5-ill2-abonnement-vs-api.png | PNG ekstern | 5 | ✅ |
| modul5-ill3-pris-sammenligning.png | PNG ekstern | 5 | ✅ |
