from os import name as OSname
from os import system as OSsys
from random import randint
from time import sleep


# Clear screen after each round
def clearScreen():
    if OSname == "nt":
        OSsys("cls")
    else:
        OSsys("clear")


# Creating throw dice function
def throw_dice(player_name):
    top = randint(1, 6)
    print(f"\n{player_name} threw the dice...\n")
    sleep(0.3)
    sleep(randint(10, 30) * 0.05)
    print_dice(top)
    return top


# Creating function to visualize dice top
def print_dice(top):
    sides = [
        "|     |\n|  *  |\n|     |",
        "|  *  |\n|     |\n|  *  |",
        "|*    |\n|  *  |\n|    *|",
        "|*   *|\n|     |\n|*   *|",
        "|*   *|\n|  *  |\n|*   *|",
        "|*   *|\n|*   *|\n|*   *|",
    ]
    print("+-----+")
    sleep(0.3)
    print(sides[top - 1])
    print("+-----+")
    sleep(0.3)


def show_score(roundnum, p1, p2, p1_points, p2_points):
    print(f"\nRound {roundnum}")
    sleep(0.3)
    print("------------------------------------------")
    sleep(0.3)
    print(f"{p1} : {p1_points}")
    sleep(0.3)
    print(f"{p2} : {p2_points}")
    sleep(0.3)
    print("------------------------------------------\n")
    sleep(0.3)


def main():
    # Number of rounds
    done = False
    while not done:
        try:
            n = int(input("Enter the number of rounds: "))
            if n > 0:
                done = True
            else:
                print("Please Enter a positive number!")
                sleep(0.3)
        except ValueError:
            print("please Enter an integer.")
            sleep(0.3)

    # Name of players and initialize points
    p1 = input("\nName of first player? ")
    p2 = input("\nName of second player? ")

    p1_points = 0
    p2_points = 0

    for i in range(n):
        print("Scoreboard:")
        sleep(0.3)
        show_score(i + 1, p1, p2, p1_points, p2_points)
        sleep(0.3)

        r1 = throw_dice(p1)
        sleep(0.3)
        r2 = throw_dice(p2)
        sleep(0.3)

        if r1 > r2:
            print(f"\n{p1} won this round.")
            sleep(0.3)
            p1_points += 1
        elif r2 > r1:
            print(f"\n{p2} won this round.")
            sleep(0.3)
            p2_points += 1
        else:
            print("\nIt's a draw.")
            sleep(0.3)

        q = input(
            "\n\nPress enter to continue to next round. (Q to stop rounds)"
        )

        if q.upper() == "Q":
            break

        clearScreen()

    print("\n\n")
    if p1_points > p2_points:
        print(f"{p1} won by {p1_points - p2_points} points.")
        sleep(0.3)
    elif p2_points > p1_points:
        print(f"{p2} won by {p2_points - p1_points} points.")
        sleep(0.3)
    else:
        print("Game ended in a draw...")
        sleep(0.3)

    print("\nFinal Score Board:")
    show_score(i + 1, p1, p2, p1_points, p2_points)

    with open("result_rolladice.txt", "a") as file:
        cov = "\n------------------------------------\n"
        r = f"Number of rounds: {n}\n{p1}: {p1_points}\n{p2}: {p2_points}"
        res = cov + r + cov

        file.write(res)


if __name__ == "__main__":
    main()
