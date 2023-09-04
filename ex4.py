import re

def cadastrar_usuario(campos_obrigatorios):
    dados_usuario = {}

    for campo in campos_obrigatorios:
        dados_usuario[campo] = input(f"Digite o valor do campo {campo}: ")

    while True:
        campo_adicional = input("Digite o nome de um campo adicional (ou sair): ")
        if campo_adicional == "sair":
            break

        dados_usuario[campo_adicional] = input(f"Digite o valor do campo {campo_adicional}: ")

    return dados_usuario

def imprimir_usuarios(opcao):

    usuarios = banco_usuarios.values()

    match opcao:
        case "1":
            for usuario in usuarios:
                print(usuario)

        case "2":
            nomes_escolhidos = input("Digite o(s) nome(s) que deseja filtrar, separados por vírgulas: ")
            nomes_escolhidos = nomes_escolhidos.split(",")
            for nome in nomes_escolhidos:
                if nome in banco_usuarios:
                    print(banco_usuarios[nome])

        case "3":
            while True:
                campo_busca = input("Digite o campo de busca(ou sair): ")

                if campo_busca.lower() == "sair":
                    break

                valor_busca = input(f"Digite o valor do campo {campo_busca}: ")

                for usuario in usuarios:
                    if campo_busca in usuario and usuario[campo_busca] == valor_busca:
                        print(usuario)


        case "4":
            while True:
                nomes_escolhidos = input("Digite o(s) nome(s) que deseja filtrar, separados por vírgulas: ")
                nomes_escolhidos = nomes_escolhidos.split(",")
                if not nomes_escolhidos:
                    break

                campo_busca = input("Digite o campo de busca (ou 'sair' para encerrar): ")
                if campo_busca.lower() == "sair":
                    break

                valor_busca = input(f"Digite o valor do campo {campo_busca}: ")

                for usuario in usuarios:
                    for nome in nomes_escolhidos:
                        if campo_busca in usuario and usuario[campo_busca] == valor_busca:
                            print(usuario)
                        break
        
        case _:
            print("Opção Invalida")

banco_usuarios = {}

campos_obrigatorios = input("Digite os campos obrigatórios para cadastro, separados por vírgulas: ")
campos_obrigatorios = campos_obrigatorios.split(",")

while True:
    print(" 1-Cadastrar usuário\n 2-Imprimir usuários\n 0-Encerrar")

    opcao = input("Digite a sua opção: ")

    match opcao:
        case "0":
            break
        case "1":
            dados_usuario = cadastrar_usuario(campos_obrigatorios)
            banco_usuarios[dados_usuario["nome"]] = dados_usuario
        case "2":
            print(" 1- Imprimir todos\n 2- Filtrar por nomes\n 3- Filtrar por campos\n 4- Filtrar po nomes e campos")
            opcao2 = input("Digite a sua opção: ")
            imprimir_usuarios(opcao2)
        case _:
            print("Opção inválida.")