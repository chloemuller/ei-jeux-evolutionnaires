from RotTable import RotTable
from Traj3D import *
import numpy as np
from math import sqrt
from random import random

P1 = 0.015

class Individu():

    def __init__(self, table):
        self.table = table
        self.score = None
    
    def evaluate(self, brin):
        traj = Traj3D()
        traj.compute(brin, self.table)
        traj_array = np.array(traj.getTraj())

        first_nucleotide = traj_array[0, :]
        last_nucleotide = traj_array[-1, :]
        distance = sqrt(sum((first_nucleotide - last_nucleotide) ** 2))

        first_name = brin[0]
        last_name = brin[-1]

        rot_computed = self.table[last_name+first_name]
        rot_traj = first_name - last_name
        diff_angle = sum(abs(rot_computed - rot_traj))

        self.score = 1/(distance + diff_angle)
        
    
    __ORIGINAL_ROT_TABLE = {\
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


    def mutation(self, proba = P1):
        table_rotations = self.table.rot_table
        for doublet in table_rotations :
            for coord in range(3):
                tir = random()
                if tir < proba :
                    print("mutation", doublet, coord)
                    print("table", table_rotations[doublet][coord])
                    table_rotations[doublet][coord] =np.random.uniform(low = Individu.__ORIGINAL_ROT_TABLE[doublet][coord] - Individu.__ORIGINAL_ROT_TABLE[doublet][coord + 3], high = Individu.__ORIGINAL_ROT_TABLE[doublet][coord] + Individu.__ORIGINAL_ROT_TABLE[doublet][coord + 3])
                    print("table", table_rotations[doublet][coord])

individu1 = Individu(RotTable())
print(individu1.table.rot_table)
individu1.mutation()