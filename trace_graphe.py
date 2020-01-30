import csv
import numpy
import matplotlib.pyplot as plt
from copy import deepcopy

def extract_data1(filename):
    f = open(filename, newline = '')
    liste_selections = ["selection_p_best", "selection_duel_pondere", "selection_duel", "selection_par_rang", "selection_proportionnelle"]
    listedeliste = [[] for i in range(len(liste_selections))]
    ligne = f.readline()
    while ligne != "" :
        row = ligne.split(",")
        if row[1] in liste_selections:
            listedeliste[liste_selections.index(row[1])].append(row[3])
        ligne = f.readline()
        numpy.save("choix_selection", listedeliste)
    


def trace_histogramme_selections(listedeliste):
    listedeliste = [[float(element) for element in numpy.load(listedeliste)[i]] for i in range(5)]
    liste_selections = ["selection_p_best", "selection_duel_pondere", "selection_duel", "selection_par_rang", "selection_proportionnelle"]
    plt.figure()
    for i in range(len(liste_selections)) :
        moy = moyenne(listedeliste[i])
        mediane = sorted(listedeliste[i])[len(listedeliste[i])//2]
        plt.subplot(2,3,i+1)
        n, bins, patches = plt.hist(listedeliste[i], bins = 40)
        plt.plot([moy,moy], [0,max(n)], label = "Moyenne")
        plt.plot([mediane,mediane], [0,max(n)], label = "Médiane")
        plt.legend()
        plt.title(liste_selections[i])
    plt.show()


def moyenne(liste):
    somme = 0
    for element in liste :
        somme += element
    return somme / len(liste)

# extract_data1("Resultatgroupé_final.csv")      
# trace_histogramme_selections("choix_selection.npy")


# >>> On choisit la séléction duel et selections ponderés car elles ont la meilleure moyenne/médiane

def extract_data2(filename):
    f = open(filename, newline = '')
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    dictscore = [{} for i in range(len(liste_selections))]
    listesurvivants = [[] for i in range(len(liste_selections))]
    listescore = [[] for i in range(len(liste_selections))]
    ligne = f.readline()
    while ligne != "" :
        row = ligne.split(",")
        if row[1] in liste_selections:
            rapport_survivants = float(row[7])/float(row[4])
            listesurvivants[liste_selections.index(row[1])].append(rapport_survivants)
            listescore[liste_selections.index(row[1])].append(float(row[3]))
            if rapport_survivants not in dictscore[liste_selections.index(row[1])] :
                dictscore[liste_selections.index(row[1])][rapport_survivants] = []
            dictscore[liste_selections.index(row[1])][rapport_survivants].append(float(row[3]))
        ligne = f.readline()
    moyenne_score = [[], []]
    liste_survivants = [[], []]
    for i in range(2):
        liste_survivants[i] = sorted(list(dictscore[i].keys()))
        for rapport in deepcopy(liste_survivants[i]) :
            if len(dictscore[i][rapport]) > 1 :    #Cette condition permet de supprimer les jeu de données que nous n'avons pas eu le temps de répéter
                                                    #On estime alors que le résultat n'est pas représentatif en moyenne et on ne le prend pas en compte
                moyenne_score[i].append(moyenne(dictscore[i][rapport]))
            elif len(dictscore[i][rapport]) == 1 :
                liste_survivants[i].remove(rapport)
    numpy.save("choix_survivants", [moyenne_score, liste_survivants, listesurvivants, listescore])

def choix_survivant(listedeliste):
    [moyenne_score, liste_survivants, listesurvivants, listescore] = numpy.load(listedeliste, allow_pickle = True)
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    plt.figure()
    for i in range(len(liste_selections)) :
        plt.subplot(1,2,i+1)
        plt.plot(liste_survivants[i], moyenne_score[i], label = "moyenne")
        plt.plot(listesurvivants[i], listescore[i], ".")
        plt.legend()
        plt.title(liste_selections[i])
        plt.xlabel("Taux de survivants")
        plt.ylabel("Score")
    plt.show()


# extract_data2("Resultatgroupé_final.csv")
# choix_survivant("choix_survivants.npy")

# >>> Choix proportion survivant = 0.2



def extract_data3(filename):
    f = open(filename, newline = '')
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    dictscore = [{} for i in range(len(liste_selections))]
    listemutations = [[] for i in range(len(liste_selections))]
    listescore = [[] for i in range(len(liste_selections))]
    ligne = f.readline()
    while ligne != "" :
        row = ligne.split(",")
        if row[1] in liste_selections:
            mutation = float(row[6])
            listemutations[liste_selections.index(row[1])].append(mutation)
            listescore[liste_selections.index(row[1])].append(float(row[3]))
            if mutation not in dictscore[liste_selections.index(row[1])] :
                dictscore[liste_selections.index(row[1])][mutation] = []
            dictscore[liste_selections.index(row[1])][mutation].append(float(row[3]))
        ligne = f.readline()
    moyenne_score = [[], []]
    liste_mut = [[], []]
    for i in range(2):
        liste_mut[i] = sorted(list(dictscore[i].keys()))
        for mut in deepcopy(liste_mut[i]) :
            if len(dictscore[i][mut]) > 1 :    #Cette condition permet de supprimer les jeu de données que nous n'avons pas eu le temps de répéter
                                                    #On estime alors que le résultat n'est pas représentatif en moyenne et on ne le prend pas en compte
                moyenne_score[i].append(moyenne(dictscore[i][mut]))
            elif len(dictscore[i][mut]) == 1 :
                liste_mut[i].remove(mut)
    numpy.save("choix_mutation", [moyenne_score, liste_mut, listemutations, listescore])

def choix_mutation(listedeliste):
    [moyenne_score, liste_survivants, listesurvivants, listescore] = numpy.load(listedeliste, allow_pickle = True)
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    plt.figure()
    for i in range(len(liste_selections)) :
        plt.subplot(1,2,i+1)
        plt.plot(liste_survivants[i], moyenne_score[i], label = "moyenne")
        plt.plot(listesurvivants[i], listescore[i], ".")
        plt.legend()
        plt.title(liste_selections[i])
        plt.xlabel("Mutations")
        plt.ylabel("Score")
    plt.show()

# extract_data3("Resultatgroupé_final.csv")
# choix_mutation("choix_mutation.npy")

# >>> Les résultats ne sont pas hyper concluants mais selon le graphe on a 0.005 meilleur pour duel et 0.01 meilleur pour duel ponderé



# on voulait tracer un graphique en 3d cependant ce projet a été abandonné par manque de temps 
#Les deux fonctions suivantes ne marchent donc pas


# from mpl_toolkits.mplot3d import axes3d

#Structure de donnée utilisée : dict1 = {x:{y:[z1, z2]}}   et    dict2 = {y:{x:[z1, z2]}}

# def extract_data4(filename):
#     f = open(filename, newline = '')
#     liste_selections = ["selection_duel_pondere", "selection_duel"]
#     liste_mutations = [0.005, 0.01]
#     survivants = 0.2
#     liste_dict1 = [{}, {}]
#     liste_dict2 = [{}, {}]
#     ligne = f.readline()
#     while ligne != "" :
#         row = ligne.split(",")
#         if row[1] in liste_selections:
#             i = liste_selections.index(row[1])
#             if liste_mutations[i] == float(row[6]) and survivants == float(row[7])/float(row[4]):
#                 x = float(row[4])
#                 y = float(row[5])
#                 z = float(row[3])
#                 if x not in liste_dict1[i]:
#                     liste_dict1[i][x] = {}
#                 if y not in liste_dict1[i][x]:
#                     liste_dict1[i][x][y] = []
#                 liste_dict1[i][x][y].append(z)
#                 if y not in liste_dict2[i]:
#                     liste_dict2[i][y] = {}
#                 if x not in liste_dict2[i][y]:
#                     liste_dict2[i][y][x] = []
#                 liste_dict2[i][y][x].append(z)
#         ligne = f.readline()
#     LISTE = []
#     for i in range(2):
#         X = [0 for k in range(len(liste_dict1[i].keys())) for j in range(len(liste_dict2[i].keys()))]
#         Y = [0 for k in range(len(liste_dict2[i].keys())) for j in range(len(liste_dict1[i].keys()))]
#         Z = [
#         for x in sorted(liste_dict1[i]) :
#             Y.append([])
#             Z.append([])
#             for y in liste_dict1[i][x]:
#                 Y[-1].append(y)
#                 Z[-1].append(moyenne(liste_dict1[i][x][y]))
#         for y in liste_dict2[i] :
#             X.append([])
#             for x in liste_dict2[i][y]:
#                 X[-1].append(x)       
#         LISTE.append((X,Y,Z))
#     return LISTE


# def graphe(filename):
#     LISTE = extract_data4(filename)
#     for i in range(2):
#         X, Y, Z = LISTE[i]
#         print(X)
#         print(Y)
#         print(Z)
#         fig = plt.figure()
#         ax = fig.add_subplot(111, projection='3d')
#         ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
#         plt.show()

# graphe("Resultatgroupé_final.csv")  >>> Cette fonction a échoué, on abandonne l'idée du graphe 3d par manque de temps 






def extract_data5(filename):
    f = open(filename, newline = '')
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    dictscore = [{} for i in range(len(liste_selections))]
    listeindividus = [[] for i in range(len(liste_selections))]
    listescore = [[] for i in range(len(liste_selections))]
    ligne = f.readline()
    while ligne != "" :
        row = ligne.split(",")
        if row[1] in liste_selections:
            individu = float(row[4])
            listeindividus[liste_selections.index(row[1])].append(individu)
            listescore[liste_selections.index(row[1])].append(float(row[3]))
            if individu not in dictscore[liste_selections.index(row[1])] :
                dictscore[liste_selections.index(row[1])][individu] = []
            dictscore[liste_selections.index(row[1])][individu].append(float(row[3]))
        ligne = f.readline()
    moyenne_score = [[], []]
    liste_mut = [[], []]
    for i in range(2):
        liste_mut[i] = sorted(list(dictscore[i].keys()))
        for mut in deepcopy(liste_mut[i]) :
            if len(dictscore[i][mut]) > 1 :    #Cette condition permet de supprimer les jeu de données que nous n'avons pas eu le temps de répéter
                                                    #On estime alors que le résultat n'est pas représentatif en moyenne et on ne le prend pas en compte
                moyenne_score[i].append(moyenne(dictscore[i][mut]))
            elif len(dictscore[i][mut]) == 1 :
                liste_mut[i].remove(mut)
    numpy.save("choix_individus", [moyenne_score, liste_mut, listeindividus, listescore])
            
def choix_individu(listedeliste):
    [moyenne_score, liste_survivants, listesurvivants, listescore] = numpy.load(listedeliste, allow_pickle = True)
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    plt.figure()
    for i in range(len(liste_selections)) :
        plt.subplot(1,2,i+1)
        plt.plot(liste_survivants[i], moyenne_score[i], label = "moyenne")
        plt.plot(listesurvivants[i], listescore[i], ".")
        plt.legend()
        plt.title(liste_selections[i])
        plt.xlabel("Taille de la population")
        plt.ylabel("Score")
    plt.show()
            

# extract_data5("Resultatgroupé_final.csv")
# choix_individu("choix_individus.npy")




def extract_data6(filename):
    f = open(filename, newline = '')
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    dictscore = [{} for i in range(len(liste_selections))]
    listegenerations = [[] for i in range(len(liste_selections))]
    listescore = [[] for i in range(len(liste_selections))]
    ligne = f.readline()
    while ligne != "" :
        row = ligne.split(",")
        if row[1] in liste_selections:
            generation = float(row[5])
            listegenerations[liste_selections.index(row[1])].append(generation)
            listescore[liste_selections.index(row[1])].append(float(row[3]))
            if generation not in dictscore[liste_selections.index(row[1])] :
                dictscore[liste_selections.index(row[1])][generation] = []
            dictscore[liste_selections.index(row[1])][generation].append(float(row[3]))
        ligne = f.readline()
    moyenne_score = [[], []]
    liste_mut = [[], []]
    for i in range(2):
        liste_mut[i] = sorted(list(dictscore[i].keys()))
        for mut in deepcopy(liste_mut[i]) :
            if len(dictscore[i][mut]) > 1 :    #Cette condition permet de supprimer les jeu de données que nous n'avons pas eu le temps de répéter
                                                    #On estime alors que le résultat n'est pas représentatif en moyenne et on ne le prend pas en compte
                moyenne_score[i].append(moyenne(dictscore[i][mut]))
            elif len(dictscore[i][mut]) == 1 :
                liste_mut[i].remove(mut)
    numpy.save("choix_generations", [moyenne_score, liste_mut, listegenerations, listescore])
            
def choix_generation(listedeliste):
    [moyenne_score, liste_survivants, listesurvivants, listescore] = numpy.load(listedeliste, allow_pickle = True)
    liste_selections = ["selection_duel_pondere", "selection_duel"]
    plt.figure()
    for i in range(len(liste_selections)) :
        plt.subplot(1,2,i+1)
        plt.plot(liste_survivants[i], moyenne_score[i], label = "moyenne")
        plt.plot(listesurvivants[i], listescore[i], ".")
        plt.legend()
        plt.title(liste_selections[i])
        plt.xlabel("Nombre de génération")
        plt.ylabel("Score")
    plt.show()

# extract_data6("Resultatgroupé_final.csv")
# choix_generation("choix_generations.npy")