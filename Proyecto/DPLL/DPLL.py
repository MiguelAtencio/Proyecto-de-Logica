import sys
sys.path.append('../')

import DPLL.UnitPropagate as UP

def DPLL(S, I):

    if UP.UnitPropagate(S, I):
        S, I = UP.UnitPropagate(S, I)

    if  [] in S:
        #print("caso 1")
        return "Insatisfacible", {}

    if not S:
        #print("caso 2")
        return "Satisfacible", I

    #print("caso 3")
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
        lcomp = l[:0] + l[1:]

    new_S = []
    for i in S:
        new_clause = []
        for x in i:
            if lcomp != x:
                if l not in i:
                    new_clause.append(x)
        if new_clause not in new_S and new_clause:
            new_S.append(new_clause)

    if l[0] == '-':
        I[lcomp] = 0
    else:
        I[l] = 1 
    #print(I)
    res,II=DPLL(new_S,I)
    if res=="Satisfacible":
        #print("caso 3.1")
        return "Satisfacible", II
    
    else:
        #print("caso 3.2")
        new_Sv2 = []
        for i in S:
            new_clause = []
            for x in i:
                if l != x:
                    if lcomp not in i:
                        new_clause.append(x)
            if new_clause not in new_Sv2 and new_clause:
                new_Sv2.append(new_clause)
        if l[0] == '-':
            I[lcomp] = 1
        else:
            I[l] = 0 
        return DPLL(new_Sv2, I)




if __name__ == '__main__':
    b = [['p', 'q', 'r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
    print(DPLL(b, {}))
