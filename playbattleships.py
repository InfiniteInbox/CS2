'''
Created on Feb 15, 2022

@author: yjain24
'''
from battleshipspvp import BattleshipsPVP
from battleshipcomp import BattleshipsCOMP

# Script initiates game of battleships


def playbattleships():
    print("\n\n***********************")
    print("Welcome to Battleships!")
    print("***********************\n")

    print("\n 1) Player vs Player")
    print("\n 2) Player vs Computer")

    flag = True

    while flag:
        try:
            mode = int(input("\n\nPick a number to select a game mode ----> "))
            if mode == 1:
                flag = False
                BattleshipsPVP()
            elif mode == 2:
                flag = False
                BattleshipsCOMP()
            else:
                continue
        except ValueError:
            print("You can only pick either option 1 or 2")


playbattleships()