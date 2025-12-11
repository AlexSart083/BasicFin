"""
Translations for Financial Guide App
Supporta: Italiano (it), English (en), Deutsch (de)
"""

TRANSLATIONS = {
    "it": {
        # Header e navigazione
        "app_title": "💰 Guida Finanziaria per Neofiti",
        "welcome": "Benvenuto nella tua guida finanziaria personale!",
        "language": "🌍 Lingua / Language / Sprache",
        "version_info": "Versione",
        
        # Intro semplificata
        "intro_text": """Prima di iniziare con i tuoi dati, è fondamentale comprendere la **filosofia 
di prioritizzazione a tre fasi** che guiderà le tue scelte finanziarie.""",
        
        # Descrizione delle Fasi
        "phases_title": "📚 La Filosofia delle Tre Fasi",
        "phases_intro": """Questa guida segue un approccio strutturato e progressivo per costruire 
una solida base finanziaria. Ogni fase ha una priorità specifica e deve essere completata 
prima di passare alla successiva.""",
        
        "phase1_title": "🛡️ FASE 1: Fondo di Emergenza (Priorità Assoluta)",
        "phase1_desc": """**Obiettivo**: Creare un cuscinetto di sicurezza per proteggere te e la tua famiglia dagli imprevisti.

**La Regola**: Devi avere liquidità pari a **6 mesi di spese**.

**Perché è fondamentale?**
- Protegge dalla perdita improvvisa del lavoro
- Copre spese mediche urgenti non previste
- Evita di dover vendere investimenti in perdita durante una crisi personale
- Ti permette di dormire sonni tranquilli

**Dove tenere questi soldi?**
- Conto corrente o conto deposito facilmente accessibile
- NON investire in azioni o strumenti rischiosi
- Deve essere **immediatamente disponibile** in caso di emergenza

**Filosofia**: Senza questa base, qualsiasi imprevisto può distruggere i tuoi piani finanziari.""",
        
        "phase2_title": "🎯 FASE 2: Spese Prevedibili (Obiettivi a Medio-Lungo Termine)",
        "phase2_desc": """**Obiettivo**: Pianificare e accantonare mensilmente per spese future certe o altamente probabili.

**Esempi di obiettivi**:
- Acconto per l'acquisto di una casa (tra 3-5 anni)
- Matrimonio o eventi importanti (tra 2-4 anni)
- Master universitario o formazione specialistica
- Ristrutturazione casa
- Grande viaggio (es. anno sabbatico)

**Il concetto chiave: PAC (Piano di Accumulo Mensile)**

Per ogni obiettivo futuro, calcoli quanto devi risparmiare ogni mese:
```
PAC Mensile = Costo Totale / Mesi Disponibili
```

**Esempio pratico**:
- Obiettivo: Acconto casa di €30.000 tra 5 anni
- PAC Mensile = €30.000 / 60 mesi = **€500/mese**

**Dove allocare questi soldi?**
- Conti deposito o obbligazioni a breve termine per obiettivi <5 anni
- ETF obbligazionari conservativi per obiettivi 5-10 anni
- NON investire in azioni se l'obiettivo è entro 3-5 anni (troppo volatile)

**Filosofia**: Separa ciò che è "prevedibile" da ciò che è "investibile a lungo termine".""",
        
        "phase3_title": "📈 FASE 3: Investimenti a Lungo Termine (Crescita del Patrimonio)",
        "phase3_desc": """**Obiettivo**: Far crescere il tuo patrimonio per la pensione e il lungo termine (>10 anni).

**Chi può investire qui?**
Solo chi ha COMPLETATO le Fasi 1 e 2!

**Cosa puoi investire?**
Dopo aver coperto:
1. ✅ Fondo di Emergenza (6 mesi di spese)
2. ✅ PAC mensili per obiettivi futuri

Ti rimane il **capitale eccedente** e il **risparmio mensile libero**.

**Come allocare gli investimenti?**

L'allocazione dipende da:
- **Profilo di rischio**: Conservatore, Moderato, Aggressivo
- **Orizzonte temporale**: Anni alla pensione

**Classi di asset principali**:
1. **Azioni (ETF azionari globali)**:
   - Motore di crescita del portafoglio
   - Alta volatilità ma massimo potenziale di rendimento
   - Ideale per orizzonti >15 anni

2. **Obbligazioni (ETF obbligazionari)**:
   - Stabilità e reddito costante
   - Bassa volatilità
   - Protezione durante crisi azionarie

3. **Oro (ETC oro fisico)**:
   - Protezione dall'inflazione
   - Decorrelazione con azioni e obbligazioni
   - 5-10% del portafoglio

**Esempio allocazioni**:
- **Conservatore** (basso rischio): 30% Azioni, 60% Obbligazioni, 10% Oro
- **Moderato** (bilanciato): 50% Azioni, 40% Obbligazioni, 10% Oro
- **Aggressivo** (alta crescita): 70% Azioni, 20% Obbligazioni, 10% Oro

**Filosofia**: Il tempo è il tuo migliore alleato. Investi con disciplina e non vendere mai in panico durante le crisi.""",
        
        "why_this_order": "❓ Perché Questo Ordine è Fondamentale?",
        "why_this_order_desc": """1. **Senza Fondo di Emergenza** (Fase 1): Un imprevisto ti costringe a vendere investimenti in perdita o indebitarti.

2. **Senza Pianificazione Obiettivi** (Fase 2): Rischi di investire soldi di cui avrai bisogno a breve, costringendoti a disinvestire al momento sbagliato.

3. **Con Base Solida** (Fase 1 + 2 Completate): Puoi investire serenamente sapendo che le emergenze e gli obiettivi sono coperti.

**🎯 Questo approccio ti permette di investire SENZA STRESS, perché hai già protetto il tuo presente e il tuo futuro prevedibile.**""",
        
        # Input sections
        "input_data_title": "📝 Inserisci i Tuoi Dati Finanziari",
        "input_data_intro": "Ora che hai compreso la filosofia, inserisci i tuoi dati per ricevere un piano personalizzato.",
        
        "basic_data": "💰 Dati Finanziari",
        "monthly_income": "💵 Entrate Mensili Nette (€)",
        "monthly_expenses": "💳 Uscite Mensili Totali (€)",
        "current_capital": "🏦 Capitale Attuale/Liquidità (€)",
        "invested_capital": "📊 Capitale Già Investito (€)",
        "income_help": "Il tuo stipendio netto mensile o entrate regolari",
        "expenses_help": "Tutte le tue spese mensili (affitto, bollette, cibo, ecc.)",
        "capital_help": "I tuoi risparmi liquidi attuali (conti correnti, conti deposito)",
        "invested_help": "Soldi già investiti in azioni, ETF, fondi, ecc. (per info, non influisce sui calcoli)",
        
        "demographic_data": "⏰ Orizzonte Temporale",
        "years_to_retirement": "Anni alla Pensione",
        "retirement_help": "Quanti anni mancano alla tua pensione? (determina l'orizzonte per la FASE 3)",
        
        "future_goals": "🎯 Obiettivi Futuri (Spese Medio-Lungo Termine)",
        "goals_intro": "Aggiungi qui i tuoi obiettivi che richiedono pianificazione finanziaria (FASE 2).",
        "add_goal": "➕ Aggiungi Nuovo Obiettivo",
        "goal_name": "Nome Obiettivo",
        "goal_name_placeholder": "es. Acconto Casa",
        "estimated_cost": "Costo Stimato (€)",
        "years_to_goal": "Anni all'Obiettivo",
        "add_goal_btn": "✅ Aggiungi Obiettivo",
        "your_goals": "📋 I Tuoi Obiettivi",
        "no_goals": "ℹ️ Nessun obiettivo aggiunto. Se non hai obiettivi specifici, più capitale andrà agli investimenti (FASE 3)!",
        "goal_added": "✅ Obiettivo '{goal_name}' aggiunto!",
        "goal_name_required": "⚠️ Inserisci un nome per l'obiettivo",
        
        "risk_profile": "📊 Profilo di Rischio (per FASE 3)",
        "risk_intro": "Il tuo profilo di rischio determinerà l'allocazione degli investimenti a lungo termine.",
        "select_risk": "Seleziona il tuo profilo di rischio:",
        "conservative": "Conservatore",
        "moderate": "Moderato",
        "aggressive": "Aggressivo",
        "risk_help": """- **Conservatore**: Preferisci stabilità e basso rischio (adatto se pensione <10 anni)
- **Moderato**: Bilanciato tra crescita e sicurezza
- **Aggressivo**: Massimizzi la crescita accettando volatilità (adatto se pensione >20 anni)""",
        "conservative_desc": "🛡️ Proteggi il capitale con investimenti stabili",
        "moderate_desc": "⚖️ Bilancia crescita e sicurezza",
        "aggressive_desc": "🚀 Massimizza il potenziale di crescita",
        
        "generate_report": "🚀 Genera il Mio Piano Finanziario Personalizzato",
        "personalized_guide": "📊 Il Tuo Piano Finanziario Personalizzato",
        "report_success": "✅ Piano generato con successo!",
        
        # Common terms
        "cost": "Costo",
        "time": "Tempo",
        "years": "anni",
        "monthly_pac": "PAC mensile",
        "months": "mesi",
        
        # Educational resources
        "educational_sites": "🎓 Siti Educativi Consigliati",
        "educational_sites_intro": "Per approfondire la tua educazione finanziaria, ti consigliamo questi strumenti gratuiti:",
        
        "site_onepage_name": "📄 One Page Financial",
        "site_onepage_desc": "Visualizza il tuo piano finanziario completo in una singola pagina. Perfetto per avere una panoramica immediata di emergenze, obiettivi e investimenti.",
        
        "site_immobiliare_name": "🏠 Calcolatore Immobiliare",
        "site_immobiliare_desc": "Pianifica l'acquisto della tua casa: calcola mutui, acconti necessari e confronta affitto vs acquisto. Essenziale per uno dei tuoi obiettivi più importanti.",
        
        "site_finance_name": "💼 Finance App",
        "site_finance_desc": "Strumento avanzato per la gestione del budget e analisi delle spese. Monitora dove vanno i tuoi soldi e ottimizza il risparmio mensile.",
        
        "site_overview_name": "📊 Overview Asset",
        "site_overview_desc": "Analizza e confronta diverse classi di asset (azioni, obbligazioni, oro, immobili). Comprendi rischi e rendimenti storici per scelte informate.",
        
        "site_portfolio_name": "💎 Portfolio Manager",
        "site_portfolio_desc": "Costruisci e monitora il tuo portafoglio di investimenti. Simula diverse allocazioni e traccia le performance nel tempo.",
        
        # Literature recommendations
        "recommended_books": "📚 Libri Consigliati",
        "books_italian": "**In Italiano:**",
        "books_english": "**In Inglese:**",
        "books_german": "**In Tedesco:**",
    },
    
    "en": {
        # Header and navigation
        "app_title": "💰 Financial Guide for Beginners",
        "welcome": "Welcome to your personal financial guide!",
        "language": "🌍 Language / Lingua / Sprache",
        "version_info": "Version",
        
        # Simplified intro
        "intro_text": """Before starting with your data, it's essential to understand the 
**three-phase prioritization philosophy** that will guide your financial choices.""",
        
        # Phase descriptions
        "phases_title": "📚 The Three-Phase Philosophy",
        "phases_intro": """This guide follows a structured and progressive approach to building 
a solid financial foundation. Each phase has a specific priority and must be completed 
before moving to the next.""",
        
        "phase1_title": "🛡️ PHASE 1: Emergency Fund (Absolute Priority)",
        "phase1_desc": """**Goal**: Create a safety cushion to protect you and your family from unexpected events.

**The Rule**: You must have liquidity equal to **6 months of expenses**.

**Why is it fundamental?**
- Protects against sudden job loss
- Covers unexpected urgent medical expenses
- Avoids having to sell investments at a loss during a personal crisis
- Allows you to sleep peacefully

**Where to keep this money?**
- Easily accessible checking or savings account
- DO NOT invest in stocks or risky instruments
- Must be **immediately available** in case of emergency

**Philosophy**: Without this foundation, any unexpected event can destroy your financial plans.""",
        
        "phase2_title": "🎯 PHASE 2: Predictable Expenses (Medium-Long Term Goals)",
        "phase2_desc": """**Goal**: Plan and set aside monthly for certain or highly probable future expenses.

**Examples of goals**:
- Down payment for house purchase (in 3-5 years)
- Wedding or important events (in 2-4 years)
- Master's degree or specialized training
- Home renovation
- Major trip (e.g., sabbatical year)

**Key concept: PAC (Monthly Accumulation Plan)**

For each future goal, calculate how much you need to save each month:
```
Monthly PAC = Total Cost / Available Months
```

**Practical example**:
- Goal: €30,000 house down payment in 5 years
- Monthly PAC = €30,000 / 60 months = **€500/month**

**Where to allocate this money?**
- Savings accounts or short-term bonds for goals <5 years
- Conservative bond ETFs for 5-10 year goals
- DO NOT invest in stocks if goal is within 3-5 years (too volatile)

**Philosophy**: Separate what is "predictable" from what is "long-term investable".""",
        
        "phase3_title": "📈 PHASE 3: Long-Term Investments (Wealth Growth)",
        "phase3_desc": """**Goal**: Grow your wealth for retirement and the long term (>10 years).

**Who can invest here?**
Only those who have COMPLETED Phases 1 and 2!

**What can you invest?**
After covering:
1. ✅ Emergency Fund (6 months of expenses)
2. ✅ Monthly PACs for future goals

You have **surplus capital** and **free monthly savings**.

**How to allocate investments?**

Allocation depends on:
- **Risk profile**: Conservative, Moderate, Aggressive
- **Time horizon**: Years to retirement

**Main asset classes**:
1. **Stocks (Global equity ETFs)**:
   - Portfolio growth engine
   - High volatility but maximum return potential
   - Ideal for horizons >15 years

2. **Bonds (Bond ETFs)**:
   - Stability and steady income
   - Low volatility
   - Protection during stock crises

3. **Gold (Physical gold ETCs)**:
   - Inflation protection
   - Decorrelation with stocks and bonds
   - 5-10% of portfolio

**Example allocations**:
- **Conservative** (low risk): 30% Stocks, 60% Bonds, 10% Gold
- **Moderate** (balanced): 50% Stocks, 40% Bonds, 10% Gold
- **Aggressive** (high growth): 70% Stocks, 20% Bonds, 10% Gold

**Philosophy**: Time is your best ally. Invest with discipline and never sell in panic during crises.""",
        
        "why_this_order": "❓ Why Is This Order Fundamental?",
        "why_this_order_desc": """1. **Without Emergency Fund** (Phase 1): An unexpected event forces you to sell investments at a loss or go into debt.

2. **Without Goal Planning** (Phase 2): You risk investing money you'll need soon, forcing you to divest at the wrong time.

3. **With Solid Foundation** (Phases 1 + 2 Completed): You can invest peacefully knowing emergencies and goals are covered.

**🎯 This approach allows you to invest WITHOUT STRESS, because you've already protected your present and predictable future.**""",
        
        # Input sections
        "input_data_title": "📝 Enter Your Financial Data",
        "input_data_intro": "Now that you understand the philosophy, enter your data to receive a personalized plan.",
        
        "basic_data": "💰 Financial Data",
        "monthly_income": "💵 Net Monthly Income (€)",
        "monthly_expenses": "💳 Total Monthly Expenses (€)",
        "current_capital": "🏦 Current Capital/Liquidity (€)",
        "invested_capital": "📊 Already Invested Capital (€)",
        "income_help": "Your net monthly salary or regular income",
        "expenses_help": "All your monthly expenses (rent, bills, food, etc.)",
        "capital_help": "Your current liquid savings (checking accounts, savings accounts)",
        "invested_help": "Money already invested in stocks, ETFs, funds, etc. (for info, doesn't affect calculations)",
        
        "demographic_data": "⏰ Time Horizon",
        "years_to_retirement": "Years to Retirement",
        "retirement_help": "How many years until your retirement? (determines horizon for PHASE 3)",
        
        "future_goals": "🎯 Future Goals (Medium-Long Term Expenses)",
        "goals_intro": "Add here your goals that require financial planning (PHASE 2).",
        "add_goal": "➕ Add New Goal",
        "goal_name": "Goal Name",
        "goal_name_placeholder": "e.g., House Down Payment",
        "estimated_cost": "Estimated Cost (€)",
        "years_to_goal": "Years to Goal",
        "add_goal_btn": "✅ Add Goal",
        "your_goals": "📋 Your Goals",
        "no_goals": "ℹ️ No goals added. If you don't have specific goals, more capital will go to investments (PHASE 3)!",
        "goal_added": "✅ Goal '{goal_name}' added!",
        "goal_name_required": "⚠️ Enter a name for the goal",
        
        "risk_profile": "📊 Risk Profile (for PHASE 3)",
        "risk_intro": "Your risk profile will determine long-term investment allocation.",
        "select_risk": "Select your risk profile:",
        "conservative": "Conservative",
        "moderate": "Moderate",
        "aggressive": "Aggressive",
        "risk_help": """- **Conservative**: You prefer stability and low risk (suitable if retirement <10 years)
- **Moderate**: Balanced between growth and safety
- **Aggressive**: Maximize growth accepting volatility (suitable if retirement >20 years)""",
        "conservative_desc": "🛡️ Protect capital with stable investments",
        "moderate_desc": "⚖️ Balance growth and safety",
        "aggressive_desc": "🚀 Maximize growth potential",
        
        "generate_report": "🚀 Generate My Personalized Financial Plan",
        "personalized_guide": "📊 Your Personalized Financial Plan",
        "report_success": "✅ Plan generated successfully!",
        
        # Common terms
        "cost": "Cost",
        "time": "Time",
        "years": "years",
        "monthly_pac": "Monthly PAC",
        "months": "months",
        
        # Educational resources
        "educational_sites": "🎓 Recommended Educational Sites",
        "educational_sites_intro": "To deepen your financial education, we recommend these free tools:",
        
        "site_onepage_name": "📄 One Page Financial",
        "site_onepage_desc": "Visualize your complete financial plan on a single page. Perfect for an immediate overview of emergencies, goals, and investments.",
        
        "site_immobiliare_name": "🏠 Real Estate Calculator",
        "site_immobiliare_desc": "Plan your home purchase: calculate mortgages, required down payments, and compare rent vs buy. Essential for one of your most important goals.",
        
        "site_finance_name": "💼 Finance App",
        "site_finance_desc": "Advanced tool for budget management and expense analysis. Track where your money goes and optimize monthly savings.",
        
        "site_overview_name": "📊 Overview Asset",
        "site_overview_desc": "Analyze and compare different asset classes (stocks, bonds, gold, real estate). Understand historical risks and returns for informed choices.",
        
        "site_portfolio_name": "💎 Portfolio Manager",
        "site_portfolio_desc": "Build and monitor your investment portfolio. Simulate different allocations and track performance over time.",
        
        # Literature recommendations
        "recommended_books": "📚 Recommended Books",
        "books_italian": "**In Italian:**",
        "books_english": "**In English:**",
        "books_german": "**In German:**",
    },
    
    "de": {
        # Header und Navigation
        "app_title": "💰 Finanzleitfaden für Anfänger",
        "welcome": "Willkommen zu Ihrem persönlichen Finanzleitfaden!",
        "language": "🌍 Sprache / Language / Lingua",
        "version_info": "Version",
        
        # Vereinfachte Einleitung
        "intro_text": """Bevor Sie mit Ihren Daten beginnen, ist es wichtig, die 
**dreiphasige Priorisierungsphilosophie** zu verstehen, die Ihre finanziellen Entscheidungen leiten wird.""",
        
        # Phasenbeschreibungen
        "phases_title": "📚 Die Drei-Phasen-Philosophie",
        "phases_intro": """Dieser Leitfaden folgt einem strukturierten und progressiven Ansatz zum Aufbau 
einer soliden finanziellen Grundlage. Jede Phase hat eine spezifische Priorität und muss abgeschlossen 
werden, bevor Sie zur nächsten übergehen.""",
        
        "phase1_title": "🛡️ PHASE 1: Notgroschen (Absolute Priorität)",
        "phase1_desc": """**Ziel**: Schaffen Sie ein Sicherheitspolster, um Sie und Ihre Familie vor unerwarteten Ereignissen zu schützen.

**Die Regel**: Sie müssen Liquidität in Höhe von **6 Monatsausgaben** haben.

**Warum ist das grundlegend?**
- Schützt vor plötzlichem Jobverlust
- Deckt unerwartete dringende medizinische Ausgaben
- Vermeidet den Verkauf von Investitionen mit Verlust während einer persönlichen Krise
- Ermöglicht Ihnen, ruhig zu schlafen

**Wo dieses Geld aufbewahren?**
- Leicht zugängliches Giro- oder Sparkonto
- NICHT in Aktien oder riskante Instrumente investieren
- Muss **sofort verfügbar** sein im Notfall

**Philosophie**: Ohne diese Grundlage kann jedes unerwartete Ereignis Ihre Finanzpläne zerstören.""",
        
        "phase2_title": "🎯 PHASE 2: Vorhersehbare Ausgaben (Mittel-Langfristige Ziele)",
        "phase2_desc": """**Ziel**: Planen und monatlich für sichere oder sehr wahrscheinliche zukünftige Ausgaben zurücklegen.

**Beispiele für Ziele**:
- Anzahlung für Hauskauf (in 3-5 Jahren)
- Hochzeit oder wichtige Ereignisse (in 2-4 Jahren)
- Master-Abschluss oder spezialisierte Ausbildung
- Hausrenovierung
- Große Reise (z.B. Sabbatjahr)

**Schlüsselkonzept: PAC (Monatlicher Ansparplan)**

Für jedes zukünftige Ziel berechnen Sie, wie viel Sie monatlich sparen müssen:
```
Monatlicher PAC = Gesamtkosten / Verfügbare Monate
```

**Praktisches Beispiel**:
- Ziel: €30.000 Hausanzahlung in 5 Jahren
- Monatlicher PAC = €30.000 / 60 Monate = **€500/Monat**

**Wo dieses Geld allokieren?**
- Sparkonten oder kurzfristige Anleihen für Ziele <5 Jahre
- Konservative Anleihen-ETFs für 5-10 Jahre Ziele
- NICHT in Aktien investieren, wenn Ziel innerhalb 3-5 Jahren (zu volatil)

**Philosophie**: Trennen Sie das "Vorhersehbare" vom "Langfristig Investierbaren".""",
        
        "phase3_title": "📈 PHASE 3: Langfristige Investitionen (Vermögenswachstum)",
        "phase3_desc": """**Ziel**: Ihr Vermögen für die Rente und langfristig (>10 Jahre) wachsen lassen.

**Wer kann hier investieren?**
Nur diejenigen, die Phasen 1 und 2 ABGESCHLOSSEN haben!

**Was können Sie investieren?**
Nach Deckung von:
1. ✅ Notgroschen (6 Monatsausgaben)
2. ✅ Monatliche PACs für zukünftige Ziele

Haben Sie **überschüssiges Kapital** und **freie monatliche Ersparnisse**.

**Wie Investitionen allokieren?**

Allokation hängt ab von:
- **Risikoprofil**: Konservativ, Moderat, Aggressiv
- **Zeithorizont**: Jahre bis zur Rente

**Hauptanlageklassen**:
1. **Aktien (Globale Aktien-ETFs)**:
   - Portfolio-Wachstumsmotor
   - Hohe Volatilität aber maximales Renditepotenzial
   - Ideal für Horizonte >15 Jahre

2. **Anleihen (Anleihen-ETFs)**:
   - Stabilität und stetiges Einkommen
   - Niedrige Volatilität
   - Schutz während Aktienkrisen

3. **Gold (Physische Gold-ETCs)**:
   - Inflationsschutz
   - Dekorrelation mit Aktien und Anleihen
   - 5-10% des Portfolios

**Beispiel-Allokationen**:
- **Konservativ** (geringes Risiko): 30% Aktien, 60% Anleihen, 10% Gold
- **Moderat** (ausgewogen): 50% Aktien, 40% Anleihen, 10% Gold
- **Aggressiv** (hohes Wachstum): 70% Aktien, 20% Anleihen, 10% Gold

**Philosophie**: Zeit ist Ihr bester Verbündeter. Investieren Sie diszipliniert und verkaufen Sie niemals in Panik während Krisen.""",
        
        "why_this_order": "❓ Warum Ist Diese Reihenfolge Grundlegend?",
        "why_this_order_desc": """1. **Ohne Notgroschen** (Phase 1): Ein unerwartetes Ereignis zwingt Sie, Investitionen mit Verlust zu verkaufen oder sich zu verschulden.

2. **Ohne Zielplanung** (Phase 2): Sie riskieren, Geld zu investieren, das Sie bald brauchen, was Sie zwingt, zum falschen Zeitpunkt zu desinvestieren.

3. **Mit Solider Grundlage** (Phasen 1 + 2 Abgeschlossen): Sie können friedlich investieren, wissend, dass Notfälle und Ziele abgedeckt sind.

**🎯 Dieser Ansatz ermöglicht es Ihnen, OHNE STRESS zu investieren, weil Sie Ihre Gegenwart und vorhersehbare Zukunft bereits geschützt haben.**""",
        
        # Eingabeabschnitte
        "input_data_title": "📝 Geben Sie Ihre Finanzdaten Ein",
        "input_data_intro": "Jetzt, da Sie die Philosophie verstehen, geben Sie Ihre Daten ein, um einen personalisierten Plan zu erhalten.",
        
        "basic_data": "💰 Finanzdaten",
        "monthly_income": "💵 Netto-Monatseinkommen (€)",
        "monthly_expenses": "💳 Monatliche Gesamtausgaben (€)",
        "current_capital": "🏦 Aktuelles Kapital/Liquidität (€)",
        "invested_capital": "📊 Bereits Investiertes Kapital (€)",
        "income_help": "Ihr monatliches Nettogehalt oder regelmäßiges Einkommen",
        "expenses_help": "Alle Ihre monatlichen Ausgaben (Miete, Rechnungen, Essen, etc.)",
        "capital_help": "Ihre aktuellen liquiden Ersparnisse (Girokonten, Sparkonten)",
        "invested_help": "Bereits in Aktien, ETFs, Fonds, etc. investiertes Geld (zur Info, beeinflusst Berechnungen nicht)",
        
        "demographic_data": "⏰ Zeithorizont",
        "years_to_retirement": "Jahre bis zur Rente",
        "retirement_help": "Wie viele Jahre bis zu Ihrer Rente? (bestimmt Horizont für PHASE 3)",
        
        "future_goals": "🎯 Zukünftige Ziele (Mittel-Langfristige Ausgaben)",
        "goals_intro": "Fügen Sie hier Ihre Ziele hinzu, die finanzielle Planung erfordern (PHASE 2).",
        "add_goal": "➕ Neues Ziel hinzufügen",
        "goal_name": "Zielname",
        "goal_name_placeholder": "z.B. Hausanzahlung",
        "estimated_cost": "Geschätzte Kosten (€)",
        "years_to_goal": "Jahre bis zum Ziel",
        "add_goal_btn": "✅ Ziel hinzufügen",
        "your_goals": "📋 Ihre Ziele",
        "no_goals": "ℹ️ Keine Ziele hinzugefügt. Wenn Sie keine spezifischen Ziele haben, geht mehr Kapital in Investitionen (PHASE 3)!",
        "goal_added": "✅ Ziel '{goal_name}' hinzugefügt!",
        "goal_name_required": "⚠️ Geben Sie einen Namen für das Ziel ein",
        
        "risk_profile": "📊 Risikoprofil (für PHASE 3)",
        "risk_intro": "Ihr Risikoprofil bestimmt die langfristige Investitionsallokation.",
        "select_risk": "Wählen Sie Ihr Risikoprofil:",
        "conservative": "Konservativ",
        "moderate": "Moderat",
        "aggressive": "Aggressiv",
        "risk_help": """- **Konservativ**: Sie bevorzugen Stabilität und geringes Risiko (geeignet wenn Rente <10 Jahre)
- **Moderat**: Ausgewogen zwischen Wachstum und Sicherheit
- **Aggressiv**: Maximieren Sie Wachstum bei akzeptierter Volatilität (geeignet wenn Rente >20 Jahre)""",
        "conservative_desc": "🛡️ Kapital mit stabilen Investitionen schützen",
        "moderate_desc": "⚖️ Wachstum und Sicherheit ausbalancieren",
        "aggressive_desc": "🚀 Wachstumspotenzial maximieren",
        
        "generate_report": "🚀 Erstellen Sie Meinen Personalisierten Finanzplan",
        "personalized_guide": "📊 Ihr Personalisierter Finanzplan",
        "report_success": "✅ Plan erfolgreich erstellt!",
        
        # Allgemeine Begriffe
        "cost": "Kosten",
        "time": "Zeit",
        "years": "Jahre",
        "monthly_pac": "Monatlicher PAC",
        "months": "Monate",
        
        # Bildungsressourcen
        "educational_sites": "🎓 Empfohlene Bildungsseiten",
        "educational_sites_intro": "Um Ihre Finanzbildung zu vertiefen, empfehlen wir diese kostenlosen Tools:",
        
        "site_onepage_name": "📄 One Page Financial",
        "site_onepage_desc": "Visualisieren Sie Ihren kompletten Finanzplan auf einer einzigen Seite. Perfekt für einen sofortigen Überblick über Notfälle, Ziele und Investitionen.",
        
        "site_immobiliare_name": "🏠 Immobilienrechner",
        "site_immobiliare_desc": "Planen Sie Ihren Hauskauf: Berechnen Sie Hypotheken, erforderliche Anzahlungen und vergleichen Sie Miete vs. Kauf. Essentiell für eines Ihrer wichtigsten Ziele.",
        
        "site_finance_name": "💼 Finance App",
        "site_finance_desc": "Fortgeschrittenes Tool für Budgetverwaltung und Ausgabenanalyse. Verfolgen Sie, wohin Ihr Geld fließt und optimieren Sie monatliche Ersparnisse.",
        
        "site_overview_name": "📊 Overview Asset",
        "site_overview_desc": "Analysieren und vergleichen Sie verschiedene Anlageklassen (Aktien, Anleihen, Gold, Immobilien). Verstehen Sie historische Risiken und Renditen für fundierte Entscheidungen.",
        
        "site_portfolio_name": "💎 Portfolio Manager",
        "site_portfolio_desc": "Bauen und überwachen Sie Ihr Anlageportfolio. Simulieren Sie verschiedene Allokationen und verfolgen Sie die Performance im Zeitverlauf.",
        
        # Literaturempfehlungen
        "recommended_books": "📚 Empfohlene Bücher",
        "books_italian": "**Auf Italienisch:**",
        "books_english": "**Auf Englisch:**",
        "books_german": "**Auf Deutsch:**",
    }
}

def t(key, lang="it", **kwargs):
    """
    Funzione di traduzione.
    
    Args:
        key (str): Chiave di traduzione
        lang (str): Codice lingua (it, en, de)
        **kwargs: Parametri per formattazione
        
    Returns:
        str: Testo tradotto
    """
    text = TRANSLATIONS.get(lang, TRANSLATIONS["it"]).get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text
