# 📘 E-book – Direitos e Cidadania LGBT no Brasil (Guia para Jovens)

Um guia educativo, inclusivo e didático sobre **direitos, cidadania e participação** da população LGBT no Brasil. Este repositório reúne **briefings/prompts**, **ativos visuais (capa, contra-capa, infográficos)**, **conteúdo textual** e **scripts** para gerar o PDF diagramado.

> **Objetivo**: informar e inspirar jovens a conhecerem seus direitos, combater a discriminação e exercerem cidadania ativa.

---

## 🔖 Sumário do Repositório

- [Visão Geral](#-visão-geral)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Prompts & Briefings Utilizados](#-prompts--briefings-utilizados)
- [Como Reproduzir os Ativos Visuais](#-como-reproduzir-os-ativos-visuais)
- [Gerar o PDF com Design Avançado (ReportLab)](#-gerar-o-pdf-com-design-avançado-reportlab)
- [Conteúdo do E-book (Texto Base)](#-conteúdo-do-e-book-texto-base)
- [Licença e Uso](#-licença-e-uso)
- [Como Contribuir](#-como-contribuir)
- [Referências e Leis Citadas](#-referências-e-leis-citadas)

---

## 🧭 Visão Geral

Este projeto foi construído para:
- Explicar **conceitos básicos** de identidade de gênero e orientação sexual.
- Apresentar **direitos civis e sociais** e **marcos legais** no Brasil.
- Contextualizar **história, avanços e desafios** do movimento LGBT.
- Incentivar a **participação política** e a **cidadania**.
- Ensinar **como denunciar discriminação** e acessar **redes de apoio**.

Formato final: **PDF** diagramado, com **capa, contra-capa, sumário, capítulos, depoimentos inspiradores e infográficos**.

---

## 📁 Estrutura do Repositório

```text
.
├─ README.md
├─ LICENSE               # Código (MIT)
├─ CONTENT_LICENSE       # Texto (CC BY 4.0)
├─ .gitignore
├─ content/
│  ├─ ebook_conteudo.md
│  └─ depoimentos.md
├─ prompts/
│  ├─ 01_briefing_projeto_inicial.md
│  ├─ 02_briefing_capa.md
│  ├─ 03_briefing_infografico_1_espectro.md
│  ├─ 04_briefing_infografico_2_linha_do_tempo.md
│  ├─ 05_briefing_infografico_3_denuncia.md
│  ├─ 06_briefing_contracapa.md
│  ├─ 07_prompt_depoimentos.md
│  └─ 08_prompt_pdf_design_avancado_reportlab.md
├─ assets/
│  ├─ capa.png
│  ├─ contracapa.png
│  ├─ infografico_espectro.png
│  ├─ infografico_linha_do_tempo.png
│  └─ infografico_denuncia.png
└─ scripts/
   ├─ gerar_pdf_reportlab.py
   └─ gerar_slides_pptx.py
```

> **PowerPoint**: use slides **16:9** → **33,87 cm × 19,05 cm** para que a capa se ajuste perfeitamente.

---

## 💬 Prompts & Briefings Utilizados

Os briefings detalhados estão em `/prompts`. Use-os como prompts em qualquer gerador de imagem (Designer, Midjourney, etc.).

---

## 🖼️ Como Reproduzir os Ativos Visuais

1. Use a ferramenta de sua preferência e cole o briefing correspondente.
2. Exporte em PNG.
3. Salve em `assets/` com os nomes sugeridos.

Dimensões recomendadas:
- **Capa/Contra-capa**: 2480 × 3508 px (A4 vertical).
- **Infográficos**: 3508 × 2480 px (A4 horizontal).

---

## 🛠️ Gerar o PDF com Design Avançado (ReportLab)

### Requisitos

```bash
pip install reportlab
```

### Executar

```bash
python scripts/gerar_pdf_reportlab.py
```

Saída: `ebook_direitos_lgbt_brasil.pdf`.

> Alternativa: gere uma apresentação **.pptx** com `python-pptx` via `scripts/gerar_slides_pptx.py`.

---

## ✍️ Conteúdo do E-book (Texto Base)

O conteúdo completo está em `content/ebook_conteudo.md` e os depoimentos em `content/depoimentos.md`.

---

## 📜 Licença e Uso

- **Código**: MIT (LICENSE)
- **Texto/Conteúdo**: CC BY 4.0 (CONTENT_LICENSE)

---

## 🤝 Como Contribuir

1. Fork → branch → PR.
2. Commits descritivos.
3. Revise linguagem inclusiva, referências e acessibilidade.

---

## 📚 Referências e Leis Citadas

- STF – Caderno: Direitos das Pessoas LGBTQIA+ (marcos e julgados)
- CNJ Resolução nº 175/2013 – casamento civil igualitário
- ADPF 132 / ADI 4277 (2011); ADI 4275 (2018); ADO 26 e MI 4733 (2019)
- Ministério dos Direitos Humanos – Secretaria LGBTQIA+

> Consulte o `content/ebook_conteudo.md` para links e detalhes.
