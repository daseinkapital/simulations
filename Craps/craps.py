# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:25:24 2021

@author: 591168
"""
import random

class Craps:
    def __init__(self, min_bet, starting_money):
        self.min_bet = min_bet
        self.bank = starting_money
        self.point = None
        self.dice1 = None
        self.dice2 = None
        self.bets = {
            'pass_line': 0,
            'come': 0,
            'dont_pass_bar': 0,
            'dont_come_bar': 0,
            'field': 0,
            'big_68': 0,
            4: 0,
            5: 0,
            6: 0,
            8: 0,
            9: 0,
            10: 0,
            'hard_four': 0,
            'hard_six': 0,
            'hard_eight': 0,
            'hard_ten': 0,
            'any_craps': 0,
        }
        self.payout_ratio = {
            'pass_line': 1,
            'come': 1,
            'dont_pass_bar': 1,
            'dont_come_bar': 0,
            'field': {
                2: 2,
                3: 1,
                4: 1,
                5: 1,
                9: 1,
                10: 1,
                11: 1,
                12: 3
            },
            'big_68': 1,
            4: 0,
            5: 0,
            6: 0,
            8: 0,
            9: 0,
            10: 0,
            'hard_four': 8,
            'hard_six': 10,
            'hard_eight': 10,
            'hard_ten': 8,
            'snake_eyes': 30,
            'hard_twelve': 30,
            'ace_deuce': 15,
            'five_six': 15,
            'any_craps': 7,
            'seven': 4
        }
    
    def make_pass_line_bet(self, amt):
        if amt > self.min_bet:
            self.bank -= amt
            self.bets['pass_line_bet'] = amt
        else:
            print("Can't make pass bet. Amount too low.")
    
    def eval_payout(self):
        if self.point:
            # do stuff
        else:
            roll = sum(self.roll_die())
            if roll in [2,3,12]:
                pass
            elif roll in [7, 11]:
                self.bank += self.bets['pass_line'] * self.payout_ratio['pass_line']
            else:
                self.point = roll
        if self.dice1 == self.dice2:
            if self.dice1 == 2:
                self.bank += self.bets['']

        
    def roll_die(self):
        self.dice1 = int(random.uniform(0,6))
        self.dice2 = int(random.uniform(0,6))
        
        return dice1, dice2
    
    def craps_out(self):
        for key in self.bets.keys():
            self.bets[key] = 0 # this isn't explicitly true
        self.point = None
        self.dice1 = None
        self.dice2 = None
        
        if self.bank < self.min_bet:
            return 'Game Over'

game = Craps(15, 500)
print(game.roll_die())