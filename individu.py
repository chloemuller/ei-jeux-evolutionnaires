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

        first_nucleotide = traj_array[0, 0:3]
        last_nucleotide = traj_array[-1, 0:3]
        distance = sqrt(sum((first_nucleotide - last_nucleotide) ** 2))

        first_name = brin[0]
        last_name = brin[-1]

        rot_computed = self.table.Rot_Table[last_name+first_name]
        rot_traj = first_nucleotide - last_nucleotide
        print(rot_traj)
        print(rot_computed)
        diff_angle = sum(abs(rot_computed - rot_traj))

        self.score = 1/(distance + diff_angle)
        
    
    def mutation(self):
        mutation = 0
        return mutation

table = RotTable()
test = Individu(table)
test.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
print(test.score)
