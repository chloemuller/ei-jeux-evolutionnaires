from Initialisation import table_rotation
from Traj3D import *
import numpy as np
from math import sqrt

class Individu():

    def __init__(self, rot_table):
        self.rot_table = rot_table
        self.score = None
    
    def evaluate(self, brin):
        traj = Traj3D()
        traj.compute(brin, self.rot_table)
        traj_array = np.array(traj.getTraj())

        first_nucleotide = traj_array[0, :]
        last_nucleotide = traj_array[-1, :]
        distance = sqrt(sum((first_nucleotide - last_nucleotide) ** 2))

        first_name = brin[0]
        last_name = brin[-1]

        rot_computed = self.rot_table[last_name+first_name]
        rot_traj = first_name - last_name
        diff_angle = sum(abs(rot_computed - rot_traj))

        self.score = 1/(distance + diff_angle)
        
    
    # def mutation(self):

    #     return mutation

individu1 = Individu(table_rotation())
print(individu1.rot_table.dict["AA"].x)