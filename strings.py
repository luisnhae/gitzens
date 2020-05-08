"""concatenar"""
a = 'Luis'
b = 'Gustavo'

concatenar = a + " " + b + "\n"
print(concatenar)

"""contando com len, tambem conta espaco"""

tamanho = len(concatenar)
print(tamanho)

""" [] define a posicao numerica da string"""

print(a[0] + " " + b[0]) 
"""L G"""

"""[valorinicial:valorfinal]"""
print(concatenar[0:2])
"""Lu"""

"""------------------------------"""

"""Em python, strings sao objetos, podendo atribuir metodos"""
"""Alterando a caixa >>>.lower()(minusculo) .upper()(maiusculo)"""

print(concatenar.lower())
print(concatenar.upper())

concatenar = concatenar.upper()
print(concatenar)

"""funcao strip remove espaco e caractere especial"""
print(concatenar.strip())

"""split converte a sequencia em uma lista [a, b, c , d ...]"""
"""podendo tirar um valor atribuindo dentro dos ()"""
minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split()
print(minha_lista)
minha_lista = minha_string.split("r")
print(minha_lista)
"""[o, ato, oeu, a, oupa, do, ei, de, Roma] >>> case sensitive"""


"""---------------------------------------------"""
"""Busca na string, usando o metodo find() podemos vizualisar a posicao da string
procurada"""

busca = minha_string.find("rei")
print(busca)
"""return = 23, pois onde se inicia"""
print(minha_string[busca:])
"""return = rei de Roma, usando o metodo [valorinicial:valorfinal]"""

"""--------------------------------------------"""
"""metodo replace, substitue valores em uma string
	variavel.replace("valor original", "valor a ser substituido")"""

mudando = minha_string.replace("o rei", "a rainha")
print(mudando)
"""return = O rato roeu a roupa da rainha de Roma"""






