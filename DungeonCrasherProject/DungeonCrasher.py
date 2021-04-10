from PPlay.window import *
from PPlay.sprite import *

janela = Window(700,437)
background = Sprite("background.png",18)
background.set_total_duration(1100)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
player_parado_esquerda = Sprite("player_parado_esquerda.png",2)
player_parado_direita = Sprite("player_parado_direita.png",2)
player_walk_esquerda = Sprite("player_walk_esquerda.png",8)
player_walk_direita = Sprite("player_walk_direita.png",8)
player_parado_esquerda.set_total_duration(1000)
player_parado_direita.set_total_duration(1000)
player_walk_esquerda.set_total_duration(1000)
player_walk_direita.set_total_duration(1000)

#Variaveis
player_height = player_parado_esquerda.height
player_width = player_parado_esquerda.width
initialx = 400
initialy = 300
direction = "r"
velTiro = 200
recarga = 0
tiros = []
explosoes = []

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

def getLastDirection(direction):
    if teclado.key_pressed("LEFT"):
        direction = "l"
    elif teclado.key_pressed("RIGHT"):
        direction = "r"
    return direction

def collidedLake(objectPosX,objectPosY):
    if objectPosX>=264-player_width and objectPosX<=416 and objectPosY>=205-player_height and objectPosY<=229:
        return True
    if objectPosX >= 277 - player_width and objectPosX <= 403 and objectPosY >= 192 - player_height and objectPosY <= 200:
        return True
    if objectPosX >= 288 - player_width and objectPosX <= 350 and objectPosY >= 184 - player_height and objectPosY <= 188:
        return True
    if objectPosX >= 301 - player_width and objectPosX <= 336 and objectPosY >= 167 - player_height and objectPosY <= 179:
        return True
    if objectPosX >= 285 - player_width and objectPosX <= 427 and objectPosY >= 235 - player_height and objectPosY <= 246:
        return True
    if objectPosX >= 310 - player_width and objectPosX <= 395 and objectPosY >= 259 - player_height and objectPosY <= 258:
        return True
    if objectPosX >= 362 - player_width and objectPosX <= 382 and objectPosY >= 262 - player_height and objectPosY <= 270:
        return True
    if objectPosX >= 300 - player_width and objectPosX <= 370 and objectPosY >= 270 - player_height and objectPosY <= 260:
        return True
def sceneryCollision(objectPosX,objectPosY):
    if objectPosX >= 573 and objectPosY >= 200 and objectPosY <= 315:
        return True
    if objectPosX >= 580 and objectPosY >= 315 and objectPosY <= 327:
        return True
    if objectPosX >= 593 and objectPosY >= 327 and objectPosY <= 380:
        return True
    if objectPosX >= 550 and objectPosY >= 186 and objectPosY <= 243:
        return True
    if objectPosX >= 561 and objectPosY >= 243 and objectPosY <= 257:
        return True
    if objectPosX >= 535 and objectPosY >= 176 and objectPosY <= 186:
        return True
    if objectPosX >= 521 and objectPosY <= 178:
        return True
    if objectPosX >= 508 and objectPosY <= 165:
        return True
    if objectPosX >= 499 and objectPosY <= 150:
        return True
    if objectPosX >= 486 and objectPosY <= 140:
        return True
    if objectPosX >= 479 and objectPosY <= 125:
        return True
    if objectPosX >= 519 and objectPosX <= 551 and objectPosY >= 234 and objectPosY <= 271:
        return True
    if objectPosY >= 338-player_height and objectPosY<=418 and objectPosX<=135:
        return True
    if objectPosY<=305 and objectPosY>=300-player_height and objectPosX >=100 and objectPosX<=140:
        return True
    if objectPosX>=128 and objectPosX<=148 and objectPosY>=280-player_height and objectPosY<=294:
        return True
    if objectPosX<=140 and objectPosY<=280 and objectPosY>=260-player_height:
        return True
    if objectPosX<=150 and objectPosY<=256 and objectPosY>=234-player_height:
        return True
    if objectPosX<=210 and objectPosY<=234 and objectPosY>=160-player_height:
        return True
    if objectPosX>=210 and objectPosX<=242 and objectPosY<=160:
        return True
    if objectPosX>=250 and objectPosX<=280 and objectPosY<=180 and objectPosY>=168-player_height:
        return True
    if objectPosY-player_height >= objectPosX +135 and objectPosX>=285 and objectPosX<=300 and objectPosY>=420 and objectPosY<=435:
        return True
    if objectPosX <= 100:
        return True
    if objectPosX >= 543 and objectPosX <= 600 and objectPosY >= 379:
        return True
    if objectPosY >= 401 and objectPosX >= 0 and objectPosX <= 544:  ###Fundo
        return True
    if objectPosX >= 519 and objectPosX <= 551 and objectPosY >= 234 and objectPosY <= 271:
        return True
    if objectPosY<=115:
        return True
    if objectPosX>=272-player_width and objectPosX<=302 and objectPosY>=134-player_height and objectPosY<=160:
        return True
    if objectPosX>=240-player_width and objectPosX<=265 and objectPosY>=140-player_height and objectPosY<=157:
        return True
    if objectPosX>=356-player_width and objectPosX<=395 and objectPosY>=127-player_height and objectPosY<=141:
        return True
    if objectPosY <=147 and objectPosX>=400 and objectPosX<=463:
        return True
    if objectPosY <=137 and objectPosX>=460 and objectPosX<=487:
        return True
    if objectPosX>=418-player_width and objectPosX<=438 and objectPosY>=321-player_height and objectPosY<=344:
        return True
    if objectPosX>=488-player_width and objectPosX<=508 and objectPosY>=361-player_height and objectPosY<=379:
        return True
    if objectPosX>=568-player_width and objectPosX<=590 and objectPosY>=329-player_height and objectPosY<=349:
        return True
    if objectPosX>=239-player_width and objectPosX<=268 and objectPosY>=280-player_height and objectPosY<=344:
        return True
    if objectPosX>=215-player_width and objectPosX<=227 and objectPosY>=281-player_height and objectPosY<=340:
        return True
    if objectPosX>=239-player_width and objectPosX<=262 and objectPosY>=259-player_height and objectPosY<=283:
        return True
    if objectPosX >= 256 - player_width and objectPosX <= 284 and objectPosY >= 279 - player_height and objectPosY <= 287:
        return True
    if objectPosX >= 262 - player_width and objectPosX <= 276 and objectPosY >= 274 - player_height and objectPosY <= 279:
        return True
    if objectPosX >= 263 - player_width and objectPosX <= 272-player_width and objectPosY >= 260 - player_height and objectPosY <= 268:
        return True
    if objectPosX >= 287 - player_width and objectPosX <= 305 and objectPosY >= 309 - player_height and objectPosY <= 333:
        return True
    if objectPosX >= 270 - player_width and objectPosX <= 282 and objectPosY >= 295 - player_height and objectPosY <= 343:
        return True
def movePlayer(initialx, initialy):
    player_pos_x = initialx
    player_pos_y = initialy
    if teclado.key_pressed("LEFT"):
        player_vel_x = -100
    elif teclado.key_pressed("RIGHT"):
        player_vel_x = 100
    else:
        player_vel_x = 0
    if teclado.key_pressed("UP"):
        player_vel_y = -100
    elif teclado.key_pressed("DOWN"):
        player_vel_y = 100
    else:
        player_vel_y = 0
    if not sceneryCollision(player_pos_x + player_vel_x*janela.delta_time(),player_pos_y + player_vel_y*janela.delta_time()) and not collidedLake(player_pos_x + player_vel_x*janela.delta_time(),player_pos_y + player_vel_y*janela.delta_time()):
        player_pos_x = player_pos_x + player_vel_x*janela.delta_time()
        player_pos_y = player_pos_y + player_vel_y*janela.delta_time()
    return([player_pos_x,player_pos_y])


def shoot(initialx,initialy,direction):
    tiroX = initialx
    tiroY = initialy
    if teclado.key_pressed("UP"):
        direction = "u"
        tiro = Sprite("tiroVerticalCima.png", 4)
    elif teclado.key_pressed("DOWN"):
        direction = "d"
        tiro = Sprite("tiroVerticalBaixo.png",4)
    else:
        direction = getLastDirection(direction)
        if direction == "r":
            tiro = Sprite("tiroLateralDireita.png", 4)
        else:
            tiro = Sprite("tiroLateralEsquerda.png", 4)
    tiros.append([tiro, tiroX, tiroY, direction])
    return (tiros)

def explosaoGen(posX,posY):
    explosao = Sprite("explosao.png", 8)
    explosao.set_total_duration(1000)
    explosao.set_position(posX,posY)
    explosoes.append([explosao,0])

while True:
    recarga = recarga + janela.delta_time()
    direction = getLastDirection(direction)
    movePlayer(initialx,initialy)
    initialx = movePlayer(initialx, initialy)[0]
    initialy = movePlayer(initialx, initialy)[1]
    if mouse.is_button_pressed(BUTTON_LEFT):
        print(mouse.get_position())
    if mouse.is_button_pressed(BUTTON_RIGHT):
        print(initialx,initialy)
    while teclado.key_pressed("SPACE") and recarga>1:
        shoot(initialx,initialy,direction)
        recarga-= 0.40
    background.draw()
    background.update()
    getPlayerSprite(direction).set_position(initialx,initialy)
    getPlayerSprite(direction).draw()
    getPlayerSprite(direction).update()
    for tiro in tiros:
        tiro[0].set_position(tiro[1], tiro[2])
        tiro[0].set_total_duration(1000)
        tiro[0].update()
        tiro[0].draw()
        if tiro[3] == "u":
            tiro[2] = tiro[2] - velTiro * janela.delta_time()
        elif tiro[3] == "d":
            tiro[2] = tiro[2] + velTiro * janela.delta_time()
        elif tiro[3] == "l":
            tiro[1] = tiro[1] - velTiro*janela.delta_time()
        elif tiro[3] == "r":
            tiro[1] = tiro[1] + velTiro * janela.delta_time()
        if sceneryCollision(tiro[1],tiro[2]):
            explosaoGen(tiro[1],tiro[2])
            tiros.remove(tiro)
    for explosao in explosoes:
        explosao[1] += janela.delta_time()
        explosao[0].draw()
        explosao[0].update()
        if explosao[1]>=1:
            explosoes.remove(explosao)
    janela.update()
