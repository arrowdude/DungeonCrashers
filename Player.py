from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
import CollisionDC

###################### Player mechanics ######################
class player:
    def __init__(self,life):

        self.parado_direita = Sprite("Actors/player_parado_direita.png",2)
        self.parado_esquerda = Sprite("Actors/player_parado_esquerda.png",2)
        self.andando_direita = Sprite("Actors/player_walk_direita.png",8)
        self.andando_esquerda = Sprite("Actors/player_walk_esquerda.png",8)
        self.life = life

        # Player invencível
        self.parado_direitaI = Sprite("Actors/player_parado_direita_Inv.png", 4)
        self.parado_esquerdaI = Sprite("Actors/player_parado_esquerda_Inv.png", 4)
        self.andando_direitaI = Sprite("Actors/player_andando_direita_Inv.png", 16)
        self.andando_esquerdaI = Sprite("Actors/player_andando_esquerda_Inv.png", 16)
        self.invincible = 0
        self.time_invincible = 0

def getLife(life):
    lifePNG = Sprite("Actors/Life.png",1)
    if life > 1:
        prim = Sprite("Actors/Life-full.png",1)
    elif life == 1:
        prim = Sprite("Actors/Life-half.png", 1)
    else:
        prim = Sprite("Actors/Life-Empty.png", 1)
    if life > 3:
        seg = Sprite("Actors/Life-full.png",1)
    elif life == 3:
        seg = Sprite("Actors/Life-half.png", 1)
    else:
        seg = Sprite("Actors/Life-Empty.png", 1)
    if life > 5:
        ter = Sprite("Actors/Life-full.png",1)
    elif life == 5:
        ter = Sprite("Actors/Life-half.png", 1)
    else:
        ter = Sprite("Actors/Life-Empty.png", 1)
    prim.y = seg.y = ter.y = lifePNG.y = 25
    prim.x = 50 + prim.width
    seg.x = 100 + prim.width
    ter.x = 150 + prim.width
    lifePNG.x = 10
    prim.draw()
    seg.draw()
    ter.draw()
    lifePNG.draw()


    return prim,seg, ter

def playerCollideEnemies(player,sprite,enemies,Boss,janela):
    if player.invincible:
        if player.time_invincible > 2:
            player.invincible = 0
            player.time_invincible = 0
        else:
            player.time_invincible += janela.delta_time()
    else:
        for enemy in enemies:
            if Collision.collided(sprite,enemy[2]):
                player.life -= 1
                player.invincible = 1
        for enemy in Boss:
            if Collision.collided(sprite,enemy[2]):
                player.life -= 1
                player.invincible = 1


def getPlayerSprite(direction, player, teclado):
    if not player.invincible:
        if teclado.key_pressed("LEFT"):
            return (player.andando_esquerda)
        elif teclado.key_pressed("RIGHT"):
            return (player.andando_direita)
        else:
            if direction == "r":
                return (player.parado_direita)
            elif direction == "l":
                return (player.parado_esquerda)
    else:
        if teclado.key_pressed("LEFT"):
            return (player.andando_esquerdaI)
        elif teclado.key_pressed("RIGHT"):
            return (player.andando_direitaI)
        else:
            if direction == "r":
                return (player.parado_direitaI)
            elif direction == "l":
                return (player.parado_esquerdaI)

def getLastDirection(direction, teclado):
    if teclado.key_pressed("LEFT"):
        direction = "l"
    elif teclado.key_pressed("RIGHT"):
        direction = "r"
    return direction

def movePlayer(initialx, initialy, player, janela, teclado):
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
    if not CollisionDC.sceneryCollision(player_pos_x + player_vel_x * janela.delta_time(), player_pos_y, player) and not CollisionDC.collidedLake(player_pos_x + player_vel_x * janela.delta_time(), player_pos_y, player):
        player_pos_x = player_pos_x + player_vel_x*janela.delta_time()
    if not CollisionDC.sceneryCollision(player_pos_x, player_pos_y + player_vel_y * janela.delta_time(), player) and not CollisionDC.collidedLake(player_pos_x, player_pos_y + player_vel_y * janela.delta_time(), player):
        player_pos_y = player_pos_y + player_vel_y*janela.delta_time()
    return([player_pos_x,player_pos_y])

def shoot(initialx,initialy,direction, teclado, tiros):
    tiroX = initialx
    tiroY = initialy
    if teclado.key_pressed("UP"):
        direction = "u"
        tiro = Sprite("Actors/tiroVerticalCima.png", 4)
    elif teclado.key_pressed("DOWN"):
        direction = "d"
        tiro = Sprite("Actors/tiroVerticalBaixo.png",4)
    else:
        direction = getLastDirection(direction, teclado)
        if direction == "r":
            tiro = Sprite("Actors/tiroLateralDireita.png", 4)
        else:
            tiro = Sprite("Actors/tiroLateralEsquerda.png", 4)
    tiros.append([tiro, tiroX, tiroY, direction])
    return (tiros)

def explosaoGen(posX,posY,explosoes):
    explosao = Sprite("Actors/explosao.png", 8)
    explosao.set_total_duration(1000)
    explosao.set_position(posX,posY)
    explosoes.append([explosao,0])

def tirosUpdate(tiros, velTiro, janela, explosoes, enemies):
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
        if CollisionDC.sceneryCollision(tiro[1], tiro[2], tiro[0]):
            explosaoGen(tiro[1],tiro[2], explosoes)
            tiros.remove(tiro)

def explosoesUpdate(explosoes, janela):
    for explosao in explosoes:
        explosao[1] += janela.delta_time()
        explosao[0].draw()
        explosao[0].update()
        if explosao[1]>=1:
            explosoes.remove(explosao)

############################################