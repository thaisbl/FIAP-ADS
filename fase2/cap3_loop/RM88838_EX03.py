value = int(input("Insira um valor inteiro: "))
i = 1
previous = 1
while True:
    if i < value:
        holder = i + previous
        previous = i
        i = holder
    elif i == value:
        print("Ação bem sucedida!")
        break
    else:
        print("A ação falhou...")
        break
