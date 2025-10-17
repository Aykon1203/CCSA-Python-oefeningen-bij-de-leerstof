class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data=data
            self.volgende=volgende

    def __init__(self):
        self.top=None;

    def is_empty(self):
        return self.top is None;

    def push(self, data):
        nieuwe=StackList.Knoop()
        nieuwe.data=data
        nieuwe.volgende=self.top
        self.top=nieuwe

    def peek(self):
        return self.top.data

    def pop(self):
        x = self.top.data #data van top opslaan
        self.top=self.top.volgende # top verwijderen
        return x
        
stapel1=StackList()
print(stapel1.is_empty())
stapel1.push(5)
stapel1.push(1)
stapel1.push(2)
stapel1.push(3)
print(stapel1.is_empty())
print(stapel1.pop())
print(stapel1.peek())