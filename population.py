from random import *
from individu import Individu
from RotTable import RotTable
from croisement import croisement_un_point, croisement_deux_points
import copy


class Population:
    '''A class of the ensemble of individuals and the methods associated with them,such as reproduction and different types of selections'''


    #Class initialization
    def __init__(self,n,filename):
        self.filename = filename
        self.indiv=[Individu(RotTable(), self.filename) for k in range (n)]
        self.n = n
    
    #Updates the current individuals in the population  
    def modifier_population(self, liste_individus):
        """Fonction qui renvoie une nouvelle instance de population a partir d'une liste d'individus"""
        self.n = len(liste_individus)
        self.indiv = liste_individus
        return self

    #Select a fixed number of individuals in a population
    def selection_p_best(self,p=None):
        if p==None:
            p=(self.n)//2
        liste_individus=self.indiv
        liste_individus.sort(key = lambda individu : individu.score)
        individus_selectionnes = [element for element in liste_individus[:p]]
        self = self.modifier_population(individus_selectionnes)

    #Select via comparing two random individuals with some randomness involved and compared
    def selection_duel_pondere(self,p=None): 
        if p == None :
            p = (self.n)//2
        meilleur = self.indiv[0]
        for individu in self.indiv :
            if meilleur.score > individu.score:
                meilleur = individu
        newself=[meilleur] 
        m=randrange(0,self.n)
        t=randrange(0,self.n)                   
        #méthode des duels pondérée: si x=10 et y=1, y a une chance sur 11 de passer
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
    
    #Selection via comparing the player`s score randomly
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

    #Selection using a random method to select players based on their rank in score
    def selection_par_rang(self,p = None):
        if p == None :
            p = (self.n)//2
        liste_individus = self.indiv
        n = self.n        
        liste_individus.sort(key = lambda individu : individu.score, reverse = True)
        individus_selectionnes = [liste_individus[-1]]
    
        for _ in range(p-1):
            curseur = random()*n*(n+1)/2
            j = 1
            while j*(j+1)/2 < curseur :
                j+=1 
            #on doit prendre l'individu avec le jème score 
            individus_selectionnes.append(liste_individus[j-1])
        
        self = self.modifier_population(individus_selectionnes)
        
    #Selecting using a random method that takes the score into ponderation
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

    #The Function that makes the selection and reduces the quantity of players
    #and after reproduces and mutates the remaining ones into a new population
    def reproduction(self,proba_mutation = None, selection=None,enfant=croisement_un_point, p = None):
        liste_selections = [self.selection_p_best, self.selection_duel_pondere, self.selection_duel, self.selection_par_rang, self.selection_proportionnelle]
        
        #Values of variables if there are no initial conditions
        if proba_mutation == None :
            proba_mutation = 0.001
        if selection == None :
            selection = self.selection_par_rang
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
            #We have to make a deep copy so we dont lose the values of the parents
            x=copy.deepcopy(newself[m])
            y=copy.deepcopy(newself[t])

            #Creation of the childs
            couple_enfant = enfant(x,y, self.filename)
            for child in couple_enfant :
                child.mutation_close_values(proba_mutation, number_of_mutations = 2)
                child.evaluate()
            newself.append(couple_enfant[0])
            newself.append(couple_enfant[1])
        self = self.modifier_population(newself)

#Prints the current population(used for debugging)
def afficher(popu):
    for individu in popu.indiv :
        print("\n individu \n")
        print ("score", individu.score)













    

