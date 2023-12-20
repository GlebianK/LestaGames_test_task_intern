# подход FIFO реализует структура "очередь"
# по заданию необходимо представить не менее двух реализаций,
# поэтому ниже представлены две стандартных реализации очереди: обычная и круговая
# (да, видов очереди больше, чем 2, но формулировка задания позволяет ограничиться двумя реализациями)
# -----------------------------------------------------------------------------------------------------------

class UserQueue:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, new_item): # добавление элемента в очередь
        self.queue.append(new_item)

    def dequeue(self): # удаление элемента из очереди
        if (len(self.queue) < 1):
            print("Nothing to dequeue!")
            return None
        return self.queue.pop(0)

    def printQueue(self): # вывод очереди
        print(self.queue)

    def printQueueSize(self): # вывод размера очереди
        print(len(self.queue))

    def peek(self): # просмотр головного элемента (если есть)
        if(len(self.queue) >= 1):
            return self.queue[0]
        else:
            print("Failed to peek on nothing =)")
            return None

# -----------------------------------------------------------------------------------------------------------

class UserQueueCircular:

    def __init__(self, n): # n - максимальное количество элементов в кольцевой очереди
        self.n = n
        self.free_cells = n
        self.queue = [None] * n
        self.head = -1
        self.tail = -1

    def enqueueC(self, new_item):                       # добавление элемента в очередь
        if (((self.tail + 1) % self.n) == self.head):
            print("Queue is full!")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = new_item
            self.UpdateNumberOfFreeCells(-1)                 # метод обновления количества "свободных мест" реализован в конце класса
        else:
            self.tail = (self.tail + 1) % self.n
            self.queue[self.tail] = new_item
            self.UpdateNumberOfFreeCells(-1)

    def dequeueC(self):                                 # удаление элемента из очереди
        if (self.head == -1):
            print("Queue is alredy empty!!!")
        elif (self.head == self.tail):
            self.head = -1
            self.tail = -1
            self.UpdateNumberOfFreeCells(1)
            return self.queue.pop(0)
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.n
            self.UpdateNumberOfFreeCells(1)
            return data

    def printQueueC(self):                              # вывод очереди
        if (self.head == -1):
            print("Queue is empty!")
        elif (self.tail >= self.head):
            for position in range(self.head, self.tail + 1):
                print(self.queue[position])
        else:
            for position in range(self.head, self.n):
                print(self.queue[position])
            for position in range(0, self.tail + 1):
                print(self.queue[position])

    def printQueueCNumberOfFreeCells(self):             # вывод количества "свободных мест" в очереди (если их 0, то произойдёт перезапись данных)
        print("Free cells:", self.free_cells)

    def peekC(self):                                    # просмотр головного элемента (если есть)
        if(self.head >= 0):
            return self.queue[self.head]
        else:
            print("Failed to peek on nothing!!!")
            return None

    def UpdateNumberOfFreeCells(self, num_to_add):      # обновление информации о количестве "свободных мест". 1 - место освободилось, -1 - место занялось 
        self.free_cells += num_to_add
        if (self.free_cells < 0):
            self.free_cells = 0
        elif (self.free_cells > self.n):
            self.free_cells = self.n
            

# -----------------------------------------------------------------------------------------------------------

'''
Обычная очередь:
# Может не иметь предварительно заданного размера (размер ограничен количеством свободной памяти >:D)

# В общем случае при удалении элементов остальные в памяти не сдвигаются,
    т.е. остаются пустые пространства, ранее занятые удалёнными элементами,
    что приводит к нерациональному использованию памяти
    (неактуально для Python-реализации, т.к. метод pop() сдвигает список)
# Возвращает с помощью peek нулевой элемент (для Python-реализации; в общем случае - головной, который может быть не нулевым)

Круговая очередь:
# Обязательно имеет ограниченный размер для возможности закольцевать

# Перезаписывает новые данные "по кругу", итерационно, т.е. более рациональное использование памяти

# Возвращает с помощью peek head-элемент, даже для Python-реализации
'''

