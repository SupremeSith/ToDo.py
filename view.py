from controller import *
import os

sair = 0
while sair == 0:

    os.system("cls")
    print("SOFTWARE DE TO-DO \n1 - Adicionar tarefa \n2 - Listar tarefas \n3 - Excluir tarefa  \n4 - Alterar Tarefa \n5 - Concluir Tarefa \n6 - Listar Tarefas Concluidas \n7 - Sair")
    opcao = input("Digite a opção desejada > ")

    match opcao:
        case "1":
            os.system("cls")
            print("--ADICIONAR TAREFA--")
            tarefa = input("Digite a tarefa > ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")

        case "2":
            os.system("cls")
            print("--LISTAR TAREFA--")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")

        case "3":
            os.system("cls")
            print("--EXCLUIR TAREFA--")
            listarTarefa = ControllerListarTarefa()
            excluir = input("Digite o número da tarefa que deseja excluir > ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            listarTarefa = ControllerListarTarefa()
            os.system("pause")

        case "4":
            os.system("cls")
            print("--EDITAR TAREFA--")
            listarTarefa = ControllerListarTarefa()
            editar = input("Digite o número da tarefa que deseja editar > ")
            editarTarefa = ControllerEditarTarefa(editar)
            listarTarefa = ControllerListarTarefa()
            os.system("pause")


        case "5":
            os.system("cls")
            print("--MARCAR COMO FINALIZADO--")
            listarTarefa = ControllerListarTarefa()
            finalizar = input("Digite o número da tarefa que deseja marcar como finalizada > ")
            finalizarTarefa = ControllerFinalizarTarefa(finalizar)
            listarTarefa = ControllerListarTarefa()
            if listarTarefa = True:
            
            os.system("pause")

        case "7":
            os.system("cls")
            sair = 1

        case _:
            os.system("cls")
            print("Opção inválida")
