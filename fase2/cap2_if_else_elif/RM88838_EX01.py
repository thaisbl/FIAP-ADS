peso = float(input("Digite o PESO em KG: ").replace(",", "."))
altura = float(input("Digite a ALTURA em M: ").replace(",", "."))
if altura > 3:
    altura = altura / 100
imc = peso / (altura * altura)
print("##########################################")
print(f"    Para PESO: {peso:.1f}kg e ALTURA: {altura:.2f}m")
if imc < 16:
    print(f"    IMC: {imc:.2f} - Baixo peso Grau III")
elif imc < 17:
    print(f"     IMC: {imc:.2f} - Baixo peso Grau II")
elif imc < 18.5:
    print(f"     IMC: {imc:.2f} - Baixo peso Grau I")
elif imc < 25:
    print(f"        IMC: {imc:.2f} - Peso ideal")
elif imc < 30:
    print(f"        IMC: {imc:.2f} - Sobrepeso")
elif imc < 35:
    print(f"      IMC: {imc:.2f} - Obesidade Grau I")
elif imc < 40:
    print(f"     IMC: {imc:.2f} - Obesidade Grau II")
else:
    print(f"     IMC: {imc:.2f} - Obesidade Grau III")
print("##########################################")
input()
