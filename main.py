# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player1 + " " + str(goal_0) + ", " + player2 + " " + str(goal_1)
report = f'{player1} scored in the {goal_0}nd minute\n'f'{player2} scored in the {goal_1}th minute' 

player = 'Berry van Aerle'
first_name = player[:5]
last_name_len= len(player[6:15])
name_short = player[0] + ". " + player[6:15]   
chant = f'{first_name}!' " " * 4 + f'{first_name}!'
good_chant = chant != 'Berry! Berry! Berry! berry! Berry!'
