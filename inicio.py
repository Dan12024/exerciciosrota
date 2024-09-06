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

@app.route('/romulo')
def mostrar():
    return ("romulo e o professor")

@app.route('/walter')
def ver_mensagem():
    return "e top "

@app.route ('/suzi')
def mostrar_nome():
    return "su legal"

@app.route ("/gustavo")
def ver_o_nome ():
    return "gugu"

@app.route('/daniel')
def mostrar_2():
     return render_template("daniel.html")

@app.route ("/robson")
def mostrar_3():
    return "robson robson"

@app.route ("/raposo")
def mostar_4 ():
    return render_template("raposo.html")
    

@app.route ("/gustavo")
def mostar_5 ():
    return render_template("gustavo.html")


@app.route ("/robson")
def mostar_6 ():
    return render_template("robson.html")


@app.route ("/suzane")
def mostar_7 ():
    return render_template("suzane.html")


@app.route ("/vivi")
def mostar_8 ():
    return render_template("vivi.html")






# executando um objeto flask com debug ativado (hot reload)
app.run(debug=True)