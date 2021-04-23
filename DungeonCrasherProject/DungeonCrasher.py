from PPlay.window import *
from PPlay.sprite import *
import random
import DungeonCrashersLib

janela = Window(700,437)
background = Sprite("background.png",18)
background.set_total_duration(1100)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

##Sprites##
##Player##
player_parado_esquerda = Sprite("Actors/player_parado_esquerda.png",2)
player_parado_direita = Sprite("Actors/player_parado_direita.png",2)
player_walk_esquerda = Sprite("Actors/player_walk_esquerda.png",8)
player_walk_direita = Sprite("Actors/player_walk_direita.png",8)
player_parado_esquerda.set_total_duration(1000)
player_parado_direita.set_total_duration(1000)
player_walk_esquerda.set_total_duration(1000)
player_walk_direita.set_total_duration(1000)

##MEnemies##
orc1 = DungeonCrashersLib.enemy(Sprite("Actors/Orc1Direita.png",8), Sprite("Actors/Orc1Esquerda.png",8), Sprite("Actors/Orc1Esquerda.png",8).height, Sprite("Actors/Orc1Esquerda.png",8).width)
##

#Variaveis
initialEnemyX = 436
initialEnemyY = 131
initialx = 400
initialy = 300
direction = "r"
velTiro = 200
recarga = 0
tiros = []
explosoes = []
##

def getPlayerSprite(direction):
    if teclado.key_pressed("LEFT"):
        return(player_walk_esquerda)
    elif teclado.key_pressed("RIGHT"):
        return(player_walk_direita)
    else:
        if direction == "r":
            return(player_parado_direita)
        elif direction == "l":
            return(player_parado_esquerda)

def moveEnemy(playerX, playerY, initialEnemyX, initialEnemyY, Enemy):
    enemyPosX = initialEnemyX
    enemyPosY =initialEnemyY
    if initialEnemyX >= playerX:
        velX, sprite = -60, Enemy.esquerda
    elif initialEnemyX < playerX:
        velX, sprite = 60, Enemy.direita
    if initialEnemyY > playerY:
        velY =  - 60
    elif initialEnemyY < playerY:
        velY =  + 60
    if not DungeonCrashersLib.sceneryCollision(enemyPosX + velX * janela.delta_time(), enemyPosY, Enemy) and not DungeonCrashersLib.collidedLake(enemyPosX + velX * janela.delta_time(), enemyPosY, Enemy):
        enemyPosX = enemyPosX + velX*janela.delta_time()
    if not DungeonCrashersLib.sceneryCollision(enemyPosX, enemyPosY + velY * janela.delta_time(), Enemy) and not DungeonCrashersLib.collidedLake(enemyPosX, enemyPosY + velY * janela.delta_time(), Enemy):
        enemyPosY = enemyPosY+ velY*janela.delta_time()
    return([enemyPosX, enemyPosY, sprite])


while True:
    recarga = recarga + 3*janela.delta_time()
    direction = DungeonCrashersLib.getLastDirection(direction, teclado)
    initialx = DungeonCrashersLib.movePlayer(initialx, initialy, player_parado_esquerda, janela, teclado)[0]
    initialy = DungeonCrashersLib.movePlayer(initialx, initialy, player_parado_esquerda, janela, teclado)[1]
    initialEnemyX, initialEnemyY, orc1Sprite = moveEnemy(initialx,initialy,initialEnemyX,initialEnemyY,orc1)[0], moveEnemy(initialx,initialy,initialEnemyX,initialEnemyY,orc1)[1],moveEnemy(initialx,initialy,initialEnemyX,initialEnemyY,orc1)[2]
    while teclado.key_pressed("SPACE") and recarga>1:
        DungeonCrashersLib.shoot(initialx,initialy,direction, teclado, tiros)
        recarga = 0
    getPlayerSprite(direction).set_position(initialx,initialy)
    DungeonCrashersLib.drawScene([background, getPlayerSprite(direction)])
    DungeonCrashersLib.tirosUpdate(tiros, velTiro, janela, explosoes)
    DungeonCrashersLib.explosoesUpdate(explosoes, janela)
    orc1Sprite.set_position(initialEnemyX,initialEnemyY)
    orc1Sprite.draw()
    orc1Sprite.set_total_duration(1000)
    orc1Sprite.update()
    janela.update()
