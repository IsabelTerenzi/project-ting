from ting_file_management.abstract_queue import AbstractQueue

# Requisito 1 - Implemente uma fila para armazenar os arquivos que serão lidos
class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.queue[index]
