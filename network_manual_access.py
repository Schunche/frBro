import pygame
pygame.init()

from src.code.network import \
    Network

network: Network = Network()
network.send({"type": "test"})
network.close()
