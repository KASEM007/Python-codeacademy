class PotatoSalad():
    def __init__(self, potatoes, celery=None, onions=None):
        self.potatoes = potatoes
        if not celery == None: self.celery = celery
        if not onions == None: self.onions = onions
    
    def __str__(self):
        recipe = f'{self.__class__.__name__}\n--Ingredients--\n'
        for i, a in self.__dict__.items():
          recipe += f'{i}: {a}\n'
        return recipe
    
class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions, raisins):
        super().__init__(potatoes, celery, onions)
        self.raisins = raisins
        
class EggyPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery):
        super().__init__(potatoes, celery)
        self.eggs = potatoes * 2 #we'll have 2 eggs for every potato
        
sps = SpecialPotatoSalad(3,4,5,63)
print(sps)

#new recipe: eggy potato salad has no onions
eggy_ps = EggyPotatoSalad(6, 4)
print(eggy_ps)

#say you wanted regular potato salad without celery
#you could supply keyword arguments
ps = PotatoSalad(potatoes = 12, onions = 2)
print(ps)
