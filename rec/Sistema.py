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

def recommendNoFilter(username, users):
    #aqui encontraremos os vizinhos proximos
    proximos = computeNearestNeighbor(username, users)[0][1]
    recomendacoes = []
    neighborRatings = users[proximos]
    userRatings = users[username]
    for turistico in neighborRatings:
        if not turistico in userRatings:
            recomendacoes.append((turistico, neighborRatings[turistico]))
    return sorted(recomendacoes,
                  key=lambda turisticoTuple: turisticoTuple[1],
                  reverse = True)


def recommendWithFilter(username, users, fylter):
    #aqui encontraremos os vizinhos proximos
    proximos = computeNearestNeighbor(username, users)[0][1]
    recomendacoes = []
    neighborRatings = users[proximos]
    userRatings = users[username]
    for turistico in neighborRatings:
        if not turistico in userRatings:
            if turistico in fylter:
                recomendacoes.append((turistico, neighborRatings[turistico]))
    return sorted(recomendacoes,
                  key=lambda turisticoTuple: turisticoTuple[1],
                  reverse = True)

def Principal():
    #Pega os dados no BD:
    users = usuario()
    #vai pegar os dados das categorias no BD:    
    filtros = categoria()#usa com sabedoria felipe :)
    #parte dos inputs do usuario:
    Pessoa= input("digite seu nome:")
    Lugar= input("digite seu lugar turístico 1:")
    Nota1= int(input("digite a nota:"))
    Lugar2= input("digite seu lugar turístico 2:")
    Nota2 = int(input("digite a nota 2:"))
    opcao = input("Deseja aplicar algum filtro?")
    opcao = opcao.upper()
    if(opcao == "SIM"):
        name = input("Qual categoria procura?")
        fylter = filtros[name]
    #criação do dicionario do usuario:
    Lugares=[Lugar,Lugar2]
    Notas=[Nota1,Nota2]
    Novo_Usuario=dict(zip(Lugares,Notas))
    #adicionando informaçoes do usuario no BD:
    users[Pessoa]=Novo_Usuario
    #chamamos a funçao recomendaçao e fazemos a recomendação ao usuario:
    if(opcao == "SIM"):
        Recomendacao = recommendWithFilter(Pessoa,users,fylter)
    else:
        Recomendacao = recommendNoFilter(Pessoa,users)
    return Recomendacao

def Mostrar():
    #recupera e mostra a recomendaçao ao usuario
    Rec=Principal()
    print(Rec)

Mostrar()

     



