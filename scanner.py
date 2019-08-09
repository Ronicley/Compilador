import re, json
arq = open('arquivo.txt', 'r')
codigo = []
contemPalavra = []
contemOperadores = []
contemTerminador = []
contemIdentificadores = []
contemConstantes = []
contemNumeros = []
error = []

linha = arq.read()
codigo = linha.split(' ')

palavraReservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminador = [';']
identificadores = ['i','j']


for i in codigo:
    if re.findall("([A-Za-z])\w+", i):
        if(codigo.__contains__(i)):
            contemPalavra.append(i)
        else:
            error.append('error de sitaxe: palavra "{}" desconhecida'.format(i))
    elif re.findall("(<|=|\+|-)", i):
        
        if operadores.__contains__(i):
            contemOperadores.append(i)
        else:
            error.append('erro de sintaxe: operador "{}" desconhecido'.format(i))

    elif len(i) == 2:
        if re.findall("(:|;|.|:|)$", i):
            if terminador.__contains__(i[1]):
                contemTerminador.append(i[1])
            else:
                error.append('erro de sintaxe: terminador "{}" invalido'.format(i[1]))
    elif identificadores.__contains__(i):
        contemIdentificadores.append(i)
    elif re.findall('\d', i):
        if len(i) > 0:
            contemConstantes.append(i)
        elif len(i) < 1:
            print(i)
            contemNumeros.append(i)
        else:
            error.append('erro de sitaxe: not number')



print()
arq.close()