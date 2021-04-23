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
player = DungeonCrashersLib.player(6)
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

while True:
    ##Variables##
    recargaShoot = recargaShoot + janela.delta_time()
    recargaEnemies = recargaEnemies + 3*janela.delta_time()
    direction = DungeonCrashersLib.getLastDirection(direction, teclado)
    initialx = DungeonCrashersLib.movePlayer(initialx, initialy, player.parado_esquerda, janela, teclado)[0]
    initialy = DungeonCrashersLib.movePlayer(initialx, initialy, player.parado_esquerda, janela, teclado)[1]
    ##
    ##Drawing background and other objects always on screen##
    background.draw()
    background.update()
    ##
    if mouse.is_button_pressed(BUTTON_LEFT):
        print(mouse.get_position())
    if recargaEnemies >10:
        pick = random.choice([orc1,orc2,orc3])
        enemies.append([initialEnemyX,initialEnemyY, pick.direita,pick])
        recargaEnemies = 0
    while teclado.key_pressed("SPACE") and recargaShoot>1:
        DungeonCrashersLib.shoot(initialx,initialy,direction, teclado, tiros)
        recargaShoot = 0
    DungeonCrashersLib.getPlayerSprite(direction, player, teclado).set_position(initialx,initialy)
    DungeonCrashersLib.getPlayerSprite(direction, player, teclado).set_total_duration(1000)
    DungeonCrashersLib.getPlayerSprite(direction, player, teclado).draw()
    DungeonCrashersLib.getPlayerSprite(direction, player, teclado).update()
    DungeonCrashersLib.tirosUpdate(tiros, velTiro, janela, explosoes, enemies)
    DungeonCrashersLib.updateEnemyPosition(initialx, initialy, enemies, tiros, explosoes, janela)
    DungeonCrashersLib.getLife(player.life)
    DungeonCrashersLib.explosoesUpdate(explosoes, janela)
    DungeonCrashersLib.playerCollideEnemies(player, DungeonCrashersLib.getPlayerSprite(direction, player, teclado),enemies, janela)
    janela.update()
