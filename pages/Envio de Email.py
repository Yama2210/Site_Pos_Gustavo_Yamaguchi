import streamlit as st
import smtplib
from email.message import EmailMessage
import pandas as pd
import matplotlib.pyplot as plt
import io

# --- Saudação --- #
if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

st.title("📧 Envio de Email")

# --- Carregar dados --- #
df = pd.read_csv("Dados/telco.csv")

# --- Escolha --- #
opcao = st.radio("O que deseja enviar?", ["Relatório", "Gráfico"])

email_destino = st.text_input("Digite o email:")

grafico_escolhido = None

if opcao == "Gráfico":
    grafico_escolhido = st.selectbox(
        "Escolha o gráfico:",
        [
            "Churn por Idade",
            "Churn por Contrato",
            "Churn por Valor Mensal",
            "Motivos de Cancelamento"
        ]
    )

# --- Relatório --- #
relatorio = """
RELATÓRIO DE ANÁLISE DE CHURN

Com base nas análises realizadas ao longo do projeto, foram identificados padrões relevantes que ajudam a compreender o comportamento dos clientes que cancelam os serviços.

A seguir, são apresentadas recomendações estratégicas com base nos dados analisados:

1. Incentivar contratos de longo prazo
Clientes com contratos mensais apresentam maior taxa de cancelamento.
Ações recomendadas:
- Oferecer descontos para planos anuais
- Criar benefícios exclusivos para contratos de longa duração
- Implementar programas de fidelidade

2. Melhorar retenção nos primeiros meses
Clientes com pouco tempo de uso possuem maior probabilidade de churn.
Ações recomendadas:
- Criar um processo de onboarding mais eficiente
- Acompanhar novos clientes nos primeiros meses
- Oferecer suporte proativo

3. Revisar estratégia de preços
Faixas de valor mais elevadas podem estar associadas a maior churn.
Ações recomendadas:
- Ajustar preços em planos mais caros
- Criar planos intermediários mais atrativos
- Aumentar a percepção de valor com benefícios adicionais

4. Melhorar qualidade do serviço
Os motivos de cancelamento indicam problemas relacionados à experiência do cliente.
Ações recomendadas:
- Investir na estabilidade do serviço
- Melhorar o atendimento ao cliente
- Monitorar falhas recorrentes

5. Incentivar o uso de mais serviços
Clientes que utilizam mais serviços tendem a cancelar menos.
Ações recomendadas:
- Oferecer pacotes combinados (bundles)
- Criar ofertas personalizadas
- Incentivar upgrades de plano

6. Monitorar clientes com risco de cancelamento
É possível identificar perfis com maior probabilidade de churn.
Ações recomendadas:
- Criar modelos preditivos de churn
- Realizar ações preventivas
- Desenvolver campanhas de retenção direcionadas

Conclusão

O churn está diretamente relacionado a fatores como tipo de contrato, tempo de uso, preço e experiência do cliente.

A adoção de estratégias orientadas a dados permite não apenas reduzir o cancelamento, mas também aumentar a retenção e o valor do cliente ao longo do tempo.

Atenciosamente,
Gustavo Yamaguchi
"""


# --- FUNÇÃO PARA GERAR IMAGEM --- #
def gerar_grafico(grafico):
    fig, ax = plt.subplots()

    if grafico == "Churn por Contrato":
        dados = df.groupby('Contract')['Churn Label'].value_counts().unstack()
        dados.plot(kind='bar', ax=ax)

    elif grafico == "Churn por Idade":
        dados = df.groupby('Age')['Churn Label'].value_counts().unstack()
        dados['Yes'].plot(ax=ax)

    elif grafico == "Churn por Valor Mensal":
        df_valor = df.copy()
        df_valor['Faixa'] = pd.cut(df_valor['Monthly Charge'], bins=10)
        dados = df_valor.groupby('Faixa')['Churn Label'].value_counts().unstack()
        dados['Yes'].plot(ax=ax)

    elif grafico == "Motivos de Cancelamento":
        dados = df['Churn Reason'].value_counts().head(10)
        dados.plot(kind='bar', ax=ax)

    ax.set_title(grafico)
    ax.set_ylabel("Valores")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)

    return buffer

# --- BOTÃO --- #
if st.button("Enviar"):

    if not email_destino:
        st.warning("Digite um email válido.")

    else:
        try:
            email_user = st.secrets["email"]["user"]
            email_pass = st.secrets["email"]["password"]

            msg = EmailMessage()
            msg["Subject"] = "Relatório de Churn"
            msg["From"] = email_user
            msg["To"] = email_destino

            if opcao == "Relatório":
                msg.set_content(relatorio)

            else:
                buffer = gerar_grafico(grafico_escolhido)

                msg.set_content(f"""
Segue o gráfico: {grafico_escolhido}

Atenciosamente,
Projeto de Dados
""")

                msg.add_attachment(
                    buffer.getvalue(),
                    maintype="image",
                    subtype="png",
                    filename="grafico.png"
                )

            # --- envio --- #
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email_user, email_pass)
                smtp.send_message(msg)

            st.success("Email enviado com sucesso!")

        except Exception as e:
            st.error(f"Erro: {e}")