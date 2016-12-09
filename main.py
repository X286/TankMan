import Graphics.BaseObj as Graphics
import pygame

def main ():
    screen = pygame.display.set_mode((800, 600))

    net = Graphics.Net(line_width=1, tileWidthHeight=(52,52))
    net.printOnTiles(block_num=(10,10))


    cat = Graphics.ImgLoad('res/sprite/cat.png')
    test = Graphics.GraphicObject(390, 185, cat.fullimg.get_size()[0], cat.fullimg.get_size()[1])
    crop = [
            (20, 180,  135, 140), (192, 180,  135, 140),
            (20, 340,  135, 140), (192, 340,  135, 140)]
    count = 0
    pygame.init()

    MoveFigure_down = pygame.USEREVENT + 1
    pygame.time.set_timer(MoveFigure_down, 350)
    FPS = pygame.time.Clock()
    isWorking = True
    while (isWorking):
        FPS.tick (60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isWorking = False

            if event.type == MoveFigure_down:
                count += 1

        if count <= len (crop)-1:
            test.image = cat.fullimg.subsurface(crop[count])
        else:
            count = 0
        screen.fill (pygame.Color ('#000000'))
        net.draw(screen)
        test.draw(screen)
        pygame.display.flip()
        print FPS.get_fps()


if __name__ == '__main__':
    main()