num_alimentos = int(input("Insira a quantidade de alimentos consumidos: "))
cal_total = 0
for i in range(1, num_alimentos + 1):
    cal = int(input(f"Insira a quantidade de calorias do alimento {i}: "))
    cal_total = cal_total + cal
print(f"Total de calorias consumidas é de {cal_total} kcal.")
input()
