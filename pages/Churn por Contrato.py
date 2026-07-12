import pandas as pd
import streamlit as st
import plotly.express as px

if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

df = pd.read_csv("Dados/telco.csv")

st.title("📊 Gráfico por Contrato")

df_group = df.groupby(['Contract', 'Churn Label']).size().reset_index(name='Count')

fig_contrato = px.bar(
    df_group,
    x='Contract',
    y='Count',
    color='Churn Label',
    barmode='group',
    title='Churn por tipo de contrato'
)

st.plotly_chart(fig_contrato)

fig_contrato.write_image("grafico_contrato.png")

st.markdown("### 🧠 Insight referente ao gráfico")

st.markdown('''
Clientes com contrato mensal apresentam uma taxa de cancelamento significativamente maior em comparação aos contratos de longo prazo. Isso indica que a ausência de fidelização aumenta a probabilidade de cancelamento.

Por outro lado, clientes com contratos de 1 ou 2 anos tendem a permanecer mais tempo, sugerindo que estratégias de retenção baseadas em planos mais longos podem ser eficazes para reduzir o cancelamento.''')