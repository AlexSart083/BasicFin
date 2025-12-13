"""
Guida Finanziaria per Nuovi investitori - Streamlit App v3.3
Strumento di Aiuto alla Pianificazione Finanziaria a tre fasi

Autore: Miaono Klaus
Versione: 3.3 - Restructured UX with Separate Pages
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
from pdf_generator import genera_pdf_piano_finanziario


def setup_page():
    """Configura la pagina Streamlit."""
    st.set_page_config(
        page_title="Aiuto alla Pianificazione Finanziaria",
        page_icon="💰",
        layout="wide"
    )


def init_session_state():
    """Inizializza lo stato della sessione."""
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'language' not in st.session_state:
        st.session_state.language = 'it'
    if 'obiettivi' not in st.session_state:
        st.session_state.obiettivi = []
    if 'dati_salvati' not in st.session_state:
        st.session_state.dati_salvati = False


def render_sidebar(lang):
    """Renderizza la sidebar con controlli comuni."""
    with st.sidebar:
        render_language_selector()
        st.markdown("---")
        st.markdown(f"### {t('version_info', lang)}")
        st.markdown("v3.3 - Restructured UX")
        st.markdown("🇮🇹 🇬🇧 🇩🇪")
        st.markdown("---")
        
        # Navigazione
        if st.session_state.page != 'home':
            if st.button("← Torna all'Inizio" if lang == 'it' else "← Back to Home" if lang == 'en' else "← Zurück zum Anfang"):
                st.session_state.page = 'home'
                st.session_state.dati_salvati = False
                st.rerun()
        
        st.markdown("---")
        st.markdown("**© 2025 Miaoino Klaus**")
        st.markdown("Strumento Educativo" if lang == 'it' else "Educational Tool" if lang == 'en' else "Bildungswerkzeug")


def render_home_page(lang):
    """
    PAGINA INIZIALE - Solo teoria e bottone di inizio.
    """
    # Header
    st.title(t("app_title", lang))
    
    # Modifica linguaggio da "piano personalizzato" a "aiuto alla pianificazione"
    if lang == "it":
        welcome_text = """
        ### Benvenuto nel tuo Strumento di Aiuto alla Pianificazione Finanziaria!
        
        Prima di iniziare con i tuoi dati, è fondamentale comprendere la **filosofia 
        di prioritizzazione a tre fasi** che guiderà la tua analisi finanziaria.
        """
    elif lang == "en":
        welcome_text = """
        ### Welcome to your Financial Planning Aid Tool!
        
        Before starting with your data, it's essential to understand the 
        **three-phase prioritization philosophy** that will guide your financial analysis.
        """
    else:  # de
        welcome_text = """
        ### Willkommen zu Ihrem Finanzplanungs-Hilfswerkzeug!
        
        Bevor Sie mit Ihren Daten beginnen, ist es wichtig, die 
        **dreiphasige Priorisierungsphilosophie** zu verstehen, die Ihre Finanzanalyse leiten wird.
        """
    
    st.markdown(welcome_text)
    st.markdown("---")
    
    # Descrizione delle Fasi
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
    st.markdown("---")
    
    # Bottone grande e centrale per iniziare
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        button_text = {
            'it': '🚀 Iniziamo la Pianificazione',
            'en': '🚀 Let\'s Start Planning',
            'de': '🚀 Beginnen wir mit der Planung'
        }
        if st.button(button_text[lang], type="primary", use_container_width=True):
            st.session_state.page = 'input'
            st.rerun()


def render_input_page(lang):
    """
    PAGINA 1 - Input unificato per Liquidità (FASE 1) e Obiettivi (FASE 2).
    """
    # Titolo modificato
    if lang == "it":
        st.title("📊 Analisi della Liquidità e degli Obiettivi di Medio Termine")
        st.markdown("""
        In questa sezione raccoglieremo le informazioni necessarie per analizzare:
        - **FASE 1**: La tua situazione di liquidità e il Fondo di Emergenza
        - **FASE 2**: I tuoi obiettivi finanziari a medio-lungo termine
        """)
    elif lang == "en":
        st.title("📊 Analysis of Liquidity and Medium-Term Goals")
        st.markdown("""
        In this section we will collect the information needed to analyze:
        - **PHASE 1**: Your liquidity situation and Emergency Fund
        - **PHASE 2**: Your medium-long term financial goals
        """)
    else:  # de
        st.title("📊 Analyse der Liquidität und Mittelfristigen Ziele")
        st.markdown("""
        In diesem Abschnitt sammeln wir die Informationen, die zur Analyse benötigt werden:
        - **PHASE 1**: Ihre Liquiditätssituation und Notgroschen
        - **PHASE 2**: Ihre mittel-langfristigen finanziellen Ziele
        """)
    
    st.markdown("---")
    
    # =================================================================
    # SEZIONE A: LIQUIDITÀ (FASE 1)
    # =================================================================
    if lang == "it":
        st.header("💰 Sezione A: Analisi della Liquidità (FASE 1)")
        st.markdown("Inserisci i tuoi dati finanziari attuali per valutare il tuo Fondo di Emergenza.")
    elif lang == "en":
        st.header("💰 Section A: Liquidity Analysis (PHASE 1)")
        st.markdown("Enter your current financial data to assess your Emergency Fund.")
    else:
        st.header("💰 Abschnitt A: Liquiditätsanalyse (PHASE 1)")
        st.markdown("Geben Sie Ihre aktuellen Finanzdaten ein, um Ihren Notgroschen zu bewerten.")
    
    dati_base = render_dati_base(lang)
    
    st.markdown("---")
    
    # =================================================================
    # SEZIONE B: OBIETTIVI DI MEDIO TERMINE (FASE 2)
    # =================================================================
    if lang == "it":
        st.header("🎯 Sezione B: Obiettivi di Medio-Lungo Termine (FASE 2)")
        st.markdown("Definisci i tuoi obiettivi finanziari futuri per calcolare i Piani di Accumulo necessari.")
    elif lang == "en":
        st.header("🎯 Section B: Medium-Long Term Goals (PHASE 2)")
        st.markdown("Define your future financial goals to calculate the necessary Accumulation Plans.")
    else:
        st.header("🎯 Abschnitt B: Mittel-Langfristige Ziele (PHASE 2)")
        st.markdown("Definieren Sie Ihre zukünftigen finanziellen Ziele, um die erforderlichen Ansparpläne zu berechnen.")
    
    obiettivi = render_gestione_obiettivi(lang)
    
    st.markdown("---")
    
    # =================================================================
    # SEZIONE C: PROFILO E ORIZZONTE TEMPORALE (per FASE 3)
    # =================================================================
    if lang == "it":
        st.header("⏰ Sezione C: Orizzonte Temporale e Profilo di Rischio")
        st.markdown("Queste informazioni ci aiuteranno a comprendere il tuo orizzonte di investimento a lungo termine.")
    elif lang == "en":
        st.header("⏰ Section C: Time Horizon and Risk Profile")
        st.markdown("This information will help us understand your long-term investment horizon.")
    else:
        st.header("⏰ Abschnitt C: Zeithorizont und Risikoprofil")
        st.markdown("Diese Informationen helfen uns, Ihren langfristigen Anlagehorizont zu verstehen.")
    
    dati_demografici = render_dati_demografici(lang)
    st.markdown("---")
    profilo_rischio = render_profilo_rischio(lang)
    
    st.markdown("---")
    st.markdown("---")
    
    # Salva i dati in session_state
    st.session_state.dati_base = dati_base
    st.session_state.dati_demografici = dati_demografici
    st.session_state.profilo_rischio = profilo_rischio
    
    # Bottone per passare alla pagina successiva
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        button_text = {
            'it': '📈 Vedi lo Step Successivo: Gli Investimenti →',
            'en': '📈 See Next Step: Investments →',
            'de': '📈 Nächster Schritt: Investitionen →'
        }
        if st.button(button_text[lang], type="primary", use_container_width=True):
            st.session_state.page = 'results'
            st.session_state.dati_salvati = True
            st.rerun()


def render_results_page(lang):
    """
    PAGINA 2 - Report calcolati e sezione educativa sugli investimenti.
    """
    # Verifica che i dati siano stati salvati
    if not st.session_state.dati_salvati:
        st.warning("⚠️ Devi prima completare la compilazione dei dati!" if lang == 'it' 
                  else "⚠️ You must first complete the data compilation!" if lang == 'en'
                  else "⚠️ Sie müssen zuerst die Datenkompilierung abschließen!")
        if st.button("← Torna alla Compilazione" if lang == 'it' else "← Back to Input" if lang == 'en' else "← Zurück zur Eingabe"):
            st.session_state.page = 'input'
            st.rerun()
        return
    
    # Recupera i dati salvati
    dati_base = st.session_state.dati_base
    dati_demografici = st.session_state.dati_demografici
    profilo_rischio = st.session_state.profilo_rischio
    obiettivi = st.session_state.obiettivi
    
    # Titolo
    if lang == "it":
        st.title("📊 La Tua Analisi Finanziaria Completa")
        st.markdown("Ecco l'analisi dettagliata della tua situazione finanziaria basata sui dati forniti.")
    elif lang == "en":
        st.title("📊 Your Complete Financial Analysis")
        st.markdown("Here is the detailed analysis of your financial situation based on the data provided.")
    else:
        st.title("📊 Ihre Vollständige Finanzanalyse")
        st.markdown("Hier ist die detaillierte Analyse Ihrer finanziellen Situation basierend auf den bereitgestellten Daten.")
    
    st.markdown("---")
    
    # Mostra riepilogo capitale investito (se presente)
    if dati_base['capitale_investito'] > 0:
        info_text = {
            'it': f"""ℹ️ **Nota**: Hai già {dati_base['capitale_investito']:,.2f}€ investiti. 
            Questo importo non influisce sui calcoli delle 3 fasi, ma è utile per la tua panoramica finanziaria completa.""",
            'en': f"""ℹ️ **Note**: You already have €{dati_base['capitale_investito']:,.2f} invested. 
            This amount does not affect the 3-phase calculations, but is useful for your complete financial overview.""",
            'de': f"""ℹ️ **Hinweis**: Sie haben bereits €{dati_base['capitale_investito']:,.2f} investiert. 
            Dieser Betrag beeinflusst die 3-Phasen-Berechnungen nicht, ist aber für Ihre vollständige Finanzübersicht nützlich."""
        }
        st.info(info_text[lang])
    
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
    
    # Se il Fondo di Emergenza non è completo, mostra warning
    if not fe_completo:
        warning_text = {
            'it': "⚠️ **Priorità**: Il tuo Fondo di Emergenza è incompleto. Completalo prima di investire!",
            'en': "⚠️ **Priority**: Your Emergency Fund is incomplete. Complete it before investing!",
            'de': "⚠️ **Priorität**: Ihr Notgroschen ist unvollständig. Vervollständigen Sie ihn vor dem Investieren!"
        }
        info_text = {
            'it': "ℹ️ Ti mostriamo comunque le Fasi 2 e 3 per aiutarti con la pianificazione completa.",
            'en': "ℹ️ We still show you Phases 2 and 3 to help you with complete planning.",
            'de': "ℹ️ Wir zeigen Ihnen dennoch die Phasen 2 und 3, um Ihnen bei der vollständigen Planung zu helfen."
        }
        st.warning(warning_text[lang])
        st.info(info_text[lang])
    
    # Capitale eccedente (sarà 0 se fondo emergenza incompleto)
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
    # FASE 3: Investimenti (Educativo + Allocazione)
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
    
    # Sezione link esterno per esempi di portafoglio
    st.markdown("---")
    if lang == "it":
        st.markdown("""
        ### 🔗 Esempi di Portafoglio (Link Esterno)
        
        Per visualizzare esempi generali di portafogli basati su diversi profili di rischio, 
        puoi consultare risorse educative esterne. 
        
        **Importante**: Questi sono solo esempi generici e non costituiscono una raccomandazione personalizzata 
        per la tua situazione specifica.
        
        [🔗 Vedi Esempi di Portafoglio](https://www.example.com/portfolio-examples)
        
        *(Nota: Questo è un link placeholder. Sostituisci con un link reale a risorse educative.)*
        """)
    elif lang == "en":
        st.markdown("""
        ### 🔗 Portfolio Examples (External Link)
        
        To view general examples of portfolios based on different risk profiles, 
        you can consult external educational resources.
        
        **Important**: These are only generic examples and do not constitute a personalized recommendation 
        for your specific situation.
        
        [🔗 View Portfolio Examples](https://www.example.com/portfolio-examples)
        
        *(Note: This is a placeholder link. Replace with a real link to educational resources.)*
        """)
    else:  # de
        st.markdown("""
        ### 🔗 Portfolio-Beispiele (Externer Link)
        
        Um allgemeine Beispiele von Portfolios basierend auf verschiedenen Risikoprofilen anzuzeigen, 
        können Sie externe Bildungsressourcen konsultieren.
        
        **Wichtig**: Dies sind nur generische Beispiele und stellen keine personalisierte Empfehlung 
        für Ihre spezifische Situation dar.
        
        [🔗 Portfolio-Beispiele ansehen](https://www.example.com/portfolio-examples)
        
        *(Hinweis: Dies ist ein Platzhalter-Link. Ersetzen Sie ihn durch einen echten Link zu Bildungsressourcen.)*
        """)
    
    # Disclaimer finale
    st.markdown(genera_disclaimer(lang))
    
    # Mostra risorse educative
    render_educational_resources(lang)
    
    # Messaggio di successo
    success_text = {
        'it': "✅ Analisi completata con successo!",
        'en': "✅ Analysis completed successfully!",
        'de': "✅ Analyse erfolgreich abgeschlossen!"
    }
    st.success(success_text[lang])
    
    # ========================================================================
    # EXPORT PDF
    # ========================================================================
    st.markdown("---")
    
    export_header = {
        'it': '📄 Esporta il Tuo Piano in PDF',
        'en': '📄 Export Your Plan to PDF',
        'de': '📄 Exportieren Sie Ihren Plan als PDF'
    }
    st.subheader(export_header[lang])
    
    export_description = {
        'it': 'Scarica una versione PDF completa del tuo piano finanziario con tutti i dati e i report generati. Questo documento include le informazioni chiave e può essere salvato o stampato per riferimento futuro.',
        'en': 'Download a complete PDF version of your financial plan with all data and generated reports. This document includes key information and can be saved or printed for future reference.',
        'de': 'Laden Sie eine vollständige PDF-Version Ihres Finanzplans mit allen Daten und generierten Berichten herunter. Dieses Dokument enthält wichtige Informationen und kann für zukünftige Referenz gespeichert oder gedruckt werden.'
    }
    st.markdown(export_description[lang])
    
    # Genera il PDF
    try:
        pdf_buffer = genera_pdf_piano_finanziario(
            dati_base=dati_base,
            dati_demografici=dati_demografici,
            profilo_rischio=profilo_rischio,
            obiettivi=obiettivi,
            report_fase1_text=report_fase1,
            report_fase2_text=report_fase2,
            report_fase3_text=report_fase3,
            lang=lang
        )
        
        # Nome file con data
        from datetime import datetime
        data_filename = datetime.now().strftime("%Y%m%d")
        filename_map = {
            'it': f'Piano_Finanziario_{data_filename}.pdf',
            'en': f'Financial_Plan_{data_filename}.pdf',
            'de': f'Finanzplan_{data_filename}.pdf'
        }
        
        button_text = {
            'it': '📥 Scarica Piano in PDF',
            'en': '📥 Download Plan as PDF',
            'de': '📥 Plan als PDF Herunterladen'
        }
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label=button_text[lang],
                data=pdf_buffer,
                file_name=filename_map[lang],
                mime='application/pdf',
                type='primary',
                use_container_width=True
            )
        
        pdf_note = {
            'it': '💡 **Nota:** Il PDF contiene un riepilogo dei tuoi dati e i report delle 3 fasi. Per ragioni di spazio, la sezione FASE 3 include solo i punti chiave dell\'allocazione. Consulta la versione online per i dettagli educativi completi.',
            'en': '💡 **Note:** The PDF contains a summary of your data and the 3-phase reports. For space reasons, PHASE 3 includes only key allocation points. Consult the online version for complete educational details.',
            'de': '💡 **Hinweis:** Das PDF enthält eine Zusammenfassung Ihrer Daten und die 3-Phasen-Berichte. Aus Platzgründen enthält PHASE 3 nur die wichtigsten Allokationspunkte. Konsultieren Sie die Online-Version für vollständige Bildungsdetails.'
        }
        st.info(pdf_note[lang])
        
    except Exception as e:
        error_text = {
            'it': f'⚠️ Errore nella generazione del PDF: {str(e)}',
            'en': f'⚠️ Error generating PDF: {str(e)}',
            'de': f'⚠️ Fehler beim Generieren des PDF: {str(e)}'
        }
        st.error(error_text[lang])
    
    # Bottone per ricominciare
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        button_text = {
            'it': '🔄 Ricomincia con Nuovi Dati',
            'en': '🔄 Start Over with New Data',
            'de': '🔄 Mit Neuen Daten Neu Beginnen'
        }
        if st.button(button_text[lang], use_container_width=True):
            # Reset dello stato
            st.session_state.page = 'home'
            st.session_state.dati_salvati = False
            st.session_state.obiettivi = []
            st.rerun()


def main():
    """Funzione principale dell'app."""
    setup_page()
    init_session_state()
    
    lang = st.session_state.language
    
    # Renderizza la sidebar
    render_sidebar(lang)
    
    # Routing tra le pagine
    if st.session_state.page == 'home':
        render_home_page(lang)
    elif st.session_state.page == 'input':
        render_input_page(lang)
    elif st.session_state.page == 'results':
        render_results_page(lang)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
