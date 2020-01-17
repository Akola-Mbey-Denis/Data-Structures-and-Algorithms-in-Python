from queue import Queue
from random import randint 

def potatoGameSimulator(namesList,num):
    gameQueue=Queue()
    for name in namesList:
        gameQueue.enqueue(name)

    while gameQueue.size()>1:
        for i in range (0,randint(0,7)):
            gameQueue.enqueue(gameQueue.dequeue())
        gameQueue.dequeue()


    return gameQueue.dequeue()     



if __name__ =="__main__":
    print(potatoGameSimulator(['Musah','Aziz','Olu','Nazir','Solomon','Emmanuel','Susan'],7))


