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
first_name = player[:5] # this must be: <player[:player.find(" ")]>
last_name_len= len(player[6:15]) #this must be: <len(player[player.find(" ")+1:])>
name_short = player[0] + ". " + player[6:15] # this must be <player[0] + ". " + player[player.find(" ")+1:]>  
chant = f'{first_name}!' " " * 4 + f'{first_name}!' # must be: <(f'{first_name}! '* len(first_name))[:-1]>
good_chant = chant != 'Berry! Berry! Berry! berry! Berry!' # must be: <chant != first_name> 

=======================================================================================================================
#Code has been modified from part 2. starts from line 12 up to 17. The modified codes (strings) are made in line 28 up to 33. 
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player1 + " " + str(goal_0) + ", " + player2 + " " + str(goal_1)
report = f'{player1} scored in the {goal_0}nd minute\n'f'{player2} scored in the {goal_1}th minute' 

player = 'Ruud Gullit'
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])
name_short = player[0] + ". " + player[player.find(" ")+1:]
chant = (f'{first_name}! '* len(first_name))[:-1]
good_chant = chant != first_name
