#versão 0.5.1
#dev: Eliam Rainier Gois de Lima


from database import *
import time

rodando = True

while rodando:
    print("=========")
    print("Menu: \n[1] Criar Banco de Dados \n[2] Consultar Banco\n[3] Inserir dados\n[4] Deletar Banco\n[5] Deletar Usuário\n[0] Sair")
    try:
        choice = int(input("Escolha uma opção: "))
    except:
        print("Valor indisponivel!")
        continue

    match choice:
        case 1:
            criar()
        case 2:
            listar_user()
        case 3:
            inserir_user()
        case 4:
            deletar_banco()
        case 5:
            listar_user()
            deletar_user()
        case 0:
            rodando = False
            print("Finalizando Programa...")
            time.sleep(5)
            print("Programa finalizado!")