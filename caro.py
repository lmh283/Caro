import pygame,sys
from pygame.locals import *
import numpy as np
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption('Caro')

list_pos = []
a = np.zeros((11,11), dtype = int)
winner = 0
kiemtra = False

def draw_background(): # kẻ các ô vuông
    bg = (255,255,200)
    grid  = (0,0,0)
    win.fill(bg)
    for i in range(1,10):
        pygame.draw.line(win, grid, (0, i*50), (500, i*50), 2)
        pygame.draw.line(win, grid, (i*50, 0), (i*50, 500), 2)
print(len(list_pos))


def draw_object():  # vẽ các đối tượng X O
    i = 0
    d = 0
    while i<len(list_pos):

        pos_x = list_pos[i][0]
        pos_y = list_pos[i][1]
        if (i%2 == 0):
            pygame.draw.line(win, (255, 0, 0), (pos_x*50-45, pos_y*50-45), (pos_x*50-5,pos_y*50-5), 3)
            pygame.draw.line(win, (255, 0, 0), (pos_x*50-5, pos_y*50-45), (pos_x*50-45,pos_y*50-5), 3)
        else:
            pygame.draw.circle(win, (0, 0, 255), (pos_x*50-25, pos_y*50-25), 21, 3)
        i += 1

def check_winner(x,pos_x,pos_y):  # kiểm tra thắng thua của X O
    dem = 0
    for i in range(pos_x,11):
        if (a[i][pos_y] == x):
            dem += 1
            print(i,' ',pos_y)
        else:
            for j in range(pos_x-1,1,-1):
                if (a[j][pos_y] == x):
                    dem += 1
                    print(j,' ',pos_y)
                else:
                    break
            break
    if (dem == 5):
        print(x, 'đã thắng ')
        return True

    dem = 0
    for i in range(pos_y,11):
        if (a[pos_x][i] == x):
            dem += 1
            print(i,' ',pos_y)
        else:
            for j in range(pos_y-1,1,-1):
                if (a[pos_y][j] == x):
                    dem += 1
                    print(j,' ',pos_y)
                else:
                    break
            break
    if (dem == 5):
        print(x, 'đã thắng ')
        return True

    dem = 1
    for i in range(1,11-pos_x):
        if (a[pos_x+i][pos_y+i] == x):
            dem += 1
            print(i,' ',pos_y)
        else:
            for j in range(1,pos_x):
                if (a[pos_x-j][pos_y-j] == x):
                    dem += 1
                    print(j,' ',pos_y)
                else:
                    break
            break
    if (dem == 5):
        print(x, 'đã thắng ')
        return True

    dem = 1
    for i in range(1,11-pos_x):
        if (a[pos_x+i][pos_y-i] == x):
            dem += 1
            print(i,' ',pos_y)
        else:
            for j in range(1,pos_x):
                if (a[pos_x-j][pos_y+j] == x):
                    dem += 1
                    print(j,' ',pos_y)
                else:
                    break
            break
    if (dem == 5):
        print(x, 'đã thắng ')
        return True
    

def draw_winner(x): # vẽ title chiến thắng
    title1 = f"Người chơi {x} đã chiến thắng"
    title2 = "Click to play again !!"
    font = pygame.font.Font('DFVN BridgeType-Regular.ttf', 17)
    text1 = font.render(title1, True, (0, 0, 255))
    text2 = font.render(title2, True, (0, 0, 255))
    pygame.draw.rect(win, (0, 255, 0), (500//2 - 100,500//2 - 25, 200, 25))
    pygame.draw.rect(win, (0, 255, 0), (500//2 - 100,500//2 - 100, 200, 50))
    win.blit(text1, (500//2 - 100, 500//2 - 25 ))
    win.blit(text2, (500//2 - 75, 500//2 - 80 ))


while True:
    draw_background()
    draw_object()
    if (kiemtra):
        draw_winner(winner)
    for event in pygame.event.get():
        if (kiemtra):
            if event.type == MOUSEBUTTONUP:
                list_pos = []
                a = np.zeros((11,11), dtype = int)
                winner = 0
                kiemtra = False
        else:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]//50 + 1
                pos_y = pos[1]//50 + 1
                luu = [pos_x,pos_y]
                if (luu in list_pos):
                    continue
                else:
                    list_pos.append(luu)
                    if (len(list_pos)%2 == 1):
                        a[pos_x,pos_y] = 1
                        x = 1
                        kiemtra = check_winner(x,pos_x,pos_y)
                        if (kiemtra):
                            winner = 'X'
                    else:
                        a[pos_x,pos_y] = 2
                        x = 2
                        kiemtra = check_winner(x,pos_x,pos_y)
                        if (kiemtra):
                            winner = 'O'
    pygame.display.update()
pygame.quit()
