from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
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

##Enemies##
orc1 = DungeonCrashersLib.enemy(Sprite("Actors/Orc1Direita.png",8), Sprite("Actors/Orc1Esquerda.png",8))
orc2 = DungeonCrashersLib.enemy(Sprite("Actors/Orc2Direita.png", 8), Sprite("Actors/Orc2Esquerda.png", 8))
orc3 = DungeonCrashersLib.enemy(Sprite("Actors/Orc3Direita.png", 8), Sprite("Actors/Orc3Esquerda.png", 8))
##

#Variaveis
initialEnemyX = 435
initialEnemyY = 165
initialx = 400
initialy = 300
direction = "r"
velTiro = 200
recargaShoot = 0
recargaEnemies = 0
tiros = []
explosoes = []
enemies = []
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


while True:
    ##Variables##
    recargaShoot = recargaShoot + janela.delta_time()
    recargaEnemies = recargaEnemies + 3*janela.delta_time()
    direction = DungeonCrashersLib.getLastDirection(direction, teclado)
    initialx = DungeonCrashersLib.movePlayer(initialx, initialy, player_parado_esquerda, janela, teclado)[0]
    initialy = DungeonCrashersLib.movePlayer(initialx, initialy, player_parado_esquerda, janela, teclado)[1]
    ##
    ##Drawing background and other objects always on screen##
    DungeonCrashersLib.drawScene([background, getPlayerSprite(direction)])
    ##
    if mouse.is_button_pressed(BUTTON_LEFT):
        print(mouse.get_position())
    if recargaEnemies >10:
        pick = random.choice([orc1,orc2,orc3])
        enemies.append([initialEnemyX,initialEnemyY, pick.direita,pick])
        recargaEnemies = 0
    for enemy in enemies:
        enemy[0], enemy[1], enemy[2] = DungeonCrashersLib.moveEnemy(initialx,initialy,enemy[0],enemy[1], enemy[3], enemies, janela)[0], DungeonCrashersLib.moveEnemy(initialx,initialy,enemy[0],enemy[1],enemy[3], enemies, janela)[1], DungeonCrashersLib.moveEnemy(initialx,initialy,enemy[0],enemy[1],enemy[3], enemies, janela)[2]
        enemy[2].set_position(enemy[0],enemy[1])
        enemy[2].set_total_duration(1000)
        enemy[2].draw()
        enemy[2].update()
    while teclado.key_pressed("SPACE") and recargaShoot>1:
        DungeonCrashersLib.shoot(initialx,initialy,direction, teclado, tiros)
        recargaShoot = 0
    getPlayerSprite(direction).set_position(initialx,initialy)
    DungeonCrashersLib.tirosUpdate(tiros, velTiro, janela, explosoes, enemies)
    DungeonCrashersLib.explosoesUpdate(explosoes, janela)
    janela.update()
