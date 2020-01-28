import random
from random import random, randint, randrange
from individu import Individu
from RotTable import RotTable
from croisement import croisement_un_point, croisement_deux_points

class Population:
    def __init__(self,n):
        self.indiv=[Individu(RotTable()) for k in range (n)]
        self.n = n

    def modifier_population(self, liste_individus):
        """Fonction qui renvoie une nouvelle instance de population a partir d'une liste d'individus"""
        self.n = len(liste_individus)
        self.indiv = liste_individus
        return self

    def selection_duel_pondere(self,p=None): 
        if p == None :
            p = (self.n)//2
        newself=[] 
        vu=set()
        m=randrange(0,self.n)
        t=randrange(0,self.n)                   #méthode des duels pondérée: si x=10 et y=1, y a une chance sur 11 de passer
        while len(newself)<p:
            while m in vu:
                m=randrange(0,self.n)
            while t in vu:
                t=randrange(0,self.n)
            x=self.indiv[m]
            y=self.indiv[t]
            vu.add(t)
            vu.add(m)
            p=random()
            if p>x.score/(x.score+y.score):
                newself.append(y)
            else:
                newself.append(x)
            
        self = self.modifier_population(newself)
    
    def selection_duel(self,p=None):
        if p == None :
            p = (self.n)//2
        newself=[]
        vu=set()                        
        t=randrange(0,self.n)
        m=randrange(0,self.n)             
        while len(newself)<p:
            while m in vu:
                m=randrange(0,self.n)
            while t in vu:
                t=randrange(0,self.n)
            x=self.indiv[m]
            y=self.indiv[t]
            vu.add(t)
            vu.add(m)
            if x.score>=y.score:
                newself.append(x)
            else:
                newself.append(y)
        self = self.modifier_population(newself)

    def selection_par_rang(self,p = None):
        if p == None :
            p = (self.n)//2
        liste_individus = self.indiv
        n = self.n
        
        def echanger(tableau, i, j):
            tableau[i], tableau[j] = tableau[j], tableau[i]
            
        def partitionner(tableau,debut,fin):
            echanger(tableau,debut,randint(debut,fin-1)) 
            partition=debut
            for i in range(debut+1,fin):
                # if tableau[i] < tableau[debut]:
                if tableau[i].score<tableau[debut].score: 
                    partition+=1 
                    echanger(tableau,i,partition) 
            echanger(tableau,debut,partition) 
            return partition
            
        def tri_rapide_aux(tableau,debut,fin):
            if debut < fin-1:
                positionPivot=partitionner(tableau,debut,fin)
                tri_rapide_aux(tableau,debut,positionPivot)
                tri_rapide_aux(tableau,positionPivot+1,fin)
            
        def tri_rapide(tableau):
            tri_rapide_aux(tableau,0,len(tableau))
            
        tri_rapide(liste_individus)
        individus_selectionnes = []
    
        for _ in range(p):
            curseur = random()*n*(n+1)/2
            # print("curseur", curseur)
            j = 1
            while j*(j+1)/2 < curseur :
                j+=1 
            #on doit prendre l'individu avec le jème score 
            # print("individus selectionés", individus_selectionnes)
            individus_selectionnes.append(liste_individus[j-1])
        
        self = self.modifier_population(individus_selectionnes)
        
    def selection_proportionelle(self,p= None):
        if p == None :
            p = (self.n)//2
        newself=[]
        somme=0
        for indiv in self.indiv:
            somme=somme+indiv.score
        while len(newself)<p:
            m=m=randrange(0, self.n)
            x=self.indiv[m]
            p=random()
            if p<=x.score/somme:
                newself.append(x)
        self = self.modifier_population(newself)

    def reproduction(self,selection=None,enfant=croisement_un_point, p = None):
        if selection == None :
            selection = self.selection_duel
        if p == None :
            p = (self.n)//2
        vieille_taille = self.n
        selection(p)
        newself = list(self.indiv)
        while len(newself)<vieille_taille:
            m=randrange(0,self.n)
            t=randrange(0,self.n)
            x=newself[m]
            y=newself[t]
            couple_enfant = enfant(x,y)
            newself.append(couple_enfant[0])
            newself.append(couple_enfant[1])
        self = self.modifier_population(newself)

def afficher(popu):
    for individu in popu.indiv :
        print("\n individu \n")
        print(individu.table.rot_table)
        print ("score", individu.score)
    
def test():
    popu = Population(4)
    print("\n POPULATION INITIALE \n")
    for individu in popu.indiv :
        individu.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
    afficher(popu)
    popu.reproduction(selection = popu.selection_duel)
    print("\n REPRODUCTION \n")
    afficher(popu)

#test()



    












    

