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

LetrasProposicionales = dict()

letras = 'ABCDEFGHIJ'
a = ""
for i in letras:
    for x in range(0, 10):
        for j in range(0, 10):
            a += i + str(x) + str(j)
            LetrasProposicionales[a] = "LDSAF"
            a = ""


def subregla2():
    #Cada estado de atributo solo pertenece a una persona
    pass



def string2Tree(A):
    Conectivos = ['O','Y']
    Pila = list()
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

