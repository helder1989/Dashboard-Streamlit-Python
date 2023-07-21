
import streamlit as st
import pandas as pd # leittura de arquivos csv

# Definindo o título da página

st.set_page_config(page_title="Feedback sobre li")

# Criação de containers e exibição de conteúdo, usando a declaração with

with st.container():
    st.subheader("Dados registrando a opinião dos usuários: opiniões, classificações e fontes") # subtítulo
    st.title("Linguagens de programação mais populares em todo o mundo") # título
    st.write("Informações sobre as opniões, apontamentos dos usuários")
    st.write("Quer verificar a base de dados utilizada?  [Clique aqui no link abaixo]https://www.kaggle.com/datasets/deepakdhanoliya12/most-common-programming-languages-used-worldwide")

# Carregamento e visualização de dados

@st.cache_data
def carregar_dados(): # definindo que será utilizada para ler um arquivo csv
    dados = pd.read_csv("data.csv")
    return dados

with st.container():
    st.write("---")
    dados = carregar_dados()
    # Agrupar os dados por "LanguagesWorkedWith" e contar o número de ocorrências para cada "Responder_id"

    contagem_por_idioma = dados.groupby("LanguagesWorkedWith")["Responder_id"].count()

    # Convertendo o resultado em um DataFrame

    df_contagem = pd.DataFrame(
        {"LanguagesWorkedWith": contagem_por_idioma.index, "Contagem": contagem_por_idioma.values})

    # Exibir o gráfico de área

    st.area_chart(df_contagem, x="LanguagesWorkedWith", y="Contagem")
