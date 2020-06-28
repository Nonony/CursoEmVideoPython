# Escreva um programa em Python que abra e reproduza um arquivo .mp3
# É necessário instalar a bibilioteca pygame através do comando pip install pygame

import pygame

"""# Para que a música fosse tocadas, eu precisei inicializar primeiro o módulo pygame.mixer 
e em seguida inicializar o pygame"""
pygame.mixer.init()
pygame.init()

# music = input('E:/Cursos/Python/Curso_em_video_Python/CursoEmVideoPython/MUNDO01/AULAS/AULA08/EXERCICIOS/LS.mp3')
pygame.mixer.music.load('LS.mp3')
pygame.mixer.music.play()
pygame.event.wait()
