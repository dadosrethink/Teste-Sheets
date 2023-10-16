from .lead import Lead
from .gsheets import Sheets

class Api():
    
    def __init__(self) -> None:
        self.planilha = Sheets(
            planilha_id='1rKIjFna5fHVpXyJ8i6J6CnYSnpFEYjExmrGnfw7hdZs',
            guia='leads'
        )

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
        id = str(len(self.planilha.values))
        return id
    
    def inserir(self, dados: list) -> dict:
        status = self.planilha.inserir_dado(dados)
        return status
    
    

        
