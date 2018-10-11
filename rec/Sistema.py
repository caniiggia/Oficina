# -*- coding: utf-8 -*-
import math
from DataSetUsuarios import usuario
from DataSetCategorias import categoria

def manhattan (rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances


def recommend(username, users, fylter):
    #aqui encontraremos os vizinhos proximos
    proximos = computeNearestNeighbor(username, users)[0][1]
    recomendacoes = []
    neighborRatings = users[proximos]
    userRatings = users[username]
    for turistico in neighborRatings:
        if not turistico in userRatings:
            if fylter != "NAO" and turistico in fylter:
                recomendacoes.append((turistico, neighborRatings[turistico]))
            elif fylter == "NAO":
                recomendacoes.append((turistico, neighborRatings[turistico]))
    return sorted(recomendacoes,
                  key=lambda turisticoTuple: turisticoTuple[1],
                  reverse = True)

def Principal():
    cont = 0
    #Pega os dados no BD:
    users = usuario()
    #vai pegar os dados das categorias no BD:    
    filtros = categoria()#usa com sabedoria felipe :)
    #parte dos inputs do usuario:
    lugares = []
    notas = []
    pessoa= input("digite seu nome:\n")
    print("\nPerfil: ", pessoa)
    print("------------------------------------------")
    while(True):
        lugar = input("digite seu lugar turístico " + str(cont+1) + ":\n")
        nota = int(input("digite a nota para " + lugar + ":\n"))
        escolha = input("Deseja avaliar mais lugares?\n")
        escolha = escolha.upper()
        lugares.append(lugar)
        notas.append(nota)
        if(escolha=="NÃO" or escolha=="NAO"):
            print("------------------------------------------")
            break
        print("------------------------------------------")
        cont+=1
    #Lugar2= input("digite seu lugar turístico 2:")
    #Nota2 = int(input("digite a nota 2:"))
    while(True):
        opcao = input("Deseja aplicar algum filtro?\n")
        opcao = opcao.upper()
        if(opcao == "SIM"):
            name = input("Qual categoria procura?\n")
            fylter = filtros[name]
            break
        elif(escolha=="NÃO" or escolha=="NAO"):
            fylter = 'NAO'
            break
        else:
            print("Por favor, informe sim ou não como resposta\n")
        
    #criação do dicionario do usuario:
    #Lugares=[Lugar,Lugar2]
    #Notas=[Nota1,Nota2]
    Novo_Usuario=dict(zip(lugares,notas))
    #adicionando informaçoes do usuario no BD:
    users[pessoa]=Novo_Usuario
    #chamamos a funçao recomendaçao e fazemos a recomendação ao usuario:
    Recomendacao = recommend(pessoa,users,fylter)
    return Recomendacao

def Mostrar():
    #recupera e mostra a recomendaçao ao usuario
    Rec=Principal()
    print(Rec)

Mostrar()

     



