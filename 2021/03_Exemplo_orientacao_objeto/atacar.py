class Personagem(object):
    def __init__(self, nome):
        self.nome = nome
        
    def ataque(self, alvo):
        alvo.hp -= self.mp

# Raças 
class Dracula(Personagem):
    def __init__(self,nome):
        super().__init__(nome)
        self.hp = 100
        self.mp = 10            
class Ghoust(Personagem):
    def __init__(self,nome):
        super().__init__(nome)
        self.hp = 50
        self.mp = 30

p1 = Dracula('Miguel')
p2 = Ghoust('Priscila')

p1.ataque(p2)
print(p2.hp)

