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

# Start of the time counting 
start_time = time.time()


def main(N,tmax,pmutation, proportion, filename):
    
    #Creation of the initial population
    People=Population(N, filename)
    L=[]

    #Evaluating the initial population for the histogram
    S1=[]
    for individu in People.indiv:
        individu.evaluate()
        S1.append(int(individu.score))
    maximum=int(max(S1))

    #The main loop of new generations
    for i in range(tmax):
        mini=People.indiv[0].score
        best=People.indiv[0]
        People.reproduction(p = proportion, proba_mutation= pmutation)

        #Searching for the best individual in each generation
        for individu in People.indiv:
            if individu.score<mini:
                best=individu
                mini=individu.score
        
        #Printing usefull data (generation average and their best score)
        S2=[individu.score for individu in People.indiv]
        avg = sum(S2)/len(S2)
        L.append(mini)
        print(i,"avg:",avg,"best score:", mini)



    #Plotting all the graphs
    plt.subplot(221)
    plt.plot([i for i in range(tmax)], L)

    #Graph of the original population
    plt.subplot(223)
    plt.hist(S1, range = (0, maximum+10), bins = 20, color = 'red')

    S2=[individu.score for individu in People.indiv]
    print("Score final: ",best.score)
    print("Distance finale: ", best.distance)
    print("Avg:", sum(S2)/len(S2))

    #Graph of the final population
    plt.subplot(224)
    plt.hist(S2, range = (0,maximum+10), bins = 20, color = 'blue')
    plt.show()
   

    return(best,People)


#Testing our solution and printing the result in 3D
lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
brin = ''.join(lineList[1:])
best,People = main(100,100,0.01,20, "plasmid_8k.fasta")
test = Traj3D()
test.compute(brin, best.table)
test.draw("first_plot")


# Affichage du temps d execution
print("Temps d'execution : %s secondes " % (time.time() - start_time))
