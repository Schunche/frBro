import pygame
pygame.init()

from src.code.server import \
    Server

server: Server = Server()
server.run()
