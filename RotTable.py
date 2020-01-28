import mathutils
import math
import numpy

class RotTable:
    """Represents the rotation table"""

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
        "TT": [35.62, 7.2, 154, 0.06, 0.6, 0]\
        }

    __CORRESPONDANCE = {\
        "AA": "TT",\
        "AC": "GT",\
        "AG": "CT",\
        "AT": "AT",\
        "CA": "TG",\
        "CC": "GG",\
        "CG": "CG",\
        "CT": "AG",\
        "GA": "TC",\
        "GC": "GC",\
        "GG": "CC",\
        "GT": "AC",\
        "TA": "TA",\
        "TC": "GA",\
        "TG": "CA",\
        "TT": "AA"\
        }

    __SOUS_CORRESPONDANCE = {\
        "AA": "TT",\
        "AC": "GT",\
        "AG": "CT",\
        "AT": "AT",\
        "CA": "TG",\
        "CC": "GG",\
        "CG": "CG",\
        "GA": "TC",\
        "GC": "GC",\
        "TA": "TA"\
        }
    # get the angles in each axis (x, y, z), considering the deviation
    def __init__(self):
        self.rot_table = {}
        for dinucleotide in RotTable.__ORIGINAL_ROT_TABLE:
            self.rot_table[dinucleotide] = RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][:3]
        self.alea()

    # get a random deviation, considering the "limits" given in the last 3 columns
    # of __ORIGINAL_ROT_TABLE
    def alea(self):
        for dinucleotide in RotTable.__SOUS_CORRESPONDANCE:
            for i in range(2):
                delta = numpy.random.uniform(low = -RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][i+3], high= RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][i+3])
                self.rot_table[dinucleotide][i] += delta
                self.rot_table[RotTable.__SOUS_CORRESPONDANCE[dinucleotide]][i] += delta

    # return __ORIGINAL_ROT_TABLE
    def orta(self):
        return self.__ORIGINAL_ROT_TABLE
    
    def corr(self):
        return self.__CORRESPONDANCE

    ###################
    # WRITING METHODS #
    ###################
    #table = RotTable()
    #table.rot_table["AA"] --> [35.62, 7.2, -154]

    ###################
    # READING METHODS #
    ###################

    def getTwist(self, dinucleotide):
        return RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][0]

    def getWedge(self, dinucleotide):
        return RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][1]

    def getDirection(self, dinucleotide):
        return RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][2]

    ###################

table1 = RotTable()

# print(table1.rot_table)
