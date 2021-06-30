# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:25:24 2021

@author: Andrew Samuelson
"""
import random

class Craps:
    def __init__(self, min_bet, starting_money):
        self.min_bet = min_bet
        self.bank = starting_money
        self.point = None
        self.dice1 = None
        self.dice2 = None
        self.roll_sum = None
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
            'dont_come_bar': 1,
            'field': {
                2: 2,
                3: 1,
                4: 1,
                9: 1,
                10: 1,
                11: 1,
                12: 2
            },
            'big_68': 1,
            4: 1.8,
            5: 1.4,
            6: 7/6,
            8: 7/6,
            9: 1.4,
            10: 1.8,
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
    
    def make_standard_bet(self, bet, amt):
        """
        Makes bet for bet that require table minimums
        """
        if amt >= self.min_bet:
            if bet in [6,8]:
                even_amt = amt
                while even_amt % 6:
                    even_amt += 1
                if self.bank >= even_amt:
                    amt = even_amt
                    print("Your place bet was increased to maintain even payout.")                
                else:
                    even_amt -= 1
                    while even_amt % 6:
                        even_amt -= 1
                    if self.min_bet <= even_amt:
                        amt = even_amt
                        print("Your place bet has been decreased to maintain even payout.")
                    else:
                        print("Can't make place bet. Not enough money")
                        return ''
            self.bank -= amt
            self.bets[bet] = amt
        else:
            print("Can't make bet. Amount too low.")
            return ''
    
    def eval_payout(self):
        # create logic for if the pass line bet is placed
        if self.bets['pass_line']:
            bet = 'pass_line'
            if self.point:
                # if the point is on and won, pay out the shooter
                if self.roll_sum == self.point:
                    self.bank += self.bets[bet] * self.payout_ratio[bet]
            else:
                # if one of the winning numbers if hit, pay out the shooter
                if self.roll_sum in [7, 11]:
                    self.bank += self.bets[bet] * self.payout_ratio[bet]
        
        # if a field bet is placed, evaluate the logic for field bets
        if self.bets['field']:
            bet = 'field'
            # if a winner is rolled, pay out the shooter
            if self.roll_sum in [2, 3, 4, 9, 10, 11, 12]:
                self.bank += self.bets[bet] * self.payout_ratio[bet][self.roll_sum]
            # field bet is a one off bet, so any other number is a lose
            else:
                self.bets[bet] = 0
        
        if self.roll_sum in [4,5,6,8,9,10]:
            self.bank += self.bets[self.roll_sum] * self.payout_ratio[self.roll_sum]

        # if the point is not set and a place number is rolled, turn the point on
        if not self.point:
            if self.roll_sum in [4, 5, 6, 8, 9, 10]:
                self.point = self.roll_sum
            elif self.roll_sum in [2, 3, 12]:
                self.craps_out()
        else:
            if self.roll_sum == 7:
                self.craps_out()

        
    def roll_die(self):
        self.dice1 = int(random.uniform(0,6))
        self.dice2 = int(random.uniform(0,6))
        self.roll_sum = sum([self.dice1, self.dice2])
        
        return self.dice1, self.dice2
    
    def craps_out(self):
        for key in self.bets.keys():
            # some bets are made by betting on craps out
            # keep those bets active
            if key not in ['field']:
                self.bets[key] = 0
        self.point = None
        self.dice1 = None
        self.dice2 = None
        
        if self.bank < self.min_bet:
            return 'Game Over'
    
    def shoot(self):
        self.roll_die()
        self.eval_payout()

    @property
    def bets_total(self):
        total = 0
        for key in self.bets.keys():
            total += self.bets[key]
        return total