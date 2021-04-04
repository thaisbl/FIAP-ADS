num_transacoes = int(input("Insira a quantidade de transações realizadas: "))
gasto_total = 0
for i in range(1, num_transacoes + 1):
    gasto = float(input(f"Insira o valor da transação {i}: R$").replace(",", "."))
    gasto_total = gasto_total + gasto
media = gasto_total / num_transacoes
print(f"Total gasto é de R${gasto_total:.2f} e a média de gastos é de R${media:.2f}.")
