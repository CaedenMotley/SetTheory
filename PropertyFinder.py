"""
    File: PropertyFinder.py
    Author: Caeden Motley
    Purpose: This program will take in the set contained in the MySet file
    as well as the Universe of the aforementioned set and determine if the set
    is symmetric, reflexive, transitive, and or anti-symmetric.
    this data is represented in the SetProperties list as 1's and 0's (True and
    False respectively) it is represented in the following order:

    [Symmetric, Reflexive, Transitive, Anti-Symmetric]

    from this it is also determined if the set is an equivalence relation,
    partial ordering, irreflexive partial ordering, and or well ordered

    Final data will be written to the MySet text file
"""


def pulling_setANDuniverse():
    f = open('MySet', 'r')
    f.readline()
    # eval is the cleanest and fastest way to convert here i believe
    set = eval(f.readline())
    f.readline()
    f.readline()
    universe = eval(f.readline())
    f.close()
    return set,universe
def symmetry(set):
    ''' This will determine if the set is symmetrical, this will be the FIRST
    value in the set property list [0]

    :param set: the users set
    :return: returns whether it is symmetric or not as 1 being sym. and 0
    being not sym.
    '''
    x = 0 # this var represents truth of statement
    for subset in set:
        subset = subset.split(',')
        y = (subset[1] + ',' + subset[0])
        if (subset[1] + ',' + subset[0]) in set:
            x = 1
        else:
            x = 0
            break

    return x



def reflexivity(set, universe):
    ''' this function determines the reflexivity of the set

    :param set: the users desired set
    :return: whether it is reflexive 1 or not reflexive 0. will occupy SECOND
    slot of SetProperties [1]
    '''

    x = 0 # this var represents truth of statement
    for var in universe:
        if (var + ',' + var) in set:
            x = 1
        else:
            x = 0
            break
    return x

def transitivity(set):
    x = 0 # this var represents truth of statement
    trans_relation = [] # this represents the transitive relationship

    # upper level for loop checks for (a,b) and (a,c)
    for subset in set:
        subset = subset.split(',')
        # nested for loop checks for a (b,c) relationship
        for x in set:
            x = x.split(',')
            if subset[1] == x[0] and subset != x:
                trans_relation.append(','.join(x))
                break




def antisymmetric(set):
    pass

def main():
    set,universe = pulling_setANDuniverse()
    set_properties = []
    set_properties.append(symmetry(set))
    set_properties.append(reflexivity(set,universe))
    set_properties.append(transitivity(set))
    print(set_properties)


main()
