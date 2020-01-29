import numpy
from RotTable import RotTable
from individu import Individu

ROT_TABLE = {\
        "AA": [35.62, 7.2, -154, 0.06, 0.6, 0],\
        "AC": [34.4, 1.1, 143, 1.3, 5, 0],\
        "AG": [27.7, 8.4, 2, 1.5, 3, 0],\
        "AT": [31.5, 2.6, 0, 1.1, 2, 0],\
        "CA": [34.5, 3.5, -64, 0.9, 34, 0],\
        "CC": [33.67, 2.1, -57, 0.07, 2.1, 0],\
        "CG": [29.8, 6.7, 0, 1.1, 1.5, 0],\
        "CT": [27.7, 8.4, -2, 1.5, 3, 0],\
        "GA": [36.9, 5.3, 120, 0.9, 6, 0],\
        "GC": [40, 5, 180, 1.2, 1.275, 0],\
        "GG": [33.67, 2.1, 57, 0.07, 2.1, 0],\
        "GT": [34.4, 1.1, -143, 1.3, 5, 0],\
        "TA": [36, 0.9, 0, 1.1, 2, 0],\
        "TC": [36.9, 5.3, -120, 0.9, 6, 0],\
        "TG": [34.5, 3.5, 64, 0.9, 34, 0],\
        "TT": [35.62, 7.2, -154, 0.06, 0.6, 0]\
            }


def croisement_un_point(parent1, parent2):
    '''Croise les tables de rotation des parents pour former deux enfants en respectant les symétries du problème'''
    ''' Retourne deux enfants'''
    enfant1 = Individu(RotTable())
    enfant2 = Individu(RotTable())
    comp = 0
    point_crois= numpy.random.random_integers(0,8)
    list_dinucleotides = sorted(ROT_TABLE)
    for doublet in list_dinucleotides:
        if doublet == "GA":
            break
        if comp < point_crois:
            enfant1.table.rot_table[doublet] = parent1.table.rot_table[doublet]
            correspondent_doublet1 = enfant1.table.corr()[doublet]
            enfant1.table.rot_table[correspondent_doublet1] = parent1.table.rot_table[correspondent_doublet1]
            enfant1.table.rot_table[correspondent_doublet1][2] *= -1

            enfant2.table.rot_table[doublet] = parent2.table.rot_table[doublet]
            correspondent_doublet2 = enfant2.table.corr()[doublet]
            enfant2.table.rot_table[correspondent_doublet2] = parent2.table.rot_table[correspondent_doublet2]
            enfant2.table.rot_table[correspondent_doublet2][2] *= -1
        
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
    for doublet in list_dinucleotides:
        if comp < min(point_crois1,point_crois2) or comp > max(point_crois1,point_crois2):
            enfant1.table.rot_table[doublet] = parent1.table.rot_table[doublet]
            correspondent_doublet1 = enfant1.table.corr()[doublet]
            enfant1.table.rot_table[correspondent_doublet1] = parent1.table.rot_table[correspondent_doublet1]
            enfant1.table.rot_table[correspondent_doublet1][2] *= -1

            enfant2.table.rot_table[doublet] = parent2.table.rot_table[doublet]
            correspondent_doublet2 = enfant2.table.corr()[doublet]
            enfant2.table.rot_table[correspondent_doublet2] = parent2.table.rot_table[correspondent_doublet2]
            enfant2.table.rot_table[correspondent_doublet2][2] *= -1
        
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

# parent1 = Individu(RotTable())
# parent2 = Individu(RotTable())
# print("parent1: ", parent1.table.rot_table)
# print("parent2: ", parent2.table.rot_table)
# enfant1, enfant2 = croisement_un_point(parent1, parent2)
# print("enfant1: ", enfant1.table.rot_table)
# print("enfant2: ", enfant2.table.rot_table)