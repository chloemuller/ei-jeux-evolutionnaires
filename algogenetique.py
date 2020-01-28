import mathutils
import math
import numpy
import RotTable
from individu import Individu
from population import Population
import croisement
from Traj3D import *
from random import random
import matplotlib.pyplot as plt


def main(N,tmax,pmutation, proportion,brin="plasmid_8k.fasta"):
    '''lineList = [line.rstrip('\n') for line in open(brin)]
	brin = ''.join(lineList[1:])'''
    L=[]
    People=Population(N)
    #print(People.indiv[0].table.rot_table)
    #print(People.indiv[1].table.rot_table)
    #print(People.indiv[2].table.rot_table)
    #print(People.indiv[3].table.rot_table)
    for i in range(tmax):
        max=0
        best=None
        for individu in People.indiv:
            individu.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
        People.reproduction(p = proportion)
        for individu in People.indiv:
            individu.mutation(pmutation)
        for individu in People.indiv:
            individu.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
            if individu.score>max:
                best=individu
                max=individu.score
        L.append(max)
    plt.plot([i for i in range(tmax)], L)
    plt.show()
    return(individu)


main(100,50,0.015,2)

