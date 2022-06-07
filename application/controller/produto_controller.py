from flask import render_template
from application import main
from application.model.dao.produto_dao import Produtos_Dao
from application.model.entity.produto import Produtos
from flask import Flask, render_template, url_for, request, jsonify, json
import re 



@main.route("/exibir_produto/<int:id>")
def ExibirProduto(id):
    lista_produtos = Produtos_Dao.Listar_Produtos()

    for produto in lista_produtos:

        if produto.get_id() == id:
            return render_template("produto.html",
                produto=produto,
                 )
    return render_template("home.html", produtos=lista_produtos)

@main.route("/produto_atualizar/<int:id>")
def ProdutoAtualizar(id):
    lista_produtos = Produtos_Dao.Listar_Produtos()
    for produto in lista_produtos:
        if produto.get_id() == id:
            return render_template("produto-atualizar.html",
                produto=produto,
                )
    return render_template("home.html", produtos=lista_produtos)

@main.route("/produto_alterar/<int:id>")
def AlterarProduto(id): 
    if request.method == "POST":   
        lista_produtos = Produtos_Dao.Listar_Produtos()
        for produto in lista_produtos:
            id = request.form.get('id_produto')
            if produto.get_id() == id:
                nome = request.form.get('imagem')
                preco = request.form.get('preco')
                quantidade = request.form.get('quantidade')
                status = request.form.get('status')
                imagem = request.form.get('imagem')
                
                produto.set_Nome(nome)
                produto.set_Preco(preco)
                produto.set_Quantidade(quantidade)
                produto.set_Imagem(imagem)
    print("Ok")

def InserirNovoProduto(id):    
  lista_produtos = Produtos_Dao.Listar_Produtos()      
  if request.method == "POST":
      id_produto = request.form.get('id_produto')
      nome = request.form.get('imagem')
      preco = request.form.get('preco')
      quantidade = request.form.get('quantidade')
      status = request.form.get('status')
      imagem = request.form.get('imagem')
      lista_produtos.append((Produtos(id=id_produto,nome=nome,preco=preco,quantidade=quantidade,imagem=imagem,status=status),
))