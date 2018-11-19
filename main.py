from lib import *


if not pygame.font:
    print('error pygame')
if not pygame.mixer:
    print('error pygame!')


def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Basic Game")
    pygame.mouse.set_visible(0)
    pygame.key.set_repeat(1, 30)

    clock = Clock(50)

    score_board = Text(screen, 20, 20, "Score - 0", 20, (255, 255, 100))
    health_board = Text(screen, 220, 20, "Score - 0", 20, (100, 255, 100))
    gun1_txt = Text(screen, 10, 560, "[1] Pistol", 20, color.light_grey)
    gun2_txt = Text(screen, 120, 560, "[2] Assault", 20, color.grey)
    gun3_txt = Text(screen, 230, 560, "[3] Shotgun", 20, color.grey)
    gun4_txt = Text(screen, 340, 560, "[4] MiniG", 20, color.grey)
    gun5_txt = Text(screen, 450, 560, "[5] Launchr", 20, color.grey)
    gun6_txt = Text(screen, 560, 560, "[6] 8Ball", 20, color.grey)
    gun0_txt = Text(screen, 680, 560, "[0] SuperG", 20, color.grey)

    player = Player(screen, 300, 300, 0, 100, 2)
    projectile_list = []
    missile_list = []
    enemy_list = []

    t_time = 0
    t_toggle = 0
    t_toggle_old = 0
    burst = 0
    trigger_downed = False
    trigger_downed_old = False
    gun = 1

    score = 0
    enemy_speed = 0.2

    running = True
    while running:
        if len(enemy_list) <= int(score/2) + 1 and len(enemy_list) <= 100 :
            x = randint(0, 400)
            y = randint(0, 400)
            if x > 200:
                x = 400 + x
            if y > 200:
                y = 200 + x
            enemy_list.append(Enemy(screen, x, y, 0, 100, enemy_speed))
            enemy_speed += 0.002

        clock.run()
        # t_time, t_toggle = sec_tick(t_time, clock.get_time(), t_toggle)
        if clock.sec_ticked:
            burst = 0
        screen.fill((60, 60, 60))
        pygame.draw.rect(screen, (255, 255, 0), ((200, 200), (400, 200)), 2)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player.turn(0.1)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player.turn(-0.1)
        if pygame.key.get_pressed()[pygame.K_UP]:
            player.move(1)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            player.move(-1)
        if pygame.key.get_pressed()[pygame.K_1]:
            gun = 1
            gun1_txt.color = color.light_grey
            gun2_txt.color = color.grey
            gun3_txt.color = color.grey
            gun4_txt.color = color.grey
            gun5_txt.color = color.grey
            gun6_txt.color = color.grey
            gun0_txt.color = color.grey

        if pygame.key.get_pressed()[pygame.K_2]:
            gun = 2
            gun1_txt.color = color.grey
            gun2_txt.color = color.light_grey
            gun3_txt.color = color.grey
            gun4_txt.color = color.grey
            gun5_txt.color = color.grey
            gun6_txt.color = color.grey
            gun0_txt.color = color.grey

        if pygame.key.get_pressed()[pygame.K_3]:
            gun = 3
            gun1_txt.color = color.grey
            gun2_txt.color = color.grey
            gun3_txt.color = color.light_grey
            gun4_txt.color = color.grey
            gun5_txt.color = color.grey
            gun6_txt.color = color.grey
            gun0_txt.color = color.grey

        if pygame.key.get_pressed()[pygame.K_4]:
            gun = 4
            gun1_txt.color = color.grey
            gun2_txt.color = color.grey
            gun3_txt.color = color.grey
            gun4_txt.color = color.light_grey
            gun5_txt.color = color.grey
            gun6_txt.color = color.grey
            gun0_txt.color = color.grey

        if pygame.key.get_pressed()[pygame.K_5]:
            gun = 5
            gun1_txt.color = color.grey
            gun2_txt.color = color.grey
            gun3_txt.color = color.grey
            gun4_txt.color = color.grey
            gun5_txt.color = color.light_grey
            gun6_txt.color = color.grey
            gun0_txt.color = color.grey

        if pygame.key.get_pressed()[pygame.K_6]:
            gun = 6
            gun1_txt.color = color.grey
            gun2_txt.color = color.grey
            gun3_txt.color = color.grey
            gun4_txt.color = color.grey
            gun5_txt.color = color.grey
            gun6_txt.color = color.light_grey
            gun0_txt.color = color.grey

        if pygame.key.get_pressed()[pygame.K_0]:
            gun = 0
            gun1_txt.color = color.grey
            gun2_txt.color = color.grey
            gun3_txt.color = color.grey
            gun4_txt.color = color.grey
            gun5_txt.color = color.grey
            gun0_txt.color = color.light_grey

        if pygame.key.get_pressed()[pygame.K_RCTRL]:
            trigger_downed = True
            if trigger_downed and not trigger_downed_old:
                burst = 0
            if gun == 1:
                if burst < 1:
                    burst += 1
                    projectile_list.append(player.shoot(2000))
            elif gun == 2:
                if burst < 5:
                    burst += 1
                    projectile_list.append(player.shoot(1000))
            elif gun == 3:
                if burst < 1:
                    burst += 1
                    for i in range(0, 10):
                        projectile_list.append(player.shoot(500))
            elif gun == 4:
                if burst < 100:
                    burst += 1
                    projectile_list.append(player.shoot(500))
            elif gun == 5:
                if burst < 1:
                    burst += 1
                    missile_list.append(Missile(screen, player.x, player.y, player.angle, player.health, 7))
            elif gun == 6:
                if burst < 8:
                    burst += 1
                    missile_list.append(Missile(screen, player.x, player.y, player.angle, player.health, 7))
            elif gun == 0:
                if burst < 10:
                    burst += 1
                    for i in range(0, 20):
                        projectile_list.append(player.shoot(200))
        else:
            trigger_downed = False
        trigger_downed_old = trigger_downed

        index = 0
        for enemy in enemy_list:
            enemy.angle = get_dir(enemy, player)
            enemy.move(1)
            pro_index = enemy.is_hit(projectile_list, 10, 50)
            if type(pro_index) == int:
                del projectile_list[pro_index]
            missile_index = enemy.is_hit(missile_list, 50, 120)
            if type(missile_index) == int:
                for i in range(0, 60):
                    projectile_list.append(Projectile(screen, missile.x, missile.y, missile.angle + 0.1 * i, 10, 25))
                del missile_list[missile_index]

            enemy.draw()
            if not enemy.alive():
                del enemy_list[index]
                score += 1
                score_board.update("Score - " + str(score))
            index += 1

        player.is_hit(enemy_list)
        if not player.alive():
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        player.draw()

        index = 0
        for projectile in projectile_list:
            projectile.move(1)
            projectile.health -= 2
            projectile.draw()
            if not projectile.alive():
                del projectile_list[index]
            index += 1

        index = 0
        for missile in missile_list:
            missile.move(1)
            missile.health -= 2
            missile.draw()
            if not missile.alive():
                for i in range(0, 60):
                    projectile_list.append(Projectile(screen, missile.x, missile.y, missile.angle + 0.1 * i, 20, 10))
                del missile_list[index]
            index += 1

        # draw GUI on screen
        score_board.draw()
        health_board.update("Health - " + str(player.health))
        if player.health < 50:
            health_board.color = (255, 0, 0)
        health_board.draw()
        gun0_txt.draw()
        gun1_txt.draw()
        gun2_txt.draw()
        gun3_txt.draw()
        gun4_txt.draw()
        gun5_txt.draw()
        gun6_txt.draw()

        pygame.display.flip()
        t_toggle_old = t_toggle


if __name__ == '__main__':
    main()

# end of code
