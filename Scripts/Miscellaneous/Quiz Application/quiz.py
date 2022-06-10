from simple_chalk import chalk


def start_quiz(questions):
    score = 0
    for i in range(0, len(questions)):
        print(questions[i]["question"] + "\n")
        for j in range(1, 5):
            print(str(j) + " " + questions[i]["option" + str(j)])
            print()
        try:
            answer = int(input())
        except ValueError:
            print(chalk.cyan("Please enter a choice between 1 and 4\n"))

            continue
        print()
        if 0 < answer < 5:
            if questions[i]["correct_answer"] == "option" + str(answer):
                print(chalk.green("Correct Answer!!!\n"))
                score = score + 1
            else:
                correct_answer = questions[i]["correct_answer"]
                print(
                    chalk.red(
                        "Wrong!! The Correct Answer is {}".format(
                            questions[i][correct_answer]
                        )
                    )
                )
                print()
        else:
            print(chalk.yellow("Invalid Choice\n"))

    print(chalk.yellow("Your Score is {}/{}".format(score, len(questions))))
