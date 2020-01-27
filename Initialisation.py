import numpy

ORIGINAL_ROT_TABLE = {\
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
        "TT": [35.62, 7.2, -154, 0.06, 0.6, 0]\
            }

class rotation:
    def __init__(self,doublet):
        self.x = numpy.random.uniform(low = ORIGINAL_ROT_TABLE[doublet][0] - ORIGINAL_ROT_TABLE[doublet][3], high = ORIGINAL_ROT_TABLE[doublet][0] + ORIGINAL_ROT_TABLE[doublet][3])
        self.y = numpy.random.uniform(low = ORIGINAL_ROT_TABLE[doublet][1] - ORIGINAL_ROT_TABLE[doublet][4], high = ORIGINAL_ROT_TABLE[doublet][1] + ORIGINAL_ROT_TABLE[doublet][4])
        self.z = ORIGINAL_ROT_TABLE[doublet][2]
        self.doublet = doublet

class table_rotation(rotation):
    def __init__(self):
        self.dict = {doublet : rotation(doublet) for doublet in ORIGINAL_ROT_TABLE}

table1 = table_rotation()
print(table1.dict["AA"].x)

#table1.dict --> {'AA': <__main__.rotation object at 0x000001A722E1BAC8>, 'AC': <__main__.rotation object at 0x000001A722E1BB00>, 'AG': <__main__.rotation object at 0x000001A729A66A58>, 'AT': <__main__.rotation object at 0x000001A729A66A20>, 'CA': <__main__.rotation object at 0x000001A729A669E8>, 'CC': <__main__.rotation object at 0x000001A729A66A90>, 'CG': <__main__.rotation object at 0x000001A729A66B00>, 'CT': <__main__.rotation object at 0x000001A729A66B70>, 'GA': <__main__.rotation object at 0x000001A729B88D68>, 'GC': <__main__.rotation object at 0x000001A729B88DA0>, 'GG': <__main__.rotation object at 0x000001A729B88DD8>, 'GT': <__main__.rotation object at 0x000001A729B88E10>, 'TA': <__main__.rotation object at 0x000001A729B88E48>, 'TC': <__main__.rotation object at 0x000001A729B88E80>, 'TG': <__main__.rotation object at 0x000001A729B88EB8>, 'TT': <__main__.rotation object at 0x000001A729B88EF0>}
#table1.dict["AA"] ---> <__main__.rotation object at 0x000001A722E1BAC8> (qui est l'object rotation)
#table1.dict["AA"].x ---> 35.67097790545279 (rotation selon x de AA)