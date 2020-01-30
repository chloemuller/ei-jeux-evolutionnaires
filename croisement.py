import numpy
from RotTable import RotTable
from individu import Individu

def croisement_un_point(parent1, parent2):
    '''Croise les tables de rotation des parents pour former deux enfants en respectant les symétries du problème'''
    ''' Retourne deux enfants'''

    enfant1 = Individu(RotTable())
    enfant2 = Individu(RotTable())
    comp = 0
    point_crois= numpy.random.random_integers(0,8)
    list_dinucleotides = sorted(RotTable().orta())

    #We look at the list of sorted dinucleotides and create the crossover
    for doublet in list_dinucleotides:
        if doublet == "GA":
            break

        #If it have a value smaller than the generated number it wont do the crossover
        if comp < point_crois:
            enfant1.table.rot_table[doublet] = parent1.table.rot_table[doublet]
            correspondent_doublet1 = enfant1.table.corr()[doublet]
            enfant1.table.rot_table[correspondent_doublet1] = parent1.table.rot_table[correspondent_doublet1]
            enfant1.table.rot_table[correspondent_doublet1][2] *= -1

            enfant2.table.rot_table[doublet] = parent2.table.rot_table[doublet]
            correspondent_doublet2 = enfant2.table.corr()[doublet]
            enfant2.table.rot_table[correspondent_doublet2] = parent2.table.rot_table[correspondent_doublet2]
            enfant2.table.rot_table[correspondent_doublet2][2] *= -1
        
        #If it have a value bigger than the generated number it will crossover
        else :
            enfant1.table.rot_table[doublet] = parent2.table.rot_table[doublet]
            correspondent_doublet1 = enfant1.table.corr()[doublet]
            enfant1.table.rot_table[correspondent_doublet1] = parent2.table.rot_table[correspondent_doublet1]
            enfant1.table.rot_table[correspondent_doublet1][2] *= -1

            enfant2.table.rot_table[doublet] = parent1.table.rot_table[doublet]
            correspondent_doublet2 = enfant2.table.corr()[doublet]
            enfant2.table.rot_table[correspondent_doublet2] = parent1.table.rot_table[correspondent_doublet1]
            enfant2.table.rot_table[correspondent_doublet2][2] *= -1

        comp += 1
    return enfant1, enfant2


def croisement_deux_points(parent1, parent2):
    ''' Croise les tables de rotationd des deux parents en croisant à deux points et respectant les symétries du problème'''
    ''' Retourne deux enfants'''

    enfant1 = Individu(RotTable())
    enfant2 = Individu(RotTable())
    comp = 0
    point_crois1= numpy.random.random_integers(0,8)
    point_crois2= numpy.random.random_integers(0,8)
    list_dinucleotides = sorted(ROT_TABLE)

    #We look at the list of sorted dinucleotides and create the crossover
    for doublet in list_dinucleotides:
        
        #If it have a value smaller than the first generated number it wont do the crossover
        #unless it have a value bigger than the second generated number
        if comp < min(point_crois1,point_crois2) or comp > max(point_crois1,point_crois2):
            enfant1.table.rot_table[doublet] = parent1.table.rot_table[doublet]
            correspondent_doublet1 = enfant1.table.corr()[doublet]
            enfant1.table.rot_table[correspondent_doublet1] = parent1.table.rot_table[correspondent_doublet1]
            enfant1.table.rot_table[correspondent_doublet1][2] *= -1

            enfant2.table.rot_table[doublet] = parent2.table.rot_table[doublet]
            correspondent_doublet2 = enfant2.table.corr()[doublet]
            enfant2.table.rot_table[correspondent_doublet2] = parent2.table.rot_table[correspondent_doublet2]
            enfant2.table.rot_table[correspondent_doublet2][2] *= -1
        
        #If it have a value is located in between the generated values it will do the crossover
        else :
            enfant1.table.rot_table[doublet] = parent2.table.rot_table[doublet]
            correspondent_doublet1 = enfant1.table.corr()[doublet]
            enfant1.table.rot_table[correspondent_doublet1] = parent2.table.rot_table[correspondent_doublet1]
            enfant1.table.rot_table[correspondent_doublet1][2] *= -1

            enfant2.table.rot_table[doublet] = parent1.table.rot_table[doublet]
            correspondent_doublet2 = enfant2.table.corr()[doublet]
            enfant2.table.rot_table[correspondent_doublet2] = parent1.table.rot_table[correspondent_doublet1]
            enfant2.table.rot_table[correspondent_doublet2][2] *= -1
        comp += 1
    return enfant1, enfant2
