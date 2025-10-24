import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    pl_x = constants.SCREEN_WIDTH / 2
    pl_y = constants.SCREEN_HEIGHT / 2
    pl1 = Player(pl_x, pl_y)

    asteroidfield1 = AsteroidField()
    
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
                if not type(obj) in [Player, Shot] and obj.colliding(pl1):
                    print("Game over!")
                    return True     # Exit game (player died)
        for ast in asteroids:
            for bullet in shots:
                if ast.colliding(bullet):
                    ast.split()
                    bullet.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
