import pandas as pd
import streamlit as st
import plotly.express as px

# --- Saudação --- #
if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

# --- Carregar dados --- #
df = pd.read_csv("Dados/telco.csv")

# --- Título --- #
st.title("📊 Churn por Tipo de Contrato")

# --- Tratamento --- #
df_group = df.groupby(['Contract', 'Churn Label']).size().reset_index(name='Count')

# --- Gráfico --- #
fig_contrato = px.bar(
    df_group,
    x='Contract',
    y='Count',
    color='Churn Label',
    barmode='group',
    title='Churn por tipo de contrato'
)

st.plotly_chart(fig_contrato, use_container_width=True)

# --- Insight --- #
st.markdown("### 🧠 Insight referente ao gráfico")

st.markdown("""
Clientes com contrato mensal apresentam uma taxa de cancelamento significativamente maior em comparação aos contratos de longo prazo. Isso indica que a ausência de fidelização aumenta a probabilidade de churn.

Por outro lado, clientes com contratos de 1 ou 2 anos tendem a permanecer mais tempo, sugerindo que estratégias baseadas em fidelização e benefícios de longo prazo podem ser eficazes para reduzir o cancelamento.
""")