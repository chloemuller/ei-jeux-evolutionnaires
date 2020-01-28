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


    def mutation(self, proba = P1):
        table_rotations = self.table.rot_table
        for doublet in table_rotations :
            for coord in range(3):
                tir = random()
                if tir < proba :
                    print("mutation", doublet, coord)
                    print("table", table_rotations[doublet][coord])
                    table_rotations[doublet][coord] =np.random.uniform(low = self.table.orta()[doublet][coord] - self.table.orta()[doublet][coord + 3], high = self.table.orta()[doublet][coord] + self.table.orta()[doublet][coord + 3])
                    print("table", table_rotations[doublet][coord])

individu1 = Individu(RotTable())
print(individu1.table.rot_table)
individu1.mutation()