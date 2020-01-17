import random
class DiceGame:
    '''
    Multi-slided die
    Instance variable
    current value
    num_sides

    '''
    def __init__(self,num_slides):
        self.num_slides=num_slides
        self.current_value=self.roll()

    def roll(self):
        self.current_value=random.randrange(1,self.num_slides+1)
        return self.current_value
    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}): {} ".format(self.num_slides,self.current_value)   

        
if __name__ =="__main__":
    myGame =DiceGame(6)
    for k in range(6):
        print(myGame)
        myGame.roll()

dice_list=[DiceGame(4),DiceGame(6)]
print(dice_list)       
 
