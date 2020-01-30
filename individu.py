from RotTable import RotTable
from Traj3D import Traj3D
import numpy as np
from math import sqrt, inf
from random import random, choice

P1 = 0.015

class Individu():
    ''' Un individu est caractérisé par sa table de rotations (individu.table)'''
    
    def __init__(self, table, filename):
        self.table = table
        lineList = [line.rstrip('\n') for line in open(filename)]
        self.brin = ''.join(lineList[1:])
        self.score = None
        self.distance = None

    def evaluate(self):
        ''' Evalue le score d'un individu sur un nombre numb_ajout de points'''
        # The last numb_ajout dinucleotides of the "ribbon" are joined at its beginning,
        # and the first numb_ajout dinucleotides are joined at the end of it.
        # This "new parts" of the sequence will be compared with the real beginning and end of the the ribbon.
        # If they coincide, then the chromosome is circular
        
        traj = Traj3D()

        numb_ajout = 50

        # the first and the last numb_ajout dinucleotides respectively
        first_seq = self.brin[0:numb_ajout]
        last_seq = self.brin[-numb_ajout:]

        # creation of the "new ribbon"
        traj.compute(last_seq + self.brin + first_seq, self.table)
        traj_array = traj.getTraj()

        list_distance = []

        begining = traj_array[0:2*numb_ajout]
        end = traj_array[-2*numb_ajout:]

        # score calculation, comparing the new ribbon with the real sequence,
        # according to the distance of the correspondent dinucleotides
        for i in range(numb_ajout):

                nuc_coordonate_beg = begining[i]
                nuc_coordonate_end = end[i]
                distance_nuc = np.linalg.norm(nuc_coordonate_beg - nuc_coordonate_end, ord=2)
                list_distance += [distance_nuc]
        

        self.score = max(list_distance)
        self.distance = np.linalg.norm(traj_array[numb_ajout] - traj_array[-(numb_ajout+1)], ord=2)


    def mutation(self, proba = P1):
        # each dinucleotide has a probability "proba" to mutate
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
        # each individual has a probability "proba" to be mutated
        # if it mutates, then a number "number_of_mutations" of chromosomes will be randomly mutated
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
        # each individual has a probability "proba" to be mutated
        # if it mutates, then a number "number_of_mutations" of chromosomes will be randomly mutated
        # according to the normal distribution around the current value of the dinucleotide
        table_rotations = self.table.rot_table
        table_rotation_not_seen = [i for i in sorted(table_rotations.keys())]
        table_rotation_not_seen = table_rotation_not_seen[:8]

        tir = random()
        if tir < proba :
            for i in range(0,number_of_mutations):

                doublet = choice(table_rotation_not_seen)
                table_rotation_not_seen.remove(doublet)

                for coord in range(3):
                    value = table_rotations[doublet][coord] + np.random.normal(0, self.table.orta()[doublet][coord + 3]/10)
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
