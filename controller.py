from model import*
import os
import random

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
            if tarefa == "":
                print("Digite uma tarefa válida.")
            else:
                    self.tarefa = tarefa
                    self.meu_id = random.randint(1000, 9999)
                    if TODO.AdicionarTarefa (self.tarefa) == True:
                        print(f"Tarefa adicionada: ")
                    else:
                         print ("Erro ao tentar adicionar a tarefa")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir - 1
        excluir = int(excluir) - 1
        try:
            if TODO.RemoverTarefa(self.excluir) == True:
                print("Tarefa removida.")
            else:
                print("Algum problema foi encontrado.")     
        except Exception as erro:
            print("Digite um número válido. Esta tarefa não existe.")

class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 0
        for tarefas in ControllerLista:
            cont += 1
            print(f"{cont}. {tarefas}")


class ControllerEditarTarefa():
     def __init__(self, editar):
         self.editar = editar
         ControllerEditarTarefa = TODO.alterar()
         if ControllerEditarTarefa.AlterarTarefa(self.editar) == True:
              print("Tarefa Alterada com sucesso!")


class ControllerFinalizarTarefa():
     def __init__(self, finalizar):
          self.finalizar = finalizar
          ControllerFinalizarTarefa = TODO.FinalizarTarefa()
          if ControllerFinalizarTarefa.FinalizarTarefa(self.finalizar) == True:
               print("Tarefa Finalizada com Sucesso!")
               