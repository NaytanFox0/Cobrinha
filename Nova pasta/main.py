import pygame # type: ignore
import math

class snake:
    def __init__(self) -> None:
        pass

class segment:
    def __init__(self, width, height, color, pos, fixed = (None, None)) -> None:
        self.img = pygame.Surface((width, height))
        self.img.fill(color)
        self.pos = list(pos)
        self.fixed = fixed

    def draw(self, screen) -> None:
        screen.blit(self.img, self.pos)

    def update(self) -> None:
        if self.fixed[0] is not None:
            angle = math.atan2(self.fixed[0].pos[1] - self.pos[1], self.fixed[0].pos[0] - self.pos[0])

            self.pos[0] = self.fixed[0].pos[0] - math.cos(angle) * self.fixed[1]
            self.pos[1] = self.fixed[0].pos[1] - math.sin(angle) * self.fixed[1]

class Windows:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

    def Render(self) -> None:
        self.screen.fill((0, 0, 0))

        for s in body:
            s.draw(self.screen)

        pygame.display.flip()

    def Update(self) -> None:
        for s in body:
            s.update()

    def HandleProc(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()

        sA.pos[1] += (keys[pygame.K_s] - keys[pygame.K_w]) * 3
        sA.pos[0] += (keys[pygame.K_d] - keys[pygame.K_a]) * 3

    def Run(self) -> None:
        while self.running:
            self.HandleProc()
            self.Update()
            self.Render()
            self.clock.tick(60) 
        pygame.quit()

win = Windows(800, 600)

sA = segment(10, 10, (255, 255, 255), (100, 100))
sB = segment(10, 10, (255, 255, 127), (0, 0), (sA, 10))
sC = segment(10, 10, (255, 255, 127), (0, 0), (sB, 10))
sD = segment(10, 10, (255, 255, 127), (0, 0), (sC, 10))
sE = segment(10, 10, (255, 255, 127), (0, 0), (sD, 10))
body = [sA, sB, sC, sD, sE]

win.Run()