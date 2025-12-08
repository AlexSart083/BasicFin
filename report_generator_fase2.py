"""
Report Generator Module - Fase 2 (PAC)
Genera report per la pianificazione delle spese prevedibili
"""

from calculations import formatta_valuta, calcola_pac_mensile, alloca_capitale_eccedente


def genera_report_fase2(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente, lang):
    """
    Genera il report FASE 2 nella lingua specificata.
    
    Args:
        obiettivi (list): Lista di obiettivi finanziari
        entrate_mensili (float): Entrate mensili nette
        uscite_mensili (float): Uscite mensili totali
        capitale_eccedente (float): Capitale oltre il fondo emergenza
        lang (str): Codice lingua (it, en, de)
        
    Returns:
        tuple: (report_str, pac_totale, risparmio_disponibile, capitale_investibile_subito)
    """
    if lang == "it":
        return _genera_report_fase2_it(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente)
    elif lang == "en":
        return _genera_report_fase2_en(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente)
    elif lang == "de":
        return _genera_report_fase2_de(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente)
    else:
        return _genera_report_fase2_it(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente)


def _genera_report_fase2_it(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente=0):
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

**Filosofia: "Investire Prima"** - Procedi alla FASE 3 per l'allocazione.
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
        report += f"""
### ⚠️ GAP NEGATIVO

Il totale dei tuoi PAC mensili ({formatta_valuta(pac_totale)}) supera il tuo risparmio 
disponibile ({formatta_valuta(risparmio_disponibile)})!

**Deficit mensile**: {formatta_valuta(abs(gap_mensile))}

"""
        
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
        report += f"""
### ✅ Sostenibilità

I tuoi PAC sono sostenibili! Dopo aver accantonato {formatta_valuta(pac_totale)} al mese, 
ti rimangono ancora **{formatta_valuta(gap_mensile)}** per investimenti a lungo termine.

"""
        
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 ALLOCAZIONE CAPITALE ECCEDENTE

Hai {formatta_valuta(capitale_eccedente)} di capitale eccedente.

**Filosofia: "Investire Prima"**

Poiché i tuoi PAC sono già coperti dal risparmio mensile, l'intero capitale eccedente 
può essere investito immediatamente:

- **Investimento Immediato**: {formatta_valuta(allocazione['a_investimenti'])}

Questo accelererà significativamente la crescita del tuo patrimonio!
"""
        
        report += "---\n"
        
        capitale_investibile_subito = capitale_eccedente if capitale_eccedente > 0 else 0
        return report, pac_totale, risparmio_disponibile, capitale_investibile_subito


def _genera_report_fase2_en(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente=0):
    """Genera il report FASE 2 in inglese."""
    risparmio_disponibile = entrate_mensili - uscite_mensili
    
    report = f"""
## 🎯 PHASE 2: Predictable Expenses (PAC - Accumulation Plan)

### Plan for the Future

Now that you have your Emergency Fund, it's time to plan your long-term goals.

**The key concept**: For each future goal, calculate how much you need to save each month 
(Monthly Accumulation Plan or PAC).

### Your Monthly Savings

- 💵 **Monthly Income**: {formatta_valuta(entrate_mensili)}
- 💳 **Monthly Expenses**: {formatta_valuta(uscite_mensili)}
- 💰 **Available Savings**: {formatta_valuta(risparmio_disponibile)}
"""
    
    if capitale_eccedente > 0:
        report += f"- 🎁 **Surplus Capital from Emergency Fund**: {formatta_valuta(capitale_eccedente)}\n"
    
    report += "\n"
    
    if not obiettivi:
        report += """
### ℹ️ No Goals Defined

You haven't defined long-term goals yet. Consider adding goals such as:
- Down payment for a house
- Wedding or important events
- Master's degree or training courses
- Important trip

Once defined, you'll know exactly how much to save each month!

"""
        
        if capitale_eccedente > 0:
            report += f"""
### 💎 Surplus Capital Allocation

Since you have no defined goals, your surplus capital of **{formatta_valuta(capitale_eccedente)}** 
can be allocated directly to long-term investments!

**Philosophy: "Invest First"** - Proceed to PHASE 3 for allocation.
"""
        
        report += "---\n"
        return report, 0, risparmio_disponibile, capitale_eccedente
    
    report += "### 📋 Your Goals and Monthly PACs\n\n"
    
    pac_totale = 0
    somma_anni = 0
    for obiettivo in obiettivi:
        pac_mensile = calcola_pac_mensile(obiettivo['costo'], obiettivo['anni'])
        pac_totale += pac_mensile
        somma_anni += obiettivo['anni']
        
        report += f"""
**{obiettivo['nome']}**
- Total Cost: {formatta_valuta(obiettivo['costo'])}
- Available Time: {obiettivo['anni']} years ({obiettivo['anni'] * 12} months)
- Monthly PAC: **{formatta_valuta(pac_mensile)}**

"""
    
    anni_media = somma_anni / len(obiettivi) if obiettivi else 5
    
    report += f"""
---

### 💼 Total Monthly PAC

**You need to set aside each month**: {formatta_valuta(pac_totale)}

"""
    
    gap_mensile = risparmio_disponibile - pac_totale
    
    if gap_mensile < 0:
        report += f"""
### ⚠️ NEGATIVE GAP

The total of your monthly PACs ({formatta_valuta(pac_totale)}) exceeds your available 
savings ({formatta_valuta(risparmio_disponibile)})!

**Monthly deficit**: {formatta_valuta(abs(gap_mensile))}

"""
        
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 COVERAGE WITH SURPLUS CAPITAL

You have {formatta_valuta(capitale_eccedente)} of surplus capital from the Emergency Fund.

**Smart Allocation:**
- **Allocation for Goals**: {formatta_valuta(allocazione['a_obiettivi'])}
  - This amount will cover the monthly gap of {formatta_valuta(abs(gap_mensile))} for about {int(allocazione['a_obiettivi'] / abs(gap_mensile)) if gap_mensile != 0 else 0} months
- **Available for Immediate Investments**: {formatta_valuta(allocazione['a_investimenti'])}

"""
            
            if allocazione['a_obiettivi'] >= abs(gap_mensile) * 12 * anni_media:
                report += "✅ **The gap is fully covered!** You can proceed to PHASE 3.\n"
            else:
                report += f"""
⚠️ **Gap partially covered**. After {int(allocazione['a_obiettivi'] / abs(gap_mensile))} months, you'll need to:
1. Increase income
2. Reduce expenses
3. Review goals

For now you can proceed to PHASE 3 with limited investments.
"""
        else:
            report += """
**What to do:**
1. **Reduce goals** or extend timelines
2. **Increase income** (second job, freelancing, etc.)
3. **Reduce** monthly expenses

⛔ You won't be able to invest long-term until PACs are sustainable or you use surplus capital!
"""
        
        report += "---\n"
        return report, pac_totale, risparmio_disponibile, allocazione.get('a_investimenti', 0) if capitale_eccedente > 0 else 0
    
    else:
        report += f"""
### ✅ Sustainability

Your PACs are sustainable! After setting aside {formatta_valuta(pac_totale)} per month, 
you still have **{formatta_valuta(gap_mensile)}** for long-term investments.

"""
        
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 SURPLUS CAPITAL ALLOCATION

You have {formatta_valuta(capitale_eccedente)} of surplus capital.

**Philosophy: "Invest First"**

Since your PACs are already covered by monthly savings, the entire surplus capital 
can be invested immediately:

- **Immediate Investment**: {formatta_valuta(allocazione['a_investimenti'])}

This will significantly accelerate the growth of your wealth!
"""
        
        report += "---\n"
        
        capitale_investibile_subito = capitale_eccedente if capitale_eccedente > 0 else 0
        return report, pac_totale, risparmio_disponibile, capitale_investibile_subito


def _genera_report_fase2_de(obiettivi, entrate_mensili, uscite_mensili, capitale_eccedente=0):
    """Genera il report FASE 2 in tedesco."""
    risparmio_disponibile = entrate_mensili - uscite_mensili
    
    report = f"""
## 🎯 PHASE 2: Vorhersehbare Ausgaben (PAC - Ansparplan)

### Planen Sie für die Zukunft

Jetzt, da Sie Ihren Notgroschen haben, ist es Zeit, Ihre langfristigen Ziele zu planen.

**Das Schlüsselkonzept**: Berechnen Sie für jedes zukünftige Ziel, wie viel Sie monatlich sparen müssen 
(Monatlicher Ansparplan oder PAC).

### Ihre monatlichen Ersparnisse

- 💵 **Monatliches Einkommen**: {formatta_valuta(entrate_mensili)}
- 💳 **Monatliche Ausgaben**: {formatta_valuta(uscite_mensili)}
- 💰 **Verfügbare Ersparnisse**: {formatta_valuta(risparmio_disponibile)}
"""
    
    if capitale_eccedente > 0:
        report += f"- 🎁 **Überschusskapital aus Notgroschen**: {formatta_valuta(capitale_eccedente)}\n"
    
    report += "\n"
    
    if not obiettivi:
        report += """
### ℹ️ Keine Ziele definiert

Sie haben noch keine langfristigen Ziele definiert. Erwägen Sie, Ziele hinzuzufügen wie:
- Anzahlung für ein Haus
- Hochzeit oder wichtige Ereignisse
- Master-Abschluss oder Schulungskurse
- Wichtige Reise

Sobald definiert, wissen Sie genau, wie viel Sie jeden Monat sparen müssen!

"""
        
        if capitale_eccedente > 0:
            report += f"""
### 💎 Überschusskapital-Allokation

Da Sie keine definierten Ziele haben, kann Ihr Überschusskapital von **{formatta_valuta(capitale_eccedente)}** 
direkt in langfristige Investitionen allokiert werden!

**Philosophie: "Zuerst Investieren"** - Fahren Sie mit PHASE 3 für die Allokation fort.
"""
        
        report += "---\n"
        return report, 0, risparmio_disponibile, capitale_eccedente
    
    report += "### 📋 Ihre Ziele und monatliche PACs\n\n"
    
    pac_totale = 0
    somma_anni = 0
    for obiettivo in obiettivi:
        pac_mensile = calcola_pac_mensile(obiettivo['costo'], obiettivo['anni'])
        pac_totale += pac_mensile
        somma_anni += obiettivo['anni']
        
        report += f"""
**{obiettivo['nome']}**
- Gesamtkosten: {formatta_valuta(obiettivo['costo'])}
- Verfügbare Zeit: {obiettivo['anni']} Jahre ({obiettivo['anni'] * 12} Monate)
- Monatlicher PAC: **{formatta_valuta(pac_mensile)}**

"""
    
    anni_media = somma_anni / len(obiettivi) if obiettivi else 5
    
    report += f"""
---

### 💼 Gesamter monatlicher PAC

**Sie müssen jeden Monat zurücklegen**: {formatta_valuta(pac_totale)}

"""
    
    gap_mensile = risparmio_disponibile - pac_totale
    
    if gap_mensile < 0:
        report += f"""
### ⚠️ NEGATIVE LÜCKE

Die Summe Ihrer monatlichen PACs ({formatta_valuta(pac_totale)}) übersteigt Ihre verfügbaren 
Ersparnisse ({formatta_valuta(risparmio_disponibile)})!

**Monatliches Defizit**: {formatta_valuta(abs(gap_mensile))}

"""
        
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 DECKUNG MIT ÜBERSCHUSSKAPITAL

Sie haben {formatta_valuta(capitale_eccedente)} Überschusskapital aus dem Notgroschen.

**Intelligente Allokation:**
- **Allokation für Ziele**: {formatta_valuta(allocazione['a_obiettivi'])}
  - Dieser Betrag deckt die monatliche Lücke von {formatta_valuta(abs(gap_mensile))} für etwa {int(allocazione['a_obiettivi'] / abs(gap_mensile)) if gap_mensile != 0 else 0} Monate
- **Verfügbar für sofortige Investitionen**: {formatta_valuta(allocazione['a_investimenti'])}

"""
            
            if allocazione['a_obiettivi'] >= abs(gap_mensile) * 12 * anni_media:
                report += "✅ **Die Lücke ist vollständig gedeckt!** Sie können zu PHASE 3 fortfahren.\n"
            else:
                report += f"""
⚠️ **Lücke teilweise gedeckt**. Nach {int(allocazione['a_obiettivi'] / abs(gap_mensile))} Monaten müssen Sie:
1. Einkommen erhöhen
2. Ausgaben reduzieren
3. Ziele überprüfen

Vorerst können Sie zu PHASE 3 mit begrenzten Investitionen fortfahren.
"""
        else:
            report += """
**Was zu tun ist:**
1. **Ziele reduzieren** oder Zeitrahmen verlängern
2. **Einkommen erhöhen** (Zweitjob, Freelancing, etc.)
3. **Monatliche Ausgaben reduzieren**

⛔ Sie können langfristig nicht investieren, bis PACs nachhaltig sind oder Sie Überschusskapital verwenden!
"""
        
        report += "---\n"
        return report, pac_totale, risparmio_disponibile, allocazione.get('a_investimenti', 0) if capitale_eccedente > 0 else 0
    
    else:
        report += f"""
### ✅ Nachhaltigkeit

Ihre PACs sind nachhaltig! Nach dem Zurücklegen von {formatta_valuta(pac_totale)} pro Monat 
haben Sie noch **{formatta_valuta(gap_mensile)}** für langfristige Investitionen.

"""
        
        if capitale_eccedente > 0:
            allocazione = alloca_capitale_eccedente(capitale_eccedente, gap_mensile, anni_media)
            
            report += f"""
### 💎 ÜBERSCHUSSKAPITAL-ALLOKATION

Sie haben {formatta_valuta(capitale_eccedente)} Überschusskapital.

**Philosophie: "Zuerst Investieren"**

Da Ihre PACs bereits durch monatliche Ersparnisse gedeckt sind, kann das gesamte Überschusskapital 
sofort investiert werden:

- **Sofortige Investition**: {formatta_valuta(allocazione['a_investimenti'])}

Dies wird das Wachstum Ihres Vermögens erheblich beschleunigen!
"""
        
        report += "---\n"
        
        capitale_investibile_subito = capitale_eccedente if capitale_eccedente > 0 else 0
        return report, pac_totale, risparmio_disponibile, capitale_investibile_subito
