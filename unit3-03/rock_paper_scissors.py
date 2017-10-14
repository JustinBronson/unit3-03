#Created by: Justin Bronson
#Created on: Oct 2017
#This program is supposed to play rock, paper,
#  scissors with the user.

import ui
from numpy import random

computer_choice = (random.randint(1, 3))

#constants

ROCK = 1
SCISSORS = 2
PAPER = 3

def rock_button_touch_up_inside(sender):
    if computer_choice == 1:
        view['answer_label'].text = 'I picked rock, we tied.'

    elif computer_choice == 2:
        view['answer_label'].text = 'I picked scissors, you win...'

    elif computer_choice == 3:
        view['answer_label'].text = 'I picked paper, I win!'

def scissors_button_touch_up_inside(sender):
    if computer_choice == 1:
        view['answer_label'].text = 'I picked rock, I win!'

    elif computer_choice == 2:
        view['answer_label'].text = 'I picked scissors, we tied.'

    elif computer_choice == 3:
        view['answer_label'].text = 'I picked paper, you win...'

def paper_button_touch_up_inside(sender):
    if computer_choice == 1:
        view['answer_label'].text = 'I picked rock, you win...'

    elif computer_choice == 2:
        view['answer_label'].text = 'I picked scissors, I win!'

    elif computer_choice == 3:
        view['answer_label'].text = 'I picked paper, we tied.'

view = ui.load_view()
view.present('sheet')
