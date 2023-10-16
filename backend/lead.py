from datetime import datetime

class Lead:
    
    def __init__(
        self,
        nome: str,
        cargo: str,
        email: str,
        empresa: str,
        solicitacao: str,
        resposta: str,
        data: str = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
        ) -> None:
        """
        ## Classe para geração de objetos Lead.

        Args:
        nome (str): O nome do usuário.
        cargo (str): O cargo do usuário.
        email (str): O email do usuário.
        empresa (str): O nome da empresa do usuário.
        solicitacao (str): A requisição feita ao sistema.
        resposta (str): A resposta do sistema.
        data (str, optional): A data da captura do dado.
        
        ## Exemplo de uso:
        >>> user = Lead('user_test', 'analista', 'user@example.com', 'Rethink', 'Faça um OKR...', 'OKR...', '2023-10-16 10:22:34')
        >>> print(user.__dict__)
        {'nome': 'user_test', 'cargo': 'analista', 'email': 'user@example.com', 'empresa': 'Rethink', 'solicitacao': 'Faça um OKR...', 'resposta': 'OKR...', 'data': '2023-10-16 10:22:34'}
        """

        self.nome = nome
        self.cargo = cargo
        self.email = email
        self.empresa = empresa
        self.solicitacao = solicitacao
        self.resposta = resposta
        self.data = data
    
if __name__ == '__main__':
    user = Lead('user_test', 'analista', 'user@example.com', 'Rethink', 'Faça um OKR...', 'OKR...')
    t = user.__dict__.values()
    print(list(t))