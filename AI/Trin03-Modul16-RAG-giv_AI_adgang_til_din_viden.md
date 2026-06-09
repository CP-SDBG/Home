## Modul 16: RAG - giv AI adgang til din egen viden

> **Målgruppe:** 10-15 år · Kender Python og LLM-kald · Har fulgt Modul 15
> **Illustration-filer:** modul16-ill1 til modul16-ill3 (PNG)

---

### Hvad er RAG?

**RAG** står for *Retrieval-Augmented Generation* - og det løser et af AI's største problemer: modellen kender kun det den er trænet på. Den kender ikke dine noter, din skoles regler eller gårsdagens nyheder.

Med RAG giver du AI'en adgang til et "bibliotek" af dine egne dokumenter. Når du stiller et spørgsmål, finder systemet først de relevante dokumentstykker og lægger dem ind i prompten - så AI'en svarer baseret på din faktiske viden, ikke bare sin træning.

**RAG løser tre problemer på én gang:** hallucination (AI'en ser de rigtige fakta), forældet viden (du kan give de nyeste dokumenter), og specifik viden (din AI kender dine interne dokumenter).

> 💬 **Ordforklaring:** *RAG* kombinerer søgning i et dokumentarkiv med AI-generering. *Retrieval* = hentning. *Augmented* = forbedret. *Generation* = AI's tekstgenerering. Det er ikke en model - det er en *arkitektur*.

📎 **Illustration:** `modul16-ill1-rag-pipeline.png`
**Titel:** Låsen der åbnes
*Samme spørgsmål, to versioner: UDEN RAG → AI hallucinerer et forkert svar. MED RAG → relevant chunk hentes, AI svarer korrekt fra dokumentet. Viser det KONKRETE PROBLEM RAG løser.*

---

### RAG vs. "bas bare al tekst ind i prompten"

Kan du ikke bare paste hele dit dokument ind i prompten? Teknisk ja - men det skalerer ikke:

| ❌ Al tekst i prompten | ✅ RAG |
|--------------------|-------|
| Max ~200.000 tokens - så er context-vinduet fyldt | Ubegrænset antal dokumenter i databasen |
| Koster mange tokens per kald - dyrt ved gentagne spørgsmål | Kun relevante chunks sendes - typisk 3-5 stykker |
| AI'en fortaber sig i lang tekst - kvaliteten falder | AI får præcis det relevante - koncentreret svar |
| Virker ikke med 1.000+ siders PDF-arkiv | Virker med millioner af dokumenter |

Tommelfingerregel: under 5 sider og ét enkelt dokument - paste det ind. Over det - brug RAG.

---

### Embeddings og semantisk søgning

RAG søger på *mening*, ikke nøgleord. Det sker via **embeddings** - hvert tekststykke omdannes til en lang liste tal der repræsenterer dets betydning:

```
# Keyword-søgning finder intet:
søg("bil")  →  ingen hits  # dokumentet siger "køretøj"

# Semantisk søgning finder det:
vektor_søg("bil")  →  "Et køretøj med fire hjul..."  # ens betydning
```

Dine dokumenter får hver sin embedding-vektor og gemmes i en **vektor-database**. Når du spørger, omdannes dit spørgsmål også til en vektor - databasen finder de dokumentstykker der er tættest på.

Populære vektor-databaser: **ChromaDB** (lokal, perfekt til begyndere), **Pinecone** (cloud, skalerbar), **Weaviate** (open source).

> 🔗 **Husk fra Modul 2:** Embeddings som koordinater på et betydningskort - ord med ens mening havner tæt på hinanden. RAG bruger præcis den mekanisme.

---

### Chunking - opdel dokumenter smart

Inden du kan søge i dine dokumenter, skal de opdeles i passende bidder - **chunks**. Typisk 200-500 ord med et overlap på 50-100 ord.

```python
def chunk_tekst(tekst: str, chunk_størrelse: int = 400, overlap: int = 50) -> list:
    ord = tekst.split()
    chunks = []
    i = 0
    while i < len(ord):
        chunk = " ".join(ord[i:i + chunk_størrelse])
        chunks.append(chunk)
        i += chunk_størrelse - overlap
    return chunks
```

| ❌ Dårlig chunking | ✅ God chunking |
|----------------|----------------|
| Hele dokumentet som ét chunk | 200-500 ord per chunk |
| Ingen overlap - grænse-information går tabt | 50-100 ords overlap mellem chunks |
| Sætninger klippes midt over | Klip ved naturlige grænser (afsnit, punktum) |

📎 **Illustration:** `modul16-ill2-chunking-overlap.png`
**Titel:** Nøglesætningen der går tabt
*Viser en tekst med en vigtig sætning der falder præcis på chunk-grænsen: UDEN overlap → sætningen splittes, begge chunks er ubrugelige. MED overlap → sætningen er hel i begge chunks. Viser PROBLEMET overlap løser.*

---

### RAG-pipeline: installér og opsæt

Du skal bruge to pakker:

```bash
pip install chromadb ollama
```

ChromaDB kan køre midlertidigt (nulstilles ved genstart) eller persistent på disk:

```python
import chromadb

# Midlertidigt (nulstilles ved genstart)
client = chromadb.Client()

# Persistent (gemmes på disk)
client = chromadb.PersistentClient(path="./min-rag-db")

# Opret eller hent samling
samling = client.get_or_create_collection("pensum-biologi")
```

---

### RAG i praksis med ChromaDB

Det fulde mønster: tilføj dokumenter én gang, søg og svar mange gange:

```python
import chromadb, ollama

client = chromadb.Client()
samling = client.create_collection("mine-noter")

# 1. Indlæs dokumenter (én gang)
samling.add(
    documents=[
        "Fotosyntese er den proces hvor planter omdanner sollys til sukker.",
        "Klorofyl er det grønne stof i planter der absorberer sollys.",
        "Planter frigiver oxygen som biprodukt af fotosyntese.",
    ],
    ids=["dok1", "dok2", "dok3"]
)

# 2. Søg og svar (gentages for hvert spørgsmål)
def rag_svar(spørgsmål: str, antal_resultater: int = 2) -> str:
    resultater = samling.query(query_texts=[spørgsmål], n_results=antal_resultater)
    kontekst = "\n".join(resultater["documents"][0])
    prompt = f"""Svar baseret KUN på denne kontekst. Siger konteksten ikke svaret, sig 'Det ved jeg ikke ud fra de givne dokumenter.'\n\nKontekst:\n{kontekst}\n\nSpørgsmål: {spørgsmål}"""
    svar = ollama.chat(model="qwen2.5:7b", messages=[{"role": "user", "content": prompt}])
    return svar["message"]["content"]

print(rag_svar("Hvad er klorofyl?"))
print(rag_svar("Hvad er Danmarks hovedstad?"))  # "Det ved jeg ikke..."
```

Bemærk instruksen *"Sig 'ved ikke' hvis ikke i konteksten"* - den er kritisk. Uden den gætter AI'en og hallucinerer.

---

### Søgekvalitet - hvad påvirker resultatet?

Tre parametre gør størst forskel:

| Parameter | Påvirker | Anbefaling |
|-----------|----------|------------|
| `n_results` | Antal chunks i kontekst | Start med 2-3. For mange = forvirret AI |
| Chunk-størrelse | Præcision vs. kontekst | 200-400 ord til fakta, 400-600 til analyse |
| Prompt-instruks | Om AI hallucinerer | Altid: "sig 'ved ikke' hvis ikke i kontekst" |

Fejlfinding: får du dårlige svar? Print `resultater["documents"][0]` og se hvilke chunks der faktisk hentes. Henter den de forkerte - juster chunk-størrelse eller øg overlap.

📎 **Illustration:** `modul16-ill3-rag-use-cases.png`
**Titel:** Samme arkitektur, fra 5 noter til 50.000 dokumenter
*Venstre: en elev med 5 noter → ChromaDB lokal → AI svarer. Højre: en virksomhed med 50.000 dokumenter → ChromaDB/Pinecone → AI svarer. Samme kode-mønster begge steder. Viser SKALERBARHEDEN, ikke use cases.*

---

### Praktisk eksempel: byg en pensum-assistent

Vi bygger et program der læser dine egne noter og svarer på spørgsmål om dem.

**1. Forbered noter som Python-liste:**
```python
noter = [
    "Andenskoloven: F = m * a. Kraft er lig masse gange acceleration.",
    "Newton's tredjelov: For enhver kraft er der en modsat og lige stor reaktionskraft.",
    "Energibevarelse: Energi kan ikke skabes eller forsvinde, kun omdannes.",
    "Kinetisk energi: Ek = 0.5 * m * v^2. Afhænger af masse og hastighed.",
    "Potentiel energi: Ep = m * g * h. Afhænger af højde og masse.",
]
```

**2. Indlæs i ChromaDB:**
```python
import chromadb
samling = chromadb.Client().create_collection("fysik-noter")
samling.add(documents=noter, ids=[f"note{i}" for i in range(len(noter))])
```

**3. Byg spørgsmåls-løkken:**
```python
import ollama

print("Pensum-assistent klar! (stop for at afslutte)\n")
while True:
    q = input("Spørgsmål: ")
    if q.lower() == "stop": break
    hits = samling.query(query_texts=[q], n_results=2)
    kontekst = "\n".join(hits["documents"][0])
    svar = ollama.chat(model="qwen2.5:7b", messages=[{"role": "user",
        "content": f"Baseret KUN på disse noter:\n{kontekst}\n\nSvar kort: {q}"}])
    print(f"\nSvar: {svar['message']['content']}\n")
```

**4. Udvid med dine egne noter:** skift listen ud med indhold fra dine undervisningsbøger. Jo flere og bedre noter, jo præcisere svar. Prøv at tilføje modstridende information og se om AI'en håndterer det korrekt.
