class Bank:
	def __init__(self,nob):
		self.name=nob
class Employee:
	@staticmethod
	def mymethod(e):
                        e.name="python"
                        print(e.name)

a=Bank("name")
Employee. mymethod(a)
