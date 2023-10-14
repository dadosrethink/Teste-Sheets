import streamlit as st
from backend import *


class Tela():
    
    
    def __init__(self) -> None:
        
        lead = Lead()
        
        st.title('Cadastro')        
        
        col1, col2 = st.columns(2)
        
        with col1:
            nome_ = st.text_input("Nome")
            cargo_ = st.text_input("Cargo")
            empresa_ = st.text_input("Empresa")
            
        with col2:
            sobrenome_ = st.text_input("Sobrenome")
            email_ = st.text_input("E-mail")
            telefone_ = st.text_input("Telefone")    
        
        if st.button("Registrar"):
            lead.nome = nome_
            lead.sobrenome = sobrenome_
            lead.cargo = cargo_
            lead.email = email_
            lead.empresa = empresa_
            lead.telefone = telefone_
            
            Api().registrar(lead=lead)
        
        