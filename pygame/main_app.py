import pygame

# inisialisasi game
pygame.init()
window = pygame.display.set_mode((500,500))

# object game
# posisi
x = 250
y = 250
# ukuran
panjang = 20
lebar = 20
# kecepatan
speed = 5
isRuning = True
while isRuning:
    pygame.time.delay(30)
    # user input atau databese input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRuning = False
    
    # ambil semua kyboard press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < 500-lebar:
        x += speed
    
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    if keys[pygame.K_DOWN] and y < 500-lebar:
        y += speed

    # update asset
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,120,0), (x,y,panjang,lebar))
    pygame.draw.rect(window, (255,120,0), (x-22,y,panjang,lebar))
    pygame.draw.rect(window, (255,120,0), (x-44,y,panjang,lebar))
    # render asset
    pygame.display.update()
pygame.quit()

