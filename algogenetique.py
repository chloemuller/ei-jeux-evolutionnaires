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
    L=[]
    People=Population(N)
    for i in range(tmax):
        #print(i)
        max=0
        best=None
        People.reproduction(p = proportion, proba_mutation= pmutation)
        for individu in People.indiv:
            if individu.score>max:
                best=individu
                max=individu.score
        L.append(max)
        print(i,":",max)

    plt.plot([i for i in range(tmax)], L)
    plt.show()
    return(best, People)


best, People = main(60,100,0.01,20)
traj = Traj3D()
traj.compute(best.brin,best.table)
traj.draw("plot")


best,People = main(100,100,0.01,50)
traj = Traj3D()
traj.compute(best.brin,best.table)
traj.draw("plot")
