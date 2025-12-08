"""
Financial Calculations Module
Contiene tutte le funzioni pure per i calcoli finanziari
"""

import math

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
        profilo_rischio (str): "Conservatore", "Moderato", "Aggressivo" (o versioni inglesi/tedesche)
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
