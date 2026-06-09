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
