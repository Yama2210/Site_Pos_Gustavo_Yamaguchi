import streamlit as st

st.set_page_config(
    page_title='Projeto Python',
    page_icon=':fire:',
    layout='wide',
    initial_sidebar_state='collapsed'
)

st.title('Projeto Python Pós-Graduação Gustavo Yamaguchi')  # Essa seria como se fosse o H1 no HTML

st.header('Bem vindo!') # Esse seria o H3 do HTML

# --- Subcabeçalho --- #
# st.subheader('Projeto Python para análise de dados de uma empresa.')  # É como se fosse o H4 do HTML
st.subheader('', divider='rainbow')

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style="text-align: justify; line-height: 1.8; font-size: 16px;">
    Este projeto foi desenvolvido como parte da minha <b>pós-graduação em Gestão Estratégica de Dados</b>, 
    com o objetivo de aplicar, na prática, conceitos analíticos voltados à <b>geração de valor para o negócio</b>.<br><br>

    Sou um profissional em formação na área de dados, com interesse em transformar informações em 
    <b>insights estratégicos</b> que apoiem a tomada de decisão. Neste projeto, construí um site interativo 
    com múltiplas páginas dedicado à análise de <b>churn (cancelamento de clientes)</b>.<br><br>

    Através de uma abordagem orientada a dados, o projeto busca não apenas identificar padrões de cancelamento, 
    mas também propor interpretações e caminhos que possam contribuir para a <b>retenção de clientes</b>.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
        "https://itshow.com.br/wp-content/uploads/2023/08/dados-1-1024x576.webp",
        width=500  # controla o tamanho da imagem
    )

st.subheader('', divider='rainbow')

st.markdown("### 📌 O que será abordado?")

st.markdown("""
<div style="line-height: 1.8; font-size: 16px;">
<ul>
<li>Identificar os principais motivos de churn</li>
<li>Quantificar o número de clientes cancelados</li>
<li>Analisar padrões e comportamentos</li>
<li>Gerar insights acionáveis para retenção</li>
<li>Apresentar análises estratégicas para o negócio</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
---
Quer explorar mais?

👉 Navegue pelas análises no menu lateral para entender os fatores de churn em detalhes.
""")

