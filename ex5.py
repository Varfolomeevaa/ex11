import pygame
from random import randint
from solution_5 import Molecular

colors = ['red', 'green', 'blue', 'grey', 'purple', 'pink', 'black', 'blue', 'green', 'orange']
for i in range(15):
    new_mol = Molecular(randint(0, 100), randint(0, 100), randint(5, 10), randint(5, 10),
                        colors[randint(0, 9)], randint(10, 25))
    Molecular.all_mol.append(new_mol)

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    for i in range(len(Molecular.all_mol)):
        for j in range(i + 1, len(Molecular.all_mol)):

            diff_x = Molecular.all_mol[i].x - Molecular.all_mol[j].x
            diff_y = Molecular.all_mol[i].y - Molecular.all_mol[j].y

            r_sum = Molecular.all_mol[i].radius + Molecular.all_mol[j].radius
            between = (diff_x ** 2 + diff_y ** 2) ** 0.5

            if between <= r_sum:
                Molecular.all_mol[i].vx, Molecular.all_mol[j].vx = Molecular.all_mol[j].vx, Molecular.all_mol[i].vx
                Molecular.all_mol[i].vy, Molecular.all_mol[j].vy = Molecular.all_mol[j].vy, Molecular.all_mol[i].vy

                cross = r_sum - between + 2
                Molecular.all_mol[i].x += cross + Molecular.all_mol[i].vx
                Molecular.all_mol[j].x -= cross + Molecular.all_mol[j].vx
                Molecular.all_mol[i].y += cross + Molecular.all_mol[i].vy
                Molecular.all_mol[j].y -= cross + Molecular.all_mol[j].vy

    for i in range(len(Molecular.all_mol)):
        Molecular.all_mol[i].going()

    screen.fill((255, 255, 255))
    for i in range(len(Molecular.all_mol)):
        pygame.draw.circle(screen, Molecular.all_mol[i].color,
                           (int(Molecular.all_mol[i].x), int(Molecular.all_mol[i].y)),
                           Molecular.all_mol[i].radius)

    pygame.display.flip()
    clock.tick(50)
pygame.quit()
