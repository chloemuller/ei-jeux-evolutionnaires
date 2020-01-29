from RotTable import RotTable
from Traj3D import Traj3D
import numpy as np
from math import sqrt, inf
from random import random, choice

P1 = 0.015

class Individu():
    ''' Un individu est caractérisé par sa table de rotations (individu.table)'''
    def __init__(self, table):
        lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
        brin = ''.join(lineList[1:])
        self.table = table
        lineList = [line.rstrip('\n') for line in open("plasmid_8k.fasta")]
        self.brin = ''.join(lineList[1:])
        #self.brin = "AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA"
        self.score = None

    def evaluate(self):
        ''' Evalue le score d'un individu sur un nombre numb_ajout de points'''
        
        
        traj = Traj3D()

        numb_ajout = 100

        fisrt_seq = self.brin[0:numb_ajout]
        last_seq = self.brin[-numb_ajout:]

        traj.compute(last_seq + self.brin + fisrt_seq, self.table)
        traj_array = traj.getTraj()

        list_distance = []

        begining = traj_array[0:2*numb_ajout]
        end = traj_array[-2*numb_ajout:]

        for i in range(numb_ajout):

                nuc_coordonate_beg = begining[i]
                nuc_coordonate_end = end[i]
                distance_nuc = np.linalg.norm(nuc_coordonate_beg - nuc_coordonate_end, ord=2)
                list_distance += [distance_nuc]


        self.score = max(list_distance)

        #return max(list_distance)


    def mutation(self, proba = P1):
        table_rotations = self.table.rot_table
        for doublet in sorted(table_rotations.keys()) :
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

    def mutation_with_numbers(self, proba = P1, number_of_mutations = 1):
        table_rotations = self.table.rot_table
        table_rotation_not_seen = [i for i in sorted(table_rotations.keys())]
        table_rotation_not_seen = table_rotation_not_seen[:8]

        tir = random()
        if tir < proba :
            for i in range(0,number_of_mutations):
                
                doublet = choice(table_rotation_not_seen)
                table_rotation_not_seen.remove(doublet)

                for coord in range(3):
                    table_rotations[doublet][coord] =np.random.uniform(low = self.table.orta()[doublet][coord] - self.table.orta()[doublet][coord + 3], high = self.table.orta()[doublet][coord] + self.table.orta()[doublet][coord + 3])
                    doublet2 = self.table.corr()[doublet]
                    if coord == 0 or coord == 1 :
                        table_rotations[doublet2][coord] = table_rotations[doublet][coord]
                    else :
                        #sur l'axe z il y a un moins
                        table_rotations[doublet2][coord] = - table_rotations[doublet][coord]


    def mutation_close_values(self, proba = P1, number_of_mutations = 1):
        table_rotations = self.table.rot_table
        table_rotation_not_seen = [i for i in sorted(table_rotations.keys())]
        table_rotation_not_seen = table_rotation_not_seen[:8]

        tir = random()
        if tir < proba :
            for i in range(0,number_of_mutations):

                doublet = choice(table_rotation_not_seen)
                table_rotation_not_seen.remove(doublet)

                for coord in range(3):
                    value = table_rotations[doublet][coord] + np.random.normal(0, self.table.orta()[doublet][coord + 3]/15)
                    if value > self.table.orta()[doublet][coord] + self.table.orta()[doublet][coord + 3]:
                        value = self.table.orta()[doublet][coord] + self.table.orta()[doublet][coord + 3]
                    elif value < self.table.orta()[doublet][coord] - self.table.orta()[doublet][coord + 3]:
                        value = self.table.orta()[doublet][coord] - self.table.orta()[doublet][coord + 3]
                    table_rotations[doublet][coord] = value
                    
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


# qqun=Individu(RotTable())
# qqun.table.rot_table={'AA': [35.576558502141, 7.433901511509349, -154], 'AC': [33.22048222654215, 5.25191751302917, 143], 'AG': [26.446029097301288, 6.052240462237622, -2], 'AT': [30.47045254036881, 1.333716025628036, 0], 'CA': [34.00734209585039, 33.70710613604862, -64], 'CC': [33.61019622767888, 3.713127032109607, -57], 'CG': [29.664061041382677, 6.725155507162601, 0], 'CT': [26.446029097301288, 6.052240462237622, 2], 'GA': [36.655773481637176, 10.45337581740701, 120], 'GC': [42.26984493493484, 3.5310453395352823, 180], 'GG': [33.61019622767888, 3.713127032109607, -57], 'GT': [33.22048222654215, 5.25191751302917, 143], 'TA': [36.951508786388914, -2.5174751178033303, 0], 'TC': [36.655773481637176, 10.45337581740701, -120], 'TG': [34.00734209585039, 33.70710613604862, -64], 'TT': [35.576558502141, 7.433901511509349, -154]}
# qqun.evaluate("AAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCCAGTAAACGAAAAAACCGCCTGGGGAGGCGGTTTAGTCGAA")
# print(qqun.score)
