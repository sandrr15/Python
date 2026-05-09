import streamlit as st
import pandas as pd

arquivo = open('cadastro.csv', 'r')
for linha in arquivo:
    dados = linha.strip().split(',')
    nome =  dados[0]
    idade = dados[1]
    print('Nome', nome, 'idade', idade)


arquivo.close()