from math import sqrt
from recomendacao import avaliacoes


def distancia_euclidiana(user1,user2):
    
    si={}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]:
                  
            si[item]=1
        
    if len(si) == 0: print('Nenhum filme igual')
    soma = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item],2)
                for item in avaliacoes[user1] if item in avaliacoes[user2] ])
    return 1/( sqrt(soma))
    #distancia_euclidiana = (1/ ( 1+ sqrt( pow( 3 - 1.5,2 ) + pow( 3.5 - 5,2 ) ) ) )
    #return distancia_euclidiana



"""        
for item in avaliacoes['Ana']:
    if item in avaliacoes['Marcos']:
        print('ok')
"""
print( distancia_euclidiana("Ana","Leonardo"))
