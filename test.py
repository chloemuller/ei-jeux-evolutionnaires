import random

class Population:
    def __init__(self,n):
        self.indiv=[Individu(rot_table.alea) for k in range (n)]
        self.n = n
    
    def selection_duel_pondere(self,p=(self.n)//2): 
        n=self.n
        newself=[]                           #méthode des duels pondérée: si x=10 et y=1, y a une chance sur 11 de passer
        while len(self)>p:
            m=random.randrange(0,len(self))
            t=random.randrange(0,len(self))
            x=self[m]
            y=self[t]
            p=uniform(0,1)
            if p>x.score/(x.score+y.score):
                newself.append(y)
            else:
                newself.append(x)
        return(newself)
    
    def selection_duel(self,p=(self.n)//2):
        n=self.n
        newself=[]                           #méthode des duels pondérée: si x=10 et y=1, y a une chance sur 11 de passer
        while len(self)>p:
            m=random.randrange(0,len(self))
            t=random.randrange(0,len(self))
            x=self[m]
            y=self[t]
            if x.score<=y.score:
                newself.append(x)
            else:
                newself.append(y)
        return(newself)

    def selection_par_rang(self, p):
        liste_individus = self.indiv
        n = self.n
        
        def echanger(tableau, i, j):
            tableau[i], tableau[j] = tableau[j], tableau[i]
            
        def partitionner(tableau,debut,fin):
            echanger(tableau,debut,randint(debut,fin-1)) 
            partition=debut
            for i in range(debut+1,fin):
                if tableau[i] < tableau[debut]:
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
            individus_selectionnes.append(liste[j-1])
            
        def modifier_population(self, liste_individus):
            self.n = len(liste_individus)
            self.indiv = liste_individus
            return self
        
        self = modifier_population(self, individus_selectionnes)

    def reproduction(self,selection=selection_duel,enfant=mixage,p=n//2):
        newself=selection(self,p)
        while len(newself)<self.n:
            m=random.randrange(0,len(newself))
            t=random.randrange(0,len(newself))
            x=newself[m]
            y=newself[t]
            newself.append(enfant(x,y))
        return(newself)

print([random.randrange(1,10) for i in range(5)])




    












    

