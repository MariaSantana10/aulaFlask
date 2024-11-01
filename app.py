from flask import Flask
from flask import render_template

app = Flask(__name__) #app é o primeiro objeto a ser executado __name__ é o nome do arquivo do programa que ta sendo executado

@app.route ('/') #define a rota
def inicial():
    return render_template('inicial.html', mensagem='Olá, Mundo!')

@app.route('/<idioma>')
def olaMundo(idioma):
    if idioma == 'portugues':
        mens = 'Olá, Mundo!'
    elif idioma == 'ingles':
        mens = 'Hello, Word!'
    else:
        mens = 'Não tenho conhecimento!'
    return render_template('inicial.html', mensagem=mens, idiomaHTML=idioma)