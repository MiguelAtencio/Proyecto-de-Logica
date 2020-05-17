import sys
sys.path.append('../')

import FNC.FNC as fn
import DPLL.DPLL as dp
import Codificacion.Codificacion as cf
import Tree.Tree as t

import time


Nf = 8
Nc = 8
No = 8

letrasProposicionales = []
for i in range(Nf):
    for x in range(Nc):
        for h in range(No):
            v2 = cf.codifica3(i, x, h, Nf, Nc, No)
            letrasProposicionales.append(chr(256 + v2))


def subregla1NC(Nf,Nc,No,letras):
    regla1=""
    for k in range(0,Nf): #Nfilas->nacionalidad
        for j in range(0,Nc): #Ncols->atributos
            litt=[]
            for i in letras:
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

def sub_regla2(Nf,Nc,No):
    letrap = ''
    for i in range(0, 8):
        for h in range(0, 8):
            for x in range(0, 8):
                for j in range(0, 8):
                    if j == x:
                        a = cf.codifica3(j, i, h, Nf, Nc, No)
                        a = chr(a+256)
                        letrap += '{}'.format(a)
                    else:
                        a = cf.codifica3(j, i, h, Nf, Nc, No)
                        a = chr(a+256)
                        letrap += '{}-'.format(a)
                letrap += (Nf-1)*'Y'
            letrap += (Nc-1)*'O'
    letrap += (No-1)*'Y'
    return letrap


def sub_regla2Inorder(Nf,Nc,No):
    letrap = ''
    for i in range(0, 8):
        for h in range(0, 8):
            letrap += '('
            for x in range(0, 8):
                letrap += '('
                for j in range(0, 8):
                    if j == x:
                        a = cf.codifica3(j, i, h, Nf, Nc, No)
                        b = chr(a+256)
                        letrap += '{}'.format(b)
                    else:
                        a = cf.codifica3(j, i, h, Nf, Nc, No)
                        b = chr(a+256)
                        letrap += '-{}'.format(b)
                    if j != 7:
                        letrap += 'Y'
                if x != 7: letrap += ')O'
                else: letrap += ')'
            if h != 7: letrap += ')Y'
            else: letrap += ')'
    return letrap


def regla_final():
    a = ip.StringToTree(sub_regla1())
    b = ip.StringToTree(sub_regla2())
    return ip.Tree('Y', a, b)


if __name__ == '__main__':

    t1 = time.time()
    R1=subregla1NC(Nf,Nc,No,letrasProposicionales)
    tR1=t.StringToTree(R1)
    TR1=str(tR1)
    #se pasa a Tseitin para que genere una formula equisatisfacible mas sencilla que TR1
    teis=fn.Tseitin(TR1,letrasProposicionales)
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
    print(I2)
    t2 = time.time()
    tf = t2 - t1
    tf /= 60
    print(tf, 'min')



