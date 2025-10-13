import pygame
import constants
import player
import asteroid
import asteroidfield

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)

    pl_x = constants.SCREEN_WIDTH / 2
    pl_y = constants.SCREEN_HEIGHT / 2
    pl1 = player.Player(pl_x, pl_y)

    asteroidfield1 = asteroidfield.AsteroidField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"black")
        updatable.update(dt)
        for obj in updatable:
            if hasattr(obj, "colliding"):
                if obj != pl1 and obj.colliding(pl1):
                    print("Game over!")
                    return True     # Exit game (player died)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
