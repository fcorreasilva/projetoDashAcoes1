from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco_de_dados"
)

cursor = db.cursor()

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para submeter o formulário
@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        ticker = request.form["ticker"]
        nome = request.form["nome"]

        # Inserir os dados no banco de dados
        sql = "INSERT INTO ativos (ticker, nome) VALUES (%s, %s)"
        val = (ticker, nome)
        cursor.execute(sql, val)
        db.commit()

        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
