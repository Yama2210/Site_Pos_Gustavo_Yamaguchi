import pandas as pd
import streamlit as st
import plotly.express as px

# --- Saudação --- #
if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

# --- Carregar dados --- #
df = pd.read_csv("Dados/telco.csv")

# --- Título --- #
st.title("💰 Churn por Valor Mensal")

# --- Tratamento --- #
df['Faixa de Valor'] = pd.cut(df['Monthly Charge'], bins=5).astype(str)

df_valor = (
    df.groupby('Faixa de Valor')['Churn Label']
    .value_counts(normalize=True)
    .unstack() * 100
).reset_index()

# --- Gráfico --- #
fig_valor = px.line(
    df_valor,
    x='Faixa de Valor',
    y='Yes',
    markers=True,
    title='Taxa de Churn por Faixa de Valor Mensal (%)'
)

st.plotly_chart(fig_valor, use_container_width=True)

# --- Insight --- #
st.markdown("""
### 🧠 Insight

Observa-se que a taxa de churn varia conforme o valor mensal cobrado, indicando possível **sensibilidade ao preço**.

Clientes em faixas de valor mais elevadas tendem a apresentar maior probabilidade de cancelamento, 
o que pode estar relacionado à percepção de custo-benefício ou à oferta de alternativas mais competitivas no mercado.
""")