import pygame, random, sys, os

pygame.init()
W, H = 640, 360
FPS = 60
ROUND = 30

win   = pygame.display.set_mode((W, H))
font  = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

bg     = pygame.Surface((W, H));    bg.fill((30, 40, 70))
player = pygame.Surface((40, 40));  player.fill((0, 170, 255))
coin_s = pygame.Surface((25, 25), pygame.SRCALPHA)
pygame.draw.circle(coin_s, (255, 215, 0), (12, 12), 12)

player_rect = player.get_rect(midbottom=(W // 2, H - 10))
rnd = lambda: (random.randint(40, W-40), random.randint(40, H-80))

coins = []
for _ in range(3):
    r = coin_s.get_rect(center=rnd())
    vx, vy = random.choice([-2, 2]), random.choice([-2, 2])
    coins.append([r, vx, vy])

best_path = "record.txt"
best = int(open(best_path).read()) if os.path.exists(best_path) else 0

start_ms = pygame.time.get_ticks()
spd = 4
run = True
while run:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()

    k = pygame.key.get_pressed()
    if k[pygame.K_LEFT]:  player_rect.x -= spd
    if k[pygame.K_RIGHT]: player_rect.x += spd
    if k[pygame.K_UP]:    player_rect.y -= spd
    if k[pygame.K_DOWN]:  player_rect.y += spd
    player_rect.clamp_ip(win.get_rect())

    for c in coins:
        r, vx, vy = c
        r.x += vx; r.y += vy
        if r.left <= 0 or r.right >= W: c[1] *= -1
        if r.top <= 0 or r.bottom >= H: c[2] *= -1
        if player_rect.colliderect(r):
            r.center = rnd()

    t_left = max(0, ROUND - (pygame.time.get_ticks() - start_ms)//1000)
    if t_left == 0: run = False

    win.blit(bg, (0,0))
    for r,_,_ in coins: win.blit(coin_s, r)
    win.blit(player, player_rect)
    win.blit(font.render(f"Time: {t_left}", True, (255,255,255)), (10,10))
    win.blit(font.render(f"Best: {best}", True, (180,180,180)), (10,40))
    pygame.display.update()

if ROUND > best:
    with open(best_path,"w") as f: f.write(str(ROUND))

win.fill((0,0,0))
msg = font.render("Survived! Press any key", True, (0,255,0))
win.blit(msg, msg.get_rect(center=win.get_rect().center))
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type in (pygame.KEYDOWN, pygame.QUIT):
            pygame.quit(); sys.exit()
