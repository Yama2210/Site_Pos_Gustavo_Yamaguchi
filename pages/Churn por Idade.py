import pandas as pd
import streamlit as st
import plotly.express as px

if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

df = pd.read_csv("Dados/telco.csv")

st.subheader("Churn por Idade")

df_idade = df.groupby('Age')['Churn Label'].value_counts(normalize=True).unstack() * 100

fig_idade = px.line(
    df_idade,
    y='Yes',
    title='Taxa de Churn por Idade (%)'
)

st.plotly_chart(fig_idade)

fig_idade.write_image("grafico_idade.png")

st.markdown("### 🧠 Insight referente ao gráfico")

st.markdown('''

A análise indica que a taxa de churn varia ao longo das faixas etárias, 
sugerindo que determinados grupos podem estar mais propensos ao cancelamento.

Isso pode indicar a necessidade de estratégias segmentadas, com abordagens 
específicas para diferentes perfis de clientes.''')
