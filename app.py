"""
Guida Finanziaria per Neofiti - Streamlit App v3.0
App educativa multilingue per la pianificazione finanziaria a tre fasi

Autore: Antonino Sortino
Versione: 3.0 - Modular & Multilingual
"""

import streamlit as st

# Import dei moduli personalizzati
from translations import t
from calculations import (
    calcola_fondo_emergenza,
    verifica_fondo_emergenza,
    calcola_mesi_rientro_emergenza,
    calcola_pac_totale,
    calcola_disponibilita_investimenti
)
from ui_components import (
    render_language_selector,
    render_header,
    render_dati_base,
    render_dati_demografici,
    render_gestione_obiettivi,
    render_profilo_rischio,
    render_educational_resources
)
from report_generator_fase1 import genera_report_fase1
from report_generator_fase2 import genera_report_fase2
from report_generator_fase3 import genera_report_fase3
from disclaimer import genera_disclaimer


def setup_page():
    """Configura la pagina Streamlit."""
    st.set_page_config(
        page_title="Financial Guide for Beginners",
        page_icon="💰",
        layout="wide"
    )


def main():
    """Funzione principale dell'app."""
    setup_page()
    
    # Selettore lingua in sidebar
    with st.sidebar:
        lang = render_language_selector()
        st.markdown("---")
        st.markdown(f"### {t('version_info', lang)}")
        st.markdown("v3.0 - Multilingual")
        st.markdown("🇮🇹 🇬🇧 🇩🇪")
        st.markdown("---")
        st.markdown("**© 2024 Antonino Sortino**")
        st.markdown("Educational Tool")
    
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
        
        # ====================================================================
        # FASE 1: Fondo di Emergenza
        # ====================================================================
        fondo_emergenza = calcola_fondo_emergenza(dati_base['uscite'])
        fe_completo, differenza = verifica_fondo_emergenza(
            dati_base['capitale'], 
            fondo_emergenza
        )
        
        mesi_rientro = None
        if not fe_completo and risparmio_mensile > 0:
            mesi_rientro = calcola_mesi_rientro_emergenza(differenza, risparmio_mensile)
        
        # Genera report FASE 1
        report_fase1 = genera_report_fase1(
            dati_base['capitale'],
            fondo_emergenza,
            differenza,
            dati_base['uscite'],
            risparmio_mensile,
            mesi_rientro,
            lang
        )
        
        st.markdown(report_fase1)
        
        # Se il Fondo di Emergenza non è completo, STOP
        if not fe_completo:
            if lang == "it":
                st.error("⚠️ Completa il Fondo di Emergenza prima di procedere!")
            elif lang == "en":
                st.error("⚠️ Complete the Emergency Fund before proceeding!")
            else:
                st.error("⚠️ Vervollständigen Sie den Notgroschen vor dem Fortfahren!")
            
            st.markdown(genera_disclaimer(lang))
            
            # Mostra risorse educative
            render_educational_resources(lang)
            return
        
        # Capitale eccedente
        capitale_eccedente = max(0, differenza)
        
        # ====================================================================
        # FASE 2: Spese Prevedibili (PAC)
        # ====================================================================
        report_fase2, pac_totale, _, capitale_investibile_subito = genera_report_fase2(
            obiettivi,
            dati_base['entrate'],
            dati_base['uscite'],
            capitale_eccedente,
            lang
        )
        
        st.markdown(report_fase2)
        
        # ====================================================================
        # FASE 3: Investimenti
        # ====================================================================
        disponibilita_investimenti_mensile = calcola_disponibilita_investimenti(
            dati_base['entrate'],
            dati_base['uscite'],
            pac_totale
        )
        
        report_fase3 = genera_report_fase3(
            disponibilita_investimenti_mensile,
            capitale_investibile_subito,
            profilo_rischio,
            dati_demografici['anni_pensione'],
            lang
        )
        
        st.markdown(report_fase3)
        
        # Disclaimer finale
        st.markdown(genera_disclaimer(lang))
        
        # Mostra risorse educative
        render_educational_resources(lang)
        
        # Messaggio di successo
        st.success(t("report_success", lang))


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
