def UnitPropagate(S,I):

    co=0
    for i in S:
        if len(i)==1:
            co+=1
    if co>0:
        while ([] not in S) and co>0:
            for j in S:
                if len(j)==1:
                    k=j[0]
                    break
            l=S[:]
            for h in l:
                if k in h:
                    S.remove(h)
            if len(k)==2:
                I[k[1]]=0
                for h in S:
                    if k[1] in h:
                        h.remove(k[1])
            else:
                I[k]=1
                t='-'+k
                for h in S:
                    if t in h:
                        h.remove(t)
            co=0
            for i in S:
                if len(i)==1:
                    co+=1
    
    return S,I
