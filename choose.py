from aiogram.fsm.state import StatesGroup, State

class WorkState(StatesGroup):
    OFF = State()
    ON = State()

class PlayerRegistrationState(StatesGroup):
    hero_name = State()
    hero_race = State()
    hero_class = State()
    hero_avatar = State()

#class Player():
    #counter = 0

    #def __init__(self, name):
        #self.name = name
        #Player.counter += 1
    
    #@staticmethod
    #def amount_players():
        #print('Число игроков', Player.counter)

#f1 = Player('IDAN')
#f2 = Player('IDEN')
#f3 = Player('IDUN')

#print(Player.name)
#print(f1.name)
#print(Player.counter)
#Player.amount_players()