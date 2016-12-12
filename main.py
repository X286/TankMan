import Graphics.BaseObj as Graphics
import pygame

def main ():
    screen = pygame.display.set_mode((800, 600))
    net = Graphics.Net(line_width=1, tileWidthHeight=(52,52))
    net.printOnTiles(block_num=(10, 10))
    cat = Graphics.ImgEditClass('res/sprite/cat.png')
    test = Graphics.AnimatetdSprite(390, 185, 135, 140)
    test.set_animation_list(
        cat.cut_image(20, 180,  135, 140), cat.cut_image(192, 180,  135, 140),
        cat.cut_image(20, 340,  135, 140), cat.cut_image(192, 340,  135, 140))

    pygame.init()
    MoveFigure_down = pygame.USEREVENT + 1
    pygame.time.set_timer(MoveFigure_down, 350)
    FPS = pygame.time.Clock()
    isWorking=True

    while (isWorking):
        FPS.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False
            if event.type == MoveFigure_down:
                test.animate()

        screen.fill(pygame.Color('#000000'))
        net.draw(screen)
        test.draw(screen)
        pygame.display.flip()



if __name__ == '__main__':
    main()