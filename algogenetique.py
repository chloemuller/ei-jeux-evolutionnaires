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



def main(N,tmax,pmutation, proportion,brin="plasmid_8k.fasta"):
    '''lineList = [line.rstrip('\n') for line in open(brin)]
	brin = ''.join(lineList[1:])'''
    L=[]
    People=Population(N)
    for i in range(tmax):
        print(i)
        max=0
        best=None
        People.reproduction(p = proportion, proba_mutation= pmutation)
        for individu in People.indiv:
            if individu.score>max:
                best=individu
                max=individu.score
        L.append(max)

    plt.plot([i for i in range(tmax)], L, label = str(pmutation))
    return(best)

def test_mutation():
    plt.figure()
    for i in range(10):
        print("\n \n", i)
        main(100,100,i/10,50)
    plt.legend()
    plt.xlabel("Nombre de générations")
    plt.ylabel("Score du meilleur individu")
    plt.title("Comparaison en fonction du taux de mutation")
    plt.show()

test_mutation()
