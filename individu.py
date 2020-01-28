from RotTable import RotTable
from Traj3D import Traj3D
import numpy as np
from math import sqrt
from random import random

P1 = 0.015

class Individu():

    def __init__(self, table):
        self.table = table
        self.score = self.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
    
    def evaluate(self, brin):
        traj = Traj3D()
        traj.compute(brin, self.table)
        traj_array = np.array(traj.getTraj())

        first_nucleotide = traj_array[0, 0:3]
        last_nucleotide = traj_array[-1, 0:3]
        distance = sqrt(sum((first_nucleotide - last_nucleotide) ** 2))

        first_name = brin[0]
        last_name = brin[-1]

        #rot_computed = self.table.rot_table[last_name+first_name]
        #rot_traj = first_nucleotide - last_nucleotide
        # print(rot_traj)
        # print(rot_computed)
        #diff_angle = sum(abs(rot_computed - rot_traj))
        
        self.score = 1/distance

        return 1/distance


    def mutation(self, proba = P1):
        table_rotations = self.table.rot_table
        for doublet in table_rotations :
            for coord in range(3):
                tir = random()
                if tir < proba :
                    table_rotations[doublet][coord] =np.random.uniform(low = self.table.orta()[doublet][coord] - self.table.orta()[doublet][coord + 3], high = self.table.orta()[doublet][coord] + self.table.orta()[doublet][coord + 3])
                    doublet2 = self.table.corr()[doublet]
                    if coord == 0 or coord == 1 :
                        table_rotations[doublet2][coord] = table_rotations[doublet][coord]
                    else :
                        #sur l'axe z il y a un moins
                        table_rotations[doublet2][coord] = - table_rotations[doublet][coord]


# individu1 = Individu(RotTable())
# print(individu1.table.rot_table)
# individu1.mutation()

# table = RotTable()
# test = Individu(table)
# test.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
# print(test.score)


qqun=Individu(RotTable())
qqun.table.rot_table={'AA': [35.576558502141, 7.433901511509349, -154], 'AC': [33.22048222654215, 5.25191751302917, 143], 'AG': [26.446029097301288, 6.052240462237622, -2], 'AT': [30.47045254036881, 1.333716025628036, 0], 'CA': [34.00734209585039, 33.70710613604862, -64], 'CC': [33.61019622767888, 3.713127032109607, -57], 'CG': [29.664061041382677, 6.725155507162601, 0], 'CT': [26.446029097301288, 6.052240462237622, 2], 'GA': [36.655773481637176, 10.45337581740701, 120], 'GC': [42.26984493493484, 3.5310453395352823, 180], 'GG': [33.61019622767888, 3.713127032109607, -57], 'GT': [33.22048222654215, 5.25191751302917, 143], 'TA': [36.951508786388914, -2.5174751178033303, 0], 'TC': [36.655773481637176, 10.45337581740701, -120], 'TG': [34.00734209585039, 33.70710613604862, -64], 'TT': [35.576558502141, 7.433901511509349, -154]}
qqun.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
print(qqun.score)
