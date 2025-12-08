"""
Guida Finanziaria per Neofiti - Streamlit App v2.0
App educativa per la pianificazione finanziaria a tre fasi
Con supporto multilingue e gestione avanzata del capitale
"""

import streamlit as st

# ============================================================================
# SEZIONE 0: TRADUZIONI E CONFIGURAZIONE MULTILINGUE
# ============================================================================

TRANSLATIONS = {
    "it": {
        "app_title": "💰 Guida Finanziaria per Neofiti",
        "welcome": "Benvenuto nella tua guida finanziaria personale!",
        "intro_text": """Questa app ti aiuterà a pianificare le tue finanze seguendo una filosofia 
di prioritizzazione a **tre fasi**:

1. **🛡️ FASE 1**: Costruisci il tuo Fondo di Emergenza
2. **🎯 FASE 2**: Pianifica le Spese Prevedibili (obiettivi a lungo termine)
3. **📈 FASE 3**: Investi per il Futuro""",
        "basic_data": "📊 Dati Finanziari di Base",
        "monthly_income": "💵 Entrate Mensili Nette (€)",
        "monthly_expenses": "💳 Uscite Mensili Totali (€)",
        "current_capital": "🏦 Capitale Attuale/Liquidità (€)",
        "income_help": "Il tuo stipendio netto mensile o entrate regolari",
        "expenses_help": "Tutte le tue spese mensili (affitto, bollette, cibo, ecc.)",
        "capital_help": "I tuoi risparmi attuali disponibili",
        "demographic_data": "👤 Dati Demografici e Obiettivi di Vita",
        "years_to_retirement": "⏰ Anni alla Pensione",
        "retirement_help": "Quanti anni mancano alla tua pensione?",
        "age_group": "🎂 Fascia di Età",
        "future_goals": "🎯 Spese Future Prevedibili (Obiettivi)",
        "goals_intro": "Aggiungi qui i tuoi obiettivi di lungo termine che richiedono una pianificazione (es. acconto casa, matrimonio, master universitario, ecc.).",
        "add_goal": "➕ Aggiungi Nuovo Obiettivo",
        "goal_name": "Nome Obiettivo",
        "goal_name_placeholder": "es. Acconto Casa",
        "estimated_cost": "Costo Stimato (€)",
        "years_to_goal": "Anni all'Obiettivo",
        "add_goal_btn": "✅ Aggiungi Obiettivo",
        "your_goals": "📋 I Tuoi Obiettivi",
        "no_goals": "ℹ️ Nessun obiettivo aggiunto. Aggiungi il tuo primo obiettivo sopra!",
        "goal_added": "✅ Obiettivo '{goal_name}' aggiunto!",
        "goal_name_required": "⚠️ Inserisci un nome per l'obiettivo",
        "risk_profile": "📊 Profilo di Rischio per Investimenti",
        "risk_intro": "Il tuo profilo di rischio determinerà come allocare i tuoi investimenti a lungo termine.",
        "select_risk": "Seleziona il tuo profilo di rischio:",
        "conservative": "Conservatore",
        "moderate": "Moderato",
        "aggressive": "Aggressivo",
        "risk_help": """- **Conservatore**: Preferisci stabilità e basso rischio
- **Moderato**: Bilanciato tra crescita e sicurezza
- **Aggressivo**: Massimizzi la crescita accettando volatilità""",
        "conservative_desc": "🛡️ Proteggi il capitale con investimenti stabili",
        "moderate_desc": "⚖️ Bilancia crescita e sicurezza",
        "aggressive_desc": "🚀 Massimizza il potenziale di crescita",
        "generate_report": "🚀 Genera la Tua Guida Finanziaria Personalizzata",
        "personalized_guide": "📊 La Tua Guida Finanziaria Personalizzata",
        "report_success": "✅ Report generato con successo!",
        "cost": "Costo",
        "time": "Tempo",
        "years": "anni",
        "monthly_pac": "PAC mensile",
        "language": "🌍 Lingua / Language / Sprache"
    },
    "en": {
        "app_title": "💰 Financial Guide for Beginners",
        "welcome": "Welcome to your personal financial guide!",
        "intro_text": """This app will help you plan your finances following a 
**three-phase** prioritization philosophy:

1. **🛡️ PHASE 1**: Build your Emergency Fund
2. **🎯 PHASE 2**: Plan Predictable Expenses (long-term goals)
3. **📈 PHASE 3**: Invest for the Future""",
        "basic_data": "📊 Basic Financial Data",
        "monthly_income": "💵 Net Monthly Income (€)",
        "monthly_expenses": "💳 Total Monthly Expenses (€)",
        "current_capital": "🏦 Current Capital/Liquidity (€)",
        "income_help": "Your net monthly salary or regular income",
        "expenses_help": "All your monthly expenses (rent, bills, food, etc.)",
        "capital_help": "Your current available savings",
        "demographic_data": "👤 Demographic Data and Life Goals",
        "years_to_retirement": "⏰ Years to Retirement",
        "retirement_help": "How many years until your retirement?",
        "age_group": "🎂 Age Group",
        "future_goals": "🎯 Predictable Future Expenses (Goals)",
        "goals_intro": "Add your long-term goals that require planning here (e.g., house down payment, wedding, master's degree, etc.).",
        "add_goal": "➕ Add New Goal",
        "goal_name": "Goal Name",
        "goal_name_placeholder": "e.g., House Down Payment",
        "estimated_cost": "Estimated Cost (€)",
        "years_to_goal": "Years to Goal",
        "add_goal_btn": "✅ Add Goal",
        "your_goals": "📋 Your Goals",
        "no_goals": "ℹ️ No goals added. Add your first goal above!",
        "goal_added": "✅ Goal '{goal_name}' added!",
        "goal_name_required": "⚠️ Enter a name for the goal",
        "risk_profile": "📊 Investment Risk Profile",
        "risk_intro": "Your risk profile will determine how to allocate your long-term investments.",
        "select_risk": "Select your risk profile:",
        "conservative": "Conservative",
        "moderate": "Moderate",
        "aggressive": "Aggressive",
        "risk_help": """- **Conservative**: You prefer stability and low risk
- **Moderate**: Balanced between growth and safety
- **Aggressive**: Maximize growth accepting volatility""",
        "conservative_desc": "🛡️ Protect capital with stable investments",
        "moderate_desc": "⚖️ Balance growth and safety",
        "aggressive_desc": "🚀 Maximize growth potential",
        "generate_report": "🚀 Generate Your Personalized Financial Guide",
        "personalized_guide": "📊 Your Personalized Financial Guide",
        "report_success": "✅ Report generated successfully!",
        "cost": "Cost",
        "time": "Time",
        "years": "years",
        "monthly_pac": "Monthly PAC",
        "language": "🌍 Language / Lingua / Sprache"
    },
    "de": {
        "app_title": "💰 Finanzleitfaden für Anfänger",
        "welcome": "Willkommen zu Ihrem persönlichen Finanzleitfaden!",
        "intro_text": """Diese App hilft Ihnen bei der Finanzplanung nach einer 
**dreiphasigen** Priorisierungsphilosophie:

1. **🛡️ PHASE 1**: Bauen Sie Ihren Notgroschen auf
2. **🎯 PHASE 2**: Planen Sie vorhersehbare Ausgaben (langfristige Ziele)
3. **📈 PHASE 3**: Investieren Sie für die Zukunft""",
        "basic_data": "📊 Finanzielle Basisdaten",
        "monthly_income": "💵 Netto-Monatseinkommen (€)",
        "monthly_expenses": "💳 Monatliche Gesamtausgaben (€)",
        "current_capital": "🏦 Aktuelles Kapital/Liquidität (€)",
        "income_help": "Ihr monatliches Nettogehalt oder regelmäßiges Einkommen",
        "expenses_help": "Alle Ihre monatlichen Ausgaben (Miete, Rechnungen, Essen, etc.)",
        "capital_help": "Ihre aktuell verfügbaren Ersparnisse",
        "demographic_data": "👤 Demografische Daten und Lebensziele",
        "years_to_retirement": "⏰ Jahre bis zur Rente",
        "retirement_help": "Wie viele Jahre bis zu Ihrer Rente?",
        "age_group": "🎂 Altersgruppe",
        "future_goals": "🎯 Vorhersehbare zukünftige Ausgaben (Ziele)",
        "goals_intro": "Fügen Sie hier Ihre langfristigen Ziele hinzu, die Planung erfordern (z.B. Anzahlung für ein Haus, Hochzeit, Master-Studium, etc.).",
        "add_goal": "➕ Neues Ziel hinzufügen",
        "goal_name": "Zielname",
        "goal_name_placeholder": "z.B. Hausanzahlung",
        "estimated_cost": "Geschätzte Kosten (€)",
        "years_to_goal": "Jahre bis zum Ziel",
        "add_goal_btn": "✅ Ziel hinzufügen",
        "your_goals": "📋 Ihre Ziele",
        "no_goals": "ℹ️ Keine Ziele hinzugefügt. Fügen Sie oben Ihr erstes Ziel hinzu!",
        "goal_added": "✅ Ziel '{goal_name}' hinzugefügt!",
        "goal_name_required": "⚠️ Geben Sie einen Namen für das Ziel ein",
        "risk_profile": "📊 Anlagerisikoprofil",
        "risk_intro": "Ihr Risikoprofil bestimmt, wie Ihre langfristigen Investitionen zugeordnet werden.",
        "select_risk": "Wählen Sie Ihr Risikoprofil:",
        "conservative": "Konservativ",
        "moderate": "Moderat",
        "aggressive": "Aggressiv",
        "risk_help": """- **Konservativ**: Sie bevorzugen Stabilität und geringes Risiko
- **Moderat**: Ausgewogen zwischen Wachstum und Sicherheit
- **Aggressiv**: Maximieren Sie das Wachstum bei akzeptierter Volatilität""",
        "conservative_desc": "🛡️ Kapital mit stabilen Investitionen schützen",
        "moderate_desc": "⚖️ Wachstum und Sicherheit ausbalancieren",
        "aggressive_desc": "🚀 Wachstumspotenzial maximieren",
        "generate_report": "🚀 Erstellen Sie Ihren persönlichen Finanzleitfaden",
        "personalized_guide": "📊 Ihr personalisierter Finanzleitfaden",
        "report_success": "✅ Bericht erfolgreich erstellt!",
        "cost": "Kosten",
        "time": "Zeit",
        "years": "Jahre",
        "monthly_pac": "Monatlicher PAC",
        "language": "🌍 Sprache / Language / Lingua"
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


# ============================================================================
# SEZIONE 1: FUNZIONI DI CALCOLO (LOGICA PURA)
# ============================================================================

def calcola_fondo_emergenza(uscite_mensili):
    """
    Calcola il fondo di emergenza target (6 mesi di spese).
    
    Args:
        uscite_mensili (float): Uscite mensili totali
        
    Returns:
        float: Importo target del fondo di emergenza
    """
    return uscite_mensili * 6


def verifica_fondo_emergenza(capitale_attuale, fondo_emergenza_target):
    """
    Verifica se il fondo di emergenza è completo.
    
    Args:
        capitale_attuale (float): Liquidità disponibile
        fondo_emergenza_target (float): Target del fondo di emergenza
        
    Returns:
        tuple: (bool: è completo, float: importo mancante o eccedente)
    """
    differenza = capitale_attuale - fondo_emergenza_target
    return differenza >= 0, differenza


def calcola_mesi_rientro_emergenza(deficit, risparmio_mensile):
    """
    Calcola i mesi necessari per saturare il fondo di emergenza.
    
    Args:
        deficit (float): Importo mancante al fondo emergenza
        risparmio_mensile (float): Risparmio mensile disponibile
        
    Returns:
        int: Numero di mesi necessari (arrotondato per eccesso)
    """
    if risparmio_mensile <= 0:
        return float('inf')  # Impossibile completare
    
    import math
    return math.ceil(abs(deficit) / risparmio_mensile)


def calcola_pac_mensile(costo_obiettivo, anni_obiettivo):
    """
    Calcola il Piano di Accumulo Mensile per un obiettivo.
    
    Args:
        costo_obiettivo (float): Costo totale dell'obiettivo
        anni_obiettivo (int): Anni disponibili per raggiungere l'obiettivo
        
    Returns:
        float: Importo mensile da accantonare
    """
    if anni_obiettivo <= 0:
        return 0
    mesi = anni_obiettivo * 12
    return costo_obiettivo / mesi


def calcola_pac_totale(obiettivi):
    """
    Calcola il PAC mensile totale per tutti gli obiettivi.
    
    Args:
        obiettivi (list): Lista di dizionari con obiettivi
        
    Returns:
        float: PAC mensile totale
    """
    pac_totale = 0
    for obiettivo in obiettivi:
        pac_mensile = calcola_pac_mensile(
            obiettivo['costo'], 
            obiettivo['anni']
        )
        pac_totale += pac_mensile
    return pac_totale


def alloca_capitale_eccedente(capitale_eccedente, gap_obiettivi_mensile, anni_media_obiettivi):
    """
    Alloca il capitale eccedente secondo priorità:
    1. Copertura gap obiettivi (se presente)
    2. Investimento immediato
    
    Args:
        capitale_eccedente (float): Capitale oltre il fondo emergenza
        gap_obiettivi_mensile (float): Deficit mensile per obiettivi (se negativo)
        anni_media_obiettivi (float): Media anni agli obiettivi
        
    Returns:
        dict: {
            'a_obiettivi': importo da destinare agli obiettivi,
            'a_investimenti': importo da investire subito
        }
    """
    allocazione = {
        'a_obiettivi': 0,
        'a_investimenti': 0
    }
    
    # Se non c'è gap, tutto va agli investimenti
    if gap_obiettivi_mensile >= 0:
        allocazione['a_investimenti'] = capitale_eccedente
        return allocazione
    
    # Calcola quanto serve per coprire il gap fino alla scadenza media
    gap_totale_necessario = abs(gap_obiettivi_mensile) * 12 * anni_media_obiettivi
    
    # Alloca prioritariamente al gap
    if capitale_eccedente >= gap_totale_necessario:
        allocazione['a_obiettivi'] = gap_totale_necessario
        allocazione['a_investimenti'] = capitale_eccedente - gap_totale_necessario
    else:
        # Tutto il capitale va al gap (parziale)
        allocazione['a_obiettivi'] = capitale_eccedente
        allocazione['a_investimenti'] = 0
    
    return allocazione


def calcola_disponibilita_investimenti(entrate_mensili, uscite_mensili, pac_totale):
    """
    Calcola l'importo disponibile per investimenti a lungo termine.
    
    Args:
        entrate_mensili (float): Entrate mensili nette
        uscite_mensili (float): Uscite mensili totali
        pac_totale (float): PAC mensile totale
        
    Returns:
        float: Importo mensile disponibile per investimenti
    """
    return entrate_mensili - uscite_mensili - pac_totale


def genera_allocazione_investimenti(profilo_rischio, anni_pensione):
    """
    Genera un'allocazione di portafoglio basata sul profilo di rischio e orizzonte temporale.
    
    Args:
        profilo_rischio (str): "Conservatore", "Moderato", o "Aggressivo"
        anni_pensione (int): Anni alla pensione
        
    Returns:
        dict: Allocazione percentuale per classe di attivo
    """
    # Traduci profili in inglese se necessario
    profile_map = {
        "Conservatore": "Conservative",
        "Conservative": "Conservative",
        "Konservativ": "Conservative",
        "Moderato": "Moderate",
        "Moderate": "Moderate",
        "Moderat": "Moderate",
        "Aggressivo": "Aggressive",
        "Aggressive": "Aggressive",
        "Aggressiv": "Aggressive"
    }
    
    profilo_norm = profile_map.get(profilo_rischio, "Moderate")
    
    # Allocazioni base per profilo
    allocazioni_base = {
        "Conservative": {"Azioni": 30, "Obbligazioni": 60, "Oro": 10},
        "Moderate": {"Azioni": 50, "Obbligazioni": 40, "Oro": 10},
        "Aggressive": {"Azioni": 70, "Obbligazioni": 20, "Oro": 10}
    }
    
    allocazione = allocazioni_base.get(profilo_norm, allocazioni_base["Moderate"]).copy()
    
    # Aggiustamento per orizzonte temporale lungo (>20 anni)
    if anni_pensione > 20:
        bonus_azioni = 10
        allocazione["Azioni"] += bonus_azioni
        allocazione["Obbligazioni"] -= bonus_azioni
    
    # Aggiustamento per orizzonte temporale corto (<10 anni)
    elif anni_pensione < 10:
        riduzione_azioni = 10
        allocazione["Azioni"] = max(20, allocazione["Azioni"] - riduzione_azioni)
        allocazione["Obbligazioni"] += riduzione_azioni
    
    return allocazione


def formatta_valuta(importo):
    """
    Formatta un importo in euro.
    
    Args:
        importo (float): Importo da formattare
        
    Returns:
        str: Importo formattato
    """
    return f"€{importo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ============================================================================
# SEZIONE 2: INTERFACCIA UTENTE STREAMLIT
# ============================================================================

def setup_page():
    """Configura la pagina Streamlit."""
    st.set_page_config(
        page_title="Guida Finanziaria per Neofiti",
        page_icon="💰",
        layout="wide"
    )


def render_language_selector():
    """
    Renderizza il selettore di lingua.
    
    Returns:
        str: Codice lingua selezionato
    """
    if 'language' not in st.session_state:
        st.session_state.language = 'it'
    
    lang_options = {
        'it': '🇮🇹 Italiano',
        'en': '🇬🇧 English',
        'de': '🇩🇪 Deutsch'
    }
    
    selected = st.selectbox(
        t("language", st.session_state.language),
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=list(lang_options.keys()).index(st.session_state.language),
        key='lang_selector'
    )
    
    if selected != st.session_state.language:
        st.session_state.language = selected
        st.rerun()
    
    return st.session_state.language


def render_header(lang):
    """Renderizza l'intestazione dell'app."""
    st.title(t("app_title", lang))
    st.markdown(f"""
    ### {t("welcome", lang)}
    
    {t("intro_text", lang)}
    
    ---
    """)


def render_dati_base(lang):
    """
    Renderizza la sezione input per i dati finanziari di base.
    
    Returns:
        dict: Dizionario con i dati inseriti
    """
    st.header(t("basic_data", lang))
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        entrate = st.number_input(
            t("monthly_income", lang),
            min_value=0.0,
            value=2000.0,
            step=100.0,
            help=t("income_help", lang)
        )
    
    with col2:
        uscite = st.number_input(
            t("monthly_expenses", lang),
            min_value=0.0,
            value=1500.0,
            step=100.0,
            help=t("expenses_help", lang)
        )
    
    with col3:
        capitale = st.number_input(
            t("current_capital", lang),
            min_value=0.0,
            value=5000.0,
            step=500.0,
            help=t("capital_help", lang)
        )
    
    return {
        "entrate": entrate,
        "uscite": uscite,
        "capitale": capitale
    }


def render_dati_demografici(lang):
    """
    Renderizza la sezione input per i dati demografici.
    
    Returns:
        dict: Dizionario con i dati inseriti
    """
    st.header(t("demographic_data", lang))
    
    col1, col2 = st.columns(2)
    
    with col1:
        anni_pensione = st.slider(
            t("years_to_retirement", lang),
            min_value=1,
            max_value=50,
            value=30,
            help=t("retirement_help", lang)
        )
    
    with col2:
        fascia_eta = st.selectbox(
            t("age_group", lang),
            options=["20-30", "30-40", "40-50", "50-60", "60+"],
            index=0
        )
    
    return {
        "anni_pensione": anni_pensione,
        "fascia_eta": fascia_eta
    }


def render_gestione_obiettivi(lang):
    """
    Renderizza la sezione per gestire obiettivi finanziari multipli.
    
    Returns:
        list: Lista di obiettivi
    """
    st.header(t("future_goals", lang))
    
    st.markdown(t("goals_intro", lang))
    
    # Inizializza session_state per gli obiettivi se non esiste
    if 'obiettivi' not in st.session_state:
        st.session_state.obiettivi = []
    
    # Form per aggiungere nuovo obiettivo
    with st.expander(t("add_goal", lang), expanded=len(st.session_state.obiettivi) == 0):
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            nome_obiettivo = st.text_input(
                t("goal_name", lang),
                placeholder=t("goal_name_placeholder", lang),
                key="input_nome"
            )
        
        with col2:
            costo_obiettivo = st.number_input(
                t("estimated_cost", lang),
                min_value=0.0,
                value=20000.0,
                step=1000.0,
                key="input_costo"
            )
        
        with col3:
            anni_obiettivo = st.number_input(
                t("years_to_goal", lang),
                min_value=1,
                max_value=30,
                value=5,
                key="input_anni"
            )
        
        if st.button(t("add_goal_btn", lang)):
            if nome_obiettivo:
                st.session_state.obiettivi.append({
                    "nome": nome_obiettivo,
                    "costo": costo_obiettivo,
                    "anni": anni_obiettivo
                })
                st.success(t("goal_added", lang, goal_name=nome_obiettivo))
                st.rerun()
            else:
                st.error(t("goal_name_required", lang))
    
    # Mostra obiettivi esistenti
    if st.session_state.obiettivi:
        st.subheader(t("your_goals", lang))
        for idx, obiettivo in enumerate(st.session_state.obiettivi):
            col1, col2 = st.columns([4, 1])
            with col1:
                pac_mensile = calcola_pac_mensile(obiettivo['costo'], obiettivo['anni'])
                st.info(f"""
                **{obiettivo['nome']}**  
                {t("cost", lang)}: {formatta_valuta(obiettivo['costo'])} | 
                {t("time", lang)}: {obiettivo['anni']} {t("years", lang)} | 
                {t("monthly_pac", lang)}: {formatta_valuta(pac_mensile)}
                """)
            with col2:
                if st.button("🗑️", key=f"del_{idx}", help="Delete"):
                    st.session_state.obiettivi.pop(idx)
                    st.rerun()
    else:
        st.info(t("no_goals", lang))
    
    return st.session_state.obiettivi


def render_profilo_rischio(lang):
    """
    Renderizza la sezione per il profilo di rischio.
    
    Returns:
        str: Profilo di rischio selezionato
    """
    st.header(t("risk_profile", lang))
    
    st.markdown(t("risk_intro", lang))
    
    options = [
        t("conservative", lang),
        t("moderate", lang),
        t("aggressive", lang)
    ]
    
    profilo = st.radio(
        t("select_risk", lang),
        options=options,
        index=1,
        help=t("risk_help", lang)
    )
    
    # Descrizioni dei profili
    descrizioni = {
        options[0]: t("conservative_desc", lang),
        options[1]: t("moderate_desc", lang),
        options[2]: t("aggressive_desc", lang)
    }
    
    st.info(descrizioni[profilo])
    
    return profilo


# ============================================================================
# SEZIONE 3: GENERAZIONE REPORT E LOGICA PRINCIPALE
# ============================================================================

def genera_report_fase1_it(capitale_attuale, fondo_emergenza, differenza, uscite_mensili, 
                           risparmio_mensile, mesi_rientro=None):
    """Genera il report FASE 1 in italiano."""
    report = f"""
## 🛡️ FASE 1: Fondo di Emergenza

### Priorità Assoluta!

Il **Fondo di Emergenza** è la base della tua sicurezza finanziaria. 
Ti protegge da imprevisti come perdita del lavoro, spese mediche o riparazioni urgenti.

**La regola**: Devi avere liquidità pari a **6 mesi di spese**.

### Il Tuo Fondo di Emergenza

- 💰 **Capitale Attuale**: {formatta_valuta(capitale_attuale)}
- 🎯 **Target Fondo Emergenza**: {formatta_valuta(fondo_emergenza)} (6 × {formatta_valuta(uscite_mensili)})
"""
    
    if differenza < 0:
        report += f"""
- ⚠️ **Situazione**: Il tuo fondo è **INCOMPLETO**
- 📉 **Importo Mancante**: {formatta_valuta(abs(differenza))}

### 🚨 PIANO DI RIENTRO AUTOMATICO

Prima di procedere con qualsiasi altro obiettivo finanziario, devi completare il tuo Fondo di Emergenza!

"""
        if mesi_rientro and mesi_rientro != float('inf'):
            report += f"""
**Piano di Accumulo:**
- 💵 **Risparmio Mensile Disponibile**: {formatta_valuta(risparmio_mensile)}
- ⏱️ **Tempo Necessario**: {mesi_rientro} mesi
- 📅 **Importo Mensile da Destinare**: {formatta_valuta(risparmio_mensile)} (100% del risparmio)

**Cosa fare:**
1. **Destina il 100% del tuo risparmio mensile** ({formatta_valuta(risparmio_mensile)}) al Fondo di Emergenza per i prossimi **{mesi_rientro} mesi**
2. **Mantieni questa liquidità** in un conto facilmente accessibile (conto deposito o conto corrente)
3. **Non investire** questi soldi in azioni o strumenti rischiosi
4. **Dopo {mesi_rientro} mesi**, il sistema sbloccherà automaticamente le fasi successive

**⛔ STOP: Non passare alle fasi successive finché non hai completato il tuo Fondo di Emergenza!**
"""
        else:
            report += """
⚠️ **ATTENZIONE**: Il tuo risparmio mensile è insufficiente o nullo. 

**Cosa fare:**
1. **Aumenta le tue entrate** (secondo lavoro, freelance, vendita di beni non essenziali)
2. **Riduci drasticamente le spese** per creare un margine di risparmio
3. **Rivedi il tuo budget** per trovare almeno 100-200€ al mese da destinare al fondo

**Non potrai procedere alle fasi successive senza un piano di rientro fattibile!**
"""
        
        report += """
---

### 💡 Consiglio per Neofiti

Il Fondo di Emergenza non è un "extra", è un **must**. Senza di esso, qualsiasi imprevisto 
potrebbe costringerti a indebitarti o vendere investimenti in perdita.
"""
    else:
        report += f"""
- ✅ **Situazione**: Il tuo fondo è **COMPLETO**!
- 💪 **Eccedenza**: {formatta_valuta(differenza)}

**Complimenti!** Hai una solida base di sicurezza finanziaria. 
Ora puoi procedere con le fasi successive.

**💡 Motto: "Investire Prima"**

La tua eccedenza di capitale verrà allocata secondo questa filosofia:
1. Prima priorità: Coprire eventuali gap negli obiettivi futuri
2. Seconda priorità: **Investire subito** il resto per farlo crescere

---
"""
    
    return report


def genera_report_fase2_it(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente=0):
    """Genera il report FASE 2 in italiano."""
    risparmio_disponibile = entrate_mensili - uscite_mensili
    
    report = f"""
## 🎯 FASE 2: Spese Prevedibili (PAC - Piano di Accumulo)

### Pianifica il Futuro

Ora che hai il tuo Fondo di Emergenza, è tempo di pianificare i tuoi obiettivi a lungo termine.

**Il concetto chiave**: Per ogni obiettivo futuro, calcola quanto devi risparmiare ogni mese 
(Piano di Accumulo Mensile o PAC).

### Il Tuo Risparmio Mensile

- 💵 **Entrate Mensili**: {formatta_valuta(entrate_mensili)}
- 💳 **Uscite Mensili**: {formatta_valuta(uscite_mensili)}
- 💰 **Risparmio Disponibile**: {formatta_valuta(risparmio_disponibile)}
"""
    
    if capitale_eccedente > 0:
        report += f"- 🎁 **Capitale Eccedente dal Fondo Emergenza**: {formatta_valuta(capitale_eccedente)}\n"
    
    report += "\n"
    
    if not obiettivi:
        report += """
### ℹ️ Nessun Obiettivo Definito

Non hai ancora definito obiettivi a lungo termine. Considera di aggiungere obiettivi come:
- Acconto per una casa
- Matrimonio o eventi importanti
- Master o corsi di formazione
- Viaggio importante

Una volta definiti, saprai esattamente quanto risparmiare ogni mese!

"""
        
        if capitale_eccedente > 0:
            report += f"""
### 💎 Allocazione Capitale Eccedente

Poiché non hai obiettivi definiti, il tuo capitale eccedente di **{formatta_valuta(capitale_eccedente)}** 
può essere destinato direttamente agli investimenti a lungo termine!

**Motto: "Investire Prima"** - Procedi alla FASE 3 per l'allocazione.
"""
        
        report += "---\n"
        return report, 0, risparmio_disponibile, capitale_eccedente
    
    report += "### 📋 I Tuoi Obiettivi e PAC Mensili\n\n"
    
    pac_totale = 0
    somma_anni = 0
    for obiettivo in obiettivi:
        pac_mensile = calcola_pac_mensile(obiettivo['costo'], obiettivo['anni'])
        pac_totale += pac_mensile
        somma_anni += obiettivo['anni']
        
        report += f"""
**{obiettivo['nome']}**
- Costo Totale: {formatta_valuta(obiettivo['costo'])}
- Tempo Disponibile: {obiettivo['anni']} anni ({obiettivo['anni'] * 12} mesi)
- PAC Mensile: **{formatta_valuta(pac_mensile)}**

"""
    
    anni_media = somma_anni / len(obiettivi) if obiettivi else 5
    
    report += f"""
---

### 💼 Totale PAC Mensile

**Devi accantonare ogni mese**: {formatta_valuta(pac_totale)}

"""
    
    # Verifica sostenibilità
    gap_mensile = risparmio_disponibile - pac_totale
    
    if gap_mensile < 0:
        # Deficit: PAC > Risparmio
        report += f"""
### ⚠️ GAP NEGATIVO

Il totale dei tuoi PAC mensili ({formatta_valuta(pac_totale)}) supera il tuo risparmio 
disponibile ({formatta_valuta(risparmio_disponibile)})!

**Deficit mensile**: {formatta_valuta(abs(gap_mensile))}

"""
        
        # Verifica se c'è capitale eccedente per coprire
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 COPERTURA CON CAPITALE ECCEDENTE

Hai {formatta_valuta(capitale_eccedente)} di capitale eccedente dal Fondo di Emergenza.

**Allocazione Intelligente:**
- **Accantonamento per Obiettivi**: {formatta_valuta(allocazione['a_obiettivi'])}
  - Questo importo coprirà il gap mensile di {formatta_valuta(abs(gap_mensile))} per circa {int(allocazione['a_obiettivi'] / abs(gap_mensile)) if gap_mensile != 0 else 0} mesi
- **Disponibile per Investimenti Immediati**: {formatta_valuta(allocazione['a_investimenti'])}

"""
            
            if allocazione['a_obiettivi'] >= abs(gap_mensile) * 12 * anni_media:
                report += "✅ **Il gap è completamente coperto!** Puoi procedere alla FASE 3.\n"
            else:
                report += f"""
⚠️ **Gap parzialmente coperto**. Dopo {int(allocazione['a_obiettivi'] / abs(gap_mensile))} mesi, dovrai:
1. Aumentare le entrate
2. Ridurre le spese
3. Rivedere gli obiettivi

Per ora puoi procedere alla FASE 3 con gli investimenti limitati.
"""
        else:
            report += """
**Cosa fare:**
1. **Riduci gli obiettivi** o allunga i tempi
2. **Aumenta le entrate** (secondo lavoro, freelance, ecc.)
3. **Riduci le spese** mensili

⛔ Non potrai investire a lungo termine finché i PAC non sono sostenibili o non utilizzi capitale eccedente!
"""
        
        report += "---\n"
        return report, pac_totale, risparmio_disponibile, allocazione.get('a_investimenti', 0) if capitale_eccedente > 0 else 0
    
    else:
        # Sostenibile: Risparmio >= PAC
        report += f"""
### ✅ Sostenibilità

I tuoi PAC sono sostenibili! Dopo aver accantonato {formatta_valuta(pac_totale)} al mese, 
ti rimangono ancora **{formatta_valuta(gap_mensile)}** per investimenti a lungo termine.

"""
        
        # Gestione capitale eccedente
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 ALLOCAZIONE CAPITALE ECCEDENTE

Hai {formatta_valuta(capitale_eccedente)} di capitale eccedente.

**Motto: "Investire Prima"**

Poiché i tuoi PAC sono già coperti dal risparmio mensile, l'intero capitale eccedente 
può essere investito immediatamente:

- **Investimento Immediato**: {formatta_valuta(allocazione['a_investimenti'])}

Questo accelererà significativamente la crescita del tuo patrimonio!
"""
        
        report += "---\n"
        
        capitale_investibile_subito = capitale_eccedente if capitale_eccedente > 0 else 0
        return report, pac_totale, risparmio_disponibile, capitale_investibile_subito


def genera_report_fase3_it(disponibilita_mensile, capitale_investibile_subito, profilo_rischio, anni_pensione):
    """Genera il report FASE 3 in italiano con dettagli su ETF e asset."""
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

**Cosa fare:**
1. Aumenta le tue entrate
2. Riduci le spese mensili
3. Rivedi i tuoi obiettivi e i PAC associati

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
    
    report += f"""

---

### 📚 Dettagli su Asset e Strumenti Consigliati

#### 🌍 Azioni ({allocazione['Azioni']}%) - Componente Azionaria Globale

La componente azionaria è il motore di crescita del tuo portafoglio. Per massimizzare la diversificazione e ridurre i costi:

**Strumenti Consigliati (ETF):**

1. **MSCI World** - Paesi Sviluppati (≈1,500 azioni)
   - Copertura: USA, Europa, Giappone, Australia
   - **TER Massimo Accettabile**: 0.20% annuo
   - Esempio: ETF ad accumulo (reinvestimento dividendi automatico)
   - Dove cercare: JustETF.com, ExtraETF.com

2. **MSCI ACWI o FTSE All-World** - Globale Completo (≈3,000 azioni)
   - Copertura: Paesi Sviluppati + Emergenti
   - **TER Massimo Accettabile**: 0.22% annuo
   - Vantaggio: Massima diversificazione globale
   - Dove cercare: JustETF.com, ExtraETF.com

**🔍 Come Selezionare su JustETF/ExtraETF:**
- Filtra per: "Azionario", "Globale", "Accumulo"
- Ordina per: TER crescente
- Verifica: Patrimonio gestito >€100M (liquidità)
- Preferisci: Domiciliazione Irlanda/Lussemburgo (fiscalmente efficienti)

**⚠️ COSTI CRITICI:**
- ✅ TER 0.12-0.22%: Eccellente
- ⚠️ TER 0.30-0.50%: Accettabile solo se necessario
- ❌ TER >0.50%: EVITA - Costi eccessivi
- ❌ Commissioni ingresso/uscita >1%: EVITA ASSOLUTAMENTE
- ❌ Gestioni patrimoniali bancarie >1% annuo: EVITA - Puoi risparmiare €50,000-100,000 in una vita

**💡 Calcolo Impatto Costi:**
Con €100,000 investiti per 30 anni al 7% di rendimento:
- TER 0.20%: €700,000 finali
- TER 1.50%: €530,000 finali
- **Differenza: €170,000 persi in costi!**

---

#### 🏦 Obbligazioni ({allocazione['Obbligazioni']}%) - Componente di Stabilità

Le obbligazioni riducono la volatilità del portafoglio e forniscono reddito stabile.

**Opzione 1: ETF Obbligazionari (Per Principianti)**

**Strumenti Consigliati:**
- **ETF Obbligazioni Governative Globali Investment Grade**
  - Focus: Titoli di stato USA, Europa, Giappone
  - **TER Massimo**: 0.20% annuo
  - Dove cercare: JustETF.com, filtra "Obbligazionario", "Governativo", "Investment Grade"

- **ETF Obbligazioni Corporate Investment Grade**
  - Focus: Aziende solide con rating AA/A
  - **TER Massimo**: 0.25% annuo
  - Rischio leggermente maggiore, rendimento superiore

**🔍 Come Selezionare:**
- Filtra per: Rating "Investment Grade" (BBB- o superiore)
- Verifica: Duration media 5-10 anni
- Preferisci: Accumulo o Distribuzione (a tua scelta)

**Opzione 2: Titoli Obbligazionari Singoli (Per Utenti Avanzati)**

Se hai esperienza o vuoi studiare:
- Acquista direttamente Titoli di Stato (BTP, Bund, Treasury)
- Vantaggi: Nessun TER, rendimento garantito a scadenza
- Svantaggi: Richiede più capitale, meno liquido
- Rating Minimo: BBB (Investment Grade)

**📊 Suggerimento Mix:**
- 70% ETF Governativi (stabilità)
- 30% ETF Corporate IG (rendimento extra)

---

#### 🥇 Oro ({allocazione['Oro']}%) - Protezione e Decorrelazione

L'oro protegge dall'inflazione e riduce il rischio di portafoglio (bassa correlazione con azioni).

**Strumenti Consigliati:**

1. **ETC Oro Fisico** (Exchange Traded Commodity)
   - Backed da oro fisico in caveau
   - **TER Massimo**: 0.25% annuo
   - Esempio: ETC che replicano il prezzo dell'oro spot
   - Dove cercare: JustETF.com, categoria "Materie Prime" → "Oro"

2. **ETF/Fondi Oro Fisico**
   - Simili a ETC ma struttura di fondo
   - TER leggermente superiore ma più regolamentati

**⚠️ EVITA:**
- Futures sull'oro (complessi, contango)
- Azioni di miniere d'oro (troppo volatili, non sono oro puro)
- Prodotti con leva finanziaria

**💡 Perché non oro fisico?**
- Costi di custodia
- Rischio furto
- Difficoltà di liquidazione
- ETC sono più pratici e sicuri

---

### 🛠️ Dove e Come Investire

**Broker Consigliati (a basso costo):**
- Directa, Degiro, Interactive Brokers, Trade Republic
- Verifica: Commissioni per operazione <€2

**Processo di Investimento:**

1. **Ricerca su JustETF.com o ExtraETF.com:**
   - Inserisci asset class desiderata
   - Filtra per TER, patrimonio, replicazione
   - Confronta 2-3 opzioni
   
2. **Verifica ISIN e Nome Completo:**
   - Assicurati di trovare l'ETF/ETC giusto
   
3. **Apri Conto su Broker:**
   - Completa KYC (Know Your Customer)
   - Deposita capitale
   
4. **Esegui Ordini:**
   - Usa ordini "limit" (non "market")
   - Investi secondo allocazione percentuale

**⏰ Frequenza Investimenti (PAC):**
- **Mensile**: Ideale se investi <€500/mese
- **Trimestrale**: Se investi €500-1,500/mese (riduci commissioni)

---

### 💡 Consigli Fondamentali per Neofiti

1. **Diversifica sempre**: Non mettere tutti i soldi in un unico investimento
2. **Pensa a lungo termine**: Gli investimenti danno risultati negli anni, non nei giorni
3. **Investi regolarmente (PAC)**: Stessa cifra ogni mese, riduce il timing risk
4. **Non inseguire il mercato**: Mantieni la disciplina anche quando i mercati scendono (-20% è normale!)
5. **Rivedi annualmente**: Una volta all'anno, ribilancia se necessario
6. **Studio = Risparmio**: Poche ore su JustETF ti fanno risparmiare decine di migliaia di euro
7. **EVITA prodotti bancari costosi**: La banca non è tua amica, vuole guadagnare su di te

### 📖 Risorse Educative

**Siti Web:**
- JustETF.com: Database ETF europei, guide, screener
- ExtraETF.com: Alternativa a JustETF
- Morningstar.it: Analisi fondi e ETF
- FinancialTimes.com: Notizie finanziarie

**Libri (in Italiano):**
- "L'investitore intelligente" - Benjamin Graham
- "Un passo avanti a Wall Street" - Burton Malkiel
- "I soliti ignoti" - Paolo Coletti (sugli errori degli investitori)

**Community:**
- Forum FinanzaOnline (sezione ETF)
- Reddit: r/EuropeFIRE, r/ItaliaPersonalFinance

---

### ⚠️ Cosa NON Fare

❌ **Non investire in:**
- Prodotti che non capisci
- Gestioni patrimoniali bancarie con costi >1%
- Polizze vita con costi di ingresso >3%
- Fondi attivi con TER >1% (raramente battono gli indici)
- Criptovalute come investimento principale
- Azioni singole se non hai esperienza (troppo rischio concentrato)

❌ **Non fidarti di:**
- Consulenti bancari che spingono prodotti della banca
- Promesse di rendimenti garantiti >10%/anno
- "Opportunità irripetibili" con urgenza

✅ **Fidati di:**
- Dati storici e statistiche
- Costi bassi e trasparenti
- Diversificazione
- Tempo e disciplina

---

### 🎓 Principio Fondamentale

**"Il peggior nemico dell'investitore è lui stesso"** - Benjamin Graham

- Non vendere in preda al panico quando i mercati scendono
- Non comprare euforia quando i mercati salgono
- Mantieni il piano, ignora il rumore quotidiano
- Il mercato azionario ha sempre recuperato nel lungo termine (20+ anni)

---

**Disclaimer:** Queste sono indicazioni educative generali. Prima di investire, studia, confronta e, se necessario, consulta un consulente finanziario indipendente (non bancario!).

---
"""
    
    return report


def genera_disclaimer_it():
    """Genera il disclaimer legale in italiano."""
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
- ✅ **Studia autonomamente** su JustETF, ExtraETF, Morningstar
- ✅ Confronta sempre costi e performance
- ✅ Consulta un consulente indipendente per decisioni importanti (non il consulente della tua banca!)
- ✅ Valuta sempre i rischi prima di investire
- ✅ Investi solo ciò che puoi permetterti di perdere nel breve termine

### Privacy e Dati

**Nessun dato viene salvato**: Tutte le informazioni inserite rimangono nella tua sessione 
di browser e vengono eliminate quando chiudi l'app. Non abbiamo accesso ai tuoi dati.

### Responsabilità

Tu sei l'unico responsabile delle tue decisioni di investimento. Gli investimenti comportano rischi, 
inclusa la perdita totale del capitale investito.

---

💙 **Ti auguriamo un futuro finanziario sereno e prospero!**

📚 **Ricorda**: Poche ore di studio possono farti risparmiare decine di migliaia di euro in costi evitabili!
"""


def main():
    """Funzione principale dell'app."""
    setup_page()
    
    # Selettore lingua in sidebar
    with st.sidebar:
        lang = render_language_selector()
        st.markdown("---")
        st.markdown("### Info")
        st.markdown("v2.0 - Multi-language")
        st.markdown("🇮🇹 🇬🇧 🇩🇪")
    
    render_header(lang)
    
    # Raccolta Input
    dati_base = render_dati_base(lang)
    st.markdown("---")
    
    dati_demografici = render_dati_demografici(lang)
    st.markdown("---")
    
    obiettivi = render_gestione_obiettivi(lang)
    st.markdown("---")
    
    profilo_rischio = render_profilo_rischio(lang)
    st.markdown("---")
    
    # Bottone Genera Report
    if st.button(t("generate_report", lang), type="primary", use_container_width=True):
        st.markdown("---")
        st.header(t("personalized_guide", lang))
        
        # Calcoli preliminari
        risparmio_mensile = dati_base['entrate'] - dati_base['uscite']
        
        # FASE 1: Fondo di Emergenza
        fondo_emergenza = calcola_fondo_emergenza(dati_base['uscite'])
        fe_completo, differenza = verifica_fondo_emergenza(
            dati_base['capitale'], 
            fondo_emergenza
        )
        
        mesi_rientro = None
        if not fe_completo and risparmio_mensile > 0:
            mesi_rientro = calcola_mesi_rientro_emergenza(differenza, risparmio_mensile)
        
        # Genera report FASE 1 (attualmente solo IT, estendi per altre lingue se necessario)
        if lang == "it":
            report_fase1 = genera_report_fase1_it(
                dati_base['capitale'],
                fondo_emergenza,
                differenza,
                dati_base['uscite'],
                risparmio_mensile,
                mesi_rientro
            )
        else:
            # Fallback inglese/tedesco (usa italiano per ora)
            report_fase1 = genera_report_fase1_it(
                dati_base['capitale'],
                fondo_emergenza,
                differenza,
                dati_base['uscite'],
                risparmio_mensile,
                mesi_rientro
            )
        
        st.markdown(report_fase1)
        
        # Se il Fondo di Emergenza non è completo, STOP
        if not fe_completo:
            st.error("⚠️ Completa il Fondo di Emergenza prima di procedere!")
            if lang == "it":
                st.markdown(genera_disclaimer_it())
            else:
                st.markdown(genera_disclaimer_it())  # TODO: tradurre
            return
        
        # Capitale eccedente
        capitale_eccedente = max(0, differenza)
        
        # FASE 2: Spese Prevedibili
        if lang == "it":
            report_fase2, pac_totale, _, capitale_investibile_subito = genera_report_fase2_it(
                obiettivi,
                dati_base['entrate'],
                dati_base['uscite'],
                capitale_eccedente
            )
        else:
            report_fase2, pac_totale, _, capitale_investibile_subito = genera_report_fase2_it(
                obiettivi,
                dati_base['entrate'],
                dati_base['uscite'],
                capitale_eccedente
            )  # TODO: tradurre
        
        st.markdown(report_fase2)
        
        # FASE 3: Investimenti
        disponibilita_investimenti_mensile = calcola_disponibilita_investimenti(
            dati_base['entrate'],
            dati_base['uscite'],
            pac_totale
        )
        
        # Se il gap è negativo ma c'è capitale eccedente, la FASE 3 può comunque procedere
        # con il capitale investibile subito
        
        if lang == "it":
            report_fase3 = genera_report_fase3_it(
                disponibilita_investimenti_mensile,
                capitale_investibile_subito,
                profilo_rischio,
                dati_demografici['anni_pensione']
            )
        else:
            report_fase3 = genera_report_fase3_it(
                disponibilita_investimenti_mensile,
                capitale_investibile_subito,
                profilo_rischio,
                dati_demografici['anni_pensione']
            )  # TODO: tradurre
        
        st.markdown(report_fase3)
        
        # Disclaimer finale
        if lang == "it":
            st.markdown(genera_disclaimer_it())
        else:
            st.markdown(genera_disclaimer_it())  # TODO: tradurre
        
        # Bottone per scaricare il report
        st.success(t("report_success", lang))


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
