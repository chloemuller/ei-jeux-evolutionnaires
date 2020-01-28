import mathutils
import math
import numpy
import RotTable
import individu
import population
import croisement
from Traj3D import *
from random import random
import matplotlib.pyplot as plt


def main(N,tmax,pmutation, proportion, selection="selection_duel", croisement="croisement_un_point",brin="plasmid_8k.fasta"):
    '''lineList = [line.rstrip('\n') for line in open(brin)]
	brin = ''.join(lineList[1:])'''
    L=[]
    People=Population(N)
    for i in range(tmax):
        max=0
        best=None
        for individu in People.indiv:
            individu.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
        People.reproduction(selection,p = proportion,enfant=croisement)
        for individu in People.indiv:
            individu.mutation(pmutation)
        for individu in People.indiv:
            if individu.score>max:
                best=individu
                max=individu.score
            L.append(max)
        plt.plot([i for i in range(tmax)], L)
        plt.show()
    return(individu)


main(4,10,0.015,2)

