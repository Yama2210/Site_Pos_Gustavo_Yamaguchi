import streamlit as st

nome = st.sidebar.text_input("Digite seu nome:")

if nome:
    st.session_state["nome"] = nome

# --- Páginas de navegação --- #
pg = st.navigation(
    [
        st.Page('./pages/Home.py'),
        st.Page('pages/Tabela.py'),
        st.Page('pages/Churn por Contrato.py'),
        st.Page('pages/Churn por Idade.py'),
        st.Page('pages/Churn por Valor Mensal.py'),
        st.Page('pages/Churn por Motivo de Cancelamento.py'),
        st.Page('pages/Ações para Redução de Churn.py'),
        st.Page('pages/Envio de Email.py'),
    ]
)

pg.run()