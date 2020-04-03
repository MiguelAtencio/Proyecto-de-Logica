import random 
rn1 = random.Random()


def V1(f):

    if f.right == None:
        return LetrasProposicionales[f.label]

    elif f.label == "-":
        return 1 - V1(f.right)
    
    elif f.label == "Y":
        return V1(f.left) * V1(f.right)
    
    elif f.label == "O":
        return max(V1(f.left), V1(f.right))


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

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label
	
	def __str__(self):
	    return Inorder(self)

#Crea todas las letras proposicionales
LetrasProposicionales = dict()

letras = 'ABCDEFGHIJ'
a = ""
for i in letras:
    for x in range(0, 10):
        for j in range(0, 10):
            a += i + str(x) + str(j)
            LetrasProposicionales[a] = rn1.randrange(0, 2)
            a = ""

def sub_regla1():
    #Cada persona solo tiene un estado atributo
    letrap = ""

    for f in range(0,10):
        sele = []
        for j in LetrasProposicionales:
            if j[0] in letras and j[1] == str(f):
                sele.append(j)

        for h in range(0,len(sele)):
            el = sele[h]

            for i in range(0,len(sele)):
                if sele[i] == el:
                    letrap += el

                else:
                    letrap += sele[i]+'-'
            letrap += (len(sele)-1)*'Y'
        letrap += (len(sele)-1)*'O'
    letrap += 9*'Y'

    return letrap



def sub_regla2():
    #Cada estado de atributo solo pertenece a una persona

    letrap = ""

    for f in range(0,10):
        sele = []
        for x in range(0, 10):
            for j in LetrasProposicionales:
                if j[1:] == str(f) + str(x):
                    sele.append(j)

        for h in range(0,len(sele)):
            el = sele[h]

            for i in range(0,len(sele)):
                if sele[i] == el:
                    letrap += el

                else:
                    letrap += sele[i]+'-'
            letrap += (len(sele)-1)*'Y'
        letrap += (len(sele)-1)*'O'
    letrap += 9*'Y'

    return letrap

                

def string2Tree(A):
    #Crea un arbol apartir de un string en inversa polaca
    
    Conectivos = ['O','Y']
    Pila = []
    c = 0
    while c <= len(A) - 3: 
        if A[c] + A[c+1] + A[c+2] in LetrasProposicionales:
            Pila.append(Tree(A[c] + A[c+1] + A[c+2], None, None))
            c += 3

        elif A[c] == '-':
            FormulaAux = Tree(A[c], None, Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
            c += 1

        elif A[c] in Conectivos:
            FormulaAux = Tree(A[c], Pila[-1], Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
            c += 1

    return Pila[-1]

def regla_final(regla1, regla2):
    return Tree("Y", regla1, regla2)

