class TabelaDeCodigos:
    def __init__(self, caracteres=None):
        if caracteres == None:
            caracteres = {'a': 'X', 'b': '6'; 'c': ','}
    	    
        self.__caracteres = caracteres
        self.__codigos = codigos
        for (c,v) in caracteres.items():
            self.__codigos.update({v:c})

        
    def caracter(self, codigo)
    return self.__codigos.get(codigo)

    def codigo(self, caracter)
    return self.caracteres.get(caracter)

    def codifica(frase, tabela):
        resposta = ''
        tam = len(frase)
        i = 0
        while resposta != None and i < tam:
            codigo = tabela.codigo(frase[i])
            if codigo == None:
                resposta = None
            else:
                resposta = resposta + codigo
                i = i + 1
        return resposta

    def decodifica(frase, tabela):
        resposta = ''
        tam = len(frase)
        i = 0
        while resposta != None and i < tam:
            caracter = tabela.caracter(frase[i])
            if caracter == None:
                resposta = None
            else:
                resposta = resposta + caracter
                i = i + 1
        return resposta