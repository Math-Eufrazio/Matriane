import random
import string
import time
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Bem vindo ao sistema interno da Matriane joias e bijus")
print("")
print("    digite suas credencias para logar no sistema")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
usuarios = ["@didica", "@brunoooo", "@gui_O_vei", "@dusantos_.erica", "@maicon"]

login = False

while login == False:
    usuario = input("Usuario: ")
    senha = input("Senha: ")

    if usuario == "Math" and senha == "1423":
        login = True
        print("Login efetuado com sucesso!")
        time.sleep(1)
    elif usuario == "Didi" and senha == "3241":
        login = True
        print("Login efetuado com sucesso!")
        time.sleep(1)
    else:
        print("Usuario ou senha incorretos, tente novamente.")

menu = False

while menu == False:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" [1] sortear usuarios [2] inserir novo usuario [0] sair")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    opcao = input("Digite a opcao que deseja selecionar : ")

    if opcao == "1":
        print("Sorteando", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)

        vencedor = random.choice(usuarios)
        print("\nVencedor:", vencedor)

    elif opcao == "2":
        print("Digite o @ do novo usuario")
        novo_usuario = input()

        if novo_usuario in usuarios:
            print("Esse usuario ja existe!")
        else:
            usuarios.append(novo_usuario)
            print("Usuario salvo")
            time.sleep(0.5)

            print("Gerando senha temporaria...")
            time.sleep(1)

            caracteres = string.ascii_letters + string.digits
            senha = "".join(random.choices(caracteres, k=8))
            print("Senha temporaria:", senha)

    elif opcao == "0":
        print("Saindo do sistema...")
        time.sleep(1)
        menu = True

    else:
        print("Escolha invalida")