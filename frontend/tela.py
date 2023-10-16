import streamlit as st
from backend import *
import re


def validate_email(email):
    # Expressão regular para validar um endereço de email
    pattern = r'^[\w\.-]+@[\w\.-]+.[\w\.-]$'
    if re.match(pattern, email):
        return True
    else:
        return False


class Tela():
    
    
    def __init__(self) -> None:
        
        st.title('Crie OKRs com IA')        
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            nome_ = st.text_input(
                "Nome", 
                max_chars=30, 
                placeholder='Seu nome aqui',
                help='Informe seu Nome e Sobrenome')
            
            cargo_ = st.selectbox(
                label='Posição',
                help='Informe o status do seu cargo na empresa',
                options=[
                    'Diretor','Head','Supervisor',
                    'Gerente','Analista','Estagiário'
                    ]
                )
                
        with col2:
            email_ = st.text_input(
                "E-mail",
                max_chars=30,
                placeholder='Seu melhor e-mail')
            empresa_ = st.text_input(
                "Empresa",
                max_chars=30,
                placeholder='Nome da empresa que você trabalha')
        
        
        if st.checkbox("Seguir"):
            
            if validate_email(email=email_):
                if len(nome_) >= 3 and len(empresa_) >= 3:
                
                    solicitacao_ = st.text_input("Fale um pouco sobre o OKR que deseja gerar")
                    
                    if st.button("Gerar OKR"):
                        
                        lead = Lead(
                            nome=nome_,
                            cargo=cargo_,
                            email=email_,
                            empresa=empresa_,
                            solicitacao= solicitacao_,
                            resposta= 'Teste'
                        )
                        
                        Api().registrar(lead=lead)
                        st.success("Seu OKR aqui...")
                else:
                    st.warning('Alguns dados estão inválidos, tente novamente!')
            else:
                st.warning('E-mail inválido tente novamente!')
        
        