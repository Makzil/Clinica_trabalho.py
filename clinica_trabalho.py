class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Adiciona um paciente ao final da lista de espera 
    def adicionar_paciente_lista(self, nome):
        novo_paciente = Node(nome)
        if not self.head:  # Verifica se a lista está vazia
            self.head = novo_paciente
        else:
            atual = self.head
            while atual.next:  # Percorre a lista até o último nó
                atual = atual.next
            atual.next = novo_paciente

    # Remove um paciente do início da lista de espera  
    def remover_paciente_lista(self):
        if not self.head:  # Verifica se a lista está vazia
            print("A lista está vazia.")
            return None
        paciente_removido = self.head.data
        self.head = self.head.next  # Atualiza a cabeça da lista para o próximo nó
        print(f"Paciente removido da lista de espera: {paciente_removido}")
        return paciente_removido
from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    # Adiciona um paciente ao final da fila de atendimento
    def adicionar_paciente_fila(self, nome):
        self.fila.append(nome)

    # Remove um paciente da frente da fila e indica que ele está sendo atendido
    def remover_paciente_fila(self):
        if not self.fila:  # Verifica se a fila está vazia
            print("A fila está vazia.")
            return None
        paciente_removido = self.fila.popleft()  # Remove o paciente da frente da fila
        print(f"Atendendo paciente da fila: {paciente_removido}")
        return paciente_removido
class Pilha:
    def __init__(self):
        self.pilha = []

    # Adiciona um paciente ao topo da pilha de consultas de urgência
    def adicionar_paciente_pilha(self, nome):
        self.pilha.append(nome)

    # Remove um paciente do topo da pilha e indica que ele está sendo atendido
    def remover_paciente_pilha(self):
        if not self.pilha:  # Verifica se a pilha está vazia
            print("A pilha está vazia.")
            return None
        paciente_removido = self.pilha.pop()  # Remove o paciente do topo da pilha
        print(f"Atendendo paciente de urgência: {paciente_removido}")
        return paciente_removido
# Testando a Lista Encadeada
lista_espera = LinkedList()
lista_espera.adicionar_paciente_lista("Maria")  # Adiciona "Maria" à lista de espera
lista_espera.remover_paciente_lista()  # Remove o primeiro paciente da lista de espera

# Testando a Fila
fila_atendimento = Fila()
fila_atendimento.adicionar_paciente_fila("João")  # Adiciona "João" à fila de atendimento
fila_atendimento.remover_paciente_fila()  # Remove o primeiro paciente da fila de atendimento

# Testando a Pilha
pilha_urgencia = Pilha()
pilha_urgencia.adicionar_paciente_pilha("Ana")  # Adiciona "Ana" à pilha de consultas de urgência
pilha_urgencia.remover_paciente_pilha()  # Remove o paciente do topo da pilha de consultas de urgência
