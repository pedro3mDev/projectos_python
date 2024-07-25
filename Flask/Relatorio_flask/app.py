from flask import Flask, render_template, Response, make_response
import psycopg2, psycopg2.extras
from fpdf import FPDF
import conection.connect, pdf.script

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download/report/pdf')
def download_report():
    conn = None
    cursor = None
    try:
        conn = conection.connect.cria_connecao()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM teste")
        result = cursor.fetchall()
        return pdf.script.cria_pdf(result)         
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro: {error}")
        return make_response("Erro ao gerar relatório", 500)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run()




