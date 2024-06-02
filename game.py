
import pygame
import pytmx
import pyscroll

from player import Player


class Game:
    player: Player

    def __init__(self):
        # créer la fenêtre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Aventure")

        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # génerer un joueur

        self.player = Player()


        # dessiner le groupe de claques

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

        # boucle du jeu
    def run(self):
                running = True

                while running:

                    self.group.draw(self.screen)
                    pygame.display.flip()

                #Si le joueur clique sur la croix pour fermer le jeu la fenêtre se ferme
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                            pygame.quit()