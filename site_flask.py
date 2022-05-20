from flask import Flask
app = Flask (__name__)

#criar a primeira pagina no ar 
# route(caminho) -> blablabla.com/alguma coisa
# função -> O que voce deseja exibir naquela pagina

@app.route("/")
def homepage() :
    return " Nossas Viagens "
#colocar o site no ar 
@app.route ('/contatos')
def contatos():
    return 'Nosso contatos são Email: xxxx@pmail.com'
if __name__ == "__main__":
    app.run(debug = True)
