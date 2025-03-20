import pygame # type: ignore
import random
import math

class snake:
    def __init__(self) -> None:
        self.head = segment(15, 15, (255, 255, 255), (100, 100))
        self.body = [self.head]
        self.addSegment()
        self.addSegment()
        self.addSegment()

    def draw(self, screen):
         for s in self.body:
            s.draw(screen)

    def updateSegments(self):
        for s in self.body:
            s.update()

    def addSegment(self):
        self.body.append(segment(10, 10, (255, 255, 127), (0, 0), (self.body[-1], 10)))

class segment:
    def __init__(self, width, height, color, pos, fixed = (None, None)) -> None:
        self.img = pygame.Surface((width, height))
        self.img.fill(color)
        self.rect = self.img.get_rect(center=pos)
        self.pos = list(pos)
        self.fixed = fixed

    def draw(self, screen) -> None:
        screen.blit(self.img, self.pos)

    def update(self) -> None:
        self.rect.center = self.pos
        if self.fixed[0] is not None:
            angle = math.atan2(self.fixed[0].pos[1] - self.pos[1], self.fixed[0].pos[0] - self.pos[0])

            self.pos[0] = self.fixed[0].pos[0] - math.cos(angle) * self.fixed[1]
            self.pos[1] = self.fixed[0].pos[1] - math.sin(angle) * self.fixed[1]

    def collision(self):
        pass

class Windows:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True

    def Render(self) -> None:
        self.screen.fill((0, 0, 0))

        sn.draw(self.screen)
        apple.draw(self.screen)

        pygame.display.flip()

    def Update(self) -> None:
        sn.updateSegments()

        if apple.rect.colliderect(sn.head.rect):
            sn.addSegment()
            apple.pos = (random.randint(1, 799), random.randint(1, 699))
            apple.update()

    def HandleProc(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        keys = pygame.key.get_pressed()

        if sn.head.rect.top >= 0 and sn.head.rect.bottom =< 600 and sn.head.rect.left >= 0 and sn.head.rect.right =< 800:
            sn.head.pos[1] += (keys[pygame.K_s] - keys[pygame.K_w]) * 3
            sn.head.pos[0] += (keys[pygame.K_d] - keys[pygame.K_a]) * 3
        else:
            if sn.head.rect.top < 300:
                sn.head.pos[1] = sn.head.pos[1] + 1
            else:
                sn.head.pos[1] = sn.head.pos[1] - 1 

            if sn.head.rect.left < 300:
                sn.head.pos[0] = sn.head.pos[0] + 1
            else:
                sn.head.pos[0] = sn.head.pos[0] - 1

        if keys[pygame.K_p]:
            sn.addSegment()

    def Run(self) -> None:
        while self.running:
            self.HandleProc()
            self.Update()
            self.Render()
            self.clock.tick(60) 
        pygame.quit()

win = Windows(800, 600)

sn = snake()
apple = segment(10, 10, (255, 61, 0), (random.randint(0, 800), random.randint(0, 600)))

win.Run()