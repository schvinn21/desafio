from flask import Flask, request, render_template
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Classe de cadastro dos usúrios
class Cadastro:
    def __init__(self, nome, peso, altura, imc, status):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.imc = imc
        self.status = status

app = Flask(__name__)

# Configuração da API do Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'config/credentials.json'  # Credenciais que estão no arquivo JSON
SPREADSHEET_ID = '1MstAF_t1x7gHsuoPpQTjQjNmsgeyElorX1GRlo5FAo4'  # ID da planilha

# Autenticação da conta de serviço
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

# Página inicial com o formulário para cálculo do IMC
@app.route('/')
def index():
    return render_template('calculadora_imc.html', titulo='Calculadora de IMC')

# Função para calcular o IMC e salvar no Google Sheets
@app.route('/calcular', methods=['POST'])
def calcular():
    nome = request.form['nome']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    # Calcula o IMC
    imc = round(peso / (altura * altura), 2)

    # Determina o status baseado no IMC
    if imc < 18.5:
        status = 'Abaixo do peso'
    elif 18.5 < imc <= 24.9:
        status = 'Peso normal'
    elif 25 <= imc < 29.9:
        status = 'Sobrepeso'
    elif 30 <= imc < 39.9:
        status = 'Obesidade grau 1'
    else:
        status = 'Obesidade grau 2'

    # Envia os dados para o Google Sheets
    values = [[nome, peso, altura, imc, status]]
    body = {'values': values}
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range='Página1!A1',  # Intervalo da tabela do Google Sheets
        valueInputOption='RAW',
        body=body
    ).execute()

    return render_template('calculadora_imc.html', titulo='Calculadora de IMC', resultado={
        'nome': nome,
        'peso': peso,
        'altura': altura,
        'imc': imc,
        'status': status
    })

if __name__ == '__main__':
    app.run(debug=True)

