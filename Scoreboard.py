try:
    with open("highscore.txt", "r") as f:
        highscore = f.read()
        if len(highscore) < 1:
            print("There is no previus high score")
        else:
            print("the top ten scores previasly are")
            print(highscore)
except FileNotFoundError:
    print("new file")
    f = open("highscore.txt", "w")
    f.close()

while True:
    scores = []
    name = []
    with open ("highscore.txt", "r") as fle:
        for x in fle:
            if x != "":
                x = x.strip("\n")
                x = x.split()
                name.append(x[0])
                scores.append(int(x[1]))

    print("-" * 20)
    print()
    names = input("namep ls")
    score = 0
    print("answer 3 Q")


    print("Question 1: What is the product of 2x2x2?")
    answer = int(input("Your answer :>> "))
    if answer == 8: # if the input is 8, get 1 more score.
        print("Correct")
        score += 1
        print("Your score is:", score)

    print("Question 2: What is the sum of 21+22?")
    answer = int(input("Your answer :>> "))
    if answer == 43: # is the input is corerect, +1 score
        print("Correct")
        score += 1
        print("Your score is:", score)

    print("Question 3: What is the remainder of 36 divided by 12?")
    answer = int(input("Your answer :>> "))
    if answer == 3: # is the input is corerect, +1 score
        print("Correct")
        score += 1
        print("Game over. Your score is:", score)
    print()

    if len(scores) < 1:
        scores.append (score)
        names.append(name)

    else:
        position = 0
        for i in scores:
            if score < i:
                position += 1
        scores.insert(position, score)
        names.insert (position, name)

    if len (scores) > 10:
        scores = scores[:10]
        names = names[:10]

    with open ("highscore.txt", "w") as file:
        for i in range(len(scores)):
            file.write(names[i] + "\t" + str(scores[i]) + "\n")
            print(names[i] + " " + str(scores[i]))

    exit = input("Press Enter to exit the quiz or any other key to repeat the quiz :>> ") #ends or restarts the program depending on user input
    if exit == "":
        break
