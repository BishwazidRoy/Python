import pygame
pygame.init()
window=pygame.display.set_mode((1200,400))
track=pygame.image.load('track5.png')
car=pygame.image.load('tesla.png')
car=pygame.transform.scale(car,(30,60)) #cartake soto size kore nilam
car_x=155
car_y=300
cam_x_offset=0
cam_y_offset=0
focal_dist=25
direction='up'
drive=True
clock=pygame.time.Clock()
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            drive=False
    cam_x=car_x+cam_x_offset+15
    cam_y=car_y+cam_y_offset+15

    up_px=window.get_at((cam_x,cam_y-focal_dist))[0]                #uporer ses bindu ta nirnoy korlam
    down_px=window.get_at((cam_x,cam_y+focal_dist))[0]              #down er ses er bindu ta nirdharon korlam (amar shapekkhe)
    right_px=window.get_at((cam_x+focal_dist,cam_y))[0]             #Right site er ses bindu ta nirnoy korlam(amar shapekkhe)
    print(up_px,right_px,down_px)
#ekhane kon dike jabe seta nirdharon korbo
    if direction =='up' and up_px !=255 and right_px==255:
        direction='right'
        cam_x_offset=30
        car=pygame.transform.rotate(car,(-90))
    elif direction =='right' and right_px !=255 and down_px==255:
        direction='down'
        car_x=car_x+30
        cam_x_offset=0
        cam_y_offset=30
        car=pygame.transform.rotate(car,(-90))
    elif direction =='down' and down_px !=255 and right_px==255:
        direction='right'
        car_y = car_y + 30
        cam_y_offset=0
        cam_x_offset=30
        car = pygame.transform.rotate(car, (90))

# Drive- ekhane garitake chalabo mane garita cholbe
    if direction=='up' and up_px==255:
        car_y=car_y-2
    elif direction=='right' and right_px==255:
        car_x=car_x+2
    elif direction=='down' and down_px==255:
        car_y=car_y+2
    window.blit(track,(0,0))
    window.blit(car,(car_x,car_y))
    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()
