import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    ton03 = pg.transform.flip(pg.image.load("ex01/fig/3.png"),True,False)
    ton03a = pg.transform.rotozoom(ton03,10,1)
    ton_li = [pg.transform.rotozoom(ton03,i,1) for i in range(-10,11,2)]
    ton_li_r = reversed(ton_li)
    ton_li += ton_li_r
    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False), [1600+bg_x, 0])
        screen.blit(bg_img, [3200+bg_x, 0])
        screen.blit(ton_li[tmr%len(ton_li)],[300,200])
        bg_x = (tmr%3200)*-1
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()