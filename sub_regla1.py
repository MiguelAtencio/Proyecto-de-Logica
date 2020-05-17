import codificacion as C
import FNC as fn
import DPLL as dp
import satisfacibilidad as st

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label
	
	def __str__(self):
	    return Inorder(self)

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"
    
Nfilas = 2
Ncolumnas = 2
Nobjeto = 2

#hace la codificacion de las proposiciones
letras = []

for i in range(Nfilas):
    for j in range(Ncolumnas):
        for o in range(Nobjeto):
            v2=C.codifica3(i,j,o,Nfilas,Ncolumnas,Nobjeto)
            cod = chr(v2 + 256)
            letras.append(cod)

#diseña la subregla1 "cada persona solo tiene 1 atributo" con la nueva codificacion
def subregla1NC(Nfilas,Ncols,Nobjs,letras):
    regla1=""
    for k in range(0,Nfilas): #Nfilas->nacionalidad
        for j in range(0,Ncols): #Ncols->atributos
            litt=[]
            for i in letras:
                s,q,r=C.decodifica3(ord(i)-256,Nfilas,Ncols,Nobjs)
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
        regla1+=(Ncols-1)*"Y"
    regla1+=(Nfilas-1)*"Y"
    return regla1

def string2Tree(A):
    #Crea un arbol apartir de un string en inversa polaca
    Conectivos = ['O','Y']
    Pila = []
    for c in A:
        if c in letras:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            formulaAux=Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(formulaAux)
        elif c in Conectivos:
            formulaAux=Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(formulaAux)
    return Pila[-1]

R1=subregla1NC(Nfilas,Ncolumnas,Nobjeto,letras)
tR1=string2Tree(R1)
TR1=str(tR1)
#se pasa a Tseitin para que genere una formula equisatisfacible mas sencilla que TR1
teis=fn.Tseitin(TR1,letras)
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
    if j in letras:
        if I[j]==1:
            I2[j]=1
        else:
            I2[j]=0

de=st.VI(tR1,I2)
print(de)
