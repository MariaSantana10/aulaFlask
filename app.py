from flask import Flask

app = Flask(__name__) #app é o primeiro objeto a ser executado __name__ é o nome do arquivo do programa que ta sendo executado

@app.route ('/') #define a rota
def inicial():
    return '<h1>Olá, Mundo!</h1>'

@app.route('/<idioma>')
def olaMundo(idioma):
    if idioma == 'portugues':
        mensagem = 'Olá, Mundo!'
    elif idioma == 'ingles':
        mensagem = 'Hello, Word!'
    else:
        mensagem = 'Não tenho conhecimento!'
    return f'<h1>{mensagem}</h1>'