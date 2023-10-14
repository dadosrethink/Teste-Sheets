from .lead import Lead
from .gsheets import Sheets

class Api():
    
    def __init__(self) -> None:
        pass

    def desempacotar(self, lead: Lead) -> list:
        nova_linha = [
            lead.nome, lead.sobrenome, 
            lead.cargo, lead.email, 
            lead.empresa, lead.telefone
            ]
        return nova_linha
    
    def registrar(self, lead: Lead) -> dict:
        linha = self.desempacotar(lead)
        id = self.pegar_id()
        linha.insert(0,id)
        linha = [linha]
        status = self.inserir(linha)
        return status
        
    def pegar_id(self) -> str:
        id = str(len(Sheets().values))
        return id
    
    def inserir(self, dados: list) -> dict:
        status = Sheets().inserir_dado(dados)
        return status
    
    

        
