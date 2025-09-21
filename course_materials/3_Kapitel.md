# 3 Kapitel - Parameter von LLMs und Quantisierung


## 1. Was sind Parameter eines LLM?

Ein Large Language Model (LLM) besteht im Kern aus Milliarden von Parametern.
Diese Parameter sind die „Gewichte“ in den neuronalen Netzen und bestimmen, wie das Modell Sprache versteht und generiert.

[Hier](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.32680&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false) ein einfaches Beispiel vom Neural Network, erstellt von Daniel Smilkov und Shan Carter.


Je grösser die Anzahl der Parameter, desto leistungsfähiger ist in der Regel das Modell – aber:

- Mehr Parameter → höhere Anforderungen an Rechenleistung (CPU/GPU).

- Mehr Parameter → größerer Speicherbedarf (RAM/VRAM).

- Mehr Parameter → längere Rechenzeit pro Anfrage.

Daher gilt: Die Parameter sind der Hauptfaktor, der den Einsatz von LLMs in der Praxis limitiert.


## 2. Quantisierung als Lösung

Um diese hohen Anforderungen zu reduzieren, gibt es die Methode der Quantisierung.

Dabei werden die Gewichte des Modells von einer höheren Präzision (z. B. 16 oder 32 Bit) auf kleinere Wertebereiche (z. B. 8, 5 oder 4 Bit) heruntergerechnet.

Vorteile:

- Weniger Speicherverbrauch

- Schnelleres Laden und teilweise schnelleres Inferenzieren

- LLMs können auf Laptop-CPUs oder kleineren GPUs laufen

Natürlich gibt es auch Nachteile:

- Genauigkeit des Modells kann leicht sinken

- Antworten können etwas weniger präzise oder konsistent sein


## 3. Arten der Quantisierung (am Beispiel llama.cpp)

In llama.cpp, einer weit verbreiteten Open-Source-Implementierung von LLaMA-basierten Modellen, gibt es verschiedene Quantisierungsarten:

- Qx_y: einfache Quantisierung mit x Bit, verschiedene Varianten für Geschwindigkeit und Speicheroptimierung

- Qx_K: blockbasierte Quantisierung (K = „Kürzere Blöcke“), besseres Verhältnis von Qualität zu Speicher

- IQx: „Integer Quantization“, modernere Methode mit noch stärkerer Kompression

## 4. Vergleich der Quantisierungsarten


| Quantisierung | Präzision	| Geschwindigkeit |	Speicherbedarf |
|---------------|-----------|-----------------|----------------|
| Q4_0 / Q4_1 |	gering bis mittel |hoch | sehr niedrig |
| Q5_0 / Q5_1 | mittel | hoch | niedrig |
| Q8_0 | hoch | mittel | hoch |
| Q4_K_S | mittel | hoch | sehr niedrig |
| Q5_K_M | mittel-hoch | mittel | niedrig |
| Q6_K_L | hoch | niedriger	| mittel |
| IQ2_XS / IQ2_XXS | sehr gering | sehr hoch | extrem niedrig |
| IQ3_S | mittel | sehr hoch | sehr niedrig |

(S = small, M = medium, L = large; XS/XXS = extra small)


## 5. Ressourcensteuerung mit `ollama serve`

Standardmäßig verwendet Ollama automatisch verfügbare Ressourcen (CPU, RAM, GPU falls vorhanden).
Für feinere Kontrolle können bestimmte Umgebungsvariablen oder Flags genutzt werden:

### Wichtige Optionen

| Variabel | Beschreibung |
|----------|--------------|
| OLLAMA_CONTEXT_LENGTH | Context length to use unless otherwise specified(default:4096) |
| OLLAMA_KEEP_ALIVE | The duration that models stay loaded in memory (default "5m") |
| OLLAMA_MAX_LOADED_MODELS | Maximum number of loaded models per GPU |
| OLLAMA_MAX_QUEUE | Maximum number of queued requests |
| OLLAMA_NUM_PARALLEL | Maximum number of parallel requests |
| OLLAMA_NOPRUNE | Do not prune model blobs on startup |
| OLLAMA_SCHED_SPREAD | Always schedule model across all GPUs |
| OLLAMA_GPU_OVERHEAD |Reserve a portion of VRAM per GPU (bytes) |

Beispiel:
```bash
OLLAMA_CONTEXT_LENGTH=8192 ollama serve
```
