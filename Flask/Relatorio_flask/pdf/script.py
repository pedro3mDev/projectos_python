from fpdf import FPDF
from flask import Flask, render_template, Response, make_response

def cria_pdf(result):
    pdf = FPDF()
    pdf.add_page()
    page_width = pdf.w - 2 * pdf.l_margin
    pdf.set_font('arial', 'B', 14.0)
    pdf.cell(page_width, 0.0, 'RELATÓRIO ISMAEL', align='C')
    pdf.ln(10)
    pdf.set_font('arial', '', 12)
        
    col_width = page_width / 4
    th = pdf.font_size

    pdf.set_font('arial', '', 14)
    pdf.cell(page_width, 0.0, '-------------------------------------------------------------------------------------------------------------', align='Justify')
    pdf.ln(4)

    pdf.cell(col_width, th, 'ID', border=1)
    pdf.cell(col_width, th, 'Nome', border=1)
    pdf.ln(th)

    for i in range(0, len(result), 2):
        for j in range(2):  
            if i + j < len(result): 
                pdf.cell(col_width, th, str(result[i + j]['id']), border=1)
                pdf.cell(col_width, th, str(result[i + j]['nome']), border=1)
            pdf.ln(th)

    pdf.set_font('arial', '', 14)
    pdf.cell(page_width, 0.0, '------------------------------------------------------------------------------------------------------------', align='Justify')
    pdf.ln(10)
    pdf.set_font('arial', '', 12.0)
    pdf.cell(page_width, 0.0, '(19 / MAIO / 2024)', align='R')

    
    return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf',
                        headers={'Content-Disposition': 'attachment;filename=relatorio.pdf'})

