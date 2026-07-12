import streamlit as st
import pandas as pd

if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

st.set_page_config(
    page_title='Tabela do Projeto',
    page_icon=':robot_face:',
    layout='wide'
)

# --- Título --- #
st.title('📊 Base de Dados')
st.subheader('Dados utilizados para análise de Churn')

df = pd.read_csv('Dados/telco.csv')

st.markdown("### 📋 Visualização dos dados")
st.dataframe(df, use_container_width=True)

# --- Informações --- #
st.markdown("### Informações gerais da Tabela")

col1, col2, col3 = st.columns(3)

col1.metric("Linhas", df.shape[0])
col2.metric("Colunas", df.shape[1])
col3.metric("Valores nulos", df.isnull().sum().sum())