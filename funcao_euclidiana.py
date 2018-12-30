from math import sqrt
from recomendacao import avaliacoes


def distancia_euclidiana(user1,user2):
    
    si={}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]:
           print('ok')     
    #distancia_euclidiana = (1/ ( 1+ sqrt( pow( 3 - 1.5,2 ) + pow( 3.5 - 5,2 ) ) ) )
    #return distancia_euclidiana



"""        
for item in avaliacoes['Ana']:
    if item in avaliacoes['Leonardo']:
        print('ok')
"""
distancia_euclidiana("Ana","Leonardo")
