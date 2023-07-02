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
    '''

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
    x = 0  # this var represents truth of statement

def antisymmetric(set):
    pass

def main():
    set,universe = pulling_setANDuniverse()
    set_properties = []
    set_properties.append(symmetry(set))
    set_properties.append(reflexivity(set,universe))
    print(set_properties)


main()