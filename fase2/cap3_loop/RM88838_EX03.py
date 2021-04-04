value = int(input("Insira um valor inteiro: "))
i = 1
previous = 1
while True:
    if i == value:
        print("Ação bem sucedida!")
        break
    elif i > value:
        print("A ação falhou...")
        break
    else:
        holder = i + previous
        previous = i
        i = holder
