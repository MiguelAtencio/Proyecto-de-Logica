import FNC.FNC as fn
import DPLL.DPLL as dp
import Codificacion.Codificacion as cf
import Tree.Tree as t

Nf = 9 # numero de personas
Nc = 9 # numero de atributos
No = 9 #numero de estados por atributo

#se codifican las letras proposicionales de acuerdo al numero de atributos a usar
letrasProposicionales = []
for i in range(Nf):
    for x in range(Nc):
        for h in range(No):
            v2 = cf.codifica3(i, x, h, Nf, Nc, No)
            letrasProposicionales.append(chr(256 + v2))


 #se crea la regla 1
def subregla1NC(Nf,Nc,No):
    regla1=""
    for k in range(0,Nf): #Nfilas->nacionalidad
        for j in range(0,Nc): #Ncols->atributos
            litt=[]
            for i in letrasProposicionales:
                s,q,r=cf.decodifica3(ord(i)-256,Nf,Nc,No)
                if s==k and q==j:
                    litt.append(i)
            for h in range(0,len(litt)):
                ell=litt[h]
                for t in range(0,len(litt)):
                    if litt[t]==ell:
                        regla1 +=ell
                    else:
                        regla1+=litt[t]+'-'
                regla1+=(len(litt)-1)*"Y"
            regla1+=(len(litt)-1)*"O"
        regla1+=(Nc-1)*"Y"
    regla1+=(Nf-1)*"Y"
    return regla1

# se crea la regla 2
def sub_regla2NC(Nf, Nc, No):
    letrap=""
    for k in range(0,Nf): #Nfilas->nacionalidad
        for j in range(0,Nc): #Ncols->atributos
            litt=[]
            for i in letrasProposicionales:
                s,q,r=cf.decodifica3(ord(i)-256,Nf,Nc,No)
                if q==j and r==k:
                    #print(s, q, r)
                    litt.append(i)
            for h in range(0,len(litt)):
                ell=litt[h]
                for t in range(0,len(litt)):
                    if litt[t]==ell:
                        letrap +=ell
                    else:
                        letrap+=litt[t]+'-'
                letrap+=(len(litt)-1)*"Y"
            letrap+=(len(litt)-1)*"O"
        letrap+=(Nc-1)*"Y"
    letrap+=(Nf-1)*"Y"
    return letrap


# se crea la regla final como la conjuncion de las dos subreglas
def regla_final(regla1, regla2):
    a = t.StringToTree(regla1)
    b = t.StringToTree(regla2)
    return t.Tree('Y', a, b)


if __name__ == '__main__':
 
    R1=subregla1NC(Nf,Nc,No)
    R2 = sub_regla2NC(Nf, Nc, No)
    RF = regla_final(R1, R2)

    TRF = str(RF)
    
    #se pasa a Tseitin para que genere una formula equisatisfacible mas sencilla que TR1
    teis=fn.Tseitin(TRF,letrasProposicionales)
    #pasando a forma clausal
    hk=fn.formaClausal(teis)
    #se ingresa al DPLL
    S,I=dp.DPLL(hk,{})
    #ii es una lista con las letras proposicionales de la interpretacion I
    ii=list(I.keys())
    I2={}
    #este ciclo selecciona todas las letrasproposicionales que estan en letras(lista original con codificacion) y crea un nuevo diccionario
    #I2 donde se guardan solo esas letras que son las de interes.
    for j in ii:
        if j in letrasProposicionales:
            if I[j]==1:
                I2[j]=1
            else:
                I2[j]=0

    #print(len(I2))
    # aqui se imprime la interpretacion que encuentra el programa, es decir una solucion al problema
    print(I2)



