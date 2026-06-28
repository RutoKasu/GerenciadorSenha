from database import *

rodando = True

while rodando:
    print("=========")
    print("Menu: \n[1] Criar Banco de Dados \n[2] Consultar Banco\n[3] Inserir dados\n[4] Deletar Banco")
    choice = int(input("Escolha uma opção: "))

    match choice:
        case 1:
            criar()
        case 2:
            listar_user()
        case 3:
            try:
                inserir_user()
            except:
                print("Ocorreu um erro no banco de dados!")
        case 4:
            deletar_banco()