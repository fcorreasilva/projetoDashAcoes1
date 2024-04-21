from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import psycopg2

app = Flask(__name__)

# Obtenha as credenciais de conexão do ambiente
DATABASE_URL = os.environ['postgres://vjqkijusfokyku:6ae5592a61d4da0a84f24098190a04a0c7f5b6a04f474a42b27e5a0e5b7be675@ec2-52-54-200-216.compute-1.amazonaws.com:5432/d9dlbkttuqamvs']

# Conectando ao banco de dados
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()


# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para submeter o formulário
    @app.route("/submit", methods=["GET", "POST"])
    def submit():
     if request.method == "POST":
        ticker = request.form["ticker"]
        nome = request.form["nome"]

        # Inserir os dados no banco de dados
        sql = "INSERT INTO ativos (ticker, nome) VALUES (%s, %s)"
        val = (ticker, nome)
        cursor.execute(sql, val)
        conn.commit()

        return redirect("/")

    # Caso a solicitação não seja POST, você pode lidar com isso aqui se necessário
    return "Method Not Allowed", 405


if __name__ == "__main__":
    app.run(debug=True)