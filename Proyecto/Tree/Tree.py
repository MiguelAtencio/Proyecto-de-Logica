import sys
sys.path.append('../')

import Codificacion.Codificacion as cf
import Reglas as r


letrasProposicionales = r.letrasProposicionales

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


def StringToTree(A):
    Conectivos = ['O','Y']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c == '-':
            FormulaAux = Tree (c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree (c, Pila[-1], Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)

    return Pila[-1]

def V1(f):

    if f.right == None:
        return LetrasProposicionales[f.label]

    elif f.label == "-":
        return 1 - V1(f.right)
    
    elif f.label == "Y":
        return V1(f.left) * V1(f.right)
    
    elif f.label == "O":
        return max(V1(f.left), V1(f.right))

