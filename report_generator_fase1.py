"""
Report Generator Module
Genera report finanziari personalizzati in italiano, inglese e tedesco
"""

from calculations import formatta_valuta

# ============================================================================
# FASE 1: FONDO DI EMERGENZA
# ============================================================================

def genera_report_fase1(capitale_attuale, fondo_emergenza, differenza, uscite_mensili, 
                        risparmio_mensile, mesi_rientro, lang):
    """
    Genera il report FASE 1 nella lingua specificata.
    
    Args:
        capitale_attuale (float): Capitale attuale disponibile
        fondo_emergenza (float): Target fondo emergenza
        differenza (float): Differenza capitale - target
        uscite_mensili (float): Uscite mensili totali
        risparmio_mensile (float): Risparmio mensile disponibile
        mesi_rientro (int): Mesi necessari per completare il fondo
        lang (str): Codice lingua (it, en, de)
        
    Returns:
        str: Report formattato in Markdown
    """
    if lang == "it":
        return _genera_report_fase1_it(
            capitale_attuale, fondo_emergenza, differenza, 
            uscite_mensili, risparmio_mensile, mesi_rientro
        )
    elif lang == "en":
        return _genera_report_fase1_en(
            capitale_attuale, fondo_emergenza, differenza, 
            uscite_mensili, risparmio_mensile, mesi_rientro
        )
    elif lang == "de":
        return _genera_report_fase1_de(
            capitale_attuale, fondo_emergenza, differenza, 
            uscite_mensili, risparmio_mensile, mesi_rientro
        )
    else:
        return _genera_report_fase1_it(
            capitale_attuale, fondo_emergenza, differenza, 
            uscite_mensili, risparmio_mensile, mesi_rientro
        )


def _genera_report_fase1_it(capitale_attuale, fondo_emergenza, differenza, uscite_mensili, 
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
4. **Dopo {mesi_rientro} mesi**, avrai completato la base di sicurezza e potrai considerare gli investimenti

**⚠️ PRIORITÀ ASSOLUTA**: Completa il Fondo di Emergenza prima di investire! Le fasi 2 e 3 sono mostrate sotto per aiutarti con la pianificazione completa.
"""
        else:
            report += """
⚠️ **ATTENZIONE**: Il tuo risparmio mensile è insufficiente o nullo. 

**Cosa fare:**
1. **Aumenta le tue entrate** (secondo lavoro, freelance, vendita di beni non essenziali)
2. **Riduci drasticamente le spese** per creare un margine di risparmio
3. **Rivedi il tuo budget** per trovare almeno 100-200€ al mese da destinare al fondo

**⚠️ IMPORTANTE**: Questo è un prerequisito fondamentale prima di considerare qualsiasi investimento. Le fasi 2 e 3 sono mostrate sotto per la pianificazione completa.
"""
        
        report += """
---

### 💡 Consiglio per Neofiti

Il Fondo di Emergenza non è un "extra", è un **must**. Senza di esso, qualsiasi imprevisto 
potrebbe costringerti a indebitarti o vendere investimenti in perdita.

---

### 📊 Considerazione sull'Inflazione

**Perché il Fondo di Emergenza deve essere in liquidità?**

Anche se l'**inflazione erode il potere d'acquisto** della liquidità nel tempo, il Fondo di Emergenza 
DEVE rimanere **immediatamente disponibile** e **senza rischi**:

- ✅ **Accesso immediato**: In caso di emergenza, non puoi aspettare vendite di investimenti
- ✅ **Zero rischio di perdite**: Gli investimenti possono essere in perdita proprio quando ne hai bisogno
- ⚠️ **Inflazione**: Sì, la liquidità perde valore (circa 2-3% all'anno), ma è il prezzo della sicurezza

**💡 La soluzione all'inflazione**:
1. **Completa il Fondo di Emergenza** (FASE 1) - Liquidità
2. **Pianifica gli obiettivi** (FASE 2) - PAC protetti
3. **Investi il resto** (FASE 3) - Qui batti l'inflazione!

Solo DOPO aver completato il Fondo di Emergenza puoi investire per battere l'inflazione nel lungo termine.
"""
    else:
        report += f"""
- ✅ **Situazione**: Il tuo fondo è **COMPLETO**!
- 💪 **Eccedenza**: {formatta_valuta(differenza)}

**Complimenti!** Hai una solida base di sicurezza finanziaria. 
Ora puoi procedere con le fasi successive.

**💡 Filosofia: "Investire Prima"**

La tua eccedenza di capitale verrà allocata secondo questa filosofia:
1. Prima priorità: Coprire eventuali gap negli obiettivi futuri
2. Seconda priorità: **Investire subito** il resto per farlo crescere

---

### 📊 Protezione dall'Inflazione

Ora che hai completato il Fondo di Emergenza, puoi concentrarti su **battere l'inflazione** 
con gli investimenti:

- ✅ Il tuo "cuscinetto di sicurezza" è al sicuro in liquidità
- 📈 Il capitale eccedente può essere investito per **crescere oltre l'inflazione**
- 💰 Obiettivo: rendimenti reali positivi (rendimento - inflazione > 0)

Nelle fasi successive imparerai come costruire un portafoglio che preservi e aumenti 
il tuo potere d'acquisto nel tempo!

---
"""
    
    return report


def _genera_report_fase1_en(capitale_attuale, fondo_emergenza, differenza, uscite_mensili, 
                            risparmio_mensile, mesi_rientro=None):
    """Genera il report FASE 1 in inglese."""
    report = f"""
## 🛡️ PHASE 1: Emergency Fund

### Absolute Priority!

The **Emergency Fund** is the foundation of your financial security. 
It protects you from unexpected events like job loss, medical expenses, or urgent repairs.

**The rule**: You must have liquidity equal to **6 months of expenses**.

### Your Emergency Fund

- 💰 **Current Capital**: {formatta_valuta(capitale_attuale)}
- 🎯 **Emergency Fund Target**: {formatta_valuta(fondo_emergenza)} (6 × {formatta_valuta(uscite_mensili)})
"""
    
    if differenza < 0:
        report += f"""
- ⚠️ **Status**: Your fund is **INCOMPLETE**
- 📉 **Missing Amount**: {formatta_valuta(abs(differenza))}

### 🚨 AUTOMATIC RECOVERY PLAN

Before proceeding with any other financial goal, you must complete your Emergency Fund!

"""
        if mesi_rientro and mesi_rientro != float('inf'):
            report += f"""
**Accumulation Plan:**
- 💵 **Available Monthly Savings**: {formatta_valuta(risparmio_mensile)}
- ⏱️ **Time Required**: {mesi_rientro} months
- 📅 **Monthly Amount to Allocate**: {formatta_valuta(risparmio_mensile)} (100% of savings)

**What to do:**
1. **Allocate 100% of your monthly savings** ({formatta_valuta(risparmio_mensile)}) to the Emergency Fund for the next **{mesi_rientro} months**
2. **Keep this liquidity** in an easily accessible account (savings account or checking account)
3. **Do not invest** this money in stocks or risky instruments
4. **After {mesi_rientro} months**, you will have completed your safety foundation and can consider investments

**⚠️ ABSOLUTE PRIORITY**: Complete your Emergency Fund before investing! Phases 2 and 3 are shown below to help you with complete planning.
"""
        else:
            report += """
⚠️ **WARNING**: Your monthly savings are insufficient or zero. 

**What to do:**
1. **Increase your income** (second job, freelancing, selling non-essential items)
2. **Drastically reduce expenses** to create a savings margin
3. **Review your budget** to find at least €100-200 per month to allocate to the fund

**⚠️ IMPORTANT**: This is a fundamental prerequisite before considering any investments. Phases 2 and 3 are shown below for complete planning.
"""
        
        report += """
---

### 💡 Advice for Beginners

The Emergency Fund is not an "extra", it's a **must**. Without it, any unexpected event 
could force you to go into debt or sell investments at a loss.

---

### 📊 Inflation Consideration

**Why must the Emergency Fund be in cash?**

Even though **inflation erodes the purchasing power** of cash over time, the Emergency Fund 
MUST remain **immediately available** and **risk-free**:

- ✅ **Immediate access**: In an emergency, you can't wait for investment sales
- ✅ **Zero risk of losses**: Investments can be down exactly when you need them
- ⚠️ **Inflation**: Yes, cash loses value (about 2-3% per year), but it's the price of security

**💡 The inflation solution**:
1. **Complete the Emergency Fund** (PHASE 1) - Liquidity
2. **Plan your goals** (PHASE 2) - Protected PACs
3. **Invest the rest** (PHASE 3) - Here you beat inflation!

Only AFTER completing the Emergency Fund can you invest to beat inflation in the long term.
"""
    else:
        report += f"""
- ✅ **Status**: Your fund is **COMPLETE**!
- 💪 **Surplus**: {formatta_valuta(differenza)}

**Congratulations!** You have a solid foundation of financial security. 
Now you can proceed with subsequent phases.

**💡 Philosophy: "Invest First"**

Your surplus capital will be allocated according to this philosophy:
1. First priority: Cover any gaps in future goals
2. Second priority: **Invest immediately** the rest to make it grow

---

### 📊 Protection Against Inflation

Now that you've completed the Emergency Fund, you can focus on **beating inflation** 
with investments:

- ✅ Your "safety cushion" is secure in cash
- 📈 Surplus capital can be invested to **grow beyond inflation**
- 💰 Goal: positive real returns (return - inflation > 0)

In subsequent phases you'll learn how to build a portfolio that preserves and increases 
your purchasing power over time!

---
"""
    
    return report


def _genera_report_fase1_de(capitale_attuale, fondo_emergenza, differenza, uscite_mensili, 
                            risparmio_mensile, mesi_rientro=None):
    """Genera il report FASE 1 in tedesco."""
    report = f"""
## 🛡️ PHASE 1: Notgroschen

### Absolute Priorität!

Der **Notgroschen** ist die Grundlage Ihrer finanziellen Sicherheit. 
Er schützt Sie vor unerwarteten Ereignissen wie Jobverlust, medizinischen Ausgaben oder dringenden Reparaturen.

**Die Regel**: Sie müssen Liquidität in Höhe von **6 Monatsausgaben** haben.

### Ihr Notgroschen

- 💰 **Aktuelles Kapital**: {formatta_valuta(capitale_attuale)}
- 🎯 **Notgroschen-Ziel**: {formatta_valuta(fondo_emergenza)} (6 × {formatta_valuta(uscite_mensili)})
"""
    
    if differenza < 0:
        report += f"""
- ⚠️ **Status**: Ihr Notgroschen ist **UNVOLLSTÄNDIG**
- 📉 **Fehlender Betrag**: {formatta_valuta(abs(differenza))}

### 🚨 AUTOMATISCHER RÜCKKEHRPLAN

Bevor Sie mit anderen finanziellen Zielen fortfahren, müssen Sie Ihren Notgroschen vervollständigen!

"""
        if mesi_rientro and mesi_rientro != float('inf'):
            report += f"""
**Ansparplan:**
- 💵 **Verfügbare monatliche Ersparnisse**: {formatta_valuta(risparmio_mensile)}
- ⏱️ **Erforderliche Zeit**: {mesi_rientro} Monate
- 📅 **Monatlich zuzuweisender Betrag**: {formatta_valuta(risparmio_mensile)} (100% der Ersparnisse)

**Was zu tun ist:**
1. **Weisen Sie 100% Ihrer monatlichen Ersparnisse** ({formatta_valuta(risparmio_mensile)}) dem Notgroschen für die nächsten **{mesi_rientro} Monate** zu
2. **Bewahren Sie diese Liquidität** auf einem leicht zugänglichen Konto auf (Sparkonto oder Girokonto)
3. **Investieren Sie nicht** dieses Geld in Aktien oder riskante Instrumente
4. **Nach {mesi_rientro} Monaten** werden Sie Ihre Sicherheitsgrundlage abgeschlossen haben und können Investitionen in Betracht ziehen

**⚠️ ABSOLUTE PRIORITÄT**: Vervollständigen Sie Ihren Notgroschen vor dem Investieren! Die Phasen 2 und 3 werden unten gezeigt, um Ihnen bei der vollständigen Planung zu helfen.
"""
        else:
            report += """
⚠️ **WARNUNG**: Ihre monatlichen Ersparnisse sind unzureichend oder null. 

**Was zu tun ist:**
1. **Erhöhen Sie Ihr Einkommen** (Zweitjob, Freelancing, Verkauf nicht essentieller Gegenstände)
2. **Reduzieren Sie die Ausgaben drastisch**, um eine Sparmarge zu schaffen
3. **Überprüfen Sie Ihr Budget**, um mindestens 100-200€ pro Monat für den Notgroschen zu finden

**⚠️ WICHTIG**: Dies ist eine grundlegende Voraussetzung, bevor Sie Investitionen in Betracht ziehen. Die Phasen 2 und 3 werden unten für die vollständige Planung gezeigt.
"""
        
        report += """
---

### 💡 Rat für Anfänger

Der Notgroschen ist kein "Extra", sondern ein **Muss**. Ohne ihn könnte Sie jedes unerwartete Ereignis 
zwingen, sich zu verschulden oder Investitionen mit Verlust zu verkaufen.

---

### 📊 Inflationsüberlegung

**Warum muss der Notgroschen in Bargeld sein?**

Auch wenn die **Inflation die Kaufkraft** von Bargeld im Laufe der Zeit erodiert, MUSS der Notgroschen 
**sofort verfügbar** und **risikofrei** bleiben:

- ✅ **Sofortiger Zugang**: Im Notfall können Sie nicht auf Investitionsverkäufe warten
- ✅ **Null Verlustrisiko**: Investitionen können genau dann im Minus sein, wenn Sie sie brauchen
- ⚠️ **Inflation**: Ja, Bargeld verliert an Wert (etwa 2-3% pro Jahr), aber das ist der Preis der Sicherheit

**💡 Die Inflationslösung**:
1. **Notgroschen vervollständigen** (PHASE 1) - Liquidität
2. **Ziele planen** (PHASE 2) - Geschützte PACs
3. **Den Rest investieren** (PHASE 3) - Hier schlagen Sie die Inflation!

Erst NACH Vervollständigung des Notgroschens können Sie investieren, um die Inflation langfristig zu schlagen.
"""
    else:
        report += f"""
- ✅ **Status**: Ihr Notgroschen ist **VOLLSTÄNDIG**!
- 💪 **Überschuss**: {formatta_valuta(differenza)}

**Herzlichen Glückwunsch!** Sie haben eine solide Grundlage finanzieller Sicherheit. 
Jetzt können Sie mit den nachfolgenden Phasen fortfahren.

**💡 Philosophie: "Zuerst Investieren"**

Ihr Überschusskapital wird nach dieser Philosophie zugewiesen:
1. Erste Priorität: Deckung eventueller Lücken bei zukünftigen Zielen
2. Zweite Priorität: **Sofort investieren** den Rest, um ihn wachsen zu lassen

---

### 📊 Schutz vor Inflation

Jetzt, da Sie den Notgroschen vervollständigt haben, können Sie sich darauf konzentrieren, **die Inflation zu schlagen** 
mit Investitionen:

- ✅ Ihr "Sicherheitspolster" ist sicher in Bargeld
- 📈 Überschusskapital kann investiert werden, um **über die Inflation hinaus zu wachsen**
- 💰 Ziel: positive Realrenditen (Rendite - Inflation > 0)

In den folgenden Phasen lernen Sie, wie Sie ein Portfolio aufbauen, das Ihre Kaufkraft 
im Laufe der Zeit bewahrt und erhöht!

---
"""
    
    return report
