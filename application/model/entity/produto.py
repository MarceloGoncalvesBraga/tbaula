class Produtos:
    
    def __init__(self, id, nome, preco, quantidade, imagem, status):
        self._id = id
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade
        self._imagem = imagem
        self._status = status

        
    def get_id(self):
        return self._id;

    def get_Nome(self):
        return self._nome

    def set_Nome(self,newnome):
        self._nome = newnome
        return

    def get_Preco(self):
        return self._preco

    def set_Preco(self,newpreco):
        self._preco = newpreco
        return

    def get_Quantidade(self):
         return self._quantidade
         
    def set_Quantidade(self,newquantidade):
        self._quantidade = newquantidade
        return

    def get_Imagem(self):
         return self._imagem
         
    def set_Imagem(self,newimagem):
        self._imagem = newimagem
        return

    def get_Status(self):
         return self._status
         
    def set_Status(self,newstatus):
        self._status = newstatus
        return
