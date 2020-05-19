import sys
sys.path.append('../')

import DPLL.UnitPropagate as UP

def DPLL(S, I):

    #if UnitPropagate(S, I):
    S, I = UnitPropagate(S, I)
    print(I)
    if  [] in S:
        
        return "Insatisfacible", {}

    if not S:
        return "Satisfacible", I

    l=""
    for i in S:
        for x in i:
            if x not in I:
                l = x
                break
        if l:
            break

    if l[0] != '-':
        lcomp = '-'+l
    elif l[0] == '-':
        lcomp = l[1]

    new_S = []
    for i in S:
        new_clause = []
        for x in i:
            if lcomp != x:
                if l not in i:
                    new_clause.append(x)
        if new_clause not in new_S and new_clause:
            new_S.append(new_clause)
    print(I)
    if len(l)>1:
        I[lcomp] = 0
    else:
        I[l]=1
    print(I)
    res,II=DPLL(new_S,I)
    print(I)
    if res=="Satisfacible":
        return "Satisfacible", II
    else:
        new_Sv2 = []
        for i in S:
            new_clause = []
            for x in i:
                if l != x:
                    if lcomp not in i:
                        new_clause.append(x)
            if new_clause not in new_Sv2 and new_clause:
                new_Sv2.append(new_clause)
        if len(l)>1:
            I[lcomp] = 1
        else:
            I[l]=0
        return DPLL(new_Sv2, I)


############################################################

b = [['p', 'q', 'r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
print(DPLL(b, {}))
