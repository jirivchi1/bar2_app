import streamlit as st
import pandas as pd

st.write('Bar Pitarra')

df = pd.read_excel('lista_menu.xlsx')

tapa = st.selectbox('Elige',df['Tapas'])
x = open('comanda_tapa.txt','w')
y = x.write(tapa)
x.close()

st.write(f'Ha elegido {tapa}')


bebida = st.selectbox('Elige',df['Bebidas'])
k = open('comanda_bebida.txt','w')
j = k.write(bebida)
k.close()