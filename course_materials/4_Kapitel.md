# 4. Kapitel - Unterschiedliche Modelle Verwenden

Ollama bietet eine Menge KI-Modelle auf [ihrer offiziellen Website](https://ollama.com/search). Aber es gibt unzählige Modelle auf der Welt(!!) und man möchte sie doch verwenden - Klar, das kann man!

## Modelle auf Huggingface

[Huggingface](https://huggingface.co/) eine Plattform, die Entwicklern und Forschern hilft, KI-Modelle für Texte zu nutzen. Der zentrale Punkt ist der "Model Hub", in dem tausende vortrainierte Modelle für verschiedene Aufgaben verfügbar sind. 
Die Modelle sind, wie bei Github, durch Repositorien, zur Verfügung gestellt.

Wir lernen hier die Plattform ein wenig kennen. 

Wir besuchen diese Seite jetzt: https://huggingface.co/google/gemma-3-4b-it

Quiz:

- Könnt ihr sagen, was für eine Seite ist?
- Ist das Modell hier auf dieser Seite für Ollama anwendbar?

...Okay, dann guckt mal diese Seite: https://huggingface.co/nkamiy/gemma3-4b-it-gguf

Quiz:

- Könnt ihr sagen, was für eine Seite ist?
- Ist das Modell hier auf dieser Seite für Ollama anwendbar?
- Wer hat das Modell kreiert?

Okay, das Modell wollen wir verwenden. Der Dozent zeigt wie...



## Quantisierung

Es gibt eine Software [llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master), mit der man ein LLM quantisieren kann. Auf dieser Weise können wir viele grosse Modelle für einen Rechner mit der schwachen Rechnungsleistung zur Verfügung stellen.

In dem nächsten Kapitel wird der konkrete Prozess gezeigt.
