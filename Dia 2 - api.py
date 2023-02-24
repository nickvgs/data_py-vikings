# %%
import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import yfinance as yf

yf.pdr_override()

st.sidebar.title('Menu')

#Lista das empresas - ticket b3
empresas = ['PETR4.SA', 'AMER3.SA', 'ITUB4.SA']
selecao = st.sidebar.selectbox('Selecione a empresa: ', empresas)

#Range de seleção
range = st.sidebar.slider('Período de meses', 0, 12, 1, key='barra_selecao')
selecao_range = str(range) + 'mo'

#Colunas
col1, col2 = st.columns([0.9, 0.1])

#Imagens
imagens = [
    'https://play-lh.googleusercontent.com/J_5q2mlg5glV-fbweDK6KfqhTa9TnM-HwfaRtzfi7_JVNtzhabwe1jQBbXi7xfx3BNrc=w240-h480-rw',
    'https://play-lh.googleusercontent.com/DxCHfCCQZHdX0edn7unbmQXNSvdWST-EK9UeUh8smubt-d6-EQZV94GbK0tL4wXfBVaX',
    'https://www.itau.com.br/content/dam/itau/varejo/logo-itau-varejo-desktop.png'
]

#Título
titulo = f'Análise econômica: {str(selecao)}'
col1.title(titulo)

if selecao == 'AMER3.SA':
    col2.image(imagens[0], width = 70)
elif selecao == 'PETR4.SA':
    col2.image(imagens[1], width = 70)
else:
    col2.image(imagens[2], width = 70)

#Coletar os dados da API do Yahoo
dados = web.get_data_yahoo(selecao, period=selecao_range)

#Gráfico
grafico_candlestick = go.Figure(
    data=[
        go.Candlestick(
            x = dados.index,
            open = dados['Open'],
            high = dados['High'],
            low = dados['Low'],
            close = dados['Close']
        )
    ]
)

grafico_candlestick.update_layout(
    xaxis_rangeslider_visible=False,
    title = 'Análise das ações',
    xaxis_title = 'Período',
    yaxis_title = 'Preço'
)

#Mostrar o gráfico do plotly no streamlit
st.plotly_chart(grafico_candlestick)

#Condição
if st.checkbox('Mostrar dados em tabela'):
    st.subheader('Tabela de registros')
    st.write(dados)


# %%
