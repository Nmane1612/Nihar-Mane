class abc:
        def __init__(self):
            self.name="name"
            self.change()

        def change(self):
            self.name="Python"

a=abc()
print(a.name)
