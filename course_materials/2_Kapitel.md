# 2. Kapitel - Ollama durch API betätigen

Wenn Ollama installiert ist, läuft die Software normalerweise immer im Hintergrund.
In diesem Zustand lässt die Software den Zugriff durch API zu.

Eine API (Application Programming Interface), auf Deutsch Programmierschnittstelle, ist eine Schnittstelle in Form von Regeln und Protokollen, die es verschiedenen Softwareanwendungen ermöglicht, miteinander zu kommunizieren, Daten auszutauschen und Funktionalitäten zu nutzen.

## Testen Eins

Gibt Ollama wirklich den API-Zugriff? Lass uns überprüfen!
1. Öffne einen beliebigen Webbrowser
1. Öffne ein neues Tab
1. Gib `localhost:11434` in die URL-Schlitz ein

... Läuft Ollama dort?

## Testen Zwei - Test mit CURL

CURL-Befehl sollte sowohl in MacOS als auch in Windows schon installiert sein.
Wir können mit CURL-Kommand den API-Zugriff weiter testen:

**Windows**
```powershell
curl -X POST http://localhost:11434/api/generate -d "{\"model\": \"[Name des Modells]\", \"prompt\": \"Ollamaとは何ですか？\", \"temperature\": 0.8, \"max_tokens\": 200 }"
```


**MacOS**
```bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "[Name des Modells]",
  "prompt": "Ollamaとは何ですか？",
  "temperature": 0.8,
  "max_tokens": 200
}'
```

Hier haben wir in der API-Query die Parameters wie "temperature" oder "max_tokens" mitgegeben. So kann man die Reaktion eines Modells durch API kontrollieren.

## Übersicht der Parameters

- Für Kompletion: https://docs.ollama.com/api#generate-a-completion
- Für Chat-Kompletion: https://docs.ollama.com/api#generate-a-chat-completion

## Warum ist der API-Zugriff interessant?

Weil man damit eine neue Applikation erstellen kann und dadurch viel flexibler die Modelle einsetzen!

Beispiel: 
- Eine App ausprobieren: https://github.com/NbtKmy/ollama-spielwiese
- LLM in OpenRefine verwenden

### LLM in OpenRefine

Hier verwenden wir [LLM-Extention](https://github.com/sunilnatraj/llm-extension).

1. ZIP-file von latest release herunterladen und unzippen
2. Die ungezippte Datei in den Extention-Ordner speichern

![](./assets/openref_1.png)

3. LLM konfigurieren
![](./assets/openref_2.png)

![](./assets/openref_3.png)

4. Von einer Spalte her "Extract using AI" anwählen und durch das Prompt (wie unten) die Daten extrahieren


```text
Create JSON object from the description. Properties should include "name", "birth_date (YYYY-MM-DD)", "death_date (YYYY-MM-DD)", "themes_and_motifs".
```

