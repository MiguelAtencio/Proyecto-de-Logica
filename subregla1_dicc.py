import random
rn1=random.Random()
#sub regla 1 :
letrasproposicionales=[chr(i)+chr(j)+chr(k) for i in range(65,75) for j in range(48,58) for k in range(48,58) ]
letrap=""
for f in range(0,10):
    sele=[]
    for j in letrasproposicionales:
        if j[0]==chr(65+f) and j[1]=='1':
            sele.append(j)
    #print(sele)
    for h in range(0,len(sele)):
        el=sele[h]
        for i in range(0,len(sele)):
            if sele[i]==el:
                letrap +=el
            else:
                letrap+=sele[i]+'-'
        letrap+=(len(sele)-1)*'Y'
    letrap+=(len(sele)-1)*'O'
letrap+=9*'Y'

#crea un dicionario con una interpretacion aleatoria de todas las letras proposicionales
In={}
for i in range(0,len(letrasproposicionales)):
    In[letrasproposicionales[i]]=rn1.randrange(0,2)

