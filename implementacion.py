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

LETRAS = []
a = ''
for i in letras:
    for x in range(0, 10):
        for j in range(0, 10):
            a += i + str(x) + str(j)
            LETRAS.append(a)
            a = ""



def sub_regla1():
    #Cada persona solo tiene un estado atributo
    letrap = ""

    for f in range(0,10):
        sele = []
        for j in LetrasProposicionales:
            if j[1] == str(f):
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
    letrap = ''
    for i in range(0, 10):
        for h in range(0, 10):
            for x in range(0, 10):
                for j in letras:
                    if j == letras[x]:
                        letrap += j + str(i) + str(h)
                    else:
                        letrap += j + str(i) + str(h) + '-'
                    
                letrap += 9*'Y'
            letrap += 9*'O'
        letrap += 9*'Y'
    letrap += 9*'Y'
    #print(letrap)
    return letrap


def StringToTree(A):
    Conectivos = ['O','Y']
    stack = []
    for c in range(len(A)):
        if c + 2 < len(A)-1 and A[c] + A[c+1] + A[c+2] in LETRAS:
            aux = Tree(A[c] + A[c+1] + A[c+2], None, None)
            stack.append(aux)
        elif A[c] == '-':
            aux = Tree(A[c], None, stack[-1])
            del stack[-1]
            stack.append(aux)
        elif A[c] in Conectivos:
            aux = Tree(A[c], stack[-2], stack[-1])
            del stack[-1]
            del stack[-1]
            stack.append(aux)

    return stack[-1]




def regla_final(regla1, regla2):
    return Tree("Y", regla1, regla2)


if __name__ == "__main__":
    print(StringToTree(sub_regla2()))


