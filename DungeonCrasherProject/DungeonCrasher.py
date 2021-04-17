from PPlay.window import *
from PPlay.sprite import *
from DungeonCrashersLib import dungeonCrashersCollision

janela = Window(700,437)
background = Sprite("background.png",18)
background.set_total_duration(1100)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
player_parado_esquerda = Sprite("Actors/player_parado_esquerda.png",2)
player_parado_direita = Sprite("Actors/player_parado_direita.png",2)
player_walk_esquerda = Sprite("Actors/player_walk_esquerda.png",8)
player_walk_direita = Sprite("Actors/player_walk_direita.png",8)
player_parado_esquerda.set_total_duration(1000)
player_parado_direita.set_total_duration(1000)
player_walk_esquerda.set_total_duration(1000)
player_walk_direita.set_total_duration(1000)

#Variaveis
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

    if not dungeonCrashersCollision.sceneryCollision(player_pos_x + player_vel_x * janela.delta_time(), player_pos_y, player_parado_esquerda) and not dungeonCrashersCollision.collidedLake(player_pos_x + player_vel_x * janela.delta_time(), player_pos_y, player_parado_esquerda):
        player_pos_x = player_pos_x + player_vel_x*janela.delta_time()
    if not dungeonCrashersCollision.sceneryCollision(player_pos_x, player_pos_y + player_vel_y * janela.delta_time(), player_parado_esquerda) and not dungeonCrashersCollision.collidedLake(player_pos_x, player_pos_y + player_vel_y * janela.delta_time(), player_parado_esquerda):
        player_pos_y = player_pos_y + player_vel_y*janela.delta_time()
    return([player_pos_x,player_pos_y])


def shoot(initialx,initialy,direction):
    tiroX = initialx
    tiroY = initialy
    if teclado.key_pressed("UP"):
        direction = "u"
        tiro = Sprite("Actors/tiroVerticalCima.png", 4)
    elif teclado.key_pressed("DOWN"):
        direction = "d"
        tiro = Sprite("Actors/tiroVerticalBaixo.png",4)
    else:
        direction = getLastDirection(direction)
        if direction == "r":
            tiro = Sprite("Actors/tiroLateralDireita.png", 4)
        else:
            tiro = Sprite("Actors/tiroLateralEsquerda.png", 4)
    tiros.append([tiro, tiroX, tiroY, direction])
    return (tiros)

def explosaoGen(posX,posY):
    explosao = Sprite("Actors/explosao.png", 8)
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
        if dungeonCrashersCollision.sceneryCollision(tiro[1], tiro[2], tiro[0]):
            explosaoGen(tiro[1],tiro[2])
            tiros.remove(tiro)
    for explosao in explosoes:
        explosao[1] += janela.delta_time()
        explosao[0].draw()
        explosao[0].update()
        if explosao[1]>=1:
            explosoes.remove(explosao)
    janela.update()
