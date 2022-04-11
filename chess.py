#coding=utf-8
from tkinter import *
import math


mainWindow = Tk()
mainWindow.title("chess game")
mainWindow.minsize(800, 800)


board = []
moving_possibilities = []
current_player = 'black'
opposit_player = 'white'

def setup():
   global board
   canvas.delete("all")
   board = []
   for i in range(8):
      board.append([])
      for j in range(8):
         board[i].append(['empty', 'empty'])
   for i in range(4):
      for j in range(4):
         canvas.create_rectangle(200*i, 200*j, 100+200*i, 100+200*j, fill="grey")
         canvas.create_rectangle(100+200*i, 100+200*j, 200+200*i, 200+200*j, fill="grey")
   for i in range(8):   
      board[1][i] = ['pawn', 'black']
      board[6][i] = ['pawn', 'white']
   board[0][0] = ['rook', 'black']
   board[0][7] = ['rook', 'black']
   board[0][1] = ['knight', 'black']
   board[0][6] = ['knight', 'black']
   board[0][2] = ['bishop', 'black']
   board[0][5] = ['bishop', 'black']
   board[0][3] = ['king', 'black']
   board[0][4] = ['queen', 'black']
   board[7][0] = ['rook', 'white']
   board[7][7] = ['rook', 'white']
   board[7][1] = ['knight', 'white']
   board[7][6] = ['knight', 'white']
   board[7][2] = ['bishop', 'white']
   board[7][5] = ['bishop', 'white']
   board[7][3] = ['king', 'white']
   board[7][4] = ['queen', 'white']



def display_pieces():
   canvas.delete('piece')
   for i in range(8):
      for j in range(8):
         current_piece = board[i][j][0]
         if current_piece != 'empty':
            canvas.create_text(100*i+50, 100*j+50, text=current_piece, fill=board[i][j][1], tag='piece')



def mouse_motion(event):
   global x_mouse, y_mouse
   x_mouse = math.trunc(event.x/100)
   y_mouse = math.trunc(event.y/100)


def left_click_pressed(event):
   print("clicked in ", x_mouse+1, y_mouse+1, "(", x_mouse, y_mouse, ")")
   check_mvmt = False
   x_y_checking = [x_mouse, y_mouse]
   if moving_possibilities != []:
      for i in range(len(moving_possibilities)):
         if x_y_checking == moving_possibilities[i]:
            check_mvmt = True
            moved_location = moving_possibilities[i]
   if check_mvmt == True:
      move_piece(moved_location, current_piece_location)
   elif board[x_mouse][y_mouse][0] != 'empty':
      all_mvmt(board[x_mouse][y_mouse], x_mouse, y_mouse)
   else:
      canvas.delete('selection')



def move_piece(finish, start):
   global board
   global opposit_player
   global current_player
   board[finish[0]][finish[1]] = board[start[0]][start[1]]
   board[start[0]][start[1]] = ['empty', 'empty']
   canvas.delete('selection')
   moving_possibilities = []
   current_player = opposit_player
   if current_player == 'white':
      opposit_player = 'black'
   elif current_player == 'black':
      opposit_player = 'white'
   display_pieces()


def all_mvmt(piece, x, y):            #=================================== check all piece movements
   global moving_possibilities
   global current_piece_location
   current_piece_location = [x, y]
   moving_possibilities = []
   canvas.delete('selection')
   if current_player == piece[1]:
      canvas.create_rectangle(x*100+20, y*100+20, x*100+80, y*100+80, tag='selection', fill="blue", width=0)
      canvas.create_text(x*100+50, y*100+50, text=piece[0], tag='selection')
      if piece[0] == 'pawn':          #=================================== pawn
         if current_player == 'black':
            if x == 1:
               if board[x+1][y][0] == 'empty':
                  moving_possibilities.append([x+1, y])
               if board[x+2][y][0] == 'empty':
                  moving_possibilities.append([x+2, y])
            elif x < 7:
               if board[x+1][y][0] == 'empty':
                  moving_possibilities.append([x+1, y])
            if y+1 < 8 and board[x+1][y+1][1] == opposit_player:
               moving_possibilities.append([x+1, y+1])
            if board[x+1][y-1][1] == opposit_player:
               moving_possibilities.append([x+1, y-1])
         elif current_player == 'white':
            if x == 6:
               if board[x-1][y][0] == 'empty':
                  moving_possibilities.append([x-1, y])
               if board[x-2][y][0] == 'empty':
                  moving_possibilities.append([x-2, y])
            elif x > 0:
               if board[x-1][y][0] == 'empty':
                  moving_possibilities.append([x-1, y])
            if y+1 < 8 and board[x-1][y+1][1] == opposit_player:
               moving_possibilities.append([x-1, y+1])
            if board[x-1][y-1][1] == opposit_player:
               moving_possibilities.append([x-1, y-1])
      elif piece[0] == 'rook':         #================================== rook
         up = True
         down = True
         left = True
         right = True
         i = 1
         while (up == True or down == True or right == True or left == True) and i < 8:
            if up == True:
               if x >= 0 and x < 8 and y-i >= 0 and y-i < 8:
                  if board[x][y-i][1] != current_player:
                     moving_possibilities.append([x, y-i])
                     if board[x][y-i][1] == opposit_player:
                        up = False
                  else:
                     up = False
               else:
                  up = False
            if down == True:
               if x >= 0 and x < 8 and y+i >= 0 and y+i < 8:
                  if board[x][y+i][1] != current_player:
                     moving_possibilities.append([x, y+i])
                     if board[x][y+i][1] == opposit_player:
                        down = False
                  else:
                     down = False
               else:
                  down = False
            if right == True:
               if x+i >= 0 and x+i < 8 and y >= 0 and y < 8:
                  if board[x+i][y][1] != current_player:
                     moving_possibilities.append([x+i, y])
                     if board[x+i][y][1] == opposit_player:
                        right = False
                  else:
                     right = False
               else:
                  right = False
            if left == True:
               if x-i >= 0 and x-i < 8 and y >= 0 and y < 8:
                  if board[x-i][y][1] != current_player:
                     moving_possibilities.append([x-i, y])
                     if board[x-i][y][1] == opposit_player:
                        left = False
                  else:
                     left = False
               else:
                  left = False
            i = i+1

      elif piece[0] == 'knight':       #================================== knight // a rendre plus propre (savoir si on est su le jeu)
         print(x, y)
         if x+1 < 8 and board[x+1][y-2][1] != current_player:
            moving_possibilities.append([x+1, y-2])
         if x+2 < 8 and board[x+2][y-1][1] != current_player:
            moving_possibilities.append([x+2, y-1])
         if x+2 < 8 and y+1 < 8 and board[x+2][y+1][1] != current_player:
            moving_possibilities.append([x+2, y+1])
         if x+1 < 8 and y+2 < 8 and board[x+1][y+2][1] != current_player:
            moving_possibilities.append([x+1, y+2])
         if y+2 < 8 and board[x-1][y+2][1] != current_player:
            moving_possibilities.append([x-1, y+2])
         if y+1 < 8 and board[x-2][y+1][1] != current_player:
            moving_possibilities.append([x-2, y+1])
         if board[x-2][y-1][1] != current_player:
            moving_possibilities.append([x-2, y-1])
         if board[x-1][y-2][1] != current_player:
            moving_possibilities.append([x-1, y-2])
      elif piece[0] == 'bishop':       #================================== bishop
         upleft = True
         upright = True
         downleft = True
         downright = True
         i = 1
         while (upleft == True or downleft == True or upright == True or downright == True) and i < 8:
            if upleft == True:
               if x-i >= 0 and x-i < 8 and y-i >= 0 and y-i < 8:
                  if board[x-i][y-i][1] != current_player:
                     moving_possibilities.append([x-i, y-i])
                     if board[x-i][y-i][1] == opposit_player:
                        upleft = False
                  else:
                     upleft = False
               else:
                  upleft = False
            if downleft == True:
               if x-i >= 0 and x-i < 8 and y+i >= 0 and y+i < 8:
                  if board[x-i][y+i][1] != current_player:
                     moving_possibilities.append([x-i, y+i])
                     if board[x-i][y+i][1] == opposit_player:
                        downleft = False
                  else:
                     downleft = False
               else:
                  downleft = False
            if upright == True:
               if x+i >= 0 and x+i < 8 and y-i >= 0 and y-i < 8:
                  if board[x+i][y-i][1] != current_player:
                     moving_possibilities.append([x+i, y-i])
                     if board[x+i][y-i][1] == opposit_player:
                        upright = False
                  else:
                     upright = False
               else:
                  upright = False
            if downright == True:
               if x+i >= 0 and x+i < 8 and y+i >= 0 and y+i < 8:
                  if board[x+i][y+i][1] != current_player:
                     moving_possibilities.append([x+i, y+i])
                     if board[x+i][y+i][1] == opposit_player:
                        downright = False
                  else:
                     downright = False
               else:
                  downright = False
            i = i+1
      elif piece[0] == 'queen':        #================================== queen
         up = True
         down = True
         left = True
         right = True
         upleft = True
         upright = True
         downleft = True
         downright = True
         i = 1
         while (up == True or down == True or right == True or left == True or upleft == True or downleft == True or upright == True or downright == True) and i < 8:
            if up == True:
               if x >= 0 and x < 8 and y-i >= 0 and y-i < 8:
                  if board[x][y-i][1] != current_player:
                     moving_possibilities.append([x, y-i])
                     if board[x][y-i][1] == opposit_player:
                        up = False
                  else:
                     up = False
               else:
                  up = False
            if down == True:
               if x >= 0 and x < 8 and y+i >= 0 and y+i < 8:
                  if board[x][y+i][1] != current_player:
                     moving_possibilities.append([x, y+i])
                     if board[x][y+i][1] == opposit_player:
                        down = False
                  else:
                     down = False
               else:
                  down = False
            if right == True:
               if x+i >= 0 and x+i < 8 and y >= 0 and y < 8:
                  if board[x+i][y][1] != current_player:
                     moving_possibilities.append([x+i, y])
                     if board[x+i][y][1] == opposit_player:
                        right = False
                  else:
                     right = False
               else:
                  right = False
            if left == True:
               if x-i >= 0 and x-i < 8 and y >= 0 and y < 8:
                  if board[x-i][y][1] != current_player:
                     moving_possibilities.append([x-i, y])
                     if board[x-i][y][1] == opposit_player:
                        left = False
                  else:
                     left = False
               else:
                  left = False
            if upleft == True:
               if x-i >= 0 and x-i < 8 and y-i >= 0 and y-i < 8:
                  if board[x-i][y-i][1] != current_player:
                     moving_possibilities.append([x-i, y-i])
                     if board[x-i][y-i][1] == opposit_player:
                        upleft = False
                  else:
                     upleft = False
               else:
                  upleft = False
            if downleft == True:
               if x-i >= 0 and x-i < 8 and y+i >= 0 and y+i < 8:
                  if board[x-i][y+i][1] != current_player:
                     moving_possibilities.append([x-i, y+i])
                     if board[x-i][y+i][1] == opposit_player:
                        downleft = False
                  else:
                     downleft = False
               else:
                  downleft = False
            if upright == True:
               if x+i >= 0 and x+i < 8 and y-i >= 0 and y-i < 8:
                  if board[x+i][y-i][1] != current_player:
                     moving_possibilities.append([x+i, y-i])
                     if board[x+i][y-i][1] == opposit_player:
                        upright = False
                  else:
                     upright = False
               else:
                  upright = False
            if downright == True:
               if x+i >= 0 and x+i < 8 and y+i >= 0 and y+i < 8:
                  if board[x+i][y+i][1] != current_player:
                     moving_possibilities.append([x+i, y+i])
                     if board[x+i][y+i][1] == opposit_player:
                        downright = False
                  else:
                     downright = False
               else:
                  downright = False
            i = i+1


      elif piece[0] == 'king':         #================================== king
         check_x = -1
         check_y = -1
         for i in range(3):
            for j in range(3):
               if x+check_x < 8 and y+check_y < 8 and board[x+check_x][y+check_y][1] != current_player:
                  moving_possibilities.append([x+check_x, y+check_y])
               check_x = check_x + 1
            check_x = -1
            check_y = check_y + 1
      
      #=================================================================== end of calculating movements
      print(moving_possibilities)
      #moving_possibilities.remove([x, y])
      mp = moving_possibilities
      length = len(moving_possibilities)
      for i in range(length):
         if board[mp[i][0]][mp[i][1]][1] == opposit_player:
            canvas.create_rectangle(mp[i][0]*100+20, mp[i][1]*100+20, mp[i][0]*100+80, mp[i][1]*100+80, width=0, fill="orange", tag='selection', activefill="red")
            canvas.create_text(mp[i][0]*100+50, mp[i][1]*100+50, text=board[mp[i][0]][mp[i][1]][0], fill=board[mp[i][0]][mp[i][1]][1], tag='selection' )
         else:
            canvas.create_rectangle(mp[i][0]*100+20, mp[i][1]*100+20, mp[i][0]*100+80, mp[i][1]*100+80, width=0, fill="cyan", tag='selection', activefill="blue")
      


canvas = Canvas(mainWindow, width=800, height=800, background='#555555')
setup()
display_pieces()
canvas.place(x=0, y=0)

mainWindow.bind('<Motion>', mouse_motion)
mainWindow.bind('<Button-1>', left_click_pressed)
mainWindow.mainloop()

