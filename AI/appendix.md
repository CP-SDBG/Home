# Appendix

## Appendix 1: Hvorfor Linux? (WSL, native, containers)
- [Indhold kommer senere]

---

## Appendix 2: Linux — de vigtigste kommandoer (cheat sheet)

### Navigation & Mapper
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `pwd` | Print Working Directory — viser hvor du er | `pwd` → `/home/henrik` |
| `ls` | List — viser filer/mapper i nuværende mappe | `ls` eller `ls -la` (detaljeret) |
| `cd` | Change Directory — skifter mappe | `cd /home` eller `cd ..` (op) eller `cd -` (tidligere) eller `cd ~` (home) eller `cd /` (root) |
| `mkdir` | Make Directory — laver ny mappe | `mkdir my-project` |

### Filbehandling
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `touch` | Create file — laver tom fil | `touch script.py` |
| `cat` | Concatenate — læser indhold af fil / viser på skærmen | `cat script.py` |
| `echo` | Print text — skriver tekst til skærmen eller fil | `echo "Hello" > file.txt` (opret) eller `echo "Hello" >> file.txt` (tilføj) |
| `cp` | Copy — kopierer fil/mappe | `cp fil1.txt fil2.txt` |
| `mv` | Move — flytter eller omdøber fil | `mv old-name.txt new-name.txt` |
| `rm` | Remove — sletter fil | `rm file.txt` (forsigtig!) |
| `grep` | Search — finder tekst i filer | `grep "error" logfile.txt` |

### Teksteditorer
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `nano` | Text editor — rediger filer i terminal | `nano config.txt` |
| `vim` | Advanced text editor — mere kraftfuld | `vim script.py` |

### Bruger & Gruppe Administration
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `useradd` | Add User — opretter ny bruger | `sudo useradd -m -s /bin/bash henrik` (-m = home dir, -s = shell) |
| `userdel` | Delete User — sletter bruger | `sudo userdel -r henrik` (-r = slet home dir også) |
| `groupadd` | Add Group — opretter ny gruppe | `sudo groupadd developers` |
| `groupdel` | Delete Group — sletter gruppe | `sudo groupdel developers` |
| `usermod` | Modify User — ændrer bruger-indstillinger | `sudo usermod -aG developers henrik` (tilføj henrik til developers gruppe) |
| `passwd` | Password — ændrer adgangskode | `passwd` (egen adgangskode) eller `sudo passwd henrik` (andres adgangskode) |

### Rettigheder & Sikkerhed
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `chmod` | Change Mode — ændrer fil-rettigheder | `chmod 755 script.sh` (rwxr-xr-x) eller `chmod +x script.sh` (gør executable) eller `chmod -x script.sh` (fjern execute) eller `chmod 644 file.txt` (rw-r--r--) |
| `sudo` | Super User Do — kører kommando med admin-rettigheder | `sudo apt install python3` |

**chmod rettigheder kort forklaring:**
- `755` = rwxr-xr-x (ejer kan alt, andre kan læse+execute)
- `644` = rw-r--r-- (ejer kan læse+skrive, andre kun læse)
- `700` = rwx------ (kun ejer kan gøre noget)
- `+x` = gør fil executable
- `-x` = fjern execute-rettighed

### Processer & Services
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `ps` | Process Status — viser kørende programmer | `ps aux` |
| `kill` | Afslut process — stopper program | `kill 1234` (PID) |
| `sudo systemctl` | Service manager — starter/stopper services | `sudo systemctl start docker` |

### Pakke Installation & Software
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `apt` | Package manager (Debian/Ubuntu) — installer software | `apt install nodejs` eller `apt update` |
| `pip` | Python package manager — installer Python-biblioteker | `pip install requests` |

### Python & Scripting
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `python3` | Kør Python-script | `python3 script.py` |

### Version Control
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `git` | Version control — tracker kodeændringer | `git clone URL` eller `git commit` |

### Netværk & Web
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `curl` | Hent data fra URL — web requests i terminal | `curl https://api.example.com` |
| `wget` | Download — downloader filer fra web | `wget https://example.com/file.zip` |

### Hjælp & Dokumentation
| Kommando | Hvad det gør | Eksempel |
|----------|-------------|---------|
| `man` | Manual — viser hjælp til kommando | `man ls` |

### Docker (kommer senere)
[Reserveret til Docker-kommandoer når det modul udvikles]

---

## Appendix 3: CPU Offloading — notat

*Skal uddybes senere*

- Hvad er offloading? (når GPU-VRAM fyldes, køres nogle layers på CPU-RAM)
- Performance trade-off — langsommere, men muligt uden GPU
- Konkrete scenarioer:
  - Du har GPU men den er for lille
  - Du har ingen GPU, kun CPU
  - Mixed offloading — GPU + CPU sammen
- Værktøjer der støtter det:
  - Ollama (simpelt, auto)
  - LM Studio (manuel kontrol)
  - llama.cpp (avanceret)
- Ydeevne-eksempler (sekunder per token)
