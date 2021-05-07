from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *
import DungeonCrasher

janela = Window(700,437)
janela.set_title("Dungeon Crashers")
background = Sprite("Menu/Background Menu.png",1)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
MainTheme  = Sound("Audio/DungeonCrashersMainTheme.mp3")
MainTheme.set_volume(10)
MainTheme.set_repeat(True)
MainTheme.play()
playOn = False
gameStatus = - 1

helpInterface = False
helpIcon = Sprite("Menu/Help_icon.png",1)
helpIcon.x, helpIcon.y  = janela.width - helpIcon.width - 10, janela.height - helpIcon.height - 10

help = Sprite('Menu/Help.png',1)
help.x, help.y =janela.width/2 - help.width/2, janela.height/2 - help.height/2

result = [Sprite("Menu/Defeat.png", 1), Sprite("Menu/Victory.png", 1), Sprite("Menu/PressEsc.png", 2)]
result[2].x, result[2].y = janela.width/2-result[2].width/2, 250
result[2].set_total_duration(500)

while True:
    if mouse.is_button_pressed(BUTTON_LEFT):
        if mouse.is_over_area((171,282),(309,336)) and not (helpInterface and playOn) and gameStatus == -1:
            playOn = True
            gameStatus = DungeonCrasher.main(janela)
            playOn = False
        elif mouse.is_over_area((408,282),(531,345)) and not (helpInterface and playOn) and gameStatus == -1:
            exit()
        elif mouse.is_over_object(helpIcon) and not playOn and gameStatus == -1:
            helpInterface = True
        elif helpInterface and mouse.is_over_area((542,91),(562,108)):
            helpInterface = False

    if teclado.key_pressed("ESC"):
        gameStatus = -1

    if not playOn:
        if gameStatus >= 0:
            result[gameStatus].draw()
            result[2].draw()
            result[2].update()
        else:
            background.draw()
            helpIcon.draw()
            if helpInterface:
                help.draw()
        janela.update()