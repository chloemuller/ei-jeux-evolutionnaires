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
    # afficher(People)
    for i in range(tmax):
        print("\n \n NOUVELLE GENERATION \n \n")
        max=0
        best=None
        for individu in People.indiv:
            individu.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
        People.reproduction(p = proportion, proba_mutation= pmutation)
        # for individu in People.indiv:
        #     individu.mutation(pmutation)
        for individu in People.indiv:
            individu.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
            if individu.score>max:
                best=individu
                max=individu.score
        # afficher(People)
        L.append(max)
        #print(L)
    plt.plot([i for i in range(tmax)], L)
    plt.show()
    return(best)


main(6,8,0.01,2)



