import streamlit as st

if "nome" in st.session_state:
    st.write(f"Olá, {st.session_state['nome']}, seja bem-vindo!")

st.title("📉 Estratégias para Redução de Churn")

st.markdown("""
Com base nas análises realizadas ao longo do projeto, foram identificados padrões relevantes 
que ajudam a entender o comportamento dos clientes que cancelam os serviços.

A seguir, são apresentadas ações estratégicas que podem ser adotadas pela empresa para reduzir o churn.
""")

st.subheader("💳 1. Incentivar contratos de longo prazo")

st.markdown("""
Clientes com contratos mensais apresentam maior taxa de cancelamento.  

👉 **Ação recomendada:**
- Oferecer descontos para planos anuais  
- Criar benefícios exclusivos para contratos longos  
- Implementar programas de fidelidade  
""")

st.markdown("---")

st.subheader("👶 2. Melhorar retenção nos primeiros meses")

st.markdown("""
Clientes com pouco tempo de uso possuem maior probabilidade de churn.  

👉 **Ação recomendada:**
- Criar onboarding mais eficiente  
- Acompanhar novos clientes nos primeiros meses  
- Oferecer suporte proativo  
""")

st.markdown("---")

st.subheader("💰 3. Revisar estratégia de preços")

st.markdown("""
Faixas de valor mais altas podem estar associadas a maior churn.  

👉 **Ação recomendada:**
- Ajustar preços em planos mais caros  
- Criar planos intermediários  
- Aumentar percepção de valor (benefícios adicionais)  
""")

st.markdown("---")

st.subheader("🛠️ 4. Melhorar qualidade do serviço")

st.markdown("""
Motivos de cancelamento indicam problemas relacionados à qualidade e experiência do cliente.  

👉 **Ação recomendada:**
- Investir em estabilidade do serviço  
- Melhorar atendimento ao cliente  
- Monitorar falhas recorrentes  
""")

st.markdown("---")

st.subheader("📦 5. Incentivar uso de mais serviços")

st.markdown("""
Clientes com mais serviços tendem a cancelar menos.  

👉 **Ação recomendada:**
- Oferecer bundles (combos de serviços)  
- Criar ofertas personalizadas  
- Incentivar upgrades de plano  
""")

st.markdown("---")

st.subheader("🏁 6. Monitorar clientes de risco")

st.markdown("""
É possível identificar perfis com maior probabilidade de churn.  

👉 **Ação recomendada:**
- Criar modelos de previsão de churn  
- Ações preventivas para clientes em risco  
- Campanhas de retenção direcionadas  
""")

st.markdown("""
---

### 🧠 Conclusão

O churn está diretamente relacionado a fatores como **tipo de contrato, tempo de uso, preço e experiência do cliente**.

A adoção de estratégias orientadas a dados permite não apenas reduzir o cancelamento, mas também aumentar a retenção e o valor do cliente ao longo do tempo.
""")