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

        fisrt_nuc = brin[0]
        last_nu = brin[-1]

        traj.compute(brin + fisrt_nuc, self.table)
        traj_array = np.array(traj.getTraj())

        first_nuc_coordonate = traj_array[0, 0:3]
        last_nuc_coordonate = traj_array[-2, 0:3]

        test = np.linalg.norm(first_nuc_coordonate - last_nuc_coordonate, ord=2)
        distance = sqrt(sum((first_nuc_coordonate - last_nuc_coordonate) ** 2))
        diff_ideal_distance = abs(3.38 - distance)
        diff_ideal_distance_2 = abs(3.38 - test)
        self.score = (1/(diff_ideal_distance ), 1/diff_ideal_distance_2)
        
    
    def mutation(self):
        mutation = 0
        return mutation

table = RotTable()
test = Individu(table)
test.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
print(table.rot_table)
print(test.score)
