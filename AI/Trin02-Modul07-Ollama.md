## Modul 7: Ollama — kør AI-modeller lokalt

> **Målgruppe:** 10–15 år · Let computer science baggrund · Kræver adgang til terminal
> **Illustration-filer:** modul7-ill1 til modul7-ill4 (PNG)

---

### Hvad er Ollama og hvad løser det?

At køre en AI-model lokalt på din computer lyder måske kompliceret — og det *var* det engang. Du skulle selv finde den rigtige fil, konfigurere GPU-drivere, installere Python-biblioteker og håbe at det hele virkede sammen. Det tog timer og fejlede halvdelen af gangene.

**Ollama løser det problem.** Det er et program der pakker al den kompleksitet ind i én simpel kommando. Du skriver `ollama run llama3.2`, og Ollama finder modellen, downloader den, sætter den op og starter en chat — alt i ét.

Bag kulisserne kører Ollama som en **lokal server** på din computer. Det betyder at andre programmer — fx din browser, et Python-script eller en editor — kan tale med AI-modellen via et standard API, præcis som de ville tale med ChatGPT i skyen. Bare lokalt, privat og gratis.

> 💬 **Ordforklaring:** *Server* er et program der venter på forespørgsler og svarer på dem. En lokal server kører på din egen computer — ikke på internettet. *API* er en standardiseret måde for programmer at tale med hinanden.

📎 **Illustration:** `modul7-ill1-ollama-arkitektur.png`
**Titel:** Ollama som midterlag
*Ollama som lag mellem model-filer og bruger/programmer — terminal, browser og Python alle forbundet til Ollama i midten.*

---

### Installation

Ollama virker på Windows, Mac og Linux.

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Hent installationsfilen fra [ollama.com](https://ollama.com) og kør den. Ollama installeres og starter automatisk som en baggrundstjeneste.

**Mac:**
Hent `.dmg`-filen fra ollama.com eller installer via Homebrew: `brew install ollama`

Tjek at det virker:
```bash
ollama --version
```

Hvis du får et versionsnummer tilbage, er Ollama klar.

> 💬 **Ordforklaring:** *curl* er et terminal-kommando der downloader filer fra internettet. *Baggrundstjeneste* er et program der kører stille i baggrunden uden et synligt vindue.

---

### Download og kør din første model

```bash
ollama pull qwen2.5:7b
```

Dette downloader Qwen 2.5 7B-modellen — en god allrounder på ~4 GB. Første download tager lidt tid afhængig af din internetforbindelse. Modellen gemmes lokalt og kører offline bagefter.

Start en chat direkte i terminalen:
```bash
ollama run qwen2.5:7b
```

Du kan nu skrive til modellen og få svar — uden internet, uden abonnement, uden at dine beskeder forlader din computer. Skriv `/bye` for at afslutte.

> 🔗 **Husk fra Modul 3:** Vi gennemgik hardware-krav til lokale modeller. En 7B model kræver ~8 GB VRAM eller ~16 GB RAM. Har du mindre, prøv en 3B model: `ollama pull qwen2.5:3b`

---

### Vigtige kommandoer

```bash
ollama pull <model>    # Download en model
ollama run <model>     # Start chat med modellen
ollama list            # Se alle downloadede modeller
ollama rm <model>      # Slet en model og frigør diskplads
ollama show <model>    # Vis info om modellen (størrelse, parametre)
```

Modeller fylder fra ~1 GB (lille 1B model) til ~80 GB (70B model). Brug `ollama list` jævnligt for at holde styr på hvad du har liggende.

📎 **Illustration:** `modul7-ill2-ollama-kommandoer.png`
**Titel:** De 5 kommandoer du skal kende
*De 5 vigtigste Ollama-kommandoer med eksempler og hvad de gør*

---

### Ollama som lokal API-server

Når Ollama kører, starter det automatisk en lokal webserver på **port 11434**. Det betyder du kan sende HTTP-forespørgsler til `http://localhost:11434` — præcis som du ville kalde OpenAI's API, bare lokalt.

Det vigtige her: Ollama's API-format er **kompatibelt med OpenAI's format**. Det betyder at programmer der er skrevet til at tale med ChatGPT, ofte kan skiftes om til at bruge Ollama med én linje kode — bare skift adressen fra `api.openai.com` til `localhost:11434`.

Dette er grunden til at Ollama er blevet så populært: det er ikke bare et chat-program, det er et fundament som mange andre værktøjer kan bygge på.

> 💬 **Ordforklaring:** *Port* er som et husnummer på internettet — port 11434 er den "dør" Ollama lytter på. *localhost* er din computers adresse til sig selv — trafik der går til localhost forlader aldrig din maskine.

📎 **Illustration:** `modul7-ill3-lokal-api-server.png`
**Titel:** Port 11434 — din lokale AI-server
*Ollama på port 11434 — terminal, Python-script, Open WebUI og browser alle forbundet.*

---

### Integration med andre værktøjer

Fordi Ollama kører som en lokal server med standardiseret API, kan mange andre programmer bruge det som AI-backend:

- **Open WebUI** — grafisk chat-interface i browseren, forbinder automatisk til Ollama (Modul 8)
- **LM Studio** — kan bruge Ollama som backend eller køre egne modeller
- **Python** — kald via `requests`-biblioteket eller det dedikerede `ollama`-bibliotek
- **VS Code extensions** — flere AI-coding extensions kan pege på Ollama i stedet for cloud
- **Pi Agent og OpenCode** — begge kan konfigureres til at bruge Ollama (Modul 10–11)

```python
# Simpelt Python-kald til Ollama
import ollama
response = ollama.chat(model='qwen2.5:7b',
    messages=[{'role': 'user', 'content': 'Hvad er verdens højeste bjerg?'}])
print(response['message']['content'])
```

---

### Model library — hvad findes der, og hvad vælger du?

På [ollama.com/library](https://ollama.com/library) finder du hundredvis af modeller. Her er de vigtigste kategorier:

| Model | Størrelse | Bedst til |
|-------|-----------|----------|
| Llama 3.2 | 3B, 8B | God allrounder, hurtig |
| Qwen 2.5 | 3B, 7B, 14B | Stærk til kodning og dansk tekst |
| Mistral | 7B | Hurtig, god til instruktioner |
| Qwen2.5-coder | 7B, 14B | Specifikt til kode |
| DeepSeek-R1 | 7B, 14B | Reasoning og komplekse opgaver |
| Gemma 3 | 4B, 12B | Googles open source model |

Tommelfingerregel: **start med Qwen 2.5 7B** til generel brug. Til kodning: **Qwen2.5-coder 7B**.

📎 **Illustration:** `modul7-ill4-model-library.png`
**Titel:** Hvilken model til hvad?
*Oversigt over populære Ollama-modeller med størrelse, styrker og anbefalede use cases.*
