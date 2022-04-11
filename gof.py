from tkinter import *
from threading import *
import math as m
import time as t

size = int(input("matrix size ? >"))

def initialize():
   global size
   global matrix
   global flag
   global canvas
   global emptyMatrix
   global main
   matrix = []
   flag = False
   for i in range(size):
      matrix.append([])
      for j in range(size):
         matrix[i].append([0, "white"])
   
   emptyMatrix = []
   for i in range(size):
      emptyMatrix.append([])
      for j in range(size):
         emptyMatrix[i].append([0, "white"])
         
   try:
      main.destroy()
   except:
      pass
         
   main = Tk()
   main.geometry("800x800")
   main.resizable(width=False, height=False)
   main.title("game of life 1v1")
   canvas = Canvas(main, width=800, height=800, background="black")
   canvas.delete("all")
   for i in range(size+1):
      canvas.create_line(i*800/size, 0, i*800/size, 800, fill="#222222")
      canvas.create_line(0, i*800/size, 800, i*800/size, fill="#222222")
   canvas.place(x=0, y=0)
   main.bind('<Button-1>', button1pressed)
   main.bind('<Key>', keyPressed)
   main.mainloop()

def iterate():
   global matrix
   secondMatrix = []
   for i in range(size):
      secondMatrix.append([])
      for j in range(size):
         secondMatrix[i].append([0, "white"])
   for i in range(size):
      for j in range(size):
         neighborCells = 0
         neighborCells +=  matrix[ (i-1)%size ][ (j-1)%size ][0] + matrix[ i          ][ (j-1)%size ][0] + matrix[ (i+1)%size ][ (j-1)%size ][0] + matrix[ (i-1)%size ][ j          ][0] + matrix[ (i+1)%size ][ j          ][0] + matrix[ (i-1)%size ][ (j+1)%size ][0] + matrix[ i          ][ (j+1)%size ][0] + matrix[ (i+1)%size ][ (j+1)%size ][0]
         if neighborCells == 2 or neighborCells == 3:
            if neighborCells == 3:
               secondMatrix[i][j][0] = 1
            else:
               secondMatrix[i][j][0] = matrix[i][j][0]
         else:
            secondMatrix[i][j][0] = 0
   
   matrix = secondMatrix
   drawGame(matrix)


def drawGame(matrix):
   global canvas
   canvas.delete("squares")
   for i in range(size):
      for j in range(size):
         if matrix[i][j][0] == 1:
            canvas.create_rectangle(i*800/size, j*800/size, (i+1)*800/size, (j+1)*800/size, fill=matrix[i][j][1], tag="squares")

def button1pressed(event):
   global matrix
   x = m.trunc(event.x*size/800)
   y = m.trunc(event.y*size/800)
   if matrix[x][y][0] == 0:
      matrix[x][y][0] = 1
   else:
      matrix[x][y][0] = 0
   drawGame(matrix)

def keyPressed(event):
   global flag
   if event.keycode == 32:
      iterate()
   elif event.keycode == 13:
      if flag == False:
         flag = True
         playGofThreads.append(Thread(target=iterateGof))
         playGofThreads[len(playGofThreads)-1].start()
      else:
         flag = False
   elif event.keycode == 8:
      initialize()
      drawGame(matrix)

def iterateGof():
   global flag
   while flag == True:
      t.sleep(0.1)
      if matrix == emptyMatrix:
         flag = False
      iterate()


playGofThreads = []

initialize()


