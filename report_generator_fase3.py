"""
Report Generator Module - Fase 3 (Investimenti)
Genera report dettagliati per gli investimenti a lungo termine con risorse educative
"""

from calculations import formatta_valuta, genera_allocazione_investimenti


def genera_report_fase3(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione, lang):
    """
    Genera il report FASE 3 nella lingua specificata.
    
    Args:
        disponibilita_mensile (float): Disponibilità mensile per investimenti
        capitale_investibile_subito (float): Capitale da investire immediatamente
        profilo_rischio (str): Profilo di rischio selezionato
        anni_pensione (int): Anni alla pensione
        lang (str): Codice lingua (it, en, de)
        
    Returns:
        str: Report formattato in Markdown
    """
    if lang == "it":
        return _genera_report_fase3_it(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione)
    elif lang == "en":
        return _genera_report_fase3_en(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione)
    elif lang == "de":
        return _genera_report_fase3_de(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione)
    else:
        return _genera_report_fase3_it(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione)


def _genera_report_fase3_it(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione):
    """Genera il report FASE 3 in italiano con dettagli completi."""
    
    report = f"""
## 📈 FASE 3: Investimenti a Lungo Termine

### Fai Crescere il Tuo Patrimonio

Congratulazioni! Hai completato le basi: Fondo di Emergenza e Pianificazione degli Obiettivi. 
Ora puoi investire per il futuro.

### Disponibilità per Investimenti

**Importo Mensile Investibile**: {formatta_valuta(disponibilita_mensile)}
"""
    
    if capitale_investibile_subito > 0:
        report += f"**Capitale da Investire Subito (lump sum)**: {formatta_valuta(capitale_investibile_subito)}\n\n"
        report += """
💡 **Strategia Consigliata**: Investi il capitale iniziale in un'unica soluzione (lump sum) seguendo 
l'allocazione indicata sotto, e continua con investimenti mensili regolari (PAC).
"""
    
    report += "\n"
    
    if disponibilita_mensile <= 0 and capitale_investibile_subito <= 0:
        report += """
### ⚠️ Nessuna Disponibilità

Al momento non hai disponibilità per investimenti a lungo termine. 
Concentrati sul completare le fasi precedenti o riduci le tue spese.

---
"""
        return report
    
    # Genera allocazione
    allocazione = genera_allocazione_investimenti(profilo_rischio, anni_pensione)
    
    report += f"""
### 🎯 La Tua Allocazione di Portafoglio

**Profilo di Rischio**: {profilo_rischio}  
**Orizzonte Temporale**: {anni_pensione} anni alla pensione

Basandoci sul tuo profilo e orizzonte temporale, ecco l'allocazione suggerita:

"""
    
    for asset, percentuale in allocazione.items():
        if disponibilita_mensile > 0:
            importo_mensile = disponibilita_mensile * (percentuale / 100)
            report += f"- **{asset}**: {percentuale}% → {formatta_valuta(importo_mensile)} al mese"
        else:
            report += f"- **{asset}**: {percentuale}%"
        
        if capitale_investibile_subito > 0:
            importo_lump = capitale_investibile_subito * (percentuale / 100)
            report += f" (+ {formatta_valuta(importo_lump)} lump sum)"
        
        report += "\n"
    
    report += """

---

### 📚 Dettagli su Asset e Strumenti

#### 🌍 Azioni - Componente Azionaria Globale

La componente azionaria è il motore di crescita del tuo portafoglio. Per massimizzare la diversificazione:

**Strumenti Consigliati (ETF):**

1. **MSCI World** - Paesi Sviluppati (≈1,500 azioni globali)
2. **MSCI ACWI o FTSE All-World** - Globale Completo (≈3,000 azioni)

**Criteri di Selezione ETF:**
- TER (costi annui) <0.25%
- Patrimonio gestito >€100M (per liquidità)
- Replica fisica (possiede direttamente i titoli)
- Distribuzione: Preferisci "Accumulo" (reinvestimento automatico dividendi)

---

#### 🏦 Obbligazioni - Componente di Stabilità

Le obbligazioni riducono la volatilità del portafoglio e forniscono reddito stabile.

**🚨 PRIORITÀ: Investi SOLO in obbligazioni denominate nella TUA valuta (EUR)**

**Strumenti Consigliati:**

1. **ETF Obbligazioni Governative Eurozona** (Investment Grade)
2. **ETF Obbligazioni Corporate Eurozona** (Investment Grade, rating BBB- o superiore)

**Criteri di Selezione:**
- Denominazione EUR (nessun rischio cambio)
- TER <0.20%
- Rating minimo BBB- (Investment Grade)
- Duration media 5-10 anni

---

#### 🥇 Oro - Protezione e Decorrelazione

L'oro protegge dall'inflazione e riduce il rischio di portafoglio.

**Strumenti Consigliati:**

1. **ETC Oro Fisico** (backed da oro reale in caveau)
   - TER <0.25%
   - Preferisci quelli domiciliati in Svizzera/UK per sicurezza

---

### 💰 Aspetti Fiscali

**Tassazione (Italia):**
- Aliquota standard: 26% su capital gains e dividendi
- Verifica con il tuo commercialista le opzioni fiscali disponibili
- Alcuni broker offrono servizi di dichiarazione automatica

**Scelta del Broker:**

Quando scegli una piattaforma di investimento, valuta:
- Costi di transazione e custodia
- Disponibilità degli strumenti che ti interessano (ETF, obbligazioni, ecc.)
- Facilità d'uso dell'interfaccia
- Servizio clienti nella tua lingua

**💡 Consiglio**: Confronta diverse opzioni, leggi recensioni indipendenti e scegli in base alle tue esigenze specifiche. Non esiste "il broker migliore" in assoluto, ma quello più adatto a te.

---

### 🎯 Piano di Azione

**1. Educati:**
- Studia su siti educativi indipendenti (vedi sezione risorse sotto)
- Comprendi la differenza tra azioni, obbligazioni, ETF
- Impara cos'è il TER e il tracking error

**2. Scegli gli Strumenti:**
- Usa screener ETF per trovare i migliori prodotti
- Confronta almeno 3 ETF per categoria
- Verifica domiciliazione fiscale (Irlanda/Lussemburgo sono ottimali per EU)

**3. Apri un Conto:**
- Confronta broker
- Completa KYC (Know Your Customer)
- Deposita capitale iniziale

**4. Imposta PAC Automatico:**
- Configura investimenti mensili automatici
- **Frequenza**: Mensile
- **Orario**: Se fai ordini manuali, usa orari centrali (10:00-16:00 CET)
- **Tipo ordine**: LIMIT (mai MARKET)

---

### 💡 Principi Fondamentali

**Il Segreto del Successo:**
1. **⏱️ TEMPO = Rimanere Investiti**
   - Non vendere mai in panico durante le crisi
   - Le crisi sono opportunità (compri a sconto con PAC)

2. **💎 COSTI BASSI = Più Rendimento**
   - TER 0.20% vs 1.50% = €245,906 di differenza su €100K in 30 anni!
   - ⚠️ Calcolo teorico con interesse composto al 7% lordo annuo (non una previsione di mercato)

3. **🧘 DISCIPLINA = PAC Continuo**
   - Investi sempre la stessa cifra mensile
   - Indipendentemente dal mercato (Dollar Cost Averaging)

**Mantra:** *"Il mercato azionario ha SEMPRE recuperato nel lungo termine. Rimango investito."*

---

### 📊 Il Potere dell'Interesse Composto e l'Impatto dei Costi

#### 🧮 Calcolo Dettagliato (Interesse Composto)

**⚠️ IMPORTANTE**: I seguenti calcoli usano un rendimento ipotetico del 7% annuo lordo per illustrare l'impatto matematico dei costi. **Questo NON è una previsione di mercato reale**. I rendimenti storici non garantiscono rendimenti futuri, e i mercati possono avere performance molto diverse.

**Formula dell'Interesse Composto:**
```
Capitale Finale = Capitale Iniziale × (1 + Rendimento Netto Annuo)^Anni
Rendimento Netto = Rendimento Lordo - TER
```

**Esempio con €100,000 investiti per 30 anni:**

**Scenario 1: ETF a Basso Costo (TER 0.20%)**
- Rendimento lordo: 7.00% annuo
- Costi (TER): 0.20% annuo
- Rendimento netto: 6.80% annuo
- Capitale finale: €100,000 × (1.068)³⁰ = **€764,645**

**Scenario 2: Fondo Attivo Costoso (TER 1.50%)**
- Rendimento lordo: 7.00% annuo
- Costi (TER): 1.50% annuo
- Rendimento netto: 5.50% annuo
- Capitale finale: €100,000 × (1.055)³⁰ = **€518,739**

**💰 Differenza: €245,906 persi in costi!**

Questo significa che **ogni 1% di costi in più ti costa circa il 32% del tuo capitale finale** su un orizzonte di 30 anni.

**📉 Impatto Percentuale dei Costi:**
- Con TER 0.20%: Perdi il 3.5% del potenziale rendimento
- Con TER 1.50%: Perdi il 32.1% del potenziale rendimento

**Conclusione:** I costi hanno un impatto devastante sul lungo termine a causa dell'interesse composto. Anche differenze apparentemente piccole (1% vs 0.2%) si traducono in centinaia di migliaia di euro persi.

---

### 🎓 Risorse Educative Consigliate

#### 📄 Strumenti Pratici Gratuiti

Ti consigliamo questi tool educativi per approfondire la tua pianificazione finanziaria:

**[One Page Financial](https://onepagefinancial-as.streamlit.app/)**
Visualizza il tuo piano finanziario completo in una singola pagina. Perfetto per avere una panoramica immediata di emergenze, obiettivi e investimenti. Usa questo tool per monitorare la tua progressione attraverso le 3 fasi!

**[Calcolatore Immobiliare](https://immobiliare-as.streamlit.app/)**
Pianifica l'acquisto della tua casa: calcola mutui, acconti necessari e confronta affitto vs acquisto. Essenziale per uno dei tuoi obiettivi più importanti. Include simulazioni di ammortamento e analisi costi-opportunità.

**[Finance App](https://financeapp-as.streamlit.app/)**
Strumento avanzato per la gestione del budget e analisi delle spese. Monitora dove vanno i tuoi soldi e ottimizza il risparmio mensile. Ideale per ottimizzare la FASE 1 e FASE 2 del tuo piano.

**[Overview Asset](https://overviewasset-as.streamlit.app/)**
Analizza e confronta diverse classi di asset (azioni, obbligazioni, oro, immobili). Comprendi rischi e rendimenti storici per scelte informate. Perfetto per la FASE 3!

**[Portfolio Manager](https://portfolio-as.streamlit.app/)**
Costruisci e monitora il tuo portafoglio di investimenti. Simula diverse allocazioni e traccia le performance nel tempo. Usa questo tool per implementare la tua allocazione della FASE 3.

---

#### 📚 Libri Consigliati

**In Italiano:**
- "L'investitore intelligente" - Benjamin Graham
- "Un passo avanti a Wall Street" - Burton Malkiel  
- "I soliti ignoti" - Paolo Coletti
- "Investimenti. La guida completa" - Banca d'Italia
- "Padre ricco padre povero" - Robert Kiyosaki
- "Educazione finanziaria" - Banca d'Italia (gratuito online)

**In Inglese:**
- "The Intelligent Investor" - Benjamin Graham
- "A Random Walk Down Wall Street" - Burton Malkiel
- "The Little Book of Common Sense Investing" - John C. Bogle
- "The One-Page Financial Plan" - Carl Richards
- "Rich Dad Poor Dad" - Robert Kiyosaki
- "Your Money or Your Life" - Vicki Robin & Joe Dominguez

**In Tedesco:**
- "Souverän investieren mit Indexfonds und ETFs" - Gerd Kommer
- "Der reichste Mann von Babylon" - George S. Clason
- "Rich Dad Poor Dad" - Robert Kiyosaki (tradotto)

---

#### 📺 Canali YouTube Educativi

Per approfondire la tua educazione finanziaria, ecco alcuni canali YouTube consigliati:

**Canali Italiani:**
- **Paolo Coletti** - Finanza personale e investimenti passivi
- **Mr. RIP** - FIRE (Financial Independence, Retire Early) e investimenti
- **Pietro Michelangeli** - Educazione finanziaria e risparmio

**Canali Inglesi:**
Cerca canali di finanza personale in inglese focalizzati su:
- Index fund investing
- Personal finance basics
- FIRE movement
- ETF education

**Canali Tedeschi:**
Cerca canali di finanza personale in tedesco focalizzati su:
- ETF-Investitionen
- Finanzielle Bildung
- Altersvorsorge

💡 **Consiglio:** Verifica sempre la qualità dei contenuti e confronta diverse fonti. I migliori canali educativi sono quelli che insegnano principi, non che vendono prodotti specifici.

---

### ⚠️ Cosa NON Fare

❌ **Non investire in:**
- Prodotti che non capisci
- Gestioni patrimoniali con costi >1%
- Fondi attivi con TER >1% (raramente battono gli indici)
- Criptovalute come investimento principale
- Azioni singole se sei principiante

❌ **Non fidarti di:**
- Promesse di rendimenti garantiti >10%/anno
- "Opportunità irripetibili" con urgenza
- Prodotti finanziari venduti porta-a-porta

✅ **Fidati di:**
- Dati storici e statistiche
- Costi bassi e trasparenti
- Diversificazione
- Tempo e disciplina

---
"""
    
    return report


def _genera_report_fase3_en(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione):
    """Generates PHASE 3 report in English with complete details."""
    
    report = f"""
## 📈 PHASE 3: Long-Term Investments

### Grow Your Wealth

Congratulations! You've completed the basics: Emergency Fund and Goal Planning. 
Now you can invest for the future.

### Investment Availability

**Monthly Investable Amount**: {formatta_valuta(disponibilita_mensile)}
"""
    
    if capitale_investibile_subito > 0:
        report += f"**Capital to Invest Immediately (lump sum)**: {formatta_valuta(capitale_investibile_subito)}\n\n"
        report += """
💡 **Recommended Strategy**: Invest the initial capital in a single lump sum following 
the allocation indicated below, and continue with regular monthly investments (PAC).
"""
    
    report += "\n"
    
    if disponibilita_mensile <= 0 and capitale_investibile_subito <= 0:
        report += """
### ⚠️ No Availability

Currently you have no availability for long-term investments. 
Focus on completing previous phases or reduce your expenses.

---
"""
        return report
    
    # Generate allocation
    allocazione = genera_allocazione_investimenti(profilo_rischio, anni_pensione)
    
    report += f"""
### 🎯 Your Portfolio Allocation

**Risk Profile**: {profilo_rischio}  
**Time Horizon**: {anni_pensione} years to retirement

Based on your profile and time horizon, here's the suggested allocation:

"""
    
    for asset, percentuale in allocazione.items():
        asset_en = {"Azioni": "Stocks", "Obbligazioni": "Bonds", "Oro": "Gold"}.get(asset, asset)
        if disponibilita_mensile > 0:
            importo_mensile = disponibilita_mensile * (percentuale / 100)
            report += f"- **{asset_en}**: {percentuale}% → {formatta_valuta(importo_mensile)} per month"
        else:
            report += f"- **{asset_en}**: {percentuale}%"
        
        if capitale_investibile_subito > 0:
            importo_lump = capitale_investibile_subito * (percentuale / 100)
            report += f" (+ {formatta_valuta(importo_lump)} lump sum)"
        
        report += "\n"
    
    report += """

---

### 📚 Asset and Instrument Details

#### 🌍 Stocks - Global Equity Component

The equity component is the growth engine of your portfolio. To maximize diversification:

**Recommended Instruments (ETFs):**

1. **MSCI World** - Developed Countries (≈1,500 global stocks)
2. **MSCI ACWI or FTSE All-World** - Complete Global (≈3,000 stocks)

**ETF Selection Criteria:**
- TER (annual costs) <0.25%
- Assets under management >€100M (for liquidity)
- Physical replication (directly owns securities)
- Distribution: Prefer "Accumulating" (automatic dividend reinvestment)

---

#### 🏦 Bonds - Stability Component

Bonds reduce portfolio volatility and provide stable income.

**🚨 PRIORITY: Invest ONLY in bonds denominated in YOUR currency (EUR)**

**Recommended Instruments:**

1. **Eurozone Government Bond ETFs** (Investment Grade)
2. **Eurozone Corporate Bond ETFs** (Investment Grade, BBB- rating or higher)

**Selection Criteria:**
- EUR denomination (no currency risk)
- TER <0.20%
- Minimum rating BBB- (Investment Grade)
- Average duration 5-10 years

---

#### 🥇 Gold - Protection and Decorrelation

Gold protects against inflation and reduces portfolio risk.

**Recommended Instruments:**

1. **Physical Gold ETC** (backed by real gold in vaults)
   - TER <0.25%
   - Prefer those domiciled in Switzerland/UK for security

---

### 💰 Tax Aspects

**Taxation (varies by country):**
- Check your local capital gains tax rate
- Consult with a tax advisor for available options
- Some brokers offer automatic tax reporting services

**Choosing a Broker:**

When choosing an investment platform, evaluate:
- Transaction and custody costs
- Availability of instruments you're interested in (ETFs, bonds, etc.)
- User interface ease of use
- Customer service in your language

**💡 Tip**: Compare different options, read independent reviews, and choose based on your specific needs. There's no "best broker" in absolute terms, but the one most suitable for you.

---

### 🎯 Action Plan

**1. Educate Yourself:**
- Study on independent educational sites (see resources section below)
- Understand the difference between stocks, bonds, ETFs
- Learn what TER and tracking error are

**2. Choose Instruments:**
- Use ETF screeners to find the best products
- Compare at least 3 ETFs per category
- Verify tax domicile (Ireland/Luxembourg are optimal for EU)

**3. Open an Account:**
- Compare brokers
- Complete KYC (Know Your Customer)
- Deposit initial capital

**4. Set Up Automatic PAC:**
- Configure automatic monthly investments
- **Frequency**: Monthly
- **Timing**: If doing manual orders, use central hours (10:00-16:00 CET)
- **Order type**: LIMIT (never MARKET)

---

### 💡 Fundamental Principles

**The Secret to Success:**
1. **⏱️ TIME = Stay Invested**
   - Never sell in panic during crises
   - Crises are opportunities (buy at discount with PAC)

2. **💎 LOW COSTS = More Returns**
   - TER 0.20% vs 1.50% = €245,906 difference on €100K over 30 years!
   - ⚠️ Theoretical calculation with 7% gross annual compound interest (not a market forecast)

3. **🧘 DISCIPLINE = Continuous PAC**
   - Always invest the same monthly amount
   - Regardless of market conditions (Dollar Cost Averaging)

**Mantra:** *"The stock market has ALWAYS recovered in the long term. I stay invested."*

---

### 📊 The Power of Compound Interest and Cost Impact

#### 🧮 Detailed Calculation (Compound Interest)

**⚠️ IMPORTANT**: The following calculations use a hypothetical 7% annual gross return to illustrate the mathematical impact of costs. **This is NOT a real market forecast**. Historical returns do not guarantee future returns, and markets can perform very differently.

**Compound Interest Formula:**
```
Final Capital = Initial Capital × (1 + Net Annual Return)^Years
Net Return = Gross Return - TER
```

**Example with €100,000 invested for 30 years:**

**Scenario 1: Low-Cost ETF (TER 0.20%)**
- Gross return: 7.00% per year
- Costs (TER): 0.20% per year
- Net return: 6.80% per year
- Final capital: €100,000 × (1.068)³⁰ = **€764,645**

**Scenario 2: Expensive Active Fund (TER 1.50%)**
- Gross return: 7.00% per year
- Costs (TER): 1.50% per year
- Net return: 5.50% per year
- Final capital: €100,000 × (1.055)³⁰ = **€518,739**

**💰 Difference: €245,906 lost to costs!**

This means that **every 1% extra in costs costs you approximately 32% of your final capital** over a 30-year horizon.

**📉 Percentage Impact of Costs:**
- With TER 0.20%: You lose 3.5% of potential returns
- With TER 1.50%: You lose 32.1% of potential returns

**Conclusion:** Costs have a devastating long-term impact due to compound interest. Even seemingly small differences (1% vs 0.2%) translate into hundreds of thousands of euros lost.

---

### 🎓 Recommended Educational Resources

#### 📄 Free Practical Tools

We recommend these educational tools to deepen your financial planning:

**[One Page Financial](https://onepagefinancial-as.streamlit.app/)**
Visualize your complete financial plan on a single page. Perfect for an immediate overview of emergencies, goals and investments. Use this tool to monitor your progression through the 3 phases!

**[Real Estate Calculator](https://immobiliare-as.streamlit.app/)**
Plan your home purchase: calculate mortgages, required down payments and compare rent vs buy. Essential for one of your most important goals. Includes amortization simulations and cost-opportunity analysis.

**[Finance App](https://financeapp-as.streamlit.app/)**
Advanced tool for budget management and expense analysis. Track where your money goes and optimize monthly savings. Ideal for optimizing PHASE 1 and PHASE 2 of your plan.

**[Overview Asset](https://overviewasset-as.streamlit.app/)**
Analyze and compare different asset classes (stocks, bonds, gold, real estate). Understand historical risks and returns for informed choices. Perfect for PHASE 3!

**[Portfolio Manager](https://portfolio-as.streamlit.app/)**
Build and monitor your investment portfolio. Simulate different allocations and track performance over time. Use this tool to implement your PHASE 3 allocation.

---

#### 📚 Recommended Books

**In Italian:**
- "L'investitore intelligente" - Benjamin Graham
- "Un passo avanti a Wall Street" - Burton Malkiel  
- "I soliti ignoti" - Paolo Coletti
- "Investimenti. La guida completa" - Banca d'Italia
- "Padre ricco padre povero" - Robert Kiyosaki
- "Educazione finanziaria" - Banca d'Italia (free online)

**In English:**
- "The Intelligent Investor" - Benjamin Graham
- "A Random Walk Down Wall Street" - Burton Malkiel
- "The Little Book of Common Sense Investing" - John C. Bogle
- "The One-Page Financial Plan" - Carl Richards
- "Rich Dad Poor Dad" - Robert Kiyosaki
- "Your Money or Your Life" - Vicki Robin & Joe Dominguez

**In German:**
- "Souverän investieren mit Indexfonds und ETFs" - Gerd Kommer
- "Der reichste Mann von Babylon" - George S. Clason
- "Rich Dad Poor Dad" - Robert Kiyosaki (translated)

---

#### 📺 Educational YouTube Channels

To deepen your financial education, here are some recommended YouTube channels:

**Italian Channels:**
- **Paolo Coletti** - Personal finance and passive investing
- **Mr. RIP** - FIRE (Financial Independence, Retire Early) and investing
- **Pietro Michelangeli** - Financial education and saving

**English Channels:**
Look for English personal finance channels focused on:
- Index fund investing
- Personal finance basics
- FIRE movement
- ETF education

**German Channels:**
Look for German personal finance channels focused on:
- ETF-Investitionen
- Finanzielle Bildung
- Altersvorsorge

💡 **Tip:** Always verify content quality and compare different sources. The best educational channels are those that teach principles, not sell specific products.

---

### ⚠️ What NOT to Do

❌ **Don't invest in:**
- Products you don't understand
- Asset management with costs >1%
- Active funds with TER >1% (rarely beat indexes)
- Cryptocurrencies as main investment
- Individual stocks if you're a beginner

❌ **Don't trust:**
- Promises of guaranteed returns >10%/year
- "Unmissable opportunities" with urgency
- Financial products sold door-to-door

✅ **Trust:**
- Historical data and statistics
- Low and transparent costs
- Diversification
- Time and discipline

---
"""
    
    return report


def _genera_report_fase3_de(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione):
    """Generiert PHASE 3 Bericht auf Deutsch mit vollständigen Details."""
    
    report = f"""
## 📈 PHASE 3: Langfristige Investitionen

### Lassen Sie Ihr Vermögen wachsen

Herzlichen Glückwunsch! Sie haben die Grundlagen abgeschlossen: Notgroschen und Zielplanung. 
Jetzt können Sie für die Zukunft investieren.

### Investitionsverfügbarkeit

**Monatlich investierbarer Betrag**: {formatta_valuta(disponibilita_mensile)}
"""
    
    if capitale_investibile_subito > 0:
        report += f"**Sofort zu investierendes Kapital (Einmalanlage)**: {formatta_valuta(capitale_investibile_subito)}\n\n"
        report += """
💡 **Empfohlene Strategie**: Investieren Sie das Anfangskapital in einer Einmalanlage gemäß 
der unten angegebenen Allokation und fahren Sie mit regelmäßigen monatlichen Investitionen (PAC) fort.
"""
    
    report += "\n"
    
    if disponibilita_mensile <= 0 and capitale_investibile_subito <= 0:
        report += """
### ⚠️ Keine Verfügbarkeit

Derzeit haben Sie keine Verfügbarkeit für langfristige Investitionen. 
Konzentrieren Sie sich auf das Abschließen vorheriger Phasen oder reduzieren Sie Ihre Ausgaben.

---
"""
        return report
    
    # Allokation generieren
    allocazione = genera_allocazione_investimenti(profilo_rischio, anni_pensione)
    
    report += f"""
### 🎯 Ihre Portfolio-Allokation

**Risikoprofil**: {profilo_rischio}  
**Zeithorizont**: {anni_pensione} Jahre bis zur Rente

Basierend auf Ihrem Profil und Zeithorizont ist hier die vorgeschlagene Allokation:

"""
    
    for asset, percentuale in allocazione.items():
        asset_de = {"Azioni": "Aktien", "Obbligazioni": "Anleihen", "Oro": "Gold"}.get(asset, asset)
        if disponibilita_mensile > 0:
            importo_mensile = disponibilita_mensile * (percentuale / 100)
            report += f"- **{asset_de}**: {percentuale}% → {formatta_valuta(importo_mensile)} pro Monat"
        else:
            report += f"- **{asset_de}**: {percentuale}%"
        
        if capitale_investibile_subito > 0:
            importo_lump = capitale_investibile_subito * (percentuale / 100)
            report += f" (+ {formatta_valuta(importo_lump)} Einmalanlage)"
        
        report += "\n"
    
    report += """

---

### 📚 Details zu Vermögenswerten und Instrumenten

#### 🌍 Aktien - Globale Aktienkomponente

Die Aktienkomponente ist der Wachstumsmotor Ihres Portfolios. Um die Diversifikation zu maximieren:

**Empfohlene Instrumente (ETFs):**

1. **MSCI World** - Entwickelte Länder (≈1.500 globale Aktien)
2. **MSCI ACWI oder FTSE All-World** - Vollständig global (≈3.000 Aktien)

**ETF-Auswahlkriterien:**
- TER (jährliche Kosten) <0,25%
- Verwaltetes Vermögen >€100M (für Liquidität)
- Physische Replikation (besitzt direkt Wertpapiere)
- Verteilung: Bevorzugen Sie "Thesaurierend" (automatische Dividendenreinvestition)

---

#### 🏦 Anleihen - Stabilitätskomponente

Anleihen reduzieren die Portfolio-Volatilität und bieten stabiles Einkommen.

**🚨 PRIORITÄT: Investieren Sie NUR in Anleihen, die in IHRER Währung (EUR) denominiert sind**

**Empfohlene Instrumente:**

1. **Eurozone-Staatsanleihen-ETFs** (Investment Grade)
2. **Eurozone-Unternehmensanleihen-ETFs** (Investment Grade, BBB- Rating oder höher)

**Auswahlkriterien:**
- EUR-Denominierung (kein Währungsrisiko)
- TER <0,20%
- Mindestrating BBB- (Investment Grade)
- Durchschnittliche Duration 5-10 Jahre

---

#### 🥇 Gold - Schutz und Dekorrelation

Gold schützt vor Inflation und reduziert das Portfolio-Risiko.

**Empfohlene Instrumente:**

1. **Physische Gold-ETCs** (besichert durch echtes Gold in Tresoren)
   - TER <0,25%
   - Bevorzugen Sie solche mit Domizil in der Schweiz/UK für Sicherheit

---

### 💰 Steuerliche Aspekte

**Besteuerung (variiert je nach Land):**
- Prüfen Sie Ihren lokalen Kapitalertragsteuersatz
- Konsultieren Sie einen Steuerberater für verfügbare Optionen
- Einige Broker bieten automatische Steuermeldedienste

**Auswahl eines Brokers:**

Bei der Auswahl einer Investitionsplattform bewerten Sie:
- Transaktions- und Depotkosten
- Verfügbarkeit der Instrumente, die Sie interessieren (ETFs, Anleihen, etc.)
- Benutzerfreundlichkeit der Oberfläche
- Kundenservice in Ihrer Sprache

**💡 Tipp**: Vergleichen Sie verschiedene Optionen, lesen Sie unabhängige Bewertungen und wählen Sie basierend auf Ihren spezifischen Bedürfnissen. Es gibt keinen "besten Broker" im absoluten Sinne, sondern den für Sie am besten geeigneten.

---

### 🎯 Aktionsplan

**1. Bilden Sie sich weiter:**
- Studieren Sie auf unabhängigen Bildungsseiten (siehe Ressourcen-Abschnitt unten)
- Verstehen Sie den Unterschied zwischen Aktien, Anleihen, ETFs
- Lernen Sie, was TER und Tracking Error sind

**2. Wählen Sie Instrumente:**
- Verwenden Sie ETF-Screener, um die besten Produkte zu finden
- Vergleichen Sie mindestens 3 ETFs pro Kategorie
- Überprüfen Sie die Steuerdomizilin (Irland/Luxemburg sind optimal für EU)

**3. Eröffnen Sie ein Konto:**
- Vergleichen Sie Broker
- Schließen Sie KYC (Know Your Customer) ab
- Zahlen Sie Anfangskapital ein

**4. Richten Sie automatischen PAC ein:**
- Konfigurieren Sie automatische monatliche Investitionen
- **Häufigkeit**: Monatlich
- **Zeitpunkt**: Bei manuellen Orders zentrale Stunden nutzen (10:00-16:00 CET)
- **Ordertyp**: LIMIT (niemals MARKET)

---

### 💡 Grundlegende Prinzipien

**Das Erfolgsgeheimnis:**
1. **⏱️ ZEIT = Investiert bleiben**
   - Verkaufen Sie niemals in Panik während Krisen
   - Krisen sind Gelegenheiten (kaufen Sie mit Rabatt durch PAC)

2. **💎 NIEDRIGE KOSTEN = Mehr Rendite**
   - TER 0,20% vs. 1,50% = €245.906 Unterschied auf €100K über 30 Jahre!
   - ⚠️ Theoretische Berechnung mit 7% Brutto-Jahreszins (keine Marktprognose)

3. **🧘 DISZIPLIN = Kontinuierlicher PAC**
   - Investieren Sie immer denselben monatlichen Betrag
   - Unabhängig von Marktbedingungen (Dollar Cost Averaging)

**Mantra:** *"Der Aktienmarkt hat sich langfristig IMMER erholt. Ich bleibe investiert."*

---

### 📊 Die Kraft des Zinseszinses und die Kostenauswirkung

#### 🧮 Detaillierte Berechnung (Zinseszins)

**⚠️ WICHTIG**: Die folgenden Berechnungen verwenden eine hypothetische jährliche Bruttorendite von 7%, um die mathematische Auswirkung der Kosten zu veranschaulichen. **Dies ist KEINE echte Marktprognose**. Historische Renditen garantieren keine zukünftigen Renditen, und Märkte können sehr unterschiedlich performen.

**Zinseszins-Formel:**
```
Endkapital = Anfangskapital × (1 + Netto-Jahresrendite)^Jahre
Nettorendite = Bruttorendite - TER
```

**Beispiel mit €100.000 investiert für 30 Jahre:**

**Szenario 1: Kostengünstiger ETF (TER 0,20%)**
- Bruttorendite: 7,00% pro Jahr
- Kosten (TER): 0,20% pro Jahr
- Nettorendite: 6,80% pro Jahr
- Endkapital: €100.000 × (1,068)³⁰ = **€764.645**

**Szenario 2: Teurer aktiver Fonds (TER 1,50%)**
- Bruttorendite: 7,00% pro Jahr
- Kosten (TER): 1,50% pro Jahr
- Nettorendite: 5,50% pro Jahr
- Endkapital: €100.000 × (1,055)³⁰ = **€518.739**

**💰 Unterschied: €245.906 durch Kosten verloren!**

Das bedeutet, dass **jedes zusätzliche 1% an Kosten Sie etwa 32% Ihres Endkapitals kostet** über einen 30-Jahres-Horizont.

**📉 Prozentuale Auswirkung der Kosten:**
- Mit TER 0,20%: Sie verlieren 3,5% der potenziellen Rendite
- Mit TER 1,50%: Sie verlieren 32,1% der potenziellen Rendite

**Fazit:** Kosten haben aufgrund des Zinseszinses eine verheerende langfristige Auswirkung. Selbst scheinbar kleine Unterschiede (1% vs. 0,2%) führen zu Hunderttausenden von Euro an Verlusten.

---

### 🎓 Empfohlene Bildungsressourcen

#### 📄 Kostenlose praktische Tools

Wir empfehlen diese Bildungstools zur Vertiefung Ihrer Finanzplanung:

**[One Page Financial](https://onepagefinancial-as.streamlit.app/)**
Visualisieren Sie Ihren kompletten Finanzplan auf einer einzigen Seite. Perfekt für einen sofortigen Überblick über Notfälle, Ziele und Investitionen. Verwenden Sie dieses Tool, um Ihren Fortschritt durch die 3 Phasen zu verfolgen!

**[Immobilienrechner](https://immobiliare-as.streamlit.app/)**
Planen Sie Ihren Hauskauf: Berechnen Sie Hypotheken, erforderliche Anzahlungen und vergleichen Sie Miete vs. Kauf. Essentiell für eines Ihrer wichtigsten Ziele. Enthält Tilgungssimulationen und Kosten-Nutzen-Analyse.

**[Finance App](https://financeapp-as.streamlit.app/)**
Fortgeschrittenes Tool für Budgetverwaltung und Ausgabenanalyse. Verfolgen Sie, wohin Ihr Geld fließt und optimieren Sie monatliche Ersparnisse. Ideal zur Optimierung von PHASE 1 und PHASE 2 Ihres Plans.

**[Overview Asset](https://overviewasset-as.streamlit.app/)**
Analysieren und vergleichen Sie verschiedene Anlageklassen (Aktien, Anleihen, Gold, Immobilien). Verstehen Sie historische Risiken und Renditen für fundierte Entscheidungen. Perfekt für PHASE 3!

**[Portfolio Manager](https://portfolio-as.streamlit.app/)**
Bauen und überwachen Sie Ihr Anlageportfolio. Simulieren Sie verschiedene Allokationen und verfolgen Sie die Performance im Zeitverlauf. Verwenden Sie dieses Tool zur Umsetzung Ihrer PHASE 3 Allokation.

---

#### 📚 Empfohlene Bücher

**Auf Italienisch:**
- "L'investitore intelligente" - Benjamin Graham
- "Un passo avanti a Wall Street" - Burton Malkiel  
- "I soliti ignoti" - Paolo Coletti
- "Investimenti. La guida completa" - Banca d'Italia
- "Padre ricco padre povero" - Robert Kiyosaki
- "Educazione finanziaria" - Banca d'Italia (kostenlos online)

**Auf Englisch:**
- "The Intelligent Investor" - Benjamin Graham
- "A Random Walk Down Wall Street" - Burton Malkiel
- "The Little Book of Common Sense Investing" - John C. Bogle
- "The One-Page Financial Plan" - Carl Richards
- "Rich Dad Poor Dad" - Robert Kiyosaki
- "Your Money or Your Life" - Vicki Robin & Joe Dominguez

**Auf Deutsch:**
- "Souverän investieren mit Indexfonds und ETFs" - Gerd Kommer
- "Der reichste Mann von Babylon" - George S. Clason
- "Rich Dad Poor Dad" - Robert Kiyosaki (übersetzt)

---

#### 📺 Bildungs-YouTube-Kanäle

Um Ihre Finanzbildung zu vertiefen, hier einige empfohlene YouTube-Kanäle:

**Italienische Kanäle:**
- **Paolo Coletti** - Persönliche Finanzen und passives Investieren
- **Mr. RIP** - FIRE (Financial Independence, Retire Early) und Investitionen
- **Pietro Michelangeli** - Finanzbildung und Sparen

**Englische Kanäle:**
Suchen Sie nach englischen Personal-Finance-Kanälen mit Fokus auf:
- Index fund investing
- Personal finance basics
- FIRE movement
- ETF education

**Deutsche Kanäle:**
Suchen Sie nach deutschen Finanzbildungskanälen mit Fokus auf:
- ETF-Investitionen
- Finanzielle Bildung
- Altersvorsorge

💡 **Tipp:** Überprüfen Sie immer die Qualität der Inhalte und vergleichen Sie verschiedene Quellen. Die besten Bildungskanäle sind diejenigen, die Prinzipien lehren, nicht spezifische Produkte verkaufen.

---

### ⚠️ Was NICHT zu tun ist

❌ **Investieren Sie nicht in:**
- Produkte, die Sie nicht verstehen
- Vermögensverwaltung mit Kosten >1%
- Aktive Fonds mit TER >1% (schlagen selten Indizes)
- Kryptowährungen als Hauptinvestition
- Einzelaktien, wenn Sie Anfänger sind

❌ **Vertrauen Sie nicht:**
- Versprechungen garantierter Renditen >10%/Jahr
- "Unverpassbare Gelegenheiten" mit Dringlichkeit
- Finanzprodukten, die von Tür zu Tür verkauft werden

✅ **Vertrauen Sie:**
- Historischen Daten und Statistiken
- Niedrigen und transparenten Kosten
- Diversifikation
- Zeit und Disziplin

---
"""
    
    return report
