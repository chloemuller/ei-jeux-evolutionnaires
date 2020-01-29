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

# Debut du decompte du temps
start_time = time.time()


def main(N,tmax,pmutation, proportion):

    L=[]
    lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
    brin = ''.join(lineList[1:])
    People=Population(N)
    S1=[]
    for individu in People.indiv:
        individu.evaluate()
        S1.append(int(individu.score))
    maximum=int(max(S1))
    for i in range(tmax):
        mini=People.indiv[0].score
        best=People.indiv[0]
        People.reproduction(p = proportion, proba_mutation= pmutation)
        for individu in People.indiv:
            if individu.score<mini:
                best=individu
                mini=individu.score
        
        S2=[individu.score for individu in People.indiv]
        avg = sum(S2)/len(S2)
        L.append(mini)
        print(i,"avg:",avg,"best score:", mini)

    plt.subplot(221)
    plt.plot([i for i in range(tmax)], L)
    

    plt.subplot(223)
    plt.hist(S1, range = (0, maximum+10), bins = 20, color = 'red')

    S2=[individu.score for individu in People.indiv]
    print("Score final: ",best.score)
    print("Distance finale: ", best.distance)
    print("Avg:", sum(S2)/len(S2))

    plt.subplot(224)
    plt.hist(S2, range = (0,maximum+10), bins = 20, color = 'blue')
    plt.show()
   

    return(best,People)

lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
brin = ''.join(lineList[1:])
best,People = main(60,60,0.05,30)
test = Traj3D()
test.compute(brin, best.table)
test.draw("first_plot")


# Affichage du temps d execution
print("Temps d'execution : %s secondes " % (time.time() - start_time))
