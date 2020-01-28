import numpy
from RotTable import RotTable

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
    enfant1 = RotTable()
    enfant2 = RotTable()
    comp = 0
    point_crois= numpy.random.random_integers(0,16)
    for doublet in ROT_TABLE:
        if comp < point_crois:
            enfant1.rot_table[doublet] = parent1.rot_table[doublet]
            enfant2.rot_table[doublet] = parent2.rot_table[doublet]
        else :
            enfant1.rot_table[doublet] = parent2.rot_table[doublet]
            enfant2.rot_table[doublet] = parent1.rot_table[doublet]
        comp += 1
    return enfant1, enfant2


def croisement_deux_points(parent1, parent2):
    enfant1 = RotTable()
    enfant2 = RotTable()
    comp = 0
    point_crois1= numpy.random.random_integers(0,16)
    point_crois2= numpy.random.random_integers(0,16)
    for doublet in ROT_TABLE:
        if comp < min(point_crois1,point_crois2) or comp > max(point_crois1,point_crois2):
            enfant1.rot_table[doublet] = parent1.rot_table[doublet]
            enfant2.rot_table[doublet] = parent2.rot_table[doublet]
        else :
            enfant1.rot_table[doublet] = parent2.rot_table[doublet]
            enfant2.rot_table[doublet] = parent1.rot_table[doublet]
        comp += 1
    return enfant1, enfant2