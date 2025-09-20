# 1. Kapitel - Ollama anfassen


...zuerst Ollama installlieren! Siehe [hier](https://ollama.com/).

## Was ist Ollama? Ganz kurz

- Eine Open Source Software mit MIT-Lizenz (siehe das [Github-Repo](https://github.com/ollama/ollama?tab=MIT-1-ov-file))
- Mit Ollama kann man LLMs in der lokalen Umgebung (offline) laufen lassen
- Seit 19. Sept. 2025 sind einige Cloud-LLMs angeboten (siehe die [Blogseite](https://ollama.com/blog/cloud-models)) - Wir behandeln sie hier nicht!!

## Chat-Window und Setting

...Sehen wir kurz die GUI von Ollama...

## Starten!

Wir öffnen Terminal und selber loslegen!
Zuerst überprüfen, ob Ollama wirklich funktioniert.
Öffne den Terminal und gibt den folgenden Befehl ein:


```bash
$ ollama --help
```

Danach erscheint eine Kommand-Übersicht.
Wenn dies funktioniert, laden wir ein beliebiges LLM herunter.
Welches LLM für eure Umgebung passend ist, erklärt der Dozent vor Ort!
Zum Herunterladen eines Modells verwendet man den folgenden Befehl:

```bash
$ ollama pull [Name des Modells]

# Beispiel
$ ollama pull gpt-oss
```

Danach beginnt das Herunterladen. Ihr wartet bis es fertig wird.
Wenn fertig, checken wir, ob das Modell zur Verfügung steht.

```bash
$ ollama list
```
Mit diesem Befehl werden die verfügbaren Modelle aufgelistet.
Habt ihr ein falsches Modell heruntergeladen?
Kein Problem! Mit dem folgenden Befehl kann man das Modell aus der lokelen Umgebung löschen.

```bash
$ ollama rm [Name des Modells]
```

## Ein Modell im Terminal laufen lassen

Wenn ihr ein Modell bereit habt, dann lass uns einfach mal mit dem chatten.
Gibt den folgenden Befehl in den Terminal ein:

```bash
$ ollama run [Name des Modells]
```

Und Führe mal ein Chat durch.
Wenn ihr das Chat beenden wollt, tippe einfach `/bye`.


# Ein Modell genauer beobachten

Bisher haben wir ein Modell einfach verwendet, ohne genaue Einstellung eines Modells zu betrachen. Wollt ihr die Konfiguration des Modells überprüfen?

```bash
$ ollama show [Name des Modells]
```

```
ollama show gpt-oss:20b
  Model
    architecture        gptoss    
    parameters          20.9B     
    context length      131072    
    embedding length    2880      
    quantization        MXFP4     

  Capabilities
    completion    
    tools         
    thinking      

  Parameters
    temperature    1    

  License
    Apache License               
    Version 2.0, January 2004    
    ...                          

```

Embedding length = Embedding Dimension 
Parameters & Quantization - Sie werden später genauer angesehen.

Für jetzt sind die Information unter "Capabilities" und "Parameters" uns wichtig. 
Der Abschnitt Capabilities zeigt, was das Modell kann.
"Parameters" zeigt, wie das Modell konfiguriert ist. Die Konfiguration kann natürlich geändert werden.

Um die Konfiguration zu ändern, gibt es zwei Möglichkeiten. Eine Möglichkeit ist, die Parameters durch API zu Ollama mitzuschicken. Die andere Möglichkeit ist, ein Modell neu zu konfigurieren,  indem man den Befehl `ollama create` im Terminal eingibt.

Hier probieren wir die 2. Methode aus, yey!

