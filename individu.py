from RotTable import RotTable
from Traj3D import *
import numpy as np
from math import sqrt, inf

class Individu():

    def __init__(self, table):
        self.table = table
        self.score = None
    
    def evaluate(self, brin):
        traj = Traj3D()

        numb_ajout = 3

        fisrt_seq = brin[0:numb_ajout]
        last_seq = brin[-numb_ajout:]

        traj.compute(last_seq + brin + fisrt_seq, self.table)
        traj_array = np.array(traj.getTraj())

        list_distance = []

        for i in range(numb_ajout):
                first_nuc_coordonate = traj_array[numb_ajout+i, 0:3]
                first_nuc_coordonate_compute = traj_array[-(numb_ajout-i), 0:3]
                
                last_nuc_coordonate = traj_array[-(2*numb_ajout-i), 0:3]
                last_nuc_coordonate_compute = traj_array[i, 0:3]

                distance_first_nuc = np.linalg.norm(first_nuc_coordonate - first_nuc_coordonate_compute, ord=2)
                distance_last_nuc = np.linalg.norm(last_nuc_coordonate - last_nuc_coordonate_compute, ord=2)

                list_distance += [distance_first_nuc, distance_last_nuc]


        self.score = 1/max(list_distance)
        
    
    def mutation(self):
        mutation = 0
        return mutation

table = RotTable()
test = Individu(table)
test.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
print(table.rot_table)
print(test.score)
