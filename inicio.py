# https://dontpad.com/cursoflask



"""
Aula 1 - Entendendo Rotas

"""
# importando o flask
from flask import Flask,render_template

# criando um objeto flask
app = Flask(__name__)

#criando uma rota

@app.route('/')
def alo_flask():
    return render_template("cadastro.html")

# executando um objeto flask com debug ativado (hot reload)
app.run(debug=True)


