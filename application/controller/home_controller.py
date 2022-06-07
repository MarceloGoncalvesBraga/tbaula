from flask import Flask,render_template, request
from application import main
from application.model.dao.produto_dao import Produtos_Dao
from application.model.entity.produto import Produtos

@main.route("/")
def home():
    produtos = Produtos_Dao.Listar_Produtos()
    return render_template("index.html",
       produtos= produtos
    )

