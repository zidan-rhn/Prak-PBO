import pygame
from player import Player
from object import Block_Object, handle_move

pygame.init()

pygame.display.set_caption("Game Zidan")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1745, 1000
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    clock = pygame.time.Clock()
    bg_image = pygame.image.load("assets/Background/Mybg.jpg").convert()

    block_size = 96

    player = Player(100, 100, 50, 50)
    blocks = pygame.sprite.Group()
    floor = [Block_Object(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    blocks.add(floor)
    objects = pygame.sprite.Group(*blocks.sprites(), Block_Object(0, HEIGHT - block_size * 2, block_size),
                                  Block_Object(block_size * 3, HEIGHT - block_size * 4, block_size))

    run = True
    while run:
        clock.tick(FPS)
        window.blit(bg_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        objects.draw(window)  # Gambar semua objek
        player.draw(window)
        handle_move(player, objects)
        player.loop(FPS)
        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
