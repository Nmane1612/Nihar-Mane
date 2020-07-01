class abc:
        def __init__(self):
            self.name="Anuja"
            self.change()

        def change(self):
            self.name="Python"

a=abc()
print(a.name)
