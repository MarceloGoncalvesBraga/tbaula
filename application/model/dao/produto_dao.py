
from application.model.entity.produto import Produtos
#class Dao:
class Produtos_Dao:

    def Listar_Produtos():
        #Retorar uma lista de produtos!
        lista_produtos = [
            Produtos(1,nome="televisao",preco='1250',quantidade='150',imagem='p01.jpg',status=1),
            Produtos(1,nome="agua",preco='2',quantidade='3000',imagem='p02.jpg',status=1),

         ]

        return lista_produtos