import pandas as pd
import streamlit as st
import plotly.express as px

# --- Saudação --- #
if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

# --- Carregar dados --- #
df = pd.read_csv("Dados/telco.csv")

# --- Título --- #
st.subheader("📊 Churn por Idade")

# --- Tratamento --- #
df_idade = df.groupby('Age')['Churn Label'].value_counts(normalize=True).unstack() * 100

# --- Gráfico --- #
fig_idade = px.line(
    df_idade,
    y='Yes',
    title='Taxa de Churn por Idade (%)'
)

st.plotly_chart(fig_idade, use_container_width=True)

# --- Insight --- #
st.markdown("### 🧠 Insight referente ao gráfico")

st.markdown("""
A análise indica que a taxa de churn varia ao longo das faixas etárias, sugerindo que determinados grupos podem estar mais propensos ao cancelamento.

Isso reforça a necessidade de estratégias segmentadas, com abordagens específicas para diferentes perfis de clientes, visando aumentar a retenção.
""")
