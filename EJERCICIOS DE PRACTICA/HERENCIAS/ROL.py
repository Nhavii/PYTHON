class Personaje:
    def __init__(self,nombre,hp,atk):
        self.nombre=nombre
        self.vida=hp
        self.ataque=atk
    
    def atacar(self,enemigo):
        enemigo.recibirDaño(self.ataque)
        return f"Pegas de {self.ataque} a {enemigo.nombre}"
    
    def recibirDaño(self,daño):
        self.vida-=daño
        if self.vida<=0:
            print(f"{self.nombre} ha sido derrotado.")

class Guerrero(Personaje):
    def __init__(self,nombre,hp,atk):
        super().__init__(nombre,hp,atk)
        self.habilidad = "Embestida"
    
    def embestida(self,enemigo):
        print(f"{self.nombre} utiliza Embestida contra {enemigo.nombre}!")
        enemigo.recibirDaño(self.ataque*2.5)
        

class Mago(Personaje):
    def __init__(self,nombre,hp,atk):
        super().__init__(nombre,hp,atk)
        self.habilidad = "Ice Ball"
    
    def iceBall(self,enemigo):
        print(f"{self.nombre} utiliza Bola de Hielo contra {enemigo.nombre}!")
        enemigo.recibirDaño(self.ataque*3)

class Arquero(Personaje):
    def __init__(self,nombre,hp,atk):
        super().__init__(nombre,hp,atk)
        self.habilidad = "Lluvia de flechas"
    
    def arrowRain(self,enemigo):
        print(f"{self.nombre} utiliza Lluvia de flechas contra {enemigo.nombre}!")
        enemigo.recibirDaño(self.ataque*1.5)

class Rogue(Personaje):
    def __init__(self,nombre,hp,atk):
        super().__init__(nombre,hp,atk)
        self.habilidad = "Crítico"
    
    def arrowRain(self,enemigo):
        print(f"{self.nombre} utiliza Lluvia de flechas contra {enemigo.nombre}!")
        enemigo.recibirDaño(self.ataque*3.5)

guerrero1=Guerrero("Manolitox",120,25)
mago1=Mago("Gandalf",90,35)
arquero1=Arquero("Robin",100,30)
rogue1=Rogue("Altair",80,40)

guerrero1.atacar(mago1)
rogue1.atacar(arquero1)

print(f"Los puntos de vida de {mago1.nombre} son {mago1.vida}")
print(f"Los puntos de vida de {arquero1.nombre} son {arquero1.vida}")
        