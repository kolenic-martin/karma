import os
import time
import random
import karma_cfg


def reset_cfg():
    karma_cfg.day = 1
    karma_cfg.social = 1
    karma_cfg.hunger = 1
    karma_cfg.obey = 1
    karma_cfg.fun = 3


def clear_screen():
    os.system('cls||clear')


def print_pause(message="", speed=0.025, sleep=1.5):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(speed)
    time.sleep(sleep)


def print_ellipsis():
    count = 0
    while count < 3:
        print(".", end="", flush=True)
        count += 1
        time.sleep(0.5)
    print("\n")
    time.sleep(1.5)


def display_karma():
    clear_screen()
    print("                  (((((/((############(                \n"
          "             .*/(/(//*//((#############/##             \n"
          "          *****(/*******((#############(*(#            \n"
          "      .//****,*/,***//(///(#######((####*(###*,        \n"
          "    ((******,,*,,,*,.,,/**((######(/*/,**/######       \n"
          "   #(/*,*,*,,,**..*,,,,..,/(######(***//*(######       \n"
          "    ((/******,**,.,***(***//(######(###*/#######       \n"
          "     ,//*****,,*,..,**//***/((#####(##(*#######*       \n"
          "        ******,,,...*******//((#(#####*(#######        \n"
          "          ****,,,,..***,****/((#######((#######        \n"
          "          *****,*,,..*******(/(########(##(##(#        \n"
          "          **,*,,,,...,******//(////###########*        \n"
          "            ,*,,...,,.******..,**/***###(#             \n"
          "             **,/,..*///****,,....,/####,              \n"
          "            ,*(**....,,*(///((##(#####(,               \n"
          "            ...,/(*,..,*##&&#&#&((//**//               \n"
          "            (*.....*##*.##((((*.,*/(#&&@&              \n"
          "           ,((##(/(#**/(##&&(/*.,/#&&&&&&*             \n"
          "           ((########/**/###&&##(/(#&&&###             \n"
          "          .///(########/((##&&&##(/**/((##             \n"
          "          *****/(##(*,.//((*.. .  .***//##             \n"
          "           /***//((,    ..... .....,,,**//,            \n"
          "           *****(#             ,....,,*,,**/           \n"
          "         ,***///(                .,..,,,,,,,**,        \n"
          "      */(,(/(//((                   ,*,,**/,,****,/    \n"
          "     .*,*,,///.                       ......,,.  ..,   \n\n")
    print_pause("Oh, Karma. Aren't you cute?\n\n", sleep=5)
    clear_screen()


def train():
    clear_screen()
    if karma_cfg.obey < 5:
        print_pause("You trained with Karma using some treats.\n"
                    "She will obey you more now.\n\n")
        karma_cfg.obey += 1
    else:
        print_pause("You trained with Karma using some treats.\n"
                    "She now obeys every command.\n\n")
    while karma_cfg.hunger >= 0:
        karma_cfg.hunger -= 1
    clear_screen()


def play():
    clear_screen()
    print_pause("You played with Karma.\n"
                "She had fun with you.\n")
    karma_cfg.fun += 1
    clear_screen()


def socialize():
    clear_screen()
    if karma_cfg.hunger < 5:
        if karma_cfg.social == 0:
            print_pause("Karma is too shy to play with "
                        "other dogs.\n\n")
        elif 0 < karma_cfg.social < 5:
            outcome = random.randrange(6)
            if outcome == 0:
                print_pause("Another dog scared Karma.\n"
                            "She had no fun and feels distrust"
                            "toward you.\n\n")
                karma_cfg.fun -= 1
                karma_cfg.social -= 1
                karma_cfg.obey -= 1
            else:
                print_pause("Karma had a lot of fun.")
                karma_cfg.fun += 1
                karma_cfg.social += 1
    else:
        print_pause("Karma keeps licking and biting\n"
                    "your fingers ever so slightly.\n")
        print_pause("She's probably hungry.\n\n")
    clear_screen()


def treat():
    clear_screen()
    if karma_cfg.hunger == 0:
        print_pause("Karma doesn't want food now.\n\n")
    elif karma_cfg.hunger < 5:
        print_pause("You gave a treat to Karma. She loved it.\n\n")
        karma_cfg.fun += 2
        karma_cfg.hunger -= 1
    else:
        print_pause("Karma devoured the treat like there's no tomorrow.\n\n")
        karma_cfg.fun += 1
        karma_cfg.hunger -= 1
    clear_screen()


def feed():
    clear_screen()
    if karma_cfg.hunger == 0:
        print_pause("Karma doesn't want food now.\n\n")
    elif karma_cfg.hunger < 3:
        print_pause("You fed Karma. She is munching happily.\n\n")
        karma_cfg.hunger -= 1
    else:
        print_pause("You fed Karma. She ate it a little too fast.\n\n")
        karma_cfg.hunger = 3
    clear_screen()


def walk():
    clear_screen()
    if karma_cfg.hunger < 5:
        if karma_cfg.obey < 2:
            verb = ["peed", "pooped"]
            activity = random.randint(1, 2)
            print_pause("Karma kept sitting stubbornly.\n"
                        "Desperate, you took her in your arms\n"
                        "and went back home, where she " + verb[activity]
                        + "\non the carpet.")
            karma_cfg.hunger += 1
            clear_screen()
            home()
        if 4 > karma_cfg.obey >= 2:
            print_pause("After a while, Karma finally moved on.\n"
                        "The walk was okay, and she seemed to\n"
                        "enjoy it.\n")
            karma_cfg.fun += 1
            karma_cfg.hunger += 1
        if karma_cfg.obey >= 4:
            print_pause("Karma followed you happily.\n"
                        "You both enjoyed the walk and she seems "
                        "a little less shy.\n\n")
            karma_cfg.fun += 2
            karma_cfg.hunger += 1
            karma_cfg.social += 1
    else:
        print_pause("Karma keeps licking and biting\n"
                    "your fingers ever so slightly.\n")
        print_pause("She's probably hungry.\n\n")
    clear_screen()


def new_day():
    clear_screen()
    print_pause("Whew, what a day!\n"
                "Both of you deserve a good night's sleep.\n\n")
    karma_cfg.hunger = 4
    karma_cfg.day += 1
    clear_screen()
    print_pause("It's Day no. " + str(karma_cfg.day) + ".")


def park():
    clear_screen()
    print_pause("You are in the park.\n")
    dogs_present = random.choice([True, False])
    if dogs_present:
        print_pause("There are some people walking their dogs.\n")
        print_pause("What do you want to do?\n\n")
        outcome = input("[1] Walk Karma in the park.\n"
                        "[2] Give her a treat.\n"
                        "[3] Train her a bit.\n"
                        "[4] Let her play with other dogs.\n"
                        "[5] Go back home.\n"
                        "Type the number of your choice: ")
        if outcome == "1":
            walk()
            park()
        elif outcome == "2":
            treat()
            park()
        elif outcome == "3":
            train()
            park()
        elif outcome == "4":
            socialize()
            park()
        elif outcome == "5":
            home()
        else:
            print_pause("That doesn't seem to be an option.\n")
            print_ellipsis()
            park()
    else:
        print_pause("There seem to be no dogs in the park.\n")
        print_pause("What do you want to do?\n\n")
        outcome = input("[1] Walk Karma in the park.\n"
                        "[2] Give her a treat.\n"
                        "[3] Train her a bit.\n"
                        "[4] Go back home.\n"
                        "Type the number of your choice: ")
        if outcome == "1":
            walk()
            park()
        elif outcome == "2":
            treat()
            park()
        elif outcome == "3":
            train()
            park()
        elif outcome == "4":
            home()


def home():
    if karma_cfg.day != 7:
        print_pause("You are at home.\n")
        print_pause("What do you want to do?\n\n")
        outcome = input("[1] Take Karma to the park.\n"
                        "[2] Give her a treat.\n"
                        "[3] Train her a bit.\n"
                        "[4] Give her food.\n"
                        "[5] Take a picture.\n"
                        "[6] Play with her.\n"
                        "[0] Call it a day.\n"
                        "Type the number of your choice: ")
        if outcome == "1":
            park()
        elif outcome == "2":
            treat()
            home()
        elif outcome == "3":
            train()
            home()
        elif outcome == "4":
            feed()
            home()
        elif outcome == "5":
            display_karma()
            home()
        elif outcome == "6":
            play()
            home()
        elif outcome == "0":
            new_day()
            home()
        else:
            print_pause("That doesn't seem to be an option.\n")
            print_ellipsis()
            clear_screen()
            home()
    else:
        outro()


def intro():
    print_pause("Your friends P. and M. asked you to dogsit Karma,\n"
                "a dachshund puppy, for a week. Make sure that:\n\n"
                "- she is not hungry\n"
                "- she has fun\n"
                "- she isn't shy of other dogs.\n\n"
                "Good luck!", sleep=5)
    clear_screen()


def outro():
    print_pause("It's your last day with Karma "
                "and the owners came to pick her up.\n")
    if karma_cfg.hunger >= 4 or karma_cfg.fun < 3 or karma_cfg.social < 2:
        print_pause("She ran to them and growled sadly, "
                    "nipping at their fingers.\n")
        print_pause("'It seems she isn't too happy.', said M., "
                    "obviously worried.\n", sleep=1)
        print_ellipsis()
        print_pause("GAME OVER.\n\n")
        clear_screen()
    else:
        print_pause("She was happy to see them, but looked back "
                    "at you with longing.\n")
        print_pause("'Oh, she seems to have fallen for you, mate,' "
                    "said P. with a friendly smile.", sleep=1)
        print_ellipsis()
        print_pause("YOU WIN!\n\n")
        display_karma()
        clear_screen()
    while True:
        outcome = input("[1] Play again.\n"
                        "[2] Quit game.\n"
                        "Type the number of your choice: ")
        if "1" in outcome:
            clear_screen()
            play_game()
        elif "2" in outcome:
            exit(0)
        else:
            print_pause("That doesn't seem to be an option.\n")
            print_ellipsis()
            clear_screen()


def play_game():
    reset_cfg()
    clear_screen()
    intro()
    home()


if __name__ == '__main__':
    play_game()
