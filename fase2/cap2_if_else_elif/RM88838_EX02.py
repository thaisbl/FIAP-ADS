tipo_assinatura = input("Digite o tipo de assinatura: B - Basic / S - Silver / G - Gold / P - Platinum: ").upper()
faturamento = float(input("Digite o faturamento anual: R$").replace(",", "."))
print("#############################################")
if tipo_assinatura == "B":
    print("O valor do bônus a ser pago é de R${:.2f}".format(faturamento*0.7))
elif tipo_assinatura == "S":
    print("O valor do bônus a ser pago é de R${:.2f}".format(faturamento*0.8))
elif tipo_assinatura == "G":
    print("O valor do bônus a ser pago é de R${:.2f}".format(faturamento*0.9))
elif tipo_assinatura == "P":
    print("O valor do bônus a ser pago é de R${:.2f}".format(faturamento*0.95))
else:
    print("O tipo de assinatura inserido não é válido.")
print("#############################################")
input()