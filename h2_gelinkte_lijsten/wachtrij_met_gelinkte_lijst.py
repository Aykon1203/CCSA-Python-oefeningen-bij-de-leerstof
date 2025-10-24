class QueueList:

    class Knoop:

        def __init__(self,data=None,volgende=None) -> None:
            self.data = data
            self.volgende = volgende

    def __init__(self) -> None:
        self.kop = None
        self.staart = None

    def is_empty(self):
        return self.kop is None and self.staart is None

    def enqueue(self,data):
        nieuw = QueueList.Knoop()
        if self.is_empty():
            self.kop=self.staart=nieuw
        self.staart.volgende = nieuw
        self.staart = nieuw
        
    def front(self):
        if self.is_empty():
            return IndexError()
        return self.kop.data

    def dequeue(self):
        if self.is_empty():
            return IndexError()
        self.pop()
    def invert(self):
        pass

