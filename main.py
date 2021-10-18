import pygame
import math
import casilla

# Constantes
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --------- Clases --------- 
# Clase Nodo, será cada una casilla de las que haya en la matriz
class Node:
  def __init__(self, row, col, ancho):
      self.row = row
      self.col = col
      self.color = WHITE
      self.neighbors = []
      self.width = ancho

# --------- Funciones ---------

# Creara el tablero donde depositemos los nodos, será una lista de 2x2
# donde dentro estarán los nodos
def create_grid():
  pass

# Dibuja el tablero, con líneas en los bordes de los cuadrados 
def draw_grid():
  pass

# Dibuja los nodos con sus características
def draw_nodes():
  pass

# Este será el main
def main(): 
  print("Elige el valor de M: ")
  M = int(input())
  print("Elige el valor de N: ")
  N = int(input())

  screen = pygame.display.set_mode((M, N))
  pygame.display.set_caption("P1 Inteligencia Artificial por Juan Marrero")

if __name__ == '__main__':
  main()

