import time
import threading
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables
        self.guest_eating = []

    def guest_arrival(self, *guests):
        free_table = True
        guest_sit = False
        for guest in guests:
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest.name
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    self.guest_eating.append(guest)
                    guest.start()
                    guest_sit = True
                    break
                else:
                    guest_sit = False
            for table in self.tables:
                if table.guest == None:
                    free_table = True
                    break
                else:
                    free_table = False
            if free_table == False and guest_sit == False:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        table_is_occupied = True
        while self.queue.empty() == False or table_is_occupied == True:
            for n_table in range(len(self.tables)):
                time.sleep(0.5)
                if self.guest_eating[n_table] != None:
                    if self.guest_eating[n_table].is_alive() == False:
                        print(
                            f'{self.tables[n_table].guest} за {self.tables[n_table].number} '
                            f'столом> покушал(-а) и ушёл(ушла)')
                        self.tables[n_table].guest = None
                        self.guest_eating[n_table] = None
                        print(f'Стол номер {self.tables[n_table].number} свободен')
                        table_is_occupied = False
                        if self.queue.empty() == False:
                            guest_queue = self.queue.get()
                            self.tables[n_table].guest = guest_queue.name
                            self.guest_eating[n_table] = guest_queue
                            self.guest_eating[n_table].start()
                            print(
                                f'{guest_queue.name} из очереди> вышел(-ла) из очереди и сел(-а) '
                                f'за стол номер {self.tables[n_table].number}')
                            table_is_occupied = True
            for table in self.tables:
                if table.guest != None:
                    table_is_occupied = True
                    break
                else:
                    table_is_occupied = False


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
