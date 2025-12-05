"""
Guida Finanziaria per Neofiti - Streamlit App
App educativa per la pianificazione finanziaria a tre fasi
"""

import streamlit as st

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
    # Allocazioni base per profilo
    allocazioni_base = {
        "Conservatore": {"Azioni": 30, "Obbligazioni": 60, "Oro": 10},
        "Moderato": {"Azioni": 50, "Obbligazioni": 40, "Oro": 10},
        "Aggressivo": {"Azioni": 70, "Obbligazioni": 20, "Oro": 10}
    }
    
    allocazione = allocazioni_base.get(profilo_rischio, allocazioni_base["Moderato"]).copy()
    
    # Aggiustamento per orizzonte temporale lungo (>20 anni)
    if anni_pensione > 20:
        # Aumenta componente azionaria del 10%
        bonus_azioni = 10
        allocazione["Azioni"] += bonus_azioni
        # Riduci obbligazioni
        allocazione["Obbligazioni"] -= bonus_azioni
    
    # Aggiustamento per orizzonte temporale corto (<10 anni)
    elif anni_pensione < 10:
        # Riduci componente azionaria del 10%
        riduzione_azioni = 10
        allocazione["Azioni"] = max(20, allocazione["Azioni"] - riduzione_azioni)
        # Aumenta obbligazioni
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


def render_header():
    """Renderizza l'intestazione dell'app."""
    st.title("💰 Guida Finanziaria per Neofiti")
    st.markdown("""
    ### Benvenuto nella tua guida finanziaria personale!
    
    Questa app ti aiuterà a pianificare le tue finanze seguendo una filosofia 
    di prioritizzazione a **tre fasi**:
    
    1. **🛡️ FASE 1**: Costruisci il tuo Fondo di Emergenza
    2. **🎯 FASE 2**: Pianifica le Spese Prevedibili (obiettivi a lungo termine)
    3. **📈 FASE 3**: Investi per il Futuro
    
    ---
    """)


def render_dati_base():
    """
    Renderizza la sezione input per i dati finanziari di base.
    
    Returns:
        dict: Dizionario con i dati inseriti
    """
    st.header("📊 Dati Finanziari di Base")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        entrate = st.number_input(
            "💵 Entrate Mensili Nette (€)",
            min_value=0.0,
            value=2000.0,
            step=100.0,
            help="Il tuo stipendio netto mensile o entrate regolari"
        )
    
    with col2:
        uscite = st.number_input(
            "💳 Uscite Mensili Totali (€)",
            min_value=0.0,
            value=1500.0,
            step=100.0,
            help="Tutte le tue spese mensili (affitto, bollette, cibo, ecc.)"
        )
    
    with col3:
        capitale = st.number_input(
            "🏦 Capitale Attuale/Liquidità (€)",
            min_value=0.0,
            value=5000.0,
            step=500.0,
            help="I tuoi risparmi attuali disponibili"
        )
    
    return {
        "entrate": entrate,
        "uscite": uscite,
        "capitale": capitale
    }


def render_dati_demografici():
    """
    Renderizza la sezione input per i dati demografici.
    
    Returns:
        dict: Dizionario con i dati inseriti
    """
    st.header("👤 Dati Demografici e Obiettivi di Vita")
    
    col1, col2 = st.columns(2)
    
    with col1:
        anni_pensione = st.slider(
            "⏰ Anni alla Pensione",
            min_value=1,
            max_value=50,
            value=30,
            help="Quanti anni mancano alla tua pensione?"
        )
    
    with col2:
        fascia_eta = st.selectbox(
            "🎂 Fascia di Età",
            options=["20-30", "30-40", "40-50", "50-60", "60+"],
            index=0,
            help="La tua fascia di età attuale"
        )
    
    return {
        "anni_pensione": anni_pensione,
        "fascia_eta": fascia_eta
    }


def render_gestione_obiettivi():
    """
    Renderizza la sezione per gestire obiettivi finanziari multipli.
    
    Returns:
        list: Lista di obiettivi
    """
    st.header("🎯 Spese Future Prevedibili (Obiettivi)")
    
    st.markdown("""
    Aggiungi qui i tuoi obiettivi di lungo termine che richiedono una pianificazione 
    (es. acconto casa, matrimonio, master universitario, ecc.).
    """)
    
    # Inizializza session_state per gli obiettivi se non esiste
    if 'obiettivi' not in st.session_state:
        st.session_state.obiettivi = []
    
    # Form per aggiungere nuovo obiettivo
    with st.expander("➕ Aggiungi Nuovo Obiettivo", expanded=len(st.session_state.obiettivi) == 0):
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            nome_obiettivo = st.text_input(
                "Nome Obiettivo",
                placeholder="es. Acconto Casa",
                key="input_nome"
            )
        
        with col2:
            costo_obiettivo = st.number_input(
                "Costo Stimato (€)",
                min_value=0.0,
                value=20000.0,
                step=1000.0,
                key="input_costo"
            )
        
        with col3:
            anni_obiettivo = st.number_input(
                "Anni all'Obiettivo",
                min_value=1,
                max_value=30,
                value=5,
                key="input_anni"
            )
        
        if st.button("✅ Aggiungi Obiettivo"):
            if nome_obiettivo:
                st.session_state.obiettivi.append({
                    "nome": nome_obiettivo,
                    "costo": costo_obiettivo,
                    "anni": anni_obiettivo
                })
                st.success(f"✅ Obiettivo '{nome_obiettivo}' aggiunto!")
                st.rerun()
            else:
                st.error("⚠️ Inserisci un nome per l'obiettivo")
    
    # Mostra obiettivi esistenti
    if st.session_state.obiettivi:
        st.subheader("📋 I Tuoi Obiettivi")
        for idx, obiettivo in enumerate(st.session_state.obiettivi):
            col1, col2 = st.columns([4, 1])
            with col1:
                pac_mensile = calcola_pac_mensile(obiettivo['costo'], obiettivo['anni'])
                st.info(f"""
                **{obiettivo['nome']}**  
                Costo: {formatta_valuta(obiettivo['costo'])} | 
                Tempo: {obiettivo['anni']} anni | 
                PAC mensile: {formatta_valuta(pac_mensile)}
                """)
            with col2:
                if st.button("🗑️", key=f"del_{idx}", help="Elimina obiettivo"):
                    st.session_state.obiettivi.pop(idx)
                    st.rerun()
    else:
        st.info("ℹ️ Nessun obiettivo aggiunto. Aggiungi il tuo primo obiettivo sopra!")
    
    return st.session_state.obiettivi


def render_profilo_rischio():
    """
    Renderizza la sezione per il profilo di rischio.
    
    Returns:
        str: Profilo di rischio selezionato
    """
    st.header("📊 Profilo di Rischio per Investimenti")
    
    st.markdown("""
    Il tuo profilo di rischio determinerà come allocare i tuoi investimenti a lungo termine.
    """)
    
    profilo = st.radio(
        "Seleziona il tuo profilo di rischio:",
        options=["Conservatore", "Moderato", "Aggressivo"],
        index=1,
        help="""
        - **Conservatore**: Preferisci stabilità e basso rischio
        - **Moderato**: Bilanciato tra crescita e sicurezza
        - **Aggressivo**: Massimizzi la crescita accettando volatilità
        """
    )
    
    # Descrizioni dei profili
    descrizioni = {
        "Conservatore": "🛡️ Proteggi il capitale con investimenti stabili",
        "Moderato": "⚖️ Bilancia crescita e sicurezza",
        "Aggressivo": "🚀 Massimizza il potenziale di crescita"
    }
    
    st.info(descrizioni[profilo])
    
    return profilo


# ============================================================================
# SEZIONE 3: GENERAZIONE REPORT E LOGICA PRINCIPALE
# ============================================================================

def genera_report_fase1(capitale_attuale, fondo_emergenza, differenza, uscite_mensili):
    """
    Genera il report per la FASE 1 (Fondo di Emergenza).
    
    Args:
        capitale_attuale (float): Capitale disponibile
        fondo_emergenza (float): Target fondo emergenza
        differenza (float): Differenza tra capitale e target
        uscite_mensili (float): Uscite mensili
        
    Returns:
        str: Report formattato in Markdown
    """
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

### 🚨 AZIONE RICHIESTA

Prima di procedere con qualsiasi altro obiettivo finanziario, devi completare il tuo Fondo di Emergenza!

**Cosa fare:**
1. **Risparmia l'importo mancante**: {formatta_valuta(abs(differenza))}
2. **Mantieni questa liquidità** in un conto facilmente accessibile (conto deposito o conto corrente)
3. **Non investire** questi soldi in azioni o strumenti rischiosi

**⛔ STOP: Non passare alle fasi successive finché non hai completato il tuo Fondo di Emergenza!**

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

---
"""
    
    return report


def genera_report_fase2(obiettivi, entrate_mensili, uscite_mensili):
    """
    Genera il report per la FASE 2 (Spese Prevedibili).
    
    Args:
        obiettivi (list): Lista di obiettivi
        entrate_mensili (float): Entrate mensili
        uscite_mensili (float): Uscite mensili
        
    Returns:
        tuple: (str: report, float: pac_totale, float: risparmio_disponibile)
    """
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
    
    if not obiettivi:
        report += """
### ℹ️ Nessun Obiettivo Definito

Non hai ancora definito obiettivi a lungo termine. Considera di aggiungere obiettivi come:
- Acconto per una casa
- Matrimonio o eventi importanti
- Master o corsi di formazione
- Viaggio importante

Una volta definiti, saprai esattamente quanto risparmiare ogni mese!

---
"""
        return report, 0, risparmio_disponibile
    
    report += "### 📋 I Tuoi Obiettivi e PAC Mensili\n\n"
    
    pac_totale = 0
    for obiettivo in obiettivi:
        pac_mensile = calcola_pac_mensile(obiettivo['costo'], obiettivo['anni'])
        pac_totale += pac_mensile
        
        report += f"""
**{obiettivo['nome']}**
- Costo Totale: {formatta_valuta(obiettivo['costo'])}
- Tempo Disponibile: {obiettivo['anni']} anni ({obiettivo['anni'] * 12} mesi)
- PAC Mensile: **{formatta_valuta(pac_mensile)}**

"""
    
    report += f"""
---

### 💼 Totale PAC Mensile

**Devi accantonare ogni mese**: {formatta_valuta(pac_totale)}

"""
    
    # Verifica sostenibilità
    if pac_totale > risparmio_disponibile:
        deficit = pac_totale - risparmio_disponibile
        report += f"""
### ⚠️ ATTENZIONE

Il totale dei tuoi PAC mensili ({formatta_valuta(pac_totale)}) supera il tuo risparmio 
disponibile ({formatta_valuta(risparmio_disponibile)})!

**Deficit mensile**: {formatta_valuta(deficit)}

**Cosa fare:**
1. **Riduci gli obiettivi** o allunga i tempi
2. **Aumenta le entrate** (secondo lavoro, freelance, ecc.)
3. **Riduci le spese** mensili

⛔ Non potrai procedere alla FASE 3 finché i PAC non sono sostenibili!
"""
    else:
        report += f"""
### ✅ Sostenibilità

I tuoi PAC sono sostenibili! Dopo aver accantonato {formatta_valuta(pac_totale)} al mese, 
ti rimangono ancora **{formatta_valuta(risparmio_disponibile - pac_totale)}** per investimenti 
a lungo termine.

---
"""
    
    return report, pac_totale, risparmio_disponibile


def genera_report_fase3(disponibilita, profilo_rischio, anni_pensione):
    """
    Genera il report per la FASE 3 (Investimenti).
    
    Args:
        disponibilita (float): Disponibilità mensile per investimenti
        profilo_rischio (str): Profilo di rischio
        anni_pensione (int): Anni alla pensione
        
    Returns:
        str: Report formattato in Markdown
    """
    report = f"""
## 📈 FASE 3: Investimenti a Lungo Termine

### Fai Crescere il Tuo Patrimonio

Congratulazioni! Hai completato le basi: Fondo di Emergenza e Pianificazione degli Obiettivi. 
Ora puoi investire per il futuro.

### Disponibilità per Investimenti

**Importo Mensile Investibile**: {formatta_valuta(disponibilita)}

"""
    
    if disponibilita <= 0:
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
        importo_mensile = disponibilita * (percentuale / 100)
        report += f"- **{asset}**: {percentuale}% → {formatta_valuta(importo_mensile)} al mese\n"
    
    report += f"""

### 📚 Cosa Significa

**Azioni** ({allocazione['Azioni']}%)
- Investimenti azionari globali diversificati
- Esempio: Indici come MSCI World o MSCI All Countries
- Maggior potenziale di crescita, ma più volatilità

**Obbligazioni** ({allocazione['Obbligazioni']}%)
- Titoli di debito governativi e corporate
- Esempio: Indici Obbligazionari Governativi Globali
- Stabilità e reddito fisso, minore volatilità

**Oro** ({allocazione['Oro']}%)
- Protezione dall'inflazione e diversificazione
- Investimento in oro fisico o strumenti equivalenti
- Bassa correlazione con azioni e obbligazioni

### 💡 Consigli per Neofiti

1. **Diversifica sempre**: Non mettere tutti i soldi in un unico investimento
2. **Pensa a lungo termine**: Gli investimenti danno risultati negli anni, non nei giorni
3. **PAC (Piano di Accumulo Capitale)**: Investi la stessa cifra ogni mese, indipendentemente dal mercato
4. **Non inseguire il mercato**: Mantieni la disciplina anche quando i mercati scendono
5. **Rivedi periodicamente**: Una volta all'anno, controlla se la tua allocazione è ancora adeguata

### ⚠️ Dove Investire

Questa guida ti indica **cosa** e **quanto** investire, ma **non** prodotti specifici.

Per scegliere strumenti concreti (ETF, fondi, ecc.), considera:
- Consultare un consulente finanziario indipendente
- Studiare su piattaforme educative
- Confrontare costi e performance storiche

**Non investire** in prodotti che non comprendi!

---
"""
    
    return report


def genera_disclaimer():
    """
    Genera il disclaimer legale.
    
    Returns:
        str: Disclaimer formattato
    """
    return """
---

## ⚖️ Disclaimer Importante

### Natura Educativa

Questa applicazione fornisce **indicazioni educative generali** sulla pianificazione finanziaria 
e **non costituisce consulenza finanziaria personalizzata**.

### Limitazioni

- ❌ **Non siamo consulenti finanziari certificati**
- ❌ **Non vendiamo prodotti finanziari**
- ❌ **Non garantiamo rendimenti** sugli investimenti
- ❌ **Non salviamo i tuoi dati** (tutto resta nel tuo browser durante la sessione)

### Cosa Dovresti Fare

- ✅ Usa questa guida come punto di partenza
- ✅ Consulta un professionista per decisioni importanti
- ✅ Studia e forma te stesso sulla finanza personale
- ✅ Valuta sempre i rischi prima di investire

### Privacy e Dati

**Nessun dato viene salvato**: Tutte le informazioni inserite rimangono nella tua sessione 
di browser e vengono eliminate quando chiudi l'app. Non abbiamo accesso ai tuoi dati.

---

💙 **Ti auguriamo un futuro finanziario sereno e prospero!**
"""


def main():
    """Funzione principale dell'app."""
    setup_page()
    render_header()
    
    # Raccolta Input
    dati_base = render_dati_base()
    st.markdown("---")
    
    dati_demografici = render_dati_demografici()
    st.markdown("---")
    
    obiettivi = render_gestione_obiettivi()
    st.markdown("---")
    
    profilo_rischio = render_profilo_rischio()
    st.markdown("---")
    
    # Bottone Genera Report
    if st.button("🚀 Genera la Tua Guida Finanziaria Personalizzata", type="primary", use_container_width=True):
        st.markdown("---")
        st.header("📊 La Tua Guida Finanziaria Personalizzata")
        
        # FASE 1: Fondo di Emergenza
        fondo_emergenza = calcola_fondo_emergenza(dati_base['uscite'])
        fe_completo, differenza = verifica_fondo_emergenza(
            dati_base['capitale'], 
            fondo_emergenza
        )
        
        report_fase1 = genera_report_fase1(
            dati_base['capitale'],
            fondo_emergenza,
            differenza,
            dati_base['uscite']
        )
        st.markdown(report_fase1)
        
        # Se il Fondo di Emergenza non è completo, STOP
        if not fe_completo:
            st.error("⚠️ Completa il Fondo di Emergenza prima di procedere!")
            st.markdown(genera_disclaimer())
            return
        
        # FASE 2: Spese Prevedibili
        report_fase2, pac_totale, risparmio_disponibile = genera_report_fase2(
            obiettivi,
            dati_base['entrate'],
            dati_base['uscite']
        )
        st.markdown(report_fase2)
        
        # Verifica sostenibilità PAC
        if pac_totale > risparmio_disponibile:
            st.error("⚠️ I tuoi PAC non sono sostenibili! Rivedi gli obiettivi.")
            st.markdown(genera_disclaimer())
            return
        
        # FASE 3: Investimenti
        disponibilita_investimenti = calcola_disponibilita_investimenti(
            dati_base['entrate'],
            dati_base['uscite'],
            pac_totale
        )
        
        report_fase3 = genera_report_fase3(
            disponibilita_investimenti,
            profilo_rischio,
            dati_demografici['anni_pensione']
        )
        st.markdown(report_fase3)
        
        # Disclaimer finale
        st.markdown(genera_disclaimer())
        
        # Bottone per scaricare il report
        st.success("✅ Report generato con successo!")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
