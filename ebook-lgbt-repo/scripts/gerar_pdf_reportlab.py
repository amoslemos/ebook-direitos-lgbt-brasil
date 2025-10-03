from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm
import os

ASSETS = "assets"
OUTPUT = "ebook_direitos_lgbt_brasil.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCenter', fontSize=24, alignment=TA_CENTER, spaceAfter=20, textColor=colors.HexColor('#6A1B9A')))
styles.add(ParagraphStyle(name='SubHeading', fontSize=14, spaceAfter=6, textColor=colors.HexColor('#00897B')))
styles.add(ParagraphStyle(name='ChapterTitle', fontSize=18, spaceAfter=10, textColor=colors.HexColor('#3949AB')))
styles.add(ParagraphStyle(name='BodyCustom', fontSize=11, alignment=TA_JUSTIFY, spaceAfter=8, leading=15))
styles.add(ParagraphStyle(name='Testimonial', fontSize=11, backColor=colors.HexColor('#F3E5F5'), borderPadding=8, spaceAfter=10, leftIndent=6, rightIndent=6))


def footer(canvas, doc):
    from reportlab.lib.pagesizes import A4
    canvas.saveState()
    w, h = A4
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.grey)
    canvas.drawString(w/2 - 20, 1.5*cm, f"{doc.page}")
    canvas.restoreState()


def img(path, width=None, height=None):
    full = os.path.join(ASSETS, path)
    if not os.path.exists(full):
        return Spacer(0, 0)
    if width and height:
        return Image(full, width=width, height=height)
    return Image(full, width=16*cm, height=9*cm)


def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)
    flow = []

    flow.append(img('capa.png', width=17*cm, height=25*cm))
    flow.append(PageBreak())
    flow.append(img('contracapa.png', width=17*cm, height=25*cm))
    flow.append(PageBreak())

    flow.append(Paragraph('Sumário', styles['TitleCenter']))
    toc = [
        'Capítulo 1 – Conceitos Básicos',
        'Capítulo 2 – Direitos Civis e Sociais Garantidos por Lei',
        'Capítulo 3 – História do Movimento LGBT no Brasil',
        'Capítulo 4 – Cidadania e Participação Política',
        'Capítulo 5 – Combate à Discriminação e Promoção da Inclusão',
        'Capítulo 6 – Recursos Úteis',
        'Vozes que Inspiram'
    ]
    for i, t in enumerate(toc, start=1):
        flow.append(Paragraph(f"{i}. {t}", styles['BodyCustom']))
    flow.append(PageBreak())

    # Capítulos (texto resumido)
    flow.append(Paragraph('Capítulo 1 – Conceitos Básicos', styles['ChapterTitle']))
    flow.append(Paragraph('Identidade de gênero e orientação sexual; diferenças e respeito à diversidade.', styles['BodyCustom']))
    flow.append(img('infografico_espectro.png'))
    flow.append(Paragraph('“Entender quem você é não é um erro, é um ato de coragem.” — Lia, 19', styles['Testimonial']))
    flow.append(PageBreak())

    flow.append(Paragraph('Capítulo 2 – Direitos Civis e Sociais Garantidos por Lei', styles['ChapterTitle']))
    flow.append(Paragraph('Constituição (arts. 3º e 5º). STF (2011, 2018, 2019) e CNJ (2013).', styles['BodyCustom']))
    flow.append(img('infografico_linha_do_tempo.png'))
    flow.append(Paragraph('“Quando assinei minha certidão de casamento, senti reconhecimento.” — Rafael, 27', styles['Testimonial']))
    flow.append(PageBreak())

    flow.append(Paragraph('Capítulo 3 – História do Movimento LGBT no Brasil', styles['ChapterTitle']))
    flow.append(Paragraph('Das décadas de 1970 a 2010+: organização, políticas e marcos jurídicos.', styles['BodyCustom']))
    flow.append(Paragraph('“Cada marcha é um grito de resistência e esperança.” — João, 32', styles['Testimonial']))
    flow.append(PageBreak())

    flow.append(Paragraph('Capítulo 4 – Cidadania e Participação Política', styles['ChapterTitle']))
    flow.append(Paragraph('Representatividade, conselhos, ONGs e engajamento juvenil.', styles['BodyCustom']))
    flow.append(Paragraph('“Participar é ocupar espaços que sempre foram nossos por direito.” — Camila, 24', styles['Testimonial']))
    flow.append(PageBreak())

    flow.append(Paragraph('Capítulo 5 – Combate à Discriminação e Promoção da Inclusão', styles['ChapterTitle']))
    flow.append(Paragraph('LGBTfobia é crime; como denunciar e promover ambientes inclusivos.', styles['BodyCustom']))
    flow.append(img('infografico_denuncia.png'))
    flow.append(Paragraph('“Denunciar não é vingança.” — Bruno, 21', styles['Testimonial']))
    flow.append(PageBreak())

    flow.append(Paragraph('Capítulo 6 – Recursos Úteis', styles['ChapterTitle']))
    flow.append(Paragraph('ABGLT, Casa 1, Casa Florescer, Aliança Nacional LGBTI+; Disque 100; MDHC; STF.', styles['BodyCustom']))

    doc.build(flow, onFirstPage=footer, onLaterPages=footer)

if __name__ == '__main__':
    build()
