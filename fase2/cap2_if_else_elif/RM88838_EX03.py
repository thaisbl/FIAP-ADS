segunda = int(input("Digite a quantidade de votos para SEGUNDA-FEIRA: "))
terca = int(input("Digite a quantidade de votos para TERÇA-FEIRA: "))
quarta = int(input("Digite a quantidade de votos para QUARTA-FEIRA: "))
quinta = int(input("Digite a quantidade de votos para QUINTA-FEIRA: "))
sexta = int(input("Digite a quantidade de votos para SEXTA-FEIRA: "))
print("############################")
print("   DISTRIBUIÇÃO DE VOTOS:")
print(
    f"     SEGUNDA-FEIRA  {segunda}\n     TERÇA-FEIRA    {terca}\n     QUARTA-FEIRA   {quarta}\n"
    f"     QUINTA-FEIRA   {quinta}\n     SEXTA-FEIRA    {sexta}")
print("############################")
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("  RESULTADO: SEGUNDA-FEIRA")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("  RESULTADO: TERÇA-FEIRA")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("  RESULTADO: QUARTA-FEIRA")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("  RESULTADO: QUINTA-FEIRA")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("  RESULTADO: SEXTA-FEIRA")
else:
    print("     RESULTADO: EMPATE")
print("############################")
input()