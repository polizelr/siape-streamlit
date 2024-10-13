import streamlit as st
import pandas as pd

st.title('Catálogo de Dados')


tab0, tab1 = st.tabs(["Tabelas", "Informações Técnicas"])


with tab0:

  st.markdown("## Servidor")

  st.markdown("**Descrição:** A tabela apresenta os dados detalhados dos servidores públicos em exercício, com informações sobre seus vínculos funcionais. Cada registro inclui dados sobre o cargo, a lotação, o regime de contratação, o tempo de serviço, entre outros atributos relevantes que caracterizam a relação de trabalho do servidor com o órgão público.")
  st.markdown("**Catálogo:** *picpay*")
  st.markdown("**Schema:** *public_informations*")
  st.markdown("**Tabela:** *servidor*")



  df_servidores = pd.read_csv('data/de_para_servidores.csv', sep=";")
  st.dataframe(df_servidores, 100000, hide_index=True)


  st.markdown("---")  
  st.markdown("## Aposentado")

  st.markdown("**Descrição:** A tabela contém informações detalhadas dos servidores públicos aposentados, incluindo dados sobre seus vínculos anteriores. Cada registro fornece informações sobre o cargo ocupado antes da aposentadoria, o tempo de serviço prestado, o regime de previdência e outras características relevantes.")
  st.markdown("**Catálogo:** *picpay*")
  st.markdown("**Schema:** *public_informations*")
  st.markdown("**Tabela:** *aposentado*")  
  
  
  df_aposentados = pd.read_csv('data/de_para_aposentados.csv', sep=";")
  st.dataframe(df_aposentados, 100000, hide_index=True)


  st.markdown("---")
  st.markdown("## Pensionista")

  
  st.markdown("**Descrição:** A tabela reúne dados detalhados sobre os pensionistas de servidores públicos, caracterizando seus vínculos com o regime de previdência. Cada registro inclui informações sobre o servidor falecido, o tipo de benefício concedido, as condições de elegibilidade, e outros dados pertinentes ao pensionista.")
  st.markdown("**Catálogo:** *picpay*")
  st.markdown("**Schema:** *public_informations*")
  st.markdown("**Tabela:** *pensionista*")
  
  
  df_pensionistas = pd.read_csv('data/de_para_pensionistas.csv', sep=";")
  st.dataframe(df_pensionistas, 100000, hide_index=True)

  st.markdown("---")

  st.markdown("## Remuneração")
  
  st.markdown("**Descrição:** A tabela apresenta informações detalhadas sobre a remuneração dos servidores públicos, incluindo ativos, aposentados e pensionistas. Cada registro contém dados sobre o valor do salário, adicionais, gratificações, e outras verbas recebidas, proporcionando uma visão abrangente da estrutura de remuneração no setor público")
  st.markdown("**Catálogo:** *picpay*")
  st.markdown("**Schema:** *public_informations*")
  st.markdown("**Tabela:** *remuneracao*")

  df_remuneracao = pd.read_csv('data/de_para_remuneracao.csv', sep=";")
  st.dataframe(df_remuneracao, 100000, hide_index=True)



 
with tab1:

  st.markdown("### Introdução")
  st.markdown("Esta documentação apresenta a estrutura e as funcionalidades do projeto desenvolvido para os times de Modelagem de Crédito e Políticas de Crédito do PicPay, utilizando dados de remuneração de servidores, aposentados e pensionistas. Os dados brutos são obtidos através da API do SIAPE no Portal da Transparência. O projeto foi concebido para entregar uma base robusta, automatizada e pronta para consumo, facilitando o trabalho dos times envolvidos e otimizando a análise e a tomada de decisão baseada em dados.")

# tab1 ---------------------------------------------------------