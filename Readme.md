# 💰 Guida Finanziaria per Neofiti - Streamlit App

App educativa per la pianificazione finanziaria basata su una filosofia di prioritizzazione a tre fasi.

## 📋 Descrizione

Questa applicazione Streamlit aiuta i neofiti della finanza personale a pianificare le loro finanze seguendo un approccio strutturato in tre fasi:

1. **🛡️ FASE 1: Fondo di Emergenza** - Costruisci una base di sicurezza finanziaria
2. **🎯 FASE 2: Spese Prevedibili** - Pianifica obiettivi a lungo termine con PAC (Piano di Accumulo)
3. **📈 FASE 3: Investimenti** - Alloca i tuoi risparmi per la crescita del patrimonio

## 🚀 Installazione

### Prerequisiti
- Python 3.8 o superiore
- pip (package installer per Python)

### Passaggi

1. **Scarica i file**
   - Assicurati di avere `app.py` e `requirements.txt` nella stessa cartella

2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Come Eseguire l'App

1. Apri il terminale nella cartella contenente `app.py`

2. Esegui il comando:
   ```bash
   streamlit run app.py
   ```

3. L'app si aprirà automaticamente nel tuo browser predefinito a `http://localhost:8501`

## 🎯 Come Usare l'App

### 1. Inserisci i Dati Finanziari di Base
- **Entrate Mensili Nette**: Il tuo stipendio/entrate mensili al netto delle tasse
- **Uscite Mensili Totali**: Tutte le tue spese mensili fisse e variabili
- **Capitale Attuale**: I tuoi risparmi/liquidità disponibile

### 2. Inserisci Dati Demografici
- **Anni alla Pensione**: Quanti anni mancano alla tua pensione
- **Fascia di Età**: La tua età attuale

### 3. Aggiungi Obiettivi Futuri (Opzionale)
- Clicca su "Aggiungi Nuovo Obiettivo"
- Specifica nome, costo e tempo disponibile
- Puoi aggiungere multipli obiettivi (es. acconto casa, matrimonio, master)

### 4. Seleziona Profilo di Rischio
- **Conservatore**: Preferisci stabilità e basso rischio
- **Moderato**: Bilancio tra crescita e sicurezza
- **Aggressivo**: Massimizzi crescita accettando volatilità

### 5. Genera il Report
- Clicca su "Genera la Tua Guida Finanziaria Personalizzata"
- Leggi attentamente il report generato

## 📊 Cosa Fa l'App

### FASE 1: Fondo di Emergenza
L'app calcola il tuo fondo di emergenza target (6 mesi di spese) e verifica se è completo. Se non lo è, ti indica quanto manca e ti blocca alle fasi successive.

### FASE 2: PAC per Obiettivi
Per ogni obiettivo inserito, calcola quanto devi risparmiare mensilmente (Piano di Accumulo Mensile). Verifica anche se i tuoi PAC sono sostenibili rispetto al tuo risparmio disponibile.

### FASE 3: Allocazione Investimenti
Se hai completato le fasi precedenti, l'app suggerisce un'allocazione di portafoglio (Azioni/Obbligazioni/Oro) basata su:
- Il tuo profilo di rischio
- I tuoi anni alla pensione
- La tua disponibilità mensile per investimenti

## 🔒 Privacy e Sicurezza

- ✅ **Nessun dato viene salvato**: Tutti i dati rimangono nel tuo browser
- ✅ **Nessuna registrazione richiesta**
- ✅ **Nessun tracciamento**: L'app non invia dati a server esterni

## ⚠️ Disclaimer

Questa app fornisce **indicazioni educative generali** e **non costituisce consulenza finanziaria personalizzata**. 

- Non siamo consulenti finanziari certificati
- Non vendiamo prodotti finanziari
- Non garantiamo rendimenti sugli investimenti
- Consulta sempre un professionista per decisioni finanziarie importanti

## 🛠️ Caratteristiche Tecniche

- **Linguaggio**: Python
- **Framework**: Streamlit
- **Architettura**: Funzioni pure per calcoli + UI Streamlit
- **Output**: Report formattato in Markdown

## 📝 Funzionalità Implementate

- ✅ Calcolo Fondo di Emergenza
- ✅ Gestione multipli obiettivi con session state
- ✅ Calcolo PAC mensile per obiettivo
- ✅ Verifica sostenibilità PAC
- ✅ Allocazione portafoglio basata su profilo di rischio
- ✅ Aggiustamento allocazione per orizzonte temporale
- ✅ Report dettagliato in italiano
- ✅ Interfaccia user-friendly
- ✅ Disclaimer legale completo

## 🎓 Per Chi È Questa App

Questa app è ideale per:
- Persone che si avvicinano alla finanza personale per la prima volta
- Chi vuole una struttura chiara per organizzare le proprie finanze
- Neofiti che cercano un punto di partenza educativo
- Chi vuole capire come prioritizzare obiettivi finanziari

## 💡 Suggerimenti d'Uso

1. **Sii onesto con i numeri**: Inserisci dati realistici per ottenere consigli utili
2. **Rivedi periodicamente**: Usa l'app ogni 3-6 mesi per aggiornare il tuo piano
3. **Studia di più**: Usa questa app come punto di partenza, non come unica fonte
4. **Consulta professionisti**: Per decisioni importanti, parla con un consulente

## 🐛 Risoluzione Problemi

### L'app non si avvia
- Verifica di aver installato Streamlit: `pip install streamlit`
- Controlla la versione di Python: `python --version` (deve essere 3.8+)

### Errori durante l'esecuzione
- Prova a reinstallare le dipendenze: `pip install -r requirements.txt --upgrade`
- Assicurati di essere nella cartella corretta

### L'app si chiude inaspettatamente
- Controlla il terminale per messaggi di errore
- Riavvia l'app con `streamlit run app.py`

## 📞 Supporto

Per problemi tecnici o domande sull'app, puoi:
- Controllare la documentazione ufficiale di Streamlit: https://docs.streamlit.io
- Verificare che tutti i file siano nella stessa cartella

## 📄 Licenza

Questo progetto è fornito "as-is" per scopi educativi.

---

**Buona pianificazione finanziaria! 💪💰**
