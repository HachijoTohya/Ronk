import random
from arsenal import arsenal
rock = arsenal("paper", "scissors", "rock")
paper = arsenal("scissors", "rock", "paper")
scissors = arsenal("rock", "paper", "scissors")
weapons = [rock, paper, scissors]
yn = {
    "y": "yes",
    "n": "no"
}
playing = True


def playermove():
    print("Let's play Rock, Paper, Scissors! Which do you pick?")
    while True:
        hand = input(">").lower()
        for weapon in weapons:
            if hand == weapon.wepid:
                return hand
        print("Please enter rock, paper, or scissors.")


def opponentmove():
    opphand = weapons[random.randrange(0, 3)]
    return opphand


def playgame():
    play = playermove()
    opp = opponentmove()

    if play == opp.weakto:
        print("The opponent played " + opp.wepid + ". You win!")
    elif play == opp.beats:
        print("The opponent played " + opp.wepid + ". You lose!")
    else:
        print("The opponent also played " + opp.wepid + ". It's a tie!")


playgame()

while playing:
    again = input("\nWould you like to play again? (Y/N)\n>").lower()
    if yn.get(again, again) == "yes":
        playgame()
    elif yn.get(again, again) == "no":
        print("See you next time!")
        playing = False
    else:
        print("Please enter 'Yes' or 'no'. (Y/N)")
