import pygame as p
import os
import time
import neat
import random
p.font.init()

STAT_FONT = p.font.SysFont("comicsans", 50)

GEN = 0
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

BIRD_IMGS = [p.transform.scale2x(p.image.load("imgs/bird1.png")), p.transform.scale2x(p.image.load("imgs/bird2.png")),
             p.transform.scale2x(p.image.load("imgs/bird3.png"))]
BASE_IMG = p.transform.scale(p.image.load("imgs/base.png"), (SCREEN_WIDTH, 100))
BG_IMG = p.transform.scale(p.image.load("imgs/bg.png"),(SCREEN_WIDTH,SCREEN_HEIGHT))
PIPE_IMG = p.transform.scale2x(p.image.load("imgs/pipe.png"))


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.tilt = 0
        self.vel = 0
        self.height = self.y
        self.img = self.IMGS[0]
        self.img_count = 0

    def jump(self):
        self.vel = -8
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = (self.vel * self.tick_count) + 1.5* (self.tick_count ** 2)

        if d > 8:
            d = 8
        if d < 0:
            d -= 8

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):

        self.img_count += 1

        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # when the bird is going down no need to flap the wings
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # tilt the bird
        rotated_image = p.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        """
        gets the mask for the current image of the bird
        :return: None
        """
        return p.mask.from_surface(self.img)


class Pipe:
    GAP = 300
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_BOTTOM = PIPE_IMG
        self.PIPE_TOP = p.transform.flip(PIPE_IMG, False, True)
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(30, 500)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        top_mask = p.mask.from_surface(self.PIPE_TOP)
        bottom_mask = p.mask.from_surface(self.PIPE_BOTTOM)

        t_point = bird_mask.overlap(top_mask, top_offset)
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)

        if t_point or b_point:
            return True
        return False

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def draw_window(win, birds, pipes, base, score, GEN):
    win.blit(BG_IMG, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score " + str(score), 1, (0,0,0))
    win.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Gens " + str(GEN), 1, (0, 0, 0))
    win.blit(text, (10, 10))

    text = STAT_FONT.render("Alive " + str(len(birds)), 1, (0, 0, 0))
    win.blit(text, (10, 80))


    base.draw(win)
    for bird in birds:
        bird.draw(win)
    p.display.update()

def main(genomes, config):
    global GEN
    GEN += 1
    # start by creating lists holding the genome itself, the
    # neural network associated with the genome and the
    # bird object that uses that network to play
    nets = []
    birds = []
    ge = []
    for _, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        ge.append(genome)


    base = Base(730)
    pipes = [Pipe(SCREEN_WIDTH)]
    score = 0

    clock = p.time.Clock()
    win = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    while run and len(birds) > 0:
        clock.tick(20)
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
                p.quit()
                quit()
                break

        rem = []

        pipe_idx = 0
        if len(birds) > 0:
            if len(pipes) > 1:
                if birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                    pipe_idx = 1
        else:
            run = False
            break


        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            # send bird location, top pipe location and bottom pipe location and determine from network whether to jump or not
            output = nets[birds.index(bird)].activate(
                (bird.y, abs(bird.y - pipes[pipe_idx].height), abs(bird.y - pipes[pipe_idx].bottom), abs(pipes[pipe_idx].x - bird.x)))

            if output[0] > 0.5:  # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                bird.jump()

        base.move()



        addPipe = False
        for pipe in pipes:
            pipe.move()
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)
                if not pipe.passed and pipe.x + pipe.PIPE_TOP.get_width() < bird.x:
                    pipe.passed = True
                    addPipe = True
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

        if addPipe:
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(SCREEN_WIDTH))

        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_width() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        draw_window(win, birds, pipes, base, score, GEN)

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 50 generations.
    winner = p.run(main, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat_config.txt')
    run(config_path)
