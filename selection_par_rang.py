from random import random

def creer_population(self, liste_individus):
    self.n = len(liste_individus)
    self.indiv = set(liste_individus)
    return self

def selection_par_rang(self, p = n//2):
    set_individus = self.indiv
    n = self.n

    def partitionner(tableau,debut,fin):
        echanger(tableau,debut,random.randint(debut,fin-1)) 
        partition=debut
        for i in range(debut+1,fin):
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

    liste = list(set_individus)
    tri_rapide(liste)
    individus_selectionnes = []

    for _ in range(p):
        curseur = random()*n*(n+1)/2
        j = 1
        while j*(j+1)/2 < curseur :
            j+=1 
        #on doit prendre l'individu avec le jème score 
        individus_selectionnes.append(liste[j])
    self = creer_population(self, liste_individus)


    