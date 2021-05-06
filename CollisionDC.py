from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
###################### Collisions ######################

def sceneryCollision(objectPosX, objectPosY, actor):
    if objectPosX >= 573- actor.width and objectPosY >= 200 - actor.height and objectPosY <= 315:
        return True
    if objectPosX >= 580- actor.width and objectPosY >= 315 - actor.height and objectPosY <= 327 :
        return True
    if objectPosX >= 593- actor.width and objectPosY >= 327 - actor.height and objectPosY <= 380:
        return True
    if objectPosX >= 550- actor.width and objectPosY >= 186 - actor.height and objectPosY <= 243:
        return True
    if objectPosX >= 561 - actor.width and objectPosY >= 243 - actor.height  and objectPosY <= 257:
        return True
    if objectPosX >= 535 - actor.width and objectPosY >= 176- actor.height and objectPosY <= 186:
        return True
    if objectPosX >= 521 - actor.width and objectPosY <= 178:
        return True
    if objectPosX >= 508 - actor.width and objectPosY <= 165:
        return True
    if objectPosX >= 499 - actor.width and objectPosY <= 150:
        return True
    if objectPosX >= 486 - actor.width and objectPosY <= 140:
        return True
    if objectPosX >= 479 - actor.width and objectPosY <= 125:
        return True
    if objectPosX >= 519 - actor.width and objectPosX <= 551 and objectPosY >= 234 - actor.height and objectPosY <= 271:
        return True
    if objectPosY >= 338 - actor.height and objectPosY <= 418 and objectPosX <= 135:
        return True
    if objectPosY <= 305 and objectPosY >= 300 - actor.height and objectPosX >= 100 and objectPosX <= 140:
        return True
    if objectPosX >= 128 and objectPosX <= 148 and objectPosY >= 280 - actor.height and objectPosY <= 294:
        return True
    if objectPosX <= 140 and objectPosY <= 280 and objectPosY >= 260 - actor.height:
        return True
    if objectPosX <= 150 and objectPosY <= 256  and objectPosY >= 234 - actor.height:
        return True
    if objectPosX <= 210 and objectPosY <= 234  and objectPosY >= 160 - actor.height:
        return True
    if objectPosX >= 210 and objectPosX <= 242  and objectPosY <= 160:
        return True
    if objectPosX >= 250 and objectPosX <= 280 and objectPosY <= 180 and objectPosY >= 168 - actor.height:
        return True
    if objectPosY - actor.height >= objectPosX + 135 and objectPosX >= 285 and objectPosX <= 300 and objectPosY >= 420 - actor.height and objectPosY <= 435:
        return True
    if objectPosX <= 100:
        return True
    if objectPosX >= 543 and objectPosX <= 600 and objectPosY >= 379- actor.height :
        return True
    if objectPosY >= 401 - actor.height and objectPosX <= 544:  ###Fundo
        return True
    if objectPosX >= 519 and objectPosX <= 551 and objectPosY >= 234 - actor.height and objectPosY <= 271:
        return True
    if objectPosY <= 105:
        return True
    if objectPosX >= 272 - actor.width and objectPosX <= 302 and objectPosY >= 134 - actor.height and objectPosY <= 160:
        return True
    if objectPosX >= 240 - actor.width and objectPosX <= 265 and objectPosY >= 140 - actor.height and objectPosY <= 157:
        return True
    if objectPosX >= 356 - actor.width and objectPosX <= 395 and objectPosY >= 127 - actor.height and objectPosY <= 130:
        return True
    if objectPosY <= 147 and objectPosX >= 400 and objectPosX <= 463:
        return True
    if objectPosY <= 137 and objectPosX >= 460 and objectPosX <= 487:
        return True
    if objectPosX >= 418 - actor.width and objectPosX <= 438 and objectPosY >= 321 - actor.height and objectPosY <= 344:
        return True
    if objectPosX >= 488 - actor.width and objectPosX <= 508 and objectPosY >= 361 - actor.height and objectPosY <= 379:
        return True
    if objectPosX >= 568 - actor.width and objectPosX <= 590 and objectPosY >= 329 - actor.height and objectPosY <= 349:
        return True
    if objectPosX >= 239 - actor.width and objectPosX <= 268 and objectPosY >= 280 - actor.height and objectPosY <= 344:
        return True
    if objectPosX >= 215 - actor.width and objectPosX <= 227 and objectPosY >= 281 - actor.height and objectPosY <= 340:
        return True
    if objectPosX >= 239 - actor.width and objectPosX <= 262 and objectPosY >= 259 - actor.height and objectPosY <= 283:
        return True
    if objectPosX >= 256 - actor.width and objectPosX <= 284 and objectPosY >= 279 - actor.height and objectPosY <= 287:
        return True
    if objectPosX >= 262 - actor.width and objectPosX <= 276 and objectPosY >= 274 - actor.height and objectPosY <= 279:
        return True
    if objectPosX >= 263 - actor.width and objectPosX <= 272 - actor.width and objectPosY >= 260 - actor.height and objectPosY <= 268:
        return True
    if objectPosX >= 287 - actor.width and objectPosX <= 305 and objectPosY >= 309 - actor.height and objectPosY <= 333:
        return True
    if objectPosX >= 270 - actor.width and objectPosX <= 282 and objectPosY >= 295 - actor.height and objectPosY <= 335:
        return True
    if objectPosY <= 133 and objectPosX <= 285:
        return True
    if objectPosX >= 399 - actor.width and objectPosX <= 415 and objectPosY >= 143 - actor.height and objectPosY <= 147:
        return True
    if objectPosX >= 293 - actor.width and objectPosX <= 307 and objectPosY >= 256 - actor.height and objectPosY <= 255:
        return True
    if objectPosX >= 228 - actor.width and objectPosX <= 241 and objectPosY >= 280 - actor.height and objectPosY <= 340:
        return True
    return False


def collidedLake(objectPosX, objectPosY, actor):
    if objectPosX >= 264 - actor.width and objectPosX <= 416 and objectPosY >= 205 - actor.height and objectPosY <= 229:
        return True
    if objectPosX >= 277 - actor.width and objectPosX <= 403 and objectPosY >= 192 - actor.height and objectPosY <= 200:
        return True
    if objectPosX >= 288 - actor.width and objectPosX <= 350 and objectPosY >= 184 - actor.height and objectPosY <= 188:
        return True
    if objectPosX >= 301 - actor.width and objectPosX <= 336 and objectPosY >= 167 - actor.height and objectPosY <= 179:
        return True
    if objectPosX >= 285 - actor.width and objectPosX <= 427 and objectPosY >= 235 - actor.height and objectPosY <= 246:
        return True
    if objectPosX >= 310 - actor.width and objectPosX <= 395 and objectPosY >= 259 - actor.height and objectPosY <= 258:
        return True
    if objectPosX >= 362 - actor.width and objectPosX <= 382 and objectPosY >= 262 - actor.height and objectPosY <= 270:
        return True
    if objectPosX >= 300 - actor.width and objectPosX <= 370 and objectPosY >= 270 - actor.height and objectPosY <= 260:
        return True
    return False
############################################
