from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.title("pingpong game")
window.geometry("800x600")
canvas = Canvas(window,width=800,height=600)
canvas.config(bg="black")
canvas.pack()

player1_score = 0
player2_score = 0
score = canvas.create_text(401,20,text= f"{player1_score} {player2_score}",font=("Aerial",20),fill="white")
canvas.create_line(400,0,400,600,fill="white")
window.update()

class Paddle1:
    pos = [0,0,0,0]
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,200,20,300,fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("w",self.move_up)
        self.canvas.bind_all("s",self.move_down)

    def move_up(self,event):
        self.y = 1

    def move_down(self,event):
        self.y = 1

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= -0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0


class Paddle2:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(780,200,800,300,fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Up>",self.move_up)
        self.canvas.bind_all("<KeyPress-Down>",self.move_down)


    def move_up(self,event):
        self.y = -1

    def move_down(self,event):
        self.y = 1

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= -0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0



player1 = Paddle1(canvas,"red")
player2 = Paddle2(canvas,"blue")

class Ball:
    def __init__(self,canvas,p1,p2,color):
        self.canvas = canvas
        self.player1 = p1
        self.player2 = p2
        self.y = 0
        self.id = canvas.create_oval(375,225,425,275,fill=color)
        self.color = color
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = starts[2]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 5
            self.score2 += 1
            canvas.itemconfigure(score,text=str(self.score1) + " " + str(self.score2))
        if pos[2] >= self.canvas_width:
            self.x = -5
            self.score1 += 1
            canvas.itemconfigure(score,text=str(self.score1) + " " + str(self.score2))
        if pos[1] <= 0:
            self.y = 5
        if pos[3] >= self.canvas_height:
            self.y = -5
        if self.hit_pad1(pos) == True:
            self.x = 4
        if self.hit_pad2(pos) == True:
            self.x = -4

    def hit_pad1(self,pos):
        p1_pos = self.canvas.coords(self.player1.id)
        if pos[1] >= p1_pos[1] and p1_pos[1] <= p1_pos[3]:
            if pos[0] >= p1_pos[0] and pos[0] <= p1_pos[2]:
                return True
            else:
                return False
            
    def hit_pad2(self,pos):
        p2_pos = self.canvas.coords(self.player2.id)
        if pos[1] >= p2_pos[1] and p2_pos[1] <= p2_pos[3]:
            if pos[0] >= p2_pos[0] and pos[0] <= p2_pos[2]:
                return True
            else:
                return False


        


middle_circle = canvas.create_oval(350,200,450,300,outline="green")
ball = Ball(canvas,player1,player2,"white")
while True:
    player1.draw()
    player2.draw()
    ball.draw()
    window.update()
        

window.mainloop()
