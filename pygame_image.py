import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    ton03 = pg.transform.flip(pg.image.load("ex01/fig/3.png"),True,False)
    ton03a = pg.transform.rotozoom(ton03,10,1)
    ton_li = [ton03,ton03a]
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(ton_li[tmr%2],[300,200])
        bg_x %= 1600
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()