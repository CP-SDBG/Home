## Modul 1: Introduktion til AI

> **Målgruppe:** 10–15 år · Let computer science baggrund · Kan skrive små Python-programmer
> **Illustration-filer:** modul1-ill1 til modul1-ill6 (SVG)

---

### Hvad betyder AI egentlig?

AI står for **Artificial Intelligence** — eller på dansk: **kunstig intelligens**.

Men hvad betyder det? Tænk på det sådan her: Normalt er det kun levende væsener der kan "tænke" — altså løse problemer, genkende ting og finde på nye idéer. AI er programmer der kan gøre noget der *ligner* tænkning — uden at de er levende.

Din lommeregner er ikke AI. Den kan kun gøre præcis hvad den fik at vide. Men hvis du viser et program tusindvis af billeder af katte, og det bagefter selv kan genkende en kat på et nyt billede — det er AI.

> 💬 **Ordforklaring:** *Intelligens* betyder evnen til at lære, forstå og løse problemer. *Kunstig* betyder at det er lavet af mennesker, ikke opstået naturligt.

📎 **Illustration:** `modul1-ill1-ai-vs-ikke-ai.png`
**Titel:** Lommeregner vs. kamera — hvad er forskellen?
*Sammenligning: lommeregner (ikke AI) vs*

---

### Kort historie — fra de tidlige idéer til i dag

AI er ikke nyt. Mennesker har drømt om tænkende maskiner i årtier.

**1950'erne:** Forskere begyndte at spørge: *"Kan maskiner tænke?"* De prøvede at kode regler direkte ind — fx *"hvis X, så gør Y"*. Det virkede til simple opgaver men slog hurtigt fejl på det virkelige verdens kompleksitet.

**1997:** Deep Blue slog verdensmesteren i skak. Imponerende! Men det kunne kun spille skak.

**2012–2017:** Alt ændrede sig. Med mere data, hurtigere computere og en ny teknik kaldet *deep learning* begyndte AI at kunne gøre ting der tidligere virkede umulige — genkende tale, oversætte sprog, generere billeder. I 2017 opfandt Google **Transformer-arkitekturen** — grundlaget for al moderne AI.

**2022–nu:** Nu er vi her. AI kan skrive tekst, kode programmer, lave musik og føre en samtale der næsten lyder menneskelig.

📎 **Illustration:** `modul1-ill2-tidslinje.png`
**Titel:** AI's vej fra ide til eksplosion
*Vandret tidslinje: 1950 → 1997 → 2012–2017 → 2022–nu*

---

### Hvad er machine learning?

Normalt når du programmerer, fortæller du computeren *præcis* hvad den skal gøre — trin for trin. Det kalder vi klassisk programmering.

**Machine learning er anderledes.** I stedet for at give computeren reglerne, giver du den masser af eksempler — og den finder selv mønstrene.

Forestil dig du skal lære en robot at genkende spam-mails. Du *kunne* skrive hundredvis af regler: "hvis mailen indeholder 'vind en iPhone' er det spam". Men spammerne ville bare ændre ordene.

Med machine learning viser du i stedet robotten 10.000 spam-mails og 10.000 normale mails — og den lærer selv hvad der adskiller dem. Det er meget mere fleksibelt.

> 💬 **Ordforklaring:** *Mønster* betyder en regelmæssighed der gentager sig. Computeren leder efter sådanne regelmæssigheder i data.

📎 **Illustration:** `modul1-ill3-programmering-vs-ml.png`
**Titel:** Regler ind vs. mønstre ud
*To parallelle flowdiagrammer side om side: klassisk programmering (regler + data → output) vs*

---

### Hvad er deep learning?

Deep learning er en speciel slags machine learning — og det er den der har gjort AI så kraftfuld de seneste år.

Idéen er inspireret af din hjerne. Din hjerne er bygget af milliarder af nerveceller (*neuroner*) der sender signaler til hinanden. Deep learning efterligner det med kunstige neuroner i et **neuralt netværk**.

Forestil dig et net af lag. Hvert lag kigger på noget mere komplekst end laget før:
- **Lag 1** genkender måske bare kanter og linjer i et billede
- **Lag 2** kombinerer dem til former
- **Lag 3** genkender øjne, næse, mund
- **Lag 4** konkluderer: *"det er et ansigt"*

Jo dybere netværket er (jo flere lag), jo mere komplekse ting kan det lære. Deraf navnet: *deep* learning.

> 💬 **Ordforklaring:** *Neuron* er en nervecelle i hjernen. *Kunstig neuron* er en matematisk funktion der efterligner hvordan en nervecelle virker.

📎 **Illustration:** `modul1-ill4-neuralt-netvaerk.png`
**Titel:** Fra pixels til "ansigt"
*Neuralt netværk med input-lag, skjulte lag og output-lag — pixels til "ansigt / ikke ansigt".*

---

### Hvorfor er AI blevet så populært nu?

AI har eksisteret i årtier — så hvorfor eksploderede det først nu?

Svaret er tre ting der skete på samme tid:

**1. Mere data**
Internettet har givet os ufattelige mængder data — tekster, billeder, videoer. AI lærer af data, så mere data = smartere AI.

**2. Hurtigere hardware**
Grafikkort (GPU'er) — de samme chips der bruges til computerspil — viste sig at være perfekte til at træne AI. De kan lave millioner af beregninger på samme tid.

**3. Bedre algoritmer**
Især én opfindelse ændrede alt: **Transformer-arkitekturen** fra 2017. Den er grundlaget for ChatGPT, Claude og næsten alle moderne AI-sprogmodeller. (Vi kigger nærmere på den i Modul 2.)

> 💬 **Ordforklaring:** *GPU* står for Graphics Processing Unit — et grafikkort. *Algoritme* er en opskrift computeren følger for at løse et problem.

📎 **Illustration:** `modul1-ill5-tre-grunde.png`
**Titel:** Tre ting der skete på samme tid
*Tre kort side om side: Data + Hardware + Algoritmer med plus-tegn imellem*

---

### Hvad kan AI gøre — og hvad kan det ikke?

AI er imponerende, men det er vigtigt at forstå både hvad det er godt til og hvor det fejler.

**✅ AI er rigtig god til:**
- Genkende mønstre i store mængder data
- Generere tekst, billeder, kode og musik
- Oversætte sprog
- Besvare spørgsmål baseret på viden den har lært
- Finde fejl i kode

**❌ AI kæmper med:**
- Forstå verden som et menneske — den ved ikke hvad den siger, den *forudsiger* hvad der er sandsynligt at sige
- Holde styr på hvad der er sandt — den kan finde på fakta der lyder overbevisende men er forkerte
- Opgaver der kræver ægte kreativitet og følelser
- Ting den ikke har set eksempler på i sin træning

> 💬 **Ordforklaring:** *Hallucination* er når en AI opfinder information der ikke er sand — det sker fordi den er trænet til at lave sandsynlige svar, ikke nødvendigvis korrekte.

📎 **Illustration:** `modul1-ill6-styrker-svagheder.png`
**Titel:** Hvad AI er god til — og hvad den ikke er
*To-kolonne oversigt: grøn kolonne (styrker) og rød kolonne (svagheder) med konkrete eksempler i hvert felt.*
