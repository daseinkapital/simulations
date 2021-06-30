import pytest
from craps import Craps

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)

def set_roll(game, dice1, dice2):
    game.dice1 = dice1
    game.dice2 = dice2
    game.roll_sum = dice1 + dice2
    return game

def test_fair_die_roll():
    roll = []
    game = Craps(20, 500)
    for i in range(100000):
        game.roll_die()
        roll.append(game.dice1)
        roll.append(game.dice2)
    one = round(roll.count(1)/100000)
    two = round(roll.count(2)/100000)
    three = round(roll.count(3)/100000)
    four = round(roll.count(4)/100000)
    five = round(roll.count(5)/100000)
    six = round(roll.count(6)/100000)
    assert all_equal([one, two, three, four, five, six])

def test_make_standard_bet_subtract_money_from_bank():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    assert game.bank == 480

def test_make_standard_bet_not_enough_money_bank_amount():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 10)
    assert game.bank == 500

def test_make_standard_bet_not_enough_money_error():
    game = Craps(20, 500)
    assert game.make_standard_bet('pass_line', 10) == ''

def test_make_standard_bet_six_place_increase_bank():
    game = Craps(20, 500)
    game.make_standard_bet(6, 20)
    assert game.bank == (500-24)

def test_make_standard_bet_six_place_decrease_bank():
    game = Craps(20, 29)
    game.make_standard_bet(6, 25)
    assert game.bank == 1

def test_make_standard_bet_six_place_decrease_bank():
    game = Craps(20, 20)
    assert game.make_standard_bet(6, 20) == ''

def test_eval_payout_pass_line_bet_point_on_win_bank():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game = set_roll(game, 3, 3)
    game.point = 6
    game.eval_payout()
    assert game.bank == 500

def test_eval_payout_pass_line_bet_point_on_win_bet():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game = set_roll(game, 3, 3)
    game.point = 6
    game.eval_payout()
    assert game.bets['pass_line'] == 20

def test_eval_payout_pass_line_bet_point_on_lose_bank():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game.point = 6
    game = set_roll(game, 4, 3)
    game.eval_payout()
    assert game.bank == 480

def test_eval_payout_pass_line_bet_point_on_lose_bet():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game.point = 6
    game = set_roll(game, 4, 3)
    game.eval_payout()
    assert game.bets['pass_line'] == 0

def test_eval_payout_win_pass_line_bet_point_off_win_bank():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game = set_roll(game, 4, 3)
    game.eval_payout()
    assert game.bank == 500

def test_eval_payout_win_pass_line_bet_point_off_win_bet():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game = set_roll(game, 4, 3)
    game.eval_payout()
    assert game.bets['pass_line'] == 20

def test_eval_payout_pass_line_bet_point_off_lose_bank():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game = set_roll(game, 1, 1)
    game.eval_payout()
    assert game.bank == 480

def test_eval_payout_pass_line_bet_point_off_lose_bet():
    game = Craps(20, 500)
    game.make_standard_bet('pass_line', 20)
    game = set_roll(game, 1, 1)
    game.eval_payout()
    assert game.bets_total == 0

def test_eval_payout_field_bet_win_bank():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 2, 2)
    game.eval_payout()
    assert game.bank == 500

def test_eval_payout_field_bet_win_bet():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 2, 2)
    game.eval_payout()
    assert game.bets['field'] == 20

def test_eval_payout_field_bet_win_two_bank():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 1, 1)
    game.eval_payout()
    assert game.bank == 520

def test_eval_payout_field_bet_win_two_bet():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 1, 1)
    game.eval_payout()
    assert game.bets['field'] == 20

def test_eval_payout_field_bet_win_twelve_bank():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 6, 6)
    game.eval_payout()
    assert game.bank == 520

def test_eval_payout_field_bet_win_twelve_bet():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 6, 6)
    game.eval_payout()
    assert game.bets['field'] == 20

def test_eval_payout_field_bet_lose_bank():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 3, 3)
    game.eval_payout()
    assert game.bank == 480

def test_eval_payout_field_bet_lose_bet():
    game = Craps(20, 500)
    game.make_standard_bet('field', 20)
    game = set_roll(game, 3, 3)
    game.eval_payout()
    print("Roll sum", game.roll_sum)
    assert game.bets['field'] == 0

def test_eval_payout_place_bet_win_four_bank():
    game = Craps(20, 500)
    game.make_standard_bet(4, 20)
    game = set_roll(game, 1, 3)
    game.eval_payout()
    assert game.bank == 516

def test_eval_payout_place_bet_win_four_bet():
    game = Craps(20, 500)
    game.make_standard_bet(4, 20)
    game = set_roll(game, 1, 3)
    game.eval_payout()
    assert game.bets[4] == 20

def test_eval_payout_place_bet_win_five_bank():
    game = Craps(20, 500)
    game.make_standard_bet(5, 20)
    game = set_roll(game, 2, 3)
    game.eval_payout()
    assert game.bank == 508

def test_eval_payout_place_bet_win_four_bet():
    game = Craps(20, 500)
    game.make_standard_bet(5, 20)
    game = set_roll(game, 2, 3)
    game.eval_payout()
    assert game.bets[5] == 20

def test_eval_payout_place_bet_win_six_bank():
    game = Craps(20, 500)
    game.make_standard_bet(6, 20)
    game = set_roll(game, 3, 3)
    game.eval_payout()
    assert game.bank == 504

def test_eval_payout_place_bet_win_six_bet():
    game = Craps(20, 500)
    game.make_standard_bet(6, 20)
    game = set_roll(game, 3, 3)
    game.eval_payout()
    assert game.bets[6] == 24

def test_eval_payout_place_bet_lose_bank():
    game = Craps(20, 500)
    game.make_standard_bet(4, 20)
    game.point = 6
    game = set_roll(game, 3, 4)
    game.eval_payout()
    assert game.bank == 480

def test_eval_payout_place_bet_lose_bet():
    game = Craps(20, 500)
    game.make_standard_bet(4, 20)
    game.point = 6
    game = set_roll(game, 3, 4)
    game.eval_payout()
    assert game.bets[4] == 0

def test_eval_payout_no_point_point_off():
    game = Craps(20, 500)
    game.dice1 = game.dice2 = 1
    game.roll_sum = 2
    game.eval_payout()
    assert game.point == None

def test_eval_payout_point_on():
    game = Craps(20, 500)
    game.dice1 = game.dice2 = 3
    game.roll_sum = 6
    game.eval_payout()
    assert game.point == 6

