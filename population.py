from random import *
from individu import Individu
from RotTable import RotTable
from croisement import croisement_un_point, croisement_deux_points
import copy

class Population:
    def __init__(self,n):
        self.indiv=[Individu(RotTable()) for k in range (n)]
        self.n = n

    def modifier_population(self, liste_individus):
        """Fonction qui renvoie une nouvelle instance de population a partir d'une liste d'individus"""
        self.n = len(liste_individus)
        self.indiv = liste_individus
        return self

    def selection_p_best(self,p=None):
        if p==None:
            p=(self.n)//2
        liste_individus=self.indiv
        liste_individus.sort(key = lambda individu : individu.score)
        individus_selectionnes = [element for element in liste_individus[:p]]
        self = self.modifier_population(individus_selectionnes)


    def selection_duel_pondere(self,p=None): 
        if p == None :
            p = (self.n)//2
        meilleur = self.indiv[0]
        for individu in self.indiv :
            if meilleur.score > individu.score:
                meilleur = individu
        newself=[meilleur] 
        m=randrange(0,self.n)
        t=randrange(0,self.n)                   #méthode des duels pondérée: si x=10 et y=1, y a une chance sur 11 de passer
        non_vu = [i for i in range(0, self.n)]          
        while len(newself)<p:
            m = choice(non_vu)
            non_vu.remove(m)
            t = choice(non_vu)
            non_vu.remove(t)
            x=self.indiv[m]
            y=self.indiv[t]
            proba=random()
            if proba<x.score/(x.score+y.score):
                newself.append(y)
            else:
                newself.append(x)
            
        self = self.modifier_population(newself)
    
    def selection_duel(self,p=None):
        if p == None :
            p = (self.n)//2
        meilleur = self.indiv[0]
        for individu in self.indiv :
            if meilleur.score > individu.score:
                meilleur = individu
        newself = [meilleur]                      
        t=randrange(0,self.n)
        m=randrange(0,self.n)
        non_vu = [i for i in range(0, self.n)]          
        while len(newself)<p:
            m = choice(non_vu)
            non_vu.remove(m)
            t = choice(non_vu)
            non_vu.remove(t)
            
            x=self.indiv[m]
            y=self.indiv[t]
            if x.score<y.score:
                newself.append(x)
            else:
                newself.append(y)
        self = self.modifier_population(newself)



    def selection_par_rang(self,p = None):
        if p == None :
            p = (self.n)//2
        liste_individus = self.indiv
        n = self.n        
        liste_individus.sort(key = lambda individu : individu.score, reverse = True)
        individus_selectionnes = [liste_individus[-1]]
    
        for _ in range(p-1):
            curseur = random()*n*(n+1)/2
            # print("curseur", curseur)
            j = 1
            while j*(j+1)/2 < curseur :
                j+=1 
            #on doit prendre l'individu avec le jème score 
            # print("individus selectionés", individus_selectionnes)
            individus_selectionnes.append(liste_individus[j-1])
        
        self = self.modifier_population(individus_selectionnes)
        
    def selection_proportionnelle(self,p= None):
        if p == None :
            p = (self.n)//2
        meilleur = self.indiv[0]
        for individu in self.indiv :
            if meilleur.score > individu.score:
                meilleur = individu
        newself = [meilleur]      
        somme=0
        for indiv in self.indiv:
            somme+=1/indiv.score
        while len(newself)<p:
            m=m=randrange(0, self.n)
            x=self.indiv[m]
            proba=random()
            if proba<=x.score/somme:
                newself.append(x)
        self = self.modifier_population(newself)

    def reproduction(self,proba_mutation = None, selection=None,enfant=croisement_un_point, p = None):
        liste_selections = [self.selection_p_best, self.selection_duel_pondere, self.selection_duel, self.selection_par_rang, self.selection_proportionnelle]
        if proba_mutation == None :
            proba_mutation = 0.001
        if selection == None :
            selection = self.selection_duel
        else :
            selection = liste_selections[selection]
        if p == None :
            p = (self.n)//2
        vieille_taille = self.n
        selection(p)
        newself = [element for element in self.indiv]       
        while len(newself)<vieille_taille:
            m=randrange(0,self.n)
            t=randrange(0,self.n)
            x=copy.deepcopy(newself[m])
            y=copy.deepcopy(newself[t])
            couple_enfant = enfant(x,y)
            for child in couple_enfant :
                child.mutation_close_values(proba_mutation, number_of_mutations = 2)
                child.evaluate()
            newself.append(couple_enfant[0])
            newself.append(couple_enfant[1])
        self = self.modifier_population(newself)


def afficher(popu):
    for individu in popu.indiv :
        print("\n individu \n")
        # print(individu.table.rot_table)
        print ("score", individu.score)
    
def test():
    popu = Population(4)
    print("\n POPULATION INITIALE \n")
    for individu in popu.indiv :
        individu.evaluate()
    afficher(popu)
    popu.reproduction(selection = popu.selection_duel)
    print("\n REPRODUCTION \n")
    afficher(popu)

#test()

def test2():
    popu = Population(10)
    for individu in popu.indiv :
        lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
        brin = ''.join(lineList[1:])
        individu.evaluate()
    print("\n \n POPULATION INITIALE \n \n")
    afficher(popu)
    popu.selection_proportionnelle()
    print("\n\nAPRES SELECTION \n\n")
    afficher(popu)
    


# test2()










    

