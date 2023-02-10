class Task():
    def __init__(self):
        self.string = None

    def set(self, string:str):
        self.string = string

    def get(self) -> str:
        if self.string is not None:
            return self.string
        else:
            return " "

a = Task()
a.get()
a.set('qwerty')
print(a.get())
