import pygame
from level import Level

level_layout = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,"P",0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]

def main():
    display_height = 1200
    display_width = 1200

    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("RUSH HOUR")

    level = Level(level_layout)

    pygame.init()

    level.all_sprites.draw(display)

    running = True



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
    

    pygame.quit()


if __name__ == "__main__":
    main()