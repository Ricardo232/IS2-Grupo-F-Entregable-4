import pygame as pg
import random
import math
from Intro import *
from os import path
from settings import *
from terrain import *
from hud import *
from playerstate import Player
from mobstate import Mob
from tilemap import *

class Game:
    def __init__(self):
        #Initialize game window
        pg.init()
        pg.mixer.init()
        snd_dir = os.path.join(game_folder, "snd")

        #background music
        pg.mixer.music.load(path.join(snd_dir, 'Knight_Artorias.ogx'))
        #pg.mixer.music.set_pos(5.0)

        #volumen
        pg.mixer.music.set_volume(1.0)

        #reproducir musica con loop
        pg.mixer.music.play(loops=-1)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.running = True

    def load_data(self):
        self.map = Map(path.join(game_folder, "map.txt"))

    def new(self):
        #Start a new game
        self.all_sprites = pg.sprite.Group()
        self.mob_sprites = pg.sprite.Group()
        self.dead_sprites = pg.sprite.Group()
        self.terrain_sprites = pg.sprite.Group()
        self.hud_sprites = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "M":
                    Mob(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)

        self.camera = Camera(self.map.width, self.map.height, self.screen)
        self.terrain = Terrain()
        self.terrain_sprites.add(self.terrain)
        self.hud = HUD()
        self.hud_sprites.add(self.hud)
        Intro(self)
        self.run()

    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #Game loop - Update
        self.all_sprites.update()
        self.dead_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_map(self, row, col):
        for j in range(row, row + math.floor(WIDTH/TILESIZE)):
            for i in range(col, col + math.floor(HEIGHT/TILESIZE)):
                if self.map.data[j][i] == "M":
                    Mob(self, i, j)

    def events(self):
        #Game loop - Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def draw(self):
        #Game loop - Draw
        self.screen.fill(WHITE)
        self.draw_grid()
        for sprite in self.terrain_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.dead_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
                #print(self.screen.get_rect().x - self.camera.pos.x) #inside screen
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.hud_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #Game splash/start screen
        pass

    def show_go_screen(self):
        #Game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
quit()
