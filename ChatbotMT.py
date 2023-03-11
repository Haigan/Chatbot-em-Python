#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
NOME: Matheus Italo
Matrícula: #####
CHATBOT: DEX
OBJETIVO: USO DIÁRIO EM PESQUISAS E INTERAÇÃO
"""

import wikipedia
import pyttsx3
import yfinance as yf
import pandas as pd
import numpy as np
import json

print("Dex:Olá eu sou o Dex")
print('Dex:Vou precisar de 2 informações para gente poder começar')
nome = str(input("Dex:Digite seu nome:\n"))
str(input("Dex:Me passa seu email\n"))

opção = int(input(f"Dex:Beleza {nome}, aqui vc tem as seguintes opções 1 - Pesquisas | 2 - Conversar\n" ))

if opção == 1:
    opçãoP1 = str(input("Dex:Sobre o que você quer pesquisar? no momento temos wikipedia | voz | ações\n"))
    if opçãoP1 == 'wikipedia':
        wiki = input(f"Dex:O que deseja pesquisar {nome}?\n")
        wikipedia.set_lang('pt')
        pesquisa = wikipedia.search(str(wiki))
        for i in pesquisa:
            print(wikipedia.summary(i, sentences=1))
    if opçãoP1 == 'voz':
        Dex = pyttsx3.init()
        msg = input("Dex:Digite seu texto e em seguida receberá também uma pesquisa sobre ele\n")
        Dex.say(msg)
        Dex.runAndWait()
        wikipedia.set_lang('pt')
        pesquisa = wikipedia.search(str(msg))
        for i in pesquisa:
            print(wikipedia.summary(i, sentences=1))
    if opçãoP1 == 'ações':
        ações = str(input("Dex:Deseja consultar as ações de hoje, sim ou não?\n"))
        if ações == 'sim':
            carteira = ['PETR4.SA','GOOGL','FB','EURUSD=X','VALE3.SA']
            dados = yf.download(tickers=carteira,period='1y')
            print(dados)
        else:
            print('Dex:Que pena! é sempre um bom dia para investir.')
if opção == 2:
    def conversa():
        dialogo[chat] = resposta
        
    print("Dex:bora bater um papo, para melhor entendimento, evite o CAPSLOCK.")
    while True:
        chat = str(input(f"{nome}:"))
        dialogo = {'oi':'olá',
                   'olá':'oi',
                  'tudo e com você?':'ótimo',
                   'tudo bem?':'tudo e com você?',
                   'bem':'qual a boa hoje?',
                   'que dia é hoje?':'um bom dia para programar.',
                   'qual a melhor linguagem de programação':'Python.',
                   'ta aprendendo o que?':'Python em AEDSII.',
                   'O que é programar':'é simplesmente o nosso futuro.',
                   'como está as ações?':'se aplicar direito vai dar uma boa grana.',
                   'qual instituto você foi criado?':'IFNMG',
                   'quem é seu professor':'Rennan',
                   'quais mecanismos usou?':'Wikipedia,pyttsx3,yfinance,pandas,numpy',
                   
                  }
        try:  
            print(f"Dex:{dialogo[chat]}")
        except:
            ensinar = str(input(f"Dex:Não encontrei no banco de dados, gostaria de ensinar a resposta para a pergunta {chat} sim ou não?: \n")) 
            if ensinar == 'sim':
                resposta = str(input(f"Dex:Digite a resposta para a pergunta {chat}: "))
                conversa() 
                break
            else: 
                print(f"Dex:Encerrado {nome}! obrigado por usar nosso chatbot")


# In[ ]:




