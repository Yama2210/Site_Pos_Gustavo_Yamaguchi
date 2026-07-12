import pandas as pd
import streamlit as st
import plotly.express as px

# --- Saudação --- #
if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

# --- Carregar dados --- #
df = pd.read_csv("Dados/telco.csv")

st.title("🚨 Motivos de Cancelamento (Churn)")

df_motivos = df.dropna(subset=['Churn Reason'])

motivos = df_motivos['Churn Reason'].value_counts().head(10).reset_index()
motivos.columns = ['Motivo', 'Quantidade']

# --- Gráfico --- #
fig_motivos = px.bar(
    motivos,
    x='Quantidade',
    y='Motivo',
    orientation='h',
    title='Top 10 Motivos de Cancelamento',
    text='Quantidade'
)

fig_motivos.update_layout(yaxis={'categoryorder':'total ascending'})

st.plotly_chart(fig_motivos, use_container_width=True)

fig_motivos.write_image("grafico_motivos.png")

# --- Insight --- #
st.markdown("""
### 🧠 Insight

Os principais motivos de cancelamento estão concentrados em fatores relacionados a **preço**, 
**concorrência** e **qualidade do serviço**.

Isso indica que o churn não ocorre de forma aleatória, mas está diretamente ligado à percepção de valor do cliente.
""")