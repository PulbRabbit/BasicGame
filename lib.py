import pygame
from math import sin, cos, atan
from random import randint

class Color:
    def __init__(self):
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.dark_yellow = (150, 150, 150)
        self.white = (255, 255, 255)
        self.light_grey = (200, 200, 200)
        self.grey = (100, 100, 100)
        self.dark_grey = (50, 50, 50)


color = Color()


class Pawn:
    def __init__(self, screen, x, y, direction, health, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = direction
        self.health = health
        self.color = color.white
        self.speed = speed

    def _get_point(self, offset, size):
        x = int(cos(self.angle + offset) * size + self.x)
        y = int(sin(self.angle + offset) * size + self.y)

        return x, y

    def turn(self, angle):
        self.angle += angle

    def move(self, factor):
        self.x += cos(self.angle) * self.speed * factor
        self.y += sin(self.angle) * self.speed * factor

    def draw(self):
        size = 10

        point0 = self._get_point(0, size)
        point1 = self._get_point(10 / 6, size)
        point2 = self._get_point(-10 / 6, size)

        point_list = [point0, point1, point2]
        pygame.draw.polygon(self.screen, self.color, point_list, 0)

    def alive(self):
        return self.health > 0.0

    def shoot(self, spray_f):
        spray = randint(-100, 100) / spray_f
        projectile = Projectile(self.screen, self.x, self.y, self.angle + spray, 100, 20)
        return projectile

    def is_hit(self, projectile_list, zone, damage):
        index = 0
        for projectile in projectile_list:
            if self.x - zone < projectile.x < self.x + zone and\
             self.y - zone < projectile.y < self.y + zone:
                self.health -= damage
                return index

            index += 1


class Player(Pawn):
    def __init__(self, screen, x, y, direction, health, speed):
        super().__init__(screen, x, y, direction, health, speed)
        self.color = color.blue

    def is_hit(self, enemy_list):
        index = 0
        for projectile in enemy_list:
            if self.x - 10 < projectile.x < self.x + 10 and \
                    self.y - 10 < projectile.y < self.y + 10:
                self.health -= 1
                return index

            index += 1


class Enemy(Pawn):
    def __init__(self, screen, x, y, direction, health, speed):
        super().__init__(screen, x, y, direction, health, speed)
        self.color = color.red


class Projectile(Pawn):
    def __init__(self, screen, x, y, direction, health, speed):
        super().__init__(screen, x, y, direction, health, speed)

    def draw(self):
        size = 2

        point0 = self._get_point(0, size)
        point1 = self._get_point(10 / 6, size)
        point2 = self._get_point(-10 / 6, size)

        point_list = [point0, point1, point2]
        pygame.draw.polygon(self.screen, self.color, point_list, 0)

class Missile(Pawn):
    def __init__(self, screen, x, y, direction, health, speed):
        super().__init__(screen, x, y, direction, health, speed)

    def draw(self):
        trail = 6
        for i in range(0, trail):
            pygame.draw.circle(self.screen, (200 - i * 20, 200 - i * 20, 0), self._get_point(0, -i * 20), 8 - i, 0)


class Clock:
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.sec_ticked = 0
        self.sys_time = 0
        self.dsec = 0
        self.sec = 0
        self.halfsec_ticked = 0

    def run(self):
        self.clock.tick(self.fps)
        self.sys_time += self.clock.get_time()
        if self.sys_time > 100:
            self.sys_time -= 100
            self.dsec += 1
        if self.dsec > 10:
            self.dsec -= 10
            self.sec += 1
            self.sec_ticked = True
        else:
            self.sec_ticked = False
        self.halfsec_ticked = self.dsec % 5 == 0


class Text:
    def __init__(self, screen, x, y, text, size, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.SysFont('Arial', size)
        self.rendered = self.font.render(self.text, True, self.color)

    def update(self, text):
        self.text = text

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.rendered = self.font.render(self.text, True, self.color)
        self.screen.blit(self.rendered, (self.x, self.y + int(self.size / 2)))


def get_dir(me, target):
    dx = target.x - me.x
    dy = target.y - me.y
    if dx > 0:
        return atan(dy/dx)
    if dx < 0:
        return atan(dy/dx) - 3.14
    if dx == 0:
        return 0


# end of code
