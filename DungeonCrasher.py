from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.sound import *
import random
import Enemy
import Player

def main(janela):

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
    undead1 = Enemy.enemy(Sprite("Actors/Undead1Right.png", 8), Sprite("Actors/Undead1Left.png", 8),1)
    undead2 =Enemy.enemy(Sprite("Actors/Undead2Right.png", 8), Sprite("Actors/Undead2Left.png", 8),1)
    undead3 =Enemy.enemy(Sprite("Actors/Undead3Right.png", 8), Sprite("Actors/Undead3Left.png", 8),1)
    Frankenstein = Enemy.enemy(Sprite("Actors/FrankensteinRight.png",8), Sprite("Actors/FrankensteinLeft.png",8),30)
    demon1 = Enemy.enemy(Sprite("Actors/Demon1Right.png", 8), Sprite("Actors/Demon1Left.png", 8),1)
    demon2 =Enemy.enemy(Sprite("Actors/Demon2Right.png", 8), Sprite("Actors/Demon2Left.png", 8),1)
    demon3 =Enemy.enemy(Sprite("Actors/Demon3Right.png", 8), Sprite("Actors/Demon3Left.png", 8),1)
    TheDevil = Enemy.enemy(Sprite("Actors/TheDevilRight.png",8), Sprite("Actors/TheDevilLeft.png",8),40)
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
    waveSprites = [Sprite("Wave/Wave.png"),Sprite("Wave/1.png"),Sprite("Wave/2.png"),Sprite("Wave/3.png"),
                    Sprite("Wave/4.png"),Sprite("Wave/5.png"),Sprite("Wave/6.png"),
                    Sprite("Wave/7.png"),Sprite("Wave/8.png"),Sprite("Wave/9.png"),
                    Sprite("Wave/10.png"),Sprite("Wave/11.png"),Sprite("Wave/12.png"),
                    Sprite("Wave/13.png"),Sprite("Wave/14.png"),Sprite("Wave/15.png")]
    waveSprites[0].x,waveSprites[0].y = janela.width-waveSprites[0].width-60,25
    for i in range(1,16):
        waveSprites[i].x,waveSprites[i].y = waveSprites[0].x + waveSprites[0].width + 10,25
    ##

    while True:
        ##Variables##
        if teclado.key_pressed("J"):
            waveCounter = 5
        if teclado.key_pressed("H"):
            waveCounter = 6
        elif teclado.key_pressed("K"):
            waveCounter = 10
        elif teclado.key_pressed("G"):
            waveCounter = 11
        elif teclado.key_pressed("L"):
            waveCounter = 15
        recargaShoot = recargaShoot + janela.delta_time()
        recargaEnemies += janela.delta_time()
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
        if recargaEnemies >1 and enemyCounter<=4 + waveCounter:
            if waveCounter<= 5:
                pick = random.choice([orc1,orc2,orc3])
            elif waveCounter>5 and waveCounter <=10:
                pick = random.choice([undead1,undead2,undead3])
            elif waveCounter>10 and waveCounter<=15:
                pick = random.choice([demon1,demon2,demon3])
            enemies.append([initialEnemyX,initialEnemyY, pick.direita,pick])
            enemyCounter +=1
            recargaEnemies = 0
        if waveCounter == 5 and OrcChiefBool:
            Boss.append([initialEnemyX,initialEnemyY,OrcChief.direita,OrcChief])
            OrcChiefBool=False
        if waveCounter == 10 and FrankensteinBool:
            Boss.append([initialEnemyX,initialEnemyY,Frankenstein.direita, Frankenstein])
            FrankensteinBool=False
        if waveCounter == 15 and TheDevilBool:
            Boss.append([initialEnemyX,initialEnemyY,TheDevil.direita, TheDevil])
            TheDevilBool=False
        if enemyCounter>3 + waveCounter and enemies == [] and Boss == []:
            if waveCounter ==15:
                return 1
            else:
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
        if player.life <= 0:
            return 0
        if teclado.key_pressed("ESC"):
            return -1
        Player.explosoesUpdate(explosoes, janela)
        Player.playerCollideEnemies(player, Player.getPlayerSprite(direction, player, teclado), enemies,Boss, janela)
        waveSprites[0].draw()
        waveSprites[waveCounter].draw()
        janela.update()
