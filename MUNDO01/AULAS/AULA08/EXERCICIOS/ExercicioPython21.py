# Escreva um programa em Python que abra e reproduza um arquivo .mp3

# É necessário instalar a bibilioteca pygame através do comando pip install pygame
import pygame

# Estarta o módulo pygame
pygame.init()

# Só tocou a música depois de adicionar estas 2 linhas
# Elas criam uma janela na tela como se fosse um player
w_geometry = (100, 100)
pygame.display.set_mode(w_geometry)


pygame.mixer_music.load('LostInSpace.mp3')
pygame.mixer.music.play()
x = input('Digite algo para parar...')
