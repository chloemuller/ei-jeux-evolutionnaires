import mathutils
import math
import numpy
import RotTable
from individu import Individu
from population import Population, afficher
import croisement
from Traj3D import *
from random import random
import matplotlib.pyplot as plt
import time

# def main(N,tmax,pmutation, proportion,brin="plasmid_8k.fasta"):
#     '''lineList = [line.rstrip('\n') for line in open(brin)]
# 	brin = ''.join(lineList[1:])'''
#     L=[]
#     People=Population(N)
#     for i in range(tmax):
#         print(i)
#         max=0
#         best=None
#         People.reproduction(p = proportion, proba_mutation= pmutation)
#         for individu in People.indiv:
#             if individu.score>max:
#                 best=individu
#                 max=individu.score
#         L.append(max)

#     plt.plot([i for i in range(tmax)], L, label = str(pmutation))
#     return(best)

def main(N,tmax,pmutation, proportion):

    L=[]
    lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
    brin = ''.join(lineList[1:])
    People=Population(N)
    # S1=[]
    for individu in People.indiv:
        individu.evaluate(brin)
        # S1.append(int(individu.score))
    # maximum=int(max(S1))
    for i in range(tmax):
        #print(i)
        mini=People.indiv[0].score
        best=People.indiv[0]
        People.reproduction(p = proportion, proba_mutation= pmutation)
        for individu in People.indiv:
            if individu.score<mini:
                best=individu
                mini=individu.score
        L.append(mini)

    # plt.subplot(221)
    plt.plot([i for i in range(tmax)], L, label = str(pmutation))
    

    # plt.subplot(223)
    # plt.hist(S1, range = (0, maximum+10), bins = 20, color = 'red')

    # S2=[individu.score for individu in People.indiv]
    # print("Score final: ",best.score)


    # plt.subplot(224)
    # plt.hist(S2, range = (0,maximum+10), bins = 20, color = 'blue')
    # plt.show()
   

    return(best,People)

# lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
# brin = ''.join(lineList[1:])
# best,People = main(10,10,0.01,5)
# test = Traj3D()
# test.compute(brin, best.table)
# test.draw("first_plot")



def test_mutation():
    plt.figure()
    for i in range(1,5):
        print("\n \n", i)
        main(100,40,10**(-i),50)
    plt.legend()
    plt.xlabel("Nombre de générations")
    plt.ylabel("Score du meilleur individu")
    plt.title("Comparaison en fonction du taux de mutation")
    print("Temps d'execution : %s secondes " % (time.time() - start_time))
    plt.show()   


start_time = time.time()
test_mutation()
