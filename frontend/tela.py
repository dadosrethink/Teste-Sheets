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


def validate_phone_number(phone_number):
    # Expressão regular para validar números de celular
    pattern = r'^\([1-9]{2}\) (?:[2-8]|9[0-9])[0-9]{3}\-[0-9]{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False


class Tela():
    
    
    def __init__(self) -> None:
        
        lead = Lead()
        
        st.title('Cadastro')        
        
        col1, col2 = st.columns(2)
        
        with col1:
            nome_ = st.text_input("Nome")
            cargo_ = st.selectbox(label='Posição',
                                  options=['Diretor','Head','Supervisor','Gerente','Analista','Estagiário'])
            empresa_ = st.text_input("Empresa")
            
        with col2:
            email_ = st.text_input("E-mail")
            telefone_ = st.text_input("Telefone")    
        
        if st.button("Registrar"):
            
            if validate_email(email=email_):
                if validate_phone_number(telefone_):           
                    lead.nome = nome_
                    lead.sobrenome = None
                    lead.cargo = cargo_
                    lead.email = email_
                    lead.empresa = empresa_
                    lead.telefone = telefone_
                    
                    Api().registrar(lead=lead)
                    
                    st.success("OK")
                else:
                    st.warning('Telefone Inválido')
            else:
                st.warning('E-mail inválido tente novamente!')
        
        