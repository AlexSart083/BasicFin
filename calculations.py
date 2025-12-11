"""
UI Components for Streamlit App
Contiene tutti i componenti di interfaccia utente
"""

import streamlit as st
from translations import t
from calculations import calcola_pac_mensile, formatta_valuta


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


def render_phases_description(lang):
    """
    Renderizza la descrizione completa delle 3 fasi (sezione educativa).
    
    Args:
        lang (str): Codice lingua
    """
    st.header(t("phases_title", lang))
    st.markdown(t("phases_intro", lang))
    
    st.markdown("---")
    
    # FASE 1
    with st.expander(t("phase1_title", lang), expanded=True):
        st.markdown(t("phase1_desc", lang))
    
    # FASE 2
    with st.expander(t("phase2_title", lang), expanded=False):
        st.markdown(t("phase2_desc", lang))
    
    # FASE 3
    with st.expander(t("phase3_title", lang), expanded=False):
        st.markdown(t("phase3_desc", lang))
    
    st.markdown("---")
    
    # Perché questo ordine
    with st.expander(t("why_this_order", lang), expanded=False):
        st.markdown(t("why_this_order_desc", lang))
    
    st.markdown("---")


def render_dati_base(lang):
    """
    Renderizza la sezione input per i dati finanziari di base.
    
    Returns:
        dict: Dizionario con i dati inseriti
    """
    st.header(t("basic_data", lang))
    
    col1, col2 = st.columns(2)
    
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
    
    col3, col4 = st.columns(2)
    
    with col3:
        capitale = st.number_input(
            t("current_capital", lang),
            min_value=0.0,
            value=5000.0,
            step=500.0,
            help=t("capital_help", lang)
        )
    
    with col4:
        capitale_investito = st.number_input(
            t("invested_capital", lang),
            min_value=0.0,
            value=0.0,
            step=500.0,
            help=t("invested_help", lang)
        )
    
    return {
        "entrate": entrate,
        "uscite": uscite,
        "capitale": capitale,
        "capitale_investito": capitale_investito
    }


def render_dati_demografici(lang):
    """
    Renderizza la sezione input per l'orizzonte temporale.
    
    Returns:
        dict: Dizionario con i dati inseriti
    """
    st.header(t("demographic_data", lang))
    
    anni_pensione = st.slider(
        t("years_to_retirement", lang),
        min_value=1,
        max_value=50,
        value=30,
        help=t("retirement_help", lang)
    )
    
    return {
        "anni_pensione": anni_pensione
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


def render_educational_resources(lang):
    """Renderizza la sezione con le risorse educative consigliate."""
    st.markdown("---")
    st.header(t("educational_sites", lang))
    st.markdown(t("educational_sites_intro", lang))
    
    # One Page Financial
    with st.expander(t("site_onepage_name", lang)):
        st.markdown(t("site_onepage_desc", lang))
        st.markdown("[🔗 Visita One Page Financial](https://onepagefinancial-as.streamlit.app/)")
    
    # Calcolatore Immobiliare
    with st.expander(t("site_immobiliare_name", lang)):
        st.markdown(t("site_immobiliare_desc", lang))
        st.markdown("[🔗 Visita Calcolatore Immobiliare](https://immobiliare-as.streamlit.app/)")
    
    # Finance App
    with st.expander(t("site_finance_name", lang)):
        st.markdown(t("site_finance_desc", lang))
        st.markdown("[🔗 Visita Finance App](https://financeapp-as.streamlit.app/)")
    
    # Overview Asset
    with st.expander(t("site_overview_name", lang)):
        st.markdown(t("site_overview_desc", lang))
        st.markdown("[🔗 Visita Overview Asset](https://overviewasset-as.streamlit.app/)")
    
    # Portfolio Manager
    with st.expander(t("site_portfolio_name", lang)):
        st.markdown(t("site_portfolio_desc", lang))
        st.markdown("[🔗 Visita Portfolio Manager](https://portfolio-as.streamlit.app/)")
