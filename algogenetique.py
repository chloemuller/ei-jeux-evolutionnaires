import mathutils
import math
import numpy
import RotTable
from individu import Individu
from population import Population, afficher
from croisement import * 
from Traj3D import *
from random import random
import matplotlib.pyplot as plt
import time
from copy import deepcopy

def main(N,tmax,pmutation, proportion, indice_selection, population_initiale, enfant = croisement_un_point):

    
    lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
    brin = ''.join(lineList[1:])
    People=deepcopy(population_initiale)
    # S1=[]
    for individu in People.indiv:
        individu.evaluate()
        # S1.append(int(individu.score))
    # maximum=int(max(S1))
    mini=People.indiv[0].score
    for individu in People.indiv:
            if individu.score<mini:
                mini=individu.score
    # L=[mini]
    for i in range(tmax):
        print(i)
        People.reproduction(p = proportion, proba_mutation= pmutation, selection = indice_selection, enfant = enfant)
        mini=People.indiv[0].score
        best=People.indiv[0]
        for individu in People.indiv:
            if individu.score<mini:
                best=individu
                mini=individu.score
        
        # S2=[individu.score for individu in People.indiv]
        # avg = sum(S2)/len(S2)
        # L.append(mini)

    # plt.subplot(221)
    # liste_selections = ["selection_p_best", "selection_duel_pondere", "selection_duel", "selection_par_rang", "selection_proportionnelle"]
    # plt.plot([j for j in range(len(L))], L, label = liste_selections[indice_selection])
    

    # plt.subplot(223)
    # plt.hist(S1, range = (0, maximum+10), bins = 20, color = 'red')

    S2=[individu.score for individu in People.indiv]
    print("Score final: ",best.score)
    print("Avg:", sum(S2)/len(S2))
    print("Distance final: ",best.distance)


    # plt.subplot(224)
    # plt.hist(S2, range = (0,maximum+10), bins = 20, color = 'blue')
    # plt.show()
   

    return(best,People)

lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
brin = ''.join(lineList[1:])
best,People = main(100,10,0.05,10)
test = Traj3D()
test.compute(brin, best.table)
test.draw("first_plot")

# [['selection_p_best' '22.637820959091187' '116.30569654472626']
#  ['selection_duel_pondere' '22.636890172958374' '46.6242321955727']
#  ['selection_duel' '22.21168804168701' '234.7640748029787']
#  ['selection_par_rang' '22.180259227752686' '190.0163752068961']
#  ['selection_proportionnelle' '22.329176902770996' '315.7030719673908']]

# [['selection_p_best' '22.775274991989136' '106.89365704155766']
#  ['selection_duel_pondere' '22.716803073883057' '284.11538487097084']
#  ['selection_duel' '23.19036889076233' '155.83887357033393']
#  ['selection_par_rang' '22.752396821975708' '118.6068497149259']
#  ['selection_proportionnelle' '22.71982979774475' '151.80114914793427']]