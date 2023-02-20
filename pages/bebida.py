import streamlit as st
import pandas as pd

with open('comanda_bebida.txt') as f:
    line = f.readline()

st.write(line)