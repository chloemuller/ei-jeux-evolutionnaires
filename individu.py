from RotTable import RotTable
from Traj3D import *
import numpy as np
from math import sqrt

class Individu():

    def __init__(self, table):
        self.table = table
        self.score = None
    
    def evaluate(self, brin):
        traj = Traj3D()
        traj.compute(brin, self.table)
        traj_array = np.array(traj.getTraj())
        print(traj_array)
        first_nucleotide = traj_array[0, 0:3]
        last_nucleotide = traj_array[-1, 0:3]
        print(first_nucleotide)
        print(last_nucleotide)
        distance = sqrt(sum((first_nucleotide - last_nucleotide) ** 2))
        diff_ideal_distance = abs(3.38 - distance)

        self.score = 1/(diff_ideal_distance )
        
    
    def mutation(self):
        mutation = 0
        return mutation

table = RotTable()
test = Individu(table)
test.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
print(table.rot_table)
print(test.score)
