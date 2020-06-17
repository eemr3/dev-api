from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Rafael',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id': '1',
        'nome': 'Emerson',
        'habilidades': ['HTML', 'CSS', 'Javascrip', 'ReactJs']

     }
]

# Devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            respose = desenvolvedores[id]

        except IndexError:
            mesagem = 'Desenvolvedor de ID {} não existe'.format(id)
            respose = {'status': 'erro', 'mensagem': mesagem}
        except Exception:
            mesagem = 'Erro desconhecido. Procure o administrador da API'
            respose = {'status': 'erro', 'mensagem': mesagem}
        return jsonify(respose)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído!'})

# Lista todos os desenvolvedores e permite registrar um desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
        if request.method == 'POST':
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados['id'] = posicao
            desenvolvedores.append(dados)
            return jsonify(desenvolvedores[posicao])
        elif request.method == 'GET':
            return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)