class Enemy:
    # life = 3

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()

# def attack(self):
#     print("ouch!")
#     self.life -= 1

# def check_life(self):
#     if self.life <= 0:
#         print("I am dead")
#     else:
#         print(str(self.life) + " life left")


# enemy1 = Enemy()
# enemy2 = Enemy()

# enemy1.attack()

# enemy1.check_life()
# enemy1.attack()
# enemy2.check_life()
