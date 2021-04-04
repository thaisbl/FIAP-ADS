segunda = int(input("Digite a quantidade de votos para SEGUNDA-FEIRA: "))
terca = int(input("Digite a quantidade de votos para TERÇA-FEIRA: "))
quarta = int(input("Digite a quantidade de votos para QUARTA-FEIRA: "))
quinta = int(input("Digite a quantidade de votos para QUINTA-FEIRA: "))
sexta = int(input("Digite a quantidade de votos para SEXTA-FEIRA: "))
print("##############################")
print("\tDISTRIBUIÇÃO DE VOTOS:")
print(
    f"\t  SEGUNDA-FEIRA  {segunda}\n\t  TERÇA-FEIRA    {terca}\n\t  QUARTA-FEIRA   {quarta}\n"
    f"\t  QUINTA-FEIRA   {quinta}\n\t  SEXTA-FEIRA    {sexta}")
print("################################")
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("\tRESULTADO: SEGUNDA-FEIRA")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("\tRESULTADO: TERÇA-FEIRA")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("\tRESULTADO: QUARTA-FEIRA")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("\tRESULTADO: QUINTA-FEIRA")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("\tRESULTADO: SEXTA-FEIRA")
else:
    print("\t\tRESULTADO: EMPATE")
print("################################")
