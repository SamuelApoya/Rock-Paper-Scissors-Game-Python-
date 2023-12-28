'''
Samuel Apoya
         CS 152 Final Project
                         Fall 2022
                             December 14, 2022



'''
import random
import tkinter as tk
from tkinter import *



''' Creating a class for the game'''
class RockPaperscissors(object):
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x400")
        self.window.title("Rock Paper Scissors Game")
        self.USER_SCORE = 0
        self.COMPUTER_SCORE = 0
        self.USER_CHOICE = ""
        self.COMPUTER_CHOICE = ""
        # Creating a button and displaying them to show rock.
        self.button1 = tk.Button(text= " Rock ", highlightbackground='green', command=self.rock)
        self.button1.grid(column=0, row=1)
        # Creating a button and displaying them to show paper.
        self.button2 = tk.Button(text= " Paper ", highlightbackground="indigo", command=self.paper)
        self.button2.grid(column=0, row=2)
        # Creating a button and displaying them to show scissor.
        self.button3 = tk.Button(text= " Scissor ", highlightbackground="orange", command=self.scissor)
        self.button3.grid(column=0, row=3)

    ''' Converting user's choice to numbers'''
    def choiceToNumber(self, choice):
        rock_paper_scissors = {'rock':0, 'paper':1, 'scissor':2} # Using dictionary to assign values to correspond to rock, paper, and scissors
        return rock_paper_scissors[choice]


    ''' A function to convert the user entry from numerical value to rock, paper, or scissors'''
    def numberToChoice(self, number):
        rock_paper_scissors = {0: 'rock', 1: 'paper', 2: 'scissor'}
        return rock_paper_scissors[number]


    ''' Making computer choice using the random module to let computer randomly choose among rock, paper, or scissors'''
    def computerChoice(self):
        return random.choice(['rock', 'paper', 'scissor'])


    ''' This function defines the choices for the user and the computer'''
    def result(self, user_choice, computer_choice):
       
        user = self.choiceToNumber(user_choice)
        computer = self.choiceToNumber(computer_choice)


    # Setting conditions for draw, computer wins, and user wins
        if (user == computer):    
            print('draw')

        elif ((user-computer) % 3 == 1):
            print('you win')
            self.USER_SCORE += 1


        else:
            print("computer wins")
            self.COMPUTER_SCORE += 1
    #Creating a window to show results
        text_area = tk.Text(master=self.window, height=12, width=30, bg="orange")
        text_area.grid(column=0, row=4)
        answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc = self.USER_CHOICE, cc = self.COMPUTER_CHOICE, u = self.USER_SCORE, c = self.COMPUTER_SCORE)
        text_area.insert(tk.END, answer)
        ''' When user choses rock, the function "computerChoice is called upon to make a choice for computer'''
    def rock(self):
       


        self.USER_CHOICE = 'rock'
        self.COMPUTER_CHOICE = self.computerChoice()
        self.result(self.USER_CHOICE, self.COMPUTER_CHOICE)
        

    ''' When user choses paper, the function "computerChoice is called upon to make a choice for computer'''
    def paper(self):
       
        self.USER_CHOICE = 'paper'
        self.COMPUTER_CHOICE = self.computerChoice()
        self.result(self.USER_CHOICE, self.COMPUTER_CHOICE)



    ''' When user choses scissors, the function "computerChoice is called upon to make a choice for computer'''
    def scissor(self):
   
        self.USER_CHOICE = 'scissor'
        self.COMPUTER_CHOICE = self.computerChoice()
        self.result(self.USER_CHOICE, self.COMPUTER_CHOICE)


def main():
    win = tk.Tk()
    gui = RockPaperscissors(win)
    win.mainloop()

if __name__ == "__main__":
    main()
