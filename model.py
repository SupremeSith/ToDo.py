class ToDo():

    def __init__(self):
        self.lista = []

    def AdicionarTarefa(self, tarefa):
        self.lista.append(tarefa)
        return True

    def RemoverTarefa(self, excluir):
        self.lista.pop(excluir)
        return True

    def ListarTarefas(self):
        return self.lista
    
def ControllerEditarTarefa(self, alterar):
    self.lista.append(alterar)
    return True
    
TODO = ToDo()