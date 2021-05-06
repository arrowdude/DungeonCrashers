from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
import random
import CollisionDC
import Enemy
import Player
import Misc

janela = Window(700,437)
background = Sprite("background.png",18)
background.set_total_duration(1100)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

##Sprites##
##Player##
player = Player.player(6)
##Enemies##
orc1 = Enemy.enemy(Sprite("Actors/Orc1Direita.png", 8), Sprite("Actors/Orc1Esquerda.png", 8),1)
orc2 = Enemy.enemy(Sprite("Actors/Orc2Direita.png", 8), Sprite("Actors/Orc2Esquerda.png", 8),1)
orc3 = Enemy.enemy(Sprite("Actors/Orc3Direita.png", 8), Sprite("Actors/Orc3Esquerda.png", 8),1)
OrcChief = Enemy.enemy(Sprite("Actors/OrcChiefRight.png",8), Sprite("Actors/OrcChiefLeft.png",8),20)
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
waveCounter = 1
enemyCounter = 0
speed = 40
OrcChiefBool = True
FrankensteinBool = True
TheDevilBool = True
Boss = []
##

while True:
    ##Variables##
    recargaShoot = recargaShoot + janela.delta_time()
    recargaEnemies+=janela.delta_time()
    direction = Player.getLastDirection(direction, teclado)
    initialx = Player.movePlayer(initialx, initialy, player.parado_esquerda, janela, teclado)[0]
    initialy = Player.movePlayer(initialx, initialy, player.parado_esquerda, janela, teclado)[1]
    ##
    ##Drawing background and other objects always on screen##
    background.draw()
    background.update()
    ##
    if mouse.is_button_pressed(BUTTON_LEFT):
        print(mouse.get_position())
    if recargaEnemies >2 and enemyCounter<=3 + waveCounter:
        if waveCounter<= 5:
            pick = random.choice([orc1,orc2,orc3])
        enemies.append([initialEnemyX,initialEnemyY, pick.direita,pick])
        enemyCounter +=1
        recargaEnemies = 0
    if waveCounter == 5 and OrcChiefBool:
        Boss.append([initialEnemyX,initialEnemyY,OrcChief.direita,OrcChief])
        OrcChiefBool=False
    if enemyCounter>5 + waveCounter and enemies == []:
        waveCounter+=1
        enemyCounter = 0
        speed +=1
    while teclado.key_pressed("SPACE") and recargaShoot>1:
        Player.shoot(initialx, initialy, direction, teclado, tiros)
        recargaShoot = 0
    Player.getPlayerSprite(direction, player, teclado).set_position(initialx, initialy)
    Player.getPlayerSprite(direction, player, teclado).set_total_duration(1000)
    Player.getPlayerSprite(direction, player, teclado).draw()
    Player.getPlayerSprite(direction, player, teclado).update()
    Player.tirosUpdate(tiros, velTiro, janela, explosoes, enemies)
    Enemy.updateEnemyPosition(initialx, initialy, enemies, speed, tiros, explosoes, janela)
    Enemy.updateBossPosition(initialx, initialy, Boss, speed, tiros, explosoes, janela)
    Player.getLife(player.life)
    Player.explosoesUpdate(explosoes, janela)
    Player.playerCollideEnemies(player, Player.getPlayerSprite(direction, player, teclado), enemies,Boss, janela)
    janela.draw_text("Wave" + str(waveCounter), janela.width-40,10, size = 12, color=(255,255,255))
    janela.update()
