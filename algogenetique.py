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
    L=[mini]
    for i in range(tmax):
        print(i)
        People.reproduction(p = proportion, proba_mutation= pmutation, selection = indice_selection, enfant = enfant)
        mini=People.indiv[0].score
        best=People.indiv[0]
        for individu in People.indiv:
            if individu.score<mini:
                best=individu
                mini=individu.score
        
        S2=[individu.score for individu in People.indiv]
        avg = sum(S2)/len(S2)
        L.append(mini)

    # plt.subplot(221)
    liste_selections = ["selection_p_best", "selection_duel_pondere", "selection_duel", "selection_par_rang", "selection_proportionnelle"]
    plt.plot([j for j in range(len(L))], L, label = liste_selections[indice_selection])
    

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



def compare_mutation():
    start_time = time.time()
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


def comparaison_selections():
    liste_selections = ["selection_p_best", "selection_duel_pondere", "selection_duel", "selection_par_rang", "selection_proportionnelle"]
    liste_time = []
    plt.figure()
    People = Population(100)
    for individu in People.indiv:
        individu.evaluate()
    S2=[individu.score for individu in People.indiv]
    plt.hist(S2, range = (0,int(max(S2)+10)), bins = 20, color = 'blue')
    plt.show()
    plt.figure()
    for i in range(5):
        print("\n", liste_selections[i], "\n")
        start_time = time.time()
        best = main(100, 35, 0.001, 50, i, deepcopy(People))[0]
        liste_time.append((liste_selections[i], time.time() - start_time, best.score))
    plt.legend()
    plt.xlabel("Nombre de générations")
    plt.ylabel("Score du meilleur individu")
    plt.title("Comparaison en fonction de la méthode de sélection")
    print(numpy.array(liste_time))
    plt.show()   

# def comparaisons_croisements():
#     liste_croisements = ["croisement_un_point", "croisement_deux_points"]




# compare_mutation()

comparaison_selections()

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