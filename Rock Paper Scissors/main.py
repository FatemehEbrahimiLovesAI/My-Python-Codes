import random
selectable = ["rock","paper","scissors"]

def bot_choice(selectable):
    b_choice = random.choice(selectable)
    return b_choice
    
print("start game")
bot_score= 0
player_score= 0

while player_score<3 and bot_score<3:
    b_choice= bot_choice(selectable)
    u_choice= input("\nenter your choice [rock,paper,scissors]")
    if u_choice in selectable:
        if u_choice== selectable[0] and b_choice== selectable[1]:
            bot_score+=1
        elif u_choice== selectable[1] and b_choice== selectable[0]:
            player_score+=1
        elif u_choice== selectable[0] and b_choice== selectable[2]:
            player_score+=1
        elif u_choice== selectable[2] and b_choice== selectable[0]:
            bot_score+=1
        elif u_choice== selectable[1] and b_choice== selectable[2]:
            bot_score+=1
        elif u_choice== selectable[2] and b_choice== selectable[1]:
            player_score+=1
        else:
            print("draw!")
        print("choices: \n your choice=", u_choice,"\tbot choice:", b_choice)
        print("your score:",player_score,"\tbot score:",bot_score)
    else:
        print("incorrect choice, please select again")


if player_score== 3:
    print("you won! congratulations!")
elif bot_score== 3:
    print("you lost, try again later")

