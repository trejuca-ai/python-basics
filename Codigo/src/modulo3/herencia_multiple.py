

class B:
    def saludar(self):
        print("saludos de clase B")

class A:
    def saludar(self):
        print("saludos de clase A")

class C(B, A):
    pass

c = C()
print(c.saludar())



