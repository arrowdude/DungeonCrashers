from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
import CollisionDC
import Player
import random
###################### Enemy mechanics ######################
class enemy:
    def __init__(self, direita, esquerda, life):
        self.direita = direita
        self.esquerda = esquerda
        self.height = direita.height
        self.width = direita.width
        self.life = life

def getMaximumDiagonal(initialEnemyX,initialEnemyY, playerX, playerY, Enemy):
    enemyPosXMaximum = initialEnemyX
    enemyPosYMaximum = initialEnemyY
    while (not(CollisionDC.sceneryCollision(enemyPosXMaximum,enemyPosYMaximum,Enemy) or CollisionDC.collidedLake(enemyPosXMaximum, enemyPosYMaximum, Enemy))):
        if ((initialEnemyX> playerX and enemyPosXMaximum<playerX) or(initialEnemyX< playerX and enemyPosXMaximum>playerX)) and ((initialEnemyY>= playerY and enemyPosYMaximum<=playerY) or(initialEnemyY<= playerY and enemyPosYMaximum>=playerY)):
            break
        if initialEnemyX > playerX:
                enemyPosXMaximum = enemyPosXMaximum - 1
        elif initialEnemyX < playerX:
                enemyPosXMaximum = enemyPosXMaximum + 1
        if initialEnemyY > playerY:
                enemyPosYMaximum = enemyPosYMaximum - 1
        elif initialEnemyY < playerY:
                enemyPosYMaximum = enemyPosYMaximum + 1
    return ([enemyPosXMaximum, enemyPosYMaximum])

def getMaximum(initialEnemyX,initialEnemyY, playerX, playerY, Enemy):
    enemyPosXMaximum = initialEnemyX
    enemyPosYMaximum = initialEnemyY
    while (not (CollisionDC.sceneryCollision(enemyPosXMaximum, initialEnemyY, Enemy) or CollisionDC.collidedLake(enemyPosXMaximum,initialEnemyY, Enemy))):
        if ((initialEnemyX > playerX and enemyPosXMaximum < playerX) or (initialEnemyX < playerX and enemyPosXMaximum > playerX)):
            break
        if initialEnemyX > playerX:
                enemyPosXMaximum = enemyPosXMaximum - 1
        elif initialEnemyX < playerX:
                enemyPosXMaximum = enemyPosXMaximum + 1
    while (not (CollisionDC.sceneryCollision(enemyPosXMaximum, initialEnemyY, Enemy) or CollisionDC.collidedLake(enemyPosXMaximum, initialEnemyY,Enemy))):
        if ((initialEnemyY>= playerY and enemyPosYMaximum<=playerY) or(initialEnemyY<= playerY and enemyPosYMaximum>=playerY)):
            break
        if initialEnemyY > playerY:
                enemyPosYMaximum = enemyPosYMaximum - 1
        elif initialEnemyY < playerY:
                enemyPosYMaximum = enemyPosYMaximum + 1
    return ([enemyPosXMaximum, enemyPosYMaximum])


def moveEnemy(playerX, playerY, initialEnemyX, initialEnemyY, speed, Enemy, sprite, janela):
    maximumXD, maximumYD = getMaximumDiagonal(initialEnemyX, initialEnemyY, playerX, playerY, Enemy)[0], getMaximumDiagonal(initialEnemyX, initialEnemyY, playerX, playerY, Enemy)[1]
    #print("MaximumD: ",maximumXD,maximumYD)
    #print("Maximum: ", maximumX, maximumY)
    #print("Enemy: ",initialEnemyX,initialEnemyY)
    #print("Player: ",playerX,playerY)
    if (maximumXD >= playerX and initialEnemyX >= playerX) or (maximumXD <= playerX and initialEnemyX <= playerX):
        if playerX >= 370 and playerY >= 284 and initialEnemyX >= 370 and initialEnemyY >= 284:
            if playerY > initialEnemyY:
                velY = speed
            else:
                velY = -speed
        elif playerX<370 and initialEnemyX<370:
            if playerY <=280 and playerX <260:
                velY = -speed
            else:
                velY = speed
        else:
            velY = speed
    else:
        if initialEnemyY >= playerY:
            velY = -speed
        elif initialEnemyY < playerY:
            velY = speed

    if((maximumYD >= playerY and initialEnemyY >= playerY) or (maximumYD <= playerY and initialEnemyY <= playerY)):
        if playerX>=370 and playerY>=284 and initialEnemyX>=370 and initialEnemyY>=284:
            if playerX > initialEnemyX:
                velX = speed
                if not (initialEnemyX >= playerX and initialEnemyX < playerX + Enemy.width):
                    sprite = Enemy.esquerda
            else:
                velX = -speed
                if not (initialEnemyX >= playerX and initialEnemyX < playerX + Enemy.width):
                    sprite = Enemy.direita
        elif playerX<370 and initialEnemyX<370:
            if playerY <=280 and playerX <260:
                velX = -speed
            else:
                velX = speed
        else:
            velX = speed
    else:
        if initialEnemyX >= playerX:
            velX = -speed
            if not(initialEnemyX >= playerX and initialEnemyX < playerX + Enemy.width):
                sprite = Enemy.esquerda
        elif initialEnemyX < playerX:
            velX = speed
            if not(initialEnemyX >= playerX and initialEnemyX < playerX + Enemy.width):
                sprite = Enemy.direita
    if not CollisionDC.sceneryCollision(initialEnemyX + velX * janela.delta_time(), initialEnemyY, Enemy) and not CollisionDC.collidedLake(initialEnemyX + velX * janela.delta_time(), initialEnemyY, Enemy):
        initialEnemyX = initialEnemyX + velX*janela.delta_time()
    if not CollisionDC.sceneryCollision(initialEnemyX, initialEnemyY + velY * janela.delta_time(), Enemy) and not CollisionDC.collidedLake(initialEnemyX, initialEnemyY + velY * janela.delta_time(), Enemy):
        initialEnemyY = initialEnemyY+ velY*janela.delta_time()
    return([initialEnemyX,initialEnemyY, sprite, Enemy])



def updateBossPosition(initialx,initialy,Boss,speed, tiros, explosoes, janela):
    for enemy in Boss:
        enemy[0], enemy[1], enemy[2] = moveEnemy(initialx,initialy,enemy[0],enemy[1], speed, enemy[3], enemy[2],janela)[0], moveEnemy(initialx,initialy,enemy[0],enemy[1], speed, enemy[3], enemy[2],janela)[1], moveEnemy(initialx,initialy,enemy[0],enemy[1], speed, enemy[3], enemy[2],janela)[2]
        enemy[2].set_position(enemy[0],enemy[1])
        enemy[2].set_total_duration(1000)
        enemy[2].draw()
        enemy[2].update()
        for tiro in tiros:
            if Collision.collided(enemy[2], tiro[0]):
                tiros.remove(tiro)
                enemy[3].life -= 1
                Player.explosaoGen(enemy[0], enemy[1], explosoes)
                if enemy[3].life == 0:
                    Boss.remove(enemy)

def updateEnemyPosition(initialx,initialy,enemies,speed, tiros, explosoes,  janela):
    for enemy in enemies:
        enemy[0], enemy[1], enemy[2] = moveEnemy(initialx,initialy,enemy[0],enemy[1], speed, enemy[3], enemy[2],janela)[0], moveEnemy(initialx,initialy,enemy[0],enemy[1], speed, enemy[3], enemy[2],janela)[1], moveEnemy(initialx,initialy,enemy[0],enemy[1], speed, enemy[3], enemy[2],janela)[2]
        enemy[2].set_position(enemy[0],enemy[1])
        enemy[2].set_total_duration(1000)
        enemy[2].draw()
        enemy[2].update()
        for tiro in tiros:
            if Collision.collided(enemy[2], tiro[0]):
                tiros.remove(tiro)
                enemies.remove(enemy)
                Player.explosaoGen(enemy[0], enemy[1], explosoes)