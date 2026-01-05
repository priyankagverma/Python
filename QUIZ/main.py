questions = [
    ["Which gas do plants absorb during photosynthesis?",
     "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],

    ["How many continents are there in the world?",
     "5", "6", "7", "8", 3],
     
    ["What is the capital of India?",
     "Mumbai", "Kolkata", "New Delhi", "Chennai", 3],

    ["Who is known as the Father of Computers?",
     "Albert Einstein", "Charles Babbage", "Isaac Newton", "Thomas Edison", 2],

    ["Which is the largest ocean on Earth?",
     "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 4],

    ["Which instrument is used to measure temperature?",
     "Barometer", "Thermometer", "Hygrometer", "Speedometer", 2],

    ["Which number is the smallest prime number?",
     "0", "1", "2", "3", 3],

    ["Which animal is called the ‘Ship of the Desert’?",
     "Horse", "Camel", "Elephant", "Donkey", 2],

    ["What is the boiling point of water?",
     "80°C", "90°C", "100°C", "120°C", 3]
]

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    a = int(input("Please provide the correct answer as a->1, b->2, c->3 or d->4:\n"))
    if (a==question[5]):
        print(f"The answer is correct, The next question is:\n")
    else:
        print(f"Incorrect, The correct answer is {question[5]}")
        print("Better luck next time!!")
        break
