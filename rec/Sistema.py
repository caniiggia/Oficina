import math
from DataSetUsuarios import usuario
from DataSetCategorias import categoria
users = usuario()
filtros = categoria()


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

def recommend(username, users):
    #aqui encontraremos os vizinhos proximos
    proximos = computeNearestNeighbor(username, users)[0][1]
    recomendacoes = []
    #agora encontramos as bandas dos vizinhos que o usuario não ouvio
    neighborRatings = users[proximos]
    userRatings = users[username]
    for artista in neighborRatings:
        if not artista in userRatings:
            recomendacoes.append((artista, neighborRatings[artista]))
    return sorted(recomendacoes,
                  key=lambda artistTuple: artistTuple[1],
                  reverse = True)

    


