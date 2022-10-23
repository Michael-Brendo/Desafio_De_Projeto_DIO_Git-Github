desafio_dio = input("Você já completou o desafio? digite 1 para SIM e 0 para NAO: ")
try:
    desafio_dio = int(desafio_dio)

except:
    desafio_dio = -1

if desafio_dio != -1:
    if desafio_dio == 1:
        print("Você já pode entregar o projeto!")

    if desafio_dio == 0:
        print("Continue trabalhando no projeto!")

    else:
        print("Você não respondeu corretamente, tente novamente!")

else:
    print("Você não respondeu corretamente, tente novamente!")