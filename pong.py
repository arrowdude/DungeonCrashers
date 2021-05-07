from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import*

janela = Window(800,545)
janela.set_title("Pong")

placar1  = 0
placar2 = 0
teclado = Window.get_keyboard()
fundo = GameImage("fundo.png")
bola = GameImage("bola.png")
bola2 = GameImage("bola.png")
pad1 = Sprite("pad.png")
pad2 = Sprite("pad.png")

#Coordenadas e velocidades
pad1y, pad2y = janela.height/2, janela.height/2
velpad = 150
bolax, bolay = janela.width/2,janela.height/2
bola2x, bola2y = janela.width/2,janela.height/2
velx, vely,vel2x,vel2y = 200,200,200,200

#Variaveis para framerate
timer = 0
frameCounter = 0
temp = 0

#2 bolas
cCounter = 0
collisionB = False
while True:
    #Controle do Pad
    if(teclado.key_pressed("W")):
        if pad1y >0:
            pad1y = pad1y - velpad*janela.delta_time()
    elif(teclado.key_pressed("S")):
        if pad1y < janela.height - pad1.height:
            pad1y = pad1y + velpad*janela.delta_time()

    #AI pad2

    #Movimento Bola
    bolax = bolax + velx*janela.delta_time()
    bolay = bolay +vely*janela.delta_time()
    #Colisoes
    if bolay >= (janela.height-bola.height):
        bolay = janela.height - bola.height #Correcao da patinacao
        vely = (-1)*vely
    if bolay <= 0:
        bolay = 0                           #Correcao da patinacao
        vely = (-1)*vely
    if pad1.collided(bola):
        bolax = 0 + pad1.width             #Correcao da patinacao
        velx = (-1)*velx
        collisionB = True
    if pad2.collided(bola):
        bolax = janela.width - pad2.width-bola.width #Correcao da Patinacao
        velx = (-1)*velx
        collisionB = True
    if collisionB:
        collisionB = False
        cCounter +=1
        print(cCounter)
    #Recomeca o jogo e aumenta o placar
    if bolax > janela.width:
        bolax, bolay = janela.width / 2, janela.height / 2
        pad1y, pad2y = janela.height / 2, janela.height / 2
        placar1 += 1
    elif bolax < 0:
        bolax, bolay = janela.width / 2, janela.height / 2
        pad1y, pad2y = janela.height / 2, janela.height / 2
        placar2 += 1

    fundo.draw()
    bola.set_position(bolax,bolay)
    pad1.set_position(0,pad1y)
    pad2.set_position(janela.width-pad2.width,pad2y)
    pad1.draw()
    pad2.draw()
    #Bola 2
    if cCounter >= 3:
        bola2.set_position(bola2x,bola2y)
        bola2x = bola2x + vel2x*janela.delta_time()
        bola2y = bola2y + vel2y*janela.delta_time()
        if bola2y >= (janela.height-bola2.height):
            bola2y = janela.height - bola2.height #Correcao da patinacao
            vel2y = (-1)*vel2y
        if bola2y <= 0:
            bola2y = 0                           #Correcao da patinacao
            vel2y = (-1)*vel2y
        if pad1.collided(bola2):
            bola2x = 0 + pad1.width             #Correcao da patinacao
            ve2lx = (-1)*vel2x
        if pad2.collided(bola2):
            bola2x = janela.width - pad2.width-bola2.width #Correcao da Patinacao
            vel2x = (-1)*vel2x
        if bola2x > janela.width or bola2x < 0:   #Se a bola2 marcar ponto, ela some e o contador de colisoes volta a 0
            if bola2x > janela.width:
                placar1 += 1
            elif bola2x<0:
                placar2 +=1
            bola2x = janela.width/2               #Bola2 aparece novamente, nas coordenadas iniciais, caso o contador de colisoes volte a 3.
            bola2x = janela.width/2               #Bola2 aparece novamente, nas coordenadas iniciais, caso o contador de colisoes volte a 3.
            bola2y = janela.height/2
            cCounter = 0
        bola2.draw()
    bola.draw()
    janela.draw_text(str(placar1)+" | "+ str(placar2), janela.width/2-50, 5, size = 50, color = (0,0,0), font_name = "Arial", bold=True, italic = False)
    janela.draw_text(str(temp),5, 5, size = 50, color = (0,0,0), font_name = "Arial", bold=True, italic = False)
    janela.update()
    frameCounter +=1
    timer += janela.delta_time()
    if timer >=1:
        temp = frameCounter
        timer = 0
        frameCounter = 0