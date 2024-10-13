import streamlit as st
import pandas as pd

st.title('Teste Técnico')
st.markdown("#### Analytics Engineer & Data Engineer  - Picpay")
st.markdown("#### Rafaela Cristina Polizel Aguiar")

tab0, tab1, tab2, tab3 = st.tabs(["Introdução", "De-Para", "Dashboard", "Detalhamento Técnico"])

# tab0 ---------------------------------------------------------
with tab0:
  st.markdown("### Introdução")
  st.markdown("Esta documentação apresenta a estrutura e as funcionalidades do projeto desenvolvido para os times de Modelagem de Crédito e Políticas de Crédito do PicPay, utilizando dados de remuneração de servidores, aposentados e pensionistas. Os dados brutos são obtidos através da API do SIAPE no Portal da Transparência. O projeto foi concebido para entregar uma base robusta, automatizada e pronta para consumo, facilitando o trabalho dos times envolvidos e otimizando a análise e a tomada de decisão baseada em dados.")

# tab1 ---------------------------------------------------------
with tab1:

  st.markdown("### Servidores")
  df_servidores = pd.read_csv('data/de_para_servidores.csv', sep=";")
  st.dataframe(df_servidores, 100000, hide_index=True)

  st.markdown("### Aposentados")
  df_aposentados = pd.read_csv('data/de_para_aposentados.csv', sep=";")
  st.dataframe(df_aposentados, 100000, hide_index=True)

  st.markdown("### Pensionistas")
  df_pensionistas = pd.read_csv('data/de_para_pensionistas.csv', sep=";")
  st.dataframe(df_pensionistas, 100000, hide_index=True)

  st.markdown("---")

  st.markdown("_* ÓRGÃO SUPERIOR - Unidade da Administração Direta que tenha entidades por ele supervisionadas._")