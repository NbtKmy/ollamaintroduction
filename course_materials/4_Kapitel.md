# 4. Kapitel - GGUF selber erstellen und verwenden

## Warum selber GGUF erstellen?
Wenn ein Basemodel (oder andere Modelle wie Instruct-Model usw.) da ist, kann man daraus selber ein GGUF-File erstellen und für Ollama anwendbar machen.
Auf diese Weise kann man ein neues Modell in Ollama ausprobieren.

[gemma3:4b](https://ollama.com/library/gemma3:4b) gibt es bereits für Ollama. Aber dies ist durch Q4_K_M quantifiziert. Wenn man z.B. mit einem anderen Algorhythmen wie Q8_0 oder Q5_K_M quantifiziert, kann man noch bessere Ergebnisse erwarten.

## How to

### 1. Zuerst das Modell holen:

```python

from dotenv import load_dotenv
import os
from pathlib import Path
from huggingface_hub import snapshot_download


load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")

project_root = Path(__file__).resolve().parents[1]
local_dir = project_root / "model" # So wird das Modell unter dem Ordner "model" heruntergeladen
local_dir.mkdir(parents=True, exist_ok=True)

snapshot_download(
    repo_id="google/gemma-3-4b-it",
    local_dir=local_dir,
    token=token,
    local_dir_use_symlinks=False,
)

```

### 2. [llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master) holen

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```

Und die notwendigen packages für `convert_hf_to_gguf.py`installieren.
Dann den folgenden Befehl ausführen:

```bash

# Vom Modell zu f16 GGUF
python [your folder for llama.cpp]/llama.cpp/convert_hf_to_gguf.py \
  --outtype f16 \
  --outfile ./gguf/gemma3-4b-it-f16.gguf \
  [your goal folder]

# Wenn man die Funktion, Image-Text-To-Text, beibehaltne will:
python [your folder for llama.cpp]/llama.cpp/convert_hf_to_gguf.py \
  --mmproj \
  --outfile ./gguf/gemma3-4b-it-mmproj.gguf \
  [your goal folder]

````

### 3. llama.cpp bilden

```bash
[cd llama.cpp-folder]

cmake -B build
cmake --build build --config Release -j

# Checking the build binary
./build/bin/llama-cli -h

```

### 4. Create a GGUF file

```bash
[your llama.cpp/llama.cpp/build/bin/llama-quantize \   # we use llama-quantize
  ./gemma3-4b-it-f16.gguf \      # f16-GGUF you created just now 
  ./gemma3-4b-it.Q5_K_M.gguf \   # We create a Q5_K_M 
  Q5_K_M

```

### 5. Ein Modelfile schreiben

Wie dies: 
```text
FROM ./gemma3-4b-it.Q5_K_M.gguf
FROM ./gemma3-4b-it-mmproj.gguf

PARAMETER temperature 0.7
```

Dann dies spiechern.

### 6. In Ollama eintragen

```bash
ollama create gemma3-4b-q5km -f Modelfile
```






