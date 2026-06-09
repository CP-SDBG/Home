## Modul 6: Web-interfaces — ChatGPT, Claude, OpenRouter

> **Målgruppe:** 10–15 år · Let computer science baggrund
> **Illustration-filer:** modul6-ill1 til modul6-ill5 (PNG)

---

### Hvad er et web-interface til en LLM?

Den nemmeste måde at komme i gang med AI er via et **web-interface** — en hjemmeside du åbner i din browser, logger ind på og begynder at skrive til med det samme. Ingen installation, ingen kode, ingen konfiguration.

Du kender sikkert allerede konceptet fra Gmail eller Google Docs: software der kører i browseren, gemmer dine data i skyen og altid er opdateret. Web-interfaces til LLM'er fungerer på samme måde — du skriver en besked, modellen svarer, og historikken gemmes automatisk på udbyderens servere.

Det betyder også at udbyderen kan se dine beskeder. Det er vigtigt at huske: alt du skriver til ChatGPT eller Claude sendes over internettet og behandles af en virksomheds servere. Del aldrig adgangskoder, personlige oplysninger eller fortrolige dokumenter via et web-interface.

> 💬 **Ordforklaring:** *Web-interface* er en brugerflade der kører i din browser — som en hjemmeside der reagerer på dine input. *Cloud* betyder at beregningerne sker på en virksomheds servere langt væk, ikke på din computer.

📎 **Illustration:** `modul6-ill1-web-interface-oversigt.png`
**Titel:** Browser til AI og tilbage
*Oversigt: browser → internet → AI-server → svar tilbage — med login og historik markeret.*

---

### ChatGPT — den mest kendte

**ChatGPT** er lavet af OpenAI og er det web-interface de fleste tænker på når de hører "AI". Det blev lanceret i november 2022 og satte gang i den store AI-bølge vi er midt i nu.

**Hvad kan det?**
Standardmodellen i dag er **GPT-4o** (udtales "four-oh") — en *multimodal* model, hvilket betyder den kan forstå både tekst, billeder og lyd. Du kan indsætte et billede og spørge om det, vedhæfte en PDF og få den opsummeret, eller bede om hjælp til kode.

ChatGPT har også en **websøgning**-funktion der lader den finde aktuelle informationer — nyttigt når du spørger om noget der er sket for nylig, for modellens træningsdata stopper på et bestemt tidspunkt.

**Vigtigt at vide:**
OpenAI kan bruge dine samtaler til at træne fremtidige modeller. Du kan slå det fra under indstillinger — gør det, hvis du ikke vil have dine tekster brugt på den måde.

**Styrker:** generelle opgaver, kreativ skrivning, kode, brainstorming, websøgning
**Begrænsninger:** prisen stiger hurtigt ved højt API-forbrug, data kan bruges til træning

> 💬 **Ordforklaring:** *Multimodal* betyder at modellen kan arbejde med flere slags input — tekst, billeder og lyd — ikke kun tekst. *Træningsdata* er de eksempler modellen har lært fra.

📎 **Illustration:** `modul6-ill2-chatgpt-interface.png`
**Titel:** ChatGPT-interface annoteret
*ChatGPT-interface med eksempel på samtale, filupload og websøgning markeret med pile og labels.*

---

### Claude.ai — præcis og omhyggelig

**Claude** er lavet af Anthropic og er den model du taler med her. Den er designet med et særligt fokus på præcision, sikkerhed og ærlighed — Claude vil hellere sige "det ved jeg ikke" end opfinde et svar der lyder godt men er forkert.

**Hvad kan det?**
Claude er særligt stærk til **analyse af lange tekster**. Hvor mange modeller kæmper når dokumentet bliver langt, håndterer Claude op til **200.000 tokens** — svarende til en hel roman. Det gør den ideel til at læse store PDF'er, gennemgå lange kode-filer eller følge en lang og kompleks samtale.

Claude er også multimodal og kan analysere billeder. Den gratis plan giver et begrænset antal beskeder per dag. Claude Pro til $20/md giver prioriteret adgang og større context window.

**Styrker:** lange dokumenter, præcise og ærlige svar, kode, nuanceret analyse
**Begrænsninger:** ingen native websøgning i gratis plan, beskedbegrænsning på gratis tier

> 🔗 **Husk fra Modul 2:** Context window — den mængde tekst modellen kan "huske" på én gang. Claudes 200K tokens er markant større end de fleste lokale modellers 8–32K.

📎 **Illustration:** `modul6-ill3-claude-interface.png`
**Titel:** Claude.ai og det lange kontekstvindue
*Claude.ai-interface med eksempel på lang dokument-analyse og 200K context window markeret.*

---

### OpenRouter — ét sted, alle modeller

**OpenRouter** er anderledes end ChatGPT og Claude. Det er ikke en model — det er et **aggregator-interface** der samler adgang til hundredvis af modeller fra mange forskellige udbydere på ét sted.

Tænk på det som en streamingtjeneste der samler Netflix, Disney+ og HBO på én skærm — du betaler kun for det du bruger, og du kan skifte "kanal" med ét klik. Via OpenRouter kan du teste GPT-4o, Claude, Llama, Mistral, Gemini og mange andre med ét enkelt login og ét API-key.

Det er praktisk når du vil:
- Sammenligne to modeller på den samme opgave
- Finde den billigste model der løser dit problem godt nok
- Bygge et program der kan bruge mange forskellige modeller

Prisen er pay-per-token — du køber credits og betaler kun for det du faktisk bruger. Mange modeller er tilgængelige gratis eller meget billigt.

> 💬 **Ordforklaring:** *Aggregator* samler mange tjenester på ét sted. *API-key* er en unik kode der identificerer dig når du tilgår en tjeneste via kode — som et kørekort til API'et.

📎 **Illustration:** `modul6-ill4-openrouter-model-valg.png`
**Titel:** Ét interface — mange modeller
*OpenRouter: ét interface med mange modeller — prissammenligning og model-skift vist.*

---

### Sammenligning — hvornår bruger du hvad?

De tre interfaces løser ikke det samme problem — vælg det der passer til opgaven:

| Situation | Bedste valg |
|-----------|-------------|
| Generel hjælp, ideer, skriving, kode | ChatGPT eller Claude |
| Analysere et langt dokument eller en stor fil | Claude (200K context) |
| Aktuelle nyheder eller websøgning | ChatGPT (med søgning slået til) |
| Teste og sammenligne mange modeller | OpenRouter |
| Bygge et program der kalder en LLM | OpenRouter API eller direkte API |
| Privacy vigtigst — data må ikke forlade maskinen | Lokal model (Modul 7–8) |

Alle tre har **gratis tiers** — et godt sted at starte. Når du rammer grænserne, kan du vurdere om et betalt abonnement giver mening for dig.

---

### Gratis vs. betalte planer

Ingen af de store AI-tjenester er fuldt ud gratis — men alle tilbyder en gratis pakke der er god nok til at komme i gang.

**Gratis tier:**
- Adgang til modellen, men begrænset antal beskeder per dag
- Ældre eller mindre modeller (fx GPT-4o mini i stedet for GPT-4o)
- Kan være langsom i myldretiden når mange bruger tjenesten

**Betalt abonnement (~$20/md):**
- Ubegrænset eller markant højere antal beskeder
- Adgang til de nyeste og kraftigste modeller
- Højere prioritet i køen — hurtigere svar
- Ekstra features som avanceret billedgenerering og stemme-mode

**API (pay-per-token):**
- Bedst til programmering — du betaler kun for det du bruger
- Kræver teknisk opsætning (se Modul 14)
- For moderat brug ofte billigere end abonnement

Tommelfingerregel: start gratis. Hvis du bruger AI dagligt og rammer begrænsningerne jævnligt, er $20/md et overkommeligt beløb. Til programmering er API næsten altid det rigtige valg.

> 💬 **Ordforklaring:** *Tier* betyder niveau — fx gratis niveau, standard niveau, premium niveau. *Abonnement* er en fast månedlig betaling uanset hvor meget du bruger.

---

### Hvad er forskellen på web-interface og API-adgang?

Du kan tænke på det sådan her:

**Web-interface** er som at gå på restaurant — du sætter dig ned, bestiller, og får maden serveret. Alt er klar, men du kan kun vælge fra menuen og må bruge restaurantens åbningstider.

**API** er som at have et professionelt køkken derhjemme — du får adgang til de samme ingredienser, men kan lave præcis den ret du vil, når du vil, og i den mængde du vil. Kræver lidt mere setup.

| | Web-interface | API |
|---|---|---|
| Adgang | Browser, klik og skriv | Kode (Python, JS osv.) |
| Setup | Ingen — bare log ind | Kræver API-nøgle og kode |
| Automatisering | Manuel — du skriver selv | Kan køres automatisk |
| Pris | Gratis tier eller abonnement | Pay-per-token |
| Bedst til | Lære, eksperimentere, daglig brug | Bygge programmer |

I dette modul arbejder vi med web-interfaces. API-adgang gennemgår vi i Modul 14.

> 🔗 **Kommer i Modul 14:** Første API-kald i Python — send en besked til en LLM fra din egen kode og få svaret tilbage.

📎 **Illustration:** `modul6-ill5-web-vs-api.png`
**Titel:** Klik vs. kode — hvornår vælger du hvad?
*To kolonner: web-interface (browser, klik, manuel) vs*
