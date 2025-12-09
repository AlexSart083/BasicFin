"""
Disclaimer Module
Contiene i disclaimer legali in italiano, inglese e tedesco
"""

def genera_disclaimer(lang):
    """
    Genera il disclaimer nella lingua specificata.
    
    Args:
        lang (str): Codice lingua (it, en, de)
        
    Returns:
        str: Disclaimer formattato in Markdown
    """
    if lang == "it":
        return _genera_disclaimer_it()
    elif lang == "en":
        return _genera_disclaimer_en()
    elif lang == "de":
        return _genera_disclaimer_de()
    else:
        return _genera_disclaimer_it()


def _genera_disclaimer_it():
    """Genera il disclaimer in italiano."""
    return """
---

## ⚖️ Disclaimer Importante

### Natura Educativa

Questa applicazione fornisce **indicazioni educative generali** sulla pianificazione finanziaria 
e **non costituisce consulenza finanziaria personalizzata**.

### Limitazioni

- ❌ **Non siamo consulenti finanziari certificati**
- ❌ **Non vendiamo prodotti finanziari**
- ❌ **Non riceviamo commissioni** da broker, banche o emittenti di ETF
- ❌ **Non garantiamo rendimenti** sugli investimenti
- ❌ **Non salviamo i tuoi dati** (tutto resta nel tuo browser durante la sessione)

### Cosa Dovresti Fare

- ✅ Usa questa guida come punto di partenza
- ✅ **Studia autonomamente** su risorse educative indipendenti
- ✅ Confronta sempre costi e performance
- ✅ Consulta un consulente indipendente per decisioni importanti
- ✅ Valuta sempre i rischi prima di investire

### Privacy e Dati

**Nessun dato viene salvato**: Tutte le informazioni inserite rimangono nella tua sessione 
di browser e vengono eliminate quando chiudi l'app. Non abbiamo accesso ai tuoi dati.

### Responsabilità

Tu sei l'unico responsabile delle tue decisioni di investimento. Gli investimenti comportano rischi, 
inclusa la perdita totale del capitale investito.

---

💙 **Ti auguriamo un futuro finanziario sereno e prospero!**

📚 **Ricorda**: L'educazione finanziaria è il miglior investimento che puoi fare!
"""


def _genera_disclaimer_en():
    """Generates disclaimer in English."""
    return """
---

## ⚖️ Important Disclaimer

### Educational Nature

This application provides **general educational guidance** on financial planning 
and **does not constitute personalized financial advice**.

### Limitations

- ❌ **We are not certified financial advisors**
- ❌ **We do not sell financial products**
- ❌ **We do not receive commissions** from brokers, banks, or ETF issuers
- ❌ **We do not guarantee returns** on investments
- ❌ **We do not save your data** (everything remains in your browser during the session)

### What You Should Do

- ✅ Use this guide as a starting point
- ✅ **Study independently** on independent educational resources
- ✅ Always compare costs and performance
- ✅ Consult an independent advisor for important decisions
- ✅ Always assess risks before investing
- ✅ Invest only what you can afford to lose in the short term

### Privacy and Data

**No data is saved**: All information entered remains in your browser session 
and is deleted when you close the app. We have no access to your data.

### Responsibility

You are solely responsible for your investment decisions. Investments involve risks, 
including total loss of invested capital.

---

💙 **We wish you a serene and prosperous financial future!**

📚 **Remember**: Financial education is the best investment you can make!
"""


def _genera_disclaimer_de():
    """Generiert Disclaimer auf Deutsch."""
    return """
---

## ⚖️ Wichtiger Haftungsausschluss

### Bildungscharakter

Diese Anwendung bietet **allgemeine Bildungsanleitung** zur Finanzplanung 
und **stellt keine personalisierte Finanzberatung dar**.

### Einschränkungen

- ❌ **Wir sind keine zertifizierten Finanzberater**
- ❌ **Wir verkaufen keine Finanzprodukte**
- ❌ **Wir erhalten keine Provisionen** von Brokern, Banken oder ETF-Emittenten
- ❌ **Wir garantieren keine Renditen** auf Investitionen
- ❌ **Wir speichern Ihre Daten nicht** (alles bleibt während der Sitzung in Ihrem Browser)

### Was Sie tun sollten

- ✅ Verwenden Sie diesen Leitfaden als Ausgangspunkt
- ✅ **Studieren Sie eigenständig** auf unabhängigen Bildungsressourcen
- ✅ Vergleichen Sie immer Kosten und Performance
- ✅ Konsultieren Sie einen unabhängigen Berater für wichtige Entscheidungen
- ✅ Bewerten Sie immer die Risiken vor der Investition
- ✅ Investieren Sie nur, was Sie kurzfristig verlieren können

### Datenschutz und Daten

**Keine Daten werden gespeichert**: Alle eingegebenen Informationen bleiben in Ihrer Browser-Sitzung 
und werden gelöscht, wenn Sie die App schließen. Wir haben keinen Zugriff auf Ihre Daten.

### Verantwortung

Sie sind allein verantwortlich für Ihre Investitionsentscheidungen. Investitionen beinhalten Risiken, 
einschließlich des Totalverlusts des investierten Kapitals.

---

💙 **Wir wünschen Ihnen eine ruhige und prosperierende finanzielle Zukunft!**

📚 **Denken Sie daran**: Finanzbildung ist die beste Investition, die Sie tätigen können!
"""
