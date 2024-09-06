from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if 'erro' not in dados:
            return dados
        else:
            return None
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o CEP
@app.route('/processar', methods=['POST'])
def processar_cep():
    cep = request.form['cep']
    dados_cep = consultar_cep(cep)
    if dados_cep:
        lista_cep = list(cep)
        return render_template('resultado.html', dados_cep=dados_cep, lista_cep=lista_cep)
    else:
        return render_template('erro.html', cep=cep)


if __name__ == '__main__':
    app.run(debug=True)