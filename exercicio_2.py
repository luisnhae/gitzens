s = raw_input("Ola, por favor, digite seu nome: ")

print("Digite as notas das respectivas provas! "+s)
n1 = float(input("nota prova 1: "))
n2 = float(input("nota prova 2: "))
m = ((n1+n2) / 2)
print("\n")
print("\n")
print("Sua media foi: "+m)
if m>=6:
	print("Parabens voce esta aprovado "+s)
else:
	print("Se dedique mais e conseguira "+s)
