"""
PDF Generator Module
Genera PDF professionali del piano finanziario
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
from datetime import datetime

from calculations import formatta_valuta


def genera_pdf_piano_finanziario(
    dati_base,
    dati_demografici,
    profilo_rischio,
    obiettivi,
    report_fase1_text,
    report_fase2_text,
    report_fase3_text,
    lang='it'
):
    """
    Genera un PDF completo del piano finanziario.
    
    Args:
        dati_base (dict): Dati finanziari base
        dati_demografici (dict): Dati demografici
        profilo_rischio (str): Profilo di rischio
        obiettivi (list): Lista obiettivi
        report_fase1_text (str): Report Fase 1 in markdown
        report_fase2_text (str): Report Fase 2 in markdown
        report_fase3_text (str): Report Fase 3 in markdown
        lang (str): Lingua
        
    Returns:
        BytesIO: Buffer contenente il PDF
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Stili
    styles = getSampleStyleSheet()
    
    # Stile personalizzato per titolo
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f77b4'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Stile per sottotitoli
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Stile per sezioni
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    # Stile per testo normale
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        fontName='Helvetica'
    )
    
    # Stile per warning/info
    warning_style = ParagraphStyle(
        'CustomWarning',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#e74c3c'),
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    success_style = ParagraphStyle(
        'CustomSuccess',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#27ae60'),
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    # Contenuto del documento
    story = []
    
    # Header
    titoli = {
        'it': 'Piano di Aiuto alla Pianificazione Finanziaria',
        'en': 'Financial Planning Aid Report',
        'de': 'Finanzplanungs-Hilfsbericht'
    }
    story.append(Paragraph(titoli.get(lang, titoli['it']), title_style))
    
    # Data generazione
    data_oggi = datetime.now().strftime("%d/%m/%Y")
    sottotitoli = {
        'it': f'Generato il {data_oggi}',
        'en': f'Generated on {data_oggi}',
        'de': f'Erstellt am {data_oggi}'
    }
    story.append(Paragraph(sottotitoli.get(lang, sottotitoli['it']), normal_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Disclaimer iniziale
    disclaimer_iniziale = {
        'it': '<b>Nota Importante:</b> Questo documento fornisce indicazioni educative generali sulla pianificazione finanziaria e non costituisce consulenza finanziaria personalizzata.',
        'en': '<b>Important Note:</b> This document provides general educational guidance on financial planning and does not constitute personalized financial advice.',
        'de': '<b>Wichtiger Hinweis:</b> Dieses Dokument bietet allgemeine Bildungsanleitung zur Finanzplanung und stellt keine personalisierte Finanzberatung dar.'
    }
    story.append(Paragraph(disclaimer_iniziale.get(lang, disclaimer_iniziale['it']), warning_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Separatore
    story.append(Spacer(1, 0.3*cm))
    
    # ========================================================================
    # SEZIONE 1: RIEPILOGO DATI INSERITI
    # ========================================================================
    riepilogo_titoli = {
        'it': 'Riepilogo Dati Inseriti',
        'en': 'Summary of Entered Data',
        'de': 'Zusammenfassung der eingegebenen Daten'
    }
    story.append(Paragraph(riepilogo_titoli.get(lang, riepilogo_titoli['it']), subtitle_style))
    
    # Tabella dati finanziari
    dati_labels = {
        'it': ['Parametro', 'Valore'],
        'en': ['Parameter', 'Value'],
        'de': ['Parameter', 'Wert']
    }
    
    entrate_labels = {'it': 'Entrate Mensili', 'en': 'Monthly Income', 'de': 'Monatliches Einkommen'}
    uscite_labels = {'it': 'Uscite Mensili', 'en': 'Monthly Expenses', 'de': 'Monatliche Ausgaben'}
    capitale_labels = {'it': 'Capitale Attuale', 'en': 'Current Capital', 'de': 'Aktuelles Kapital'}
    investito_labels = {'it': 'Capitale Investito', 'en': 'Invested Capital', 'de': 'Investiertes Kapital'}
    pensione_labels = {'it': 'Anni alla Pensione', 'en': 'Years to Retirement', 'de': 'Jahre bis zur Rente'}
    
    data_table_data = [
        dati_labels.get(lang, dati_labels['it']),
        [entrate_labels.get(lang, entrate_labels['it']), formatta_valuta(dati_base['entrate'])],
        [uscite_labels.get(lang, uscite_labels['it']), formatta_valuta(dati_base['uscite'])],
        [capitale_labels.get(lang, capitale_labels['it']), formatta_valuta(dati_base['capitale'])],
        [investito_labels.get(lang, investito_labels['it']), formatta_valuta(dati_base['capitale_investito'])],
        [pensione_labels.get(lang, pensione_labels['it']), f"{dati_demografici['anni_pensione']} anni" if lang == 'it' else f"{dati_demografici['anni_pensione']} years" if lang == 'en' else f"{dati_demografici['anni_pensione']} Jahre"],
        ['Profilo di Rischio' if lang == 'it' else 'Risk Profile' if lang == 'en' else 'Risikoprofil', profilo_rischio]
    ]
    
    data_table = Table(data_table_data, colWidths=[8*cm, 6*cm])
    data_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
    ]))
    
    story.append(data_table)
    story.append(Spacer(1, 0.5*cm))
    
    # Obiettivi (se presenti)
    if obiettivi:
        obiettivi_titolo = {
            'it': 'Obiettivi Definiti',
            'en': 'Defined Goals',
            'de': 'Definierte Ziele'
        }
        story.append(Paragraph(obiettivi_titolo.get(lang, obiettivi_titolo['it']), section_style))
        
        obiettivi_headers = {
            'it': ['Obiettivo', 'Costo', 'Anni'],
            'en': ['Goal', 'Cost', 'Years'],
            'de': ['Ziel', 'Kosten', 'Jahre']
        }
        
        obiettivi_data = [obiettivi_headers.get(lang, obiettivi_headers['it'])]
        for obj in obiettivi:
            obiettivi_data.append([
                obj['nome'],
                formatta_valuta(obj['costo']),
                str(obj['anni'])
            ])
        
        obiettivi_table = Table(obiettivi_data, colWidths=[7*cm, 4*cm, 3*cm])
        obiettivi_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ]))
        
        story.append(obiettivi_table)
        story.append(Spacer(1, 0.5*cm))
    
    story.append(PageBreak())
    
    # ========================================================================
    # SEZIONE 2: REPORT FASE 1
    # ========================================================================
    fase1_titolo = {
        'it': 'FASE 1: Fondo di Emergenza',
        'en': 'PHASE 1: Emergency Fund',
        'de': 'PHASE 1: Notgroschen'
    }
    story.append(Paragraph(fase1_titolo.get(lang, fase1_titolo['it']), subtitle_style))
    
    # Converti markdown semplice in paragrafi
    fase1_paragrafi = _markdown_to_paragraphs(report_fase1_text, normal_style, warning_style, success_style)
    story.extend(fase1_paragrafi)
    
    story.append(PageBreak())
    
    # ========================================================================
    # SEZIONE 3: REPORT FASE 2
    # ========================================================================
    fase2_titolo = {
        'it': 'FASE 2: Spese Prevedibili (PAC)',
        'en': 'PHASE 2: Predictable Expenses (PAC)',
        'de': 'PHASE 2: Vorhersehbare Ausgaben (PAC)'
    }
    story.append(Paragraph(fase2_titolo.get(lang, fase2_titolo['it']), subtitle_style))
    
    fase2_paragrafi = _markdown_to_paragraphs(report_fase2_text, normal_style, warning_style, success_style)
    story.extend(fase2_paragrafi)
    
    story.append(PageBreak())
    
    # ========================================================================
    # SEZIONE 4: REPORT FASE 3 (SOMMARIO)
    # ========================================================================
    fase3_titolo = {
        'it': 'FASE 3: Investimenti a Lungo Termine',
        'en': 'PHASE 3: Long-Term Investments',
        'de': 'PHASE 3: Langfristige Investitionen'
    }
    story.append(Paragraph(fase3_titolo.get(lang, fase3_titolo['it']), subtitle_style))
    
    # Nota: Il report fase 3 è molto lungo, includiamo solo i punti chiave
    nota_fase3 = {
        'it': '<i>Nota: Per ragioni di spazio, questa sezione include solo i punti chiave dell\'allocazione. Consulta il report completo online per dettagli educativi su pensioni, inflazione e interesse composto.</i>',
        'en': '<i>Note: For space reasons, this section includes only key allocation points. Consult the complete online report for educational details on pensions, inflation, and compound interest.</i>',
        'de': '<i>Hinweis: Aus Platzgründen enthält dieser Abschnitt nur die wichtigsten Allokationspunkte. Konsultieren Sie den vollständigen Online-Bericht für Bildungsdetails zu Renten, Inflation und Zinseszins.</i>'
    }
    story.append(Paragraph(nota_fase3.get(lang, nota_fase3['it']), normal_style))
    story.append(Spacer(1, 0.3*cm))
    
    # Estrai solo le parti chiave (disponibilità e allocazione)
    fase3_key_lines = _extract_fase3_key_info(report_fase3_text, lang)
    for line in fase3_key_lines:
        story.append(Paragraph(line, normal_style))
        story.append(Spacer(1, 0.2*cm))
    
    story.append(PageBreak())
    
    # ========================================================================
    # DISCLAIMER FINALE
    # ========================================================================
    disclaimer_titolo = {
        'it': 'Disclaimer Importante',
        'en': 'Important Disclaimer',
        'de': 'Wichtiger Haftungsausschluss'
    }
    story.append(Paragraph(disclaimer_titolo.get(lang, disclaimer_titolo['it']), subtitle_style))
    
    disclaimers = {
        'it': [
            '<b>Natura Educativa:</b> Questa applicazione fornisce indicazioni educative generali sulla pianificazione finanziaria e non costituisce consulenza finanziaria personalizzata.',
            '<b>Limitazioni:</b> Non siamo consulenti finanziari certificati, non vendiamo prodotti finanziari, non riceviamo commissioni, non garantiamo rendimenti, non salviamo i tuoi dati.',
            '<b>Cosa Fare:</b> Usa questa guida come punto di partenza, studia autonomamente, confronta sempre costi e performance, consulta un consulente indipendente per decisioni importanti.',
            '<b>Responsabilità:</b> Tu sei l\'unico responsabile delle tue decisioni di investimento. Gli investimenti comportano rischi, inclusa la perdita totale del capitale investito.'
        ],
        'en': [
            '<b>Educational Nature:</b> This application provides general educational guidance on financial planning and does not constitute personalized financial advice.',
            '<b>Limitations:</b> We are not certified financial advisors, we do not sell financial products, we do not receive commissions, we do not guarantee returns, we do not save your data.',
            '<b>What to Do:</b> Use this guide as a starting point, study independently, always compare costs and performance, consult an independent advisor for important decisions.',
            '<b>Responsibility:</b> You are solely responsible for your investment decisions. Investments involve risks, including total loss of invested capital.'
        ],
        'de': [
            '<b>Bildungscharakter:</b> Diese Anwendung bietet allgemeine Bildungsanleitung zur Finanzplanung und stellt keine personalisierte Finanzberatung dar.',
            '<b>Einschränkungen:</b> Wir sind keine zertifizierten Finanzberater, wir verkaufen keine Finanzprodukte, wir erhalten keine Provisionen, wir garantieren keine Renditen, wir speichern Ihre Daten nicht.',
            '<b>Was zu tun ist:</b> Verwenden Sie diesen Leitfaden als Ausgangspunkt, studieren Sie eigenständig, vergleichen Sie immer Kosten und Performance, konsultieren Sie einen unabhängigen Berater für wichtige Entscheidungen.',
            '<b>Verantwortung:</b> Sie sind allein verantwortlich für Ihre Investitionsentscheidungen. Investitionen beinhalten Risiken, einschließlich des Totalverlusts des investierten Kapitals.'
        ]
    }
    
    for disc in disclaimers.get(lang, disclaimers['it']):
        story.append(Paragraph(disc, normal_style))
        story.append(Spacer(1, 0.2*cm))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    return buffer


def _markdown_to_paragraphs(text, normal_style, warning_style, success_style):
    """Converte markdown semplice in lista di paragrafi."""
    paragraphs = []
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Salta header markdown (##, ###)
        if line.startswith('#'):
            continue
        
        # Salta separatori
        if line.startswith('---'):
            paragraphs.append(Spacer(1, 0.3*cm))
            continue
        
        # Converti bullet points
        if line.startswith('- '):
            line = '• ' + line[2:]
        
        # Converti bold markdown in HTML
        line = line.replace('**', '<b>').replace('**', '</b>')
        
        # Determina stile
        style = normal_style
        if '⚠️' in line or 'ATTENZIONE' in line or 'WARNING' in line:
            style = warning_style
        elif '✅' in line or 'Complimenti' in line or 'Congratulations' in line:
            style = success_style
        
        # Rimuovi emoji problematici per PDF
        line = _clean_emoji(line)
        
        try:
            paragraphs.append(Paragraph(line, style))
            paragraphs.append(Spacer(1, 0.1*cm))
        except:
            # Se il parsing fallisce, skippa la riga
            continue
    
    return paragraphs


def _extract_fase3_key_info(text, lang):
    """Estrae solo le informazioni chiave dalla Fase 3."""
    lines = []
    
    # Cerca la sezione disponibilità
    if 'Importo Mensile Investibile' in text or 'Monthly Investable Amount' in text or 'Monatlich investierbarer Betrag' in text:
        for line in text.split('\n'):
            if 'Importo Mensile Investibile' in line or 'Monthly Investable Amount' in line or 'Monatlich investierbarer Betrag' in line:
                lines.append('<b>' + line.strip().replace('**', '') + '</b>')
                break
    
    # Cerca allocazione portafoglio
    if 'Allocazione di Portafoglio' in text or 'Portfolio Allocation' in text or 'Portfolio-Allokation' in text:
        lines.append('<b>Allocazione Suggerita / Suggested Allocation / Vorgeschlagene Allokation:</b>')
        
        in_allocation = False
        for line in text.split('\n'):
            if 'Allocazione di Portafoglio' in line or 'Portfolio Allocation' in line or 'Portfolio-Allokation' in line:
                in_allocation = True
                continue
            if in_allocation and ('Azioni' in line or 'Stocks' in line or 'Aktien' in line or 
                                 'Obbligazioni' in line or 'Bonds' in line or 'Anleihen' in line or
                                 'Oro' in line or 'Gold' in line):
                clean_line = line.strip().replace('**', '').replace('- ', '• ')
                lines.append(clean_line)
            if in_allocation and line.strip().startswith('---'):
                break
    
    return lines


def _clean_emoji(text):
    """Rimuove emoji problematici per il PDF."""
    # Lista di emoji comuni che possono causare problemi
    emoji_map = {
        '💰': '[€]',
        '💵': '[€]',
        '💳': '[Card]',
        '🏦': '[Bank]',
        '📊': '[Chart]',
        '🎯': '[Target]',
        '📈': '[Growth]',
        '📉': '[Down]',
        '⚠️': '[!]',
        '✅': '[OK]',
        '❌': '[X]',
        '🛡️': '[Shield]',
        '🎓': '[Education]',
        '🔗': '[Link]',
        '💡': '[Idea]',
        '📚': '[Books]',
        '📺': '[Video]',
        '🌍': '',
        '🇮🇹': 'IT',
        '🇬🇧': 'EN',
        '🇩🇪': 'DE',
        '🚀': '[->]',
        '💎': '[Diamond]',
        '🧮': '[Calc]',
        '🛒': '[Shop]',
        '⏱️': '[Time]',
        '📄': '[Doc]',
        '🏠': '[Home]',
        '💼': '[Work]',
        '🥇': '[Gold]',
        '📋': '[List]'
    }
    
    for emoji, replacement in emoji_map.items():
        text = text.replace(emoji, replacement)
    
    return text
