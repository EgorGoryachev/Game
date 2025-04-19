from pygame import *
from random import randint
input('Введите номер карты: ')
input('Введите дату: ')
input('Введите CVV код: ')
mixer.init()
mixer.music.load('gambling.ogg')
window = display.set_mode((500,500))
window.fill((240,123,44))
font.init()
font_1 = font.Font(None,40)
clock = time.Clock()
weapon = ['p90 Новое снаряжение','Лотос','Пустынный повстанец','Нож Боуи', 'Azimov','kerambit', 'Dragon lore']
game = True
text = font_1.render("",True,(255,0,0))
balance_count = 0
balance = font_1.render("Ваш баланс: " + str(balance_count) ,True,(255,0,0))
while game:
    window.fill((240,123,44))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_q:
                number = randint(0, len(weapon) - 1)
                text = font_1.render(weapon[number],True,(255,0,0))
                balance_count += number * 2000 - 5000
                balance = font_1.render("Ваш баланс: " + str(balance_count) ,True,(255,0,0))
                mixer.music.play()
    window.blit(text,(180,230))
    window.blit(balance,(0,0))
    
    clock.tick(40)
    display.update()



