import random
import string
import time
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Bem-vindo ao sistema interno da Matriane Joias e Bijus")
print("")
print("    Digite suas credencias para logar no sistema")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
usuarios = ["@didica", "@brunoooo", "@gui_O_vei", "@dusantos_.erica", "@maicon", "@KrugerFuyuki"]

login = False

while login == False:
    usuario = input("Usuário: ")
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
        print("Usuário ou senha incorretos, tente novamente.")

menu = False

while menu == False:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(" [1] Sortear usuários [2] Inserir novo usuário [0] Sair")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    opcao = input("Digite a opção que deseja selecionar: ")

    if opcao == "1":
        print("Sorteando", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)

        vencedor = random.choice(usuarios)
        print("\nVencedor:", vencedor)

    elif opcao == "2":
        print("Digite o @ do novo usuário")
        novo_usuario = input()

        if novo_usuario in usuarios:
            print("Esse usuário ja existe!")
        else:
            usuarios.append(novo_usuario)
            print("Usuário salvo")
            time.sleep(0.5)

            print("Gerando senha temporária...")
            time.sleep(1)

            caracteres = string.ascii_letters + string.digits
            senha = "".join(random.choices(caracteres, k=8))
            print("Senha temporária:", senha)

    elif opcao == "0":
        print("Saindo do sistema...")
        time.sleep(1)
        menu = True

    else:
        print("Escolha inválida")