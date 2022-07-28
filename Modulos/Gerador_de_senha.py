from random import randint

class Gerador:     
    def gera_senha():    
        letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]

        base_numeros = []
        base_letras = []
        senha = ["", "", "", "", "", ""]

        for i in range(0, 2):
            numeros = randint(0, 9)
            base_numeros.append(numeros)
        
        for i in range(0, 4): 
            sort = randint(0, 24)
            carac = letras[sort]
            base_letras.append(carac)

        senha[2] = base_numeros[0]
        senha[5] = base_numeros[1]
        
        senha[0] = base_letras[0]
        senha[1] = base_letras[1]
        senha[3] = base_letras[2]
        senha[4] = base_letras[3]

        senhaSTR = ''.join(map(str, senha))
        
        return senhaSTR