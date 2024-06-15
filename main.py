print("----====---- Real Fan Test ----====---- ")
print()
print()
print(" Select the Anime you like! ")
anime=input("(a) Naruto / (b) One Piece / (c) Quit ").lower()

#NARUTO
if anime=="a" or anime=="naruto":
    print("-------------------- Welcome to the Naruto Fan Quiz! ------------------------")

    # Initialize a score to keep track of correct answers
    score = 0

    # Question 1
    answer1 = input("Q1: Who is the main protagonist of Naruto? (a) Sasuke (b) Naruto (c) Kakashi\n").lower()
    if answer1 == "b" or answer1 == "naruto":
       score += 1

    # Question 2
    answer2 = input("Q2: Which village does Naruto belong to? (a) Konoha (b) Suna (c) Kiri\n").lower()
    if answer2 == "a" or answer2 == "konoha":
      score += 1

    # Question 3
    answer3 = input("Q3: What is the name of Naruto's signature jutsu? (a) Chidori (b) Rasengan (c) Shadow Clone Jutsu\n").lower()
    if answer3 == "b" or answer3 == "rasengan":
        score += 1

    # Question 4
    answer4 = input("Q4: Who is Naruto's childhood friend and rival? (a) Sakura (b) Sasuke (c) Hinata\n").lower()
    if answer4 == "b" or answer4 == "sasuke":
       score += 1

    # Question 5
    answer5 = input("Q5: What is the name of Naruto's teacher in the early part of the series? (a) Jiraiya (b) Orochimaru (c) Kakashi\n").lower()
    if answer5 == "c" or answer5 == "kakashi":
        score += 1

    # Question 6
    answer6 = input("Q6: What is the name of Naruto's father? (a) Minato (b) Jiraiya (c) Itachi\n").lower()
    if answer6 == "a" or answer6 == "minato":
       score += 1

    # Question 7 
    answer7 = input("Q7: Who is the main antagonist in Naruto Shippuden? (a) Orochimaru (b) Pain (c) Madara\n").lower()
    if answer7 == "c" or answer7 == "madara":
        score += 1

    # Question 8
    answer8 = input("Q8: What is the name of Naruto's mother? (a) Hinata (b) Sakura (c) Kushina\n").lower()
    if answer8 == "c" or answer8 == "kushina":
        score += 1

    # Calculate the percentage of correct answers
    percentage = (score / 8) * 100

    # Determine if the user is a fake fan or a real fan based on the percentage
    if percentage >= 75:
       print(f"Congratulations! You are a real Naruto fan 🍃🥷with a score of {percentage:.2f}%.")
    else:
       print(f"You are a fake fan. Your score is {percentage:.2f}%. Keep watching Naruto to become a real fan!🍃🥷")

#ONE PIECE
elif anime=="b" or anime=="one piece":
 print("--------- Welcome to the One Piece Fan Test! --------")
 score = 0

 # Question 1
 print("1. Who is the main protagonist of One Piece?")
 print("a) Roronoa Zoro")
 print("b) Monkey D. Luffy")
 print("c) Portgas D. Ace")
 answer = input("Your answer (a/b/c): ")
 if answer == "b":
    score += 1

 # Question 2
 print("2. What is the name of Luffy's signature attack?")
 print("a) Gomu Gomu no Pistol")
 print("b) Gum-Gum Bazooka")
 print("c) Gum-Gum Gatling")
 answer = input("Your answer (a/b/c): ")
 if answer == "c":
     score += 1

 # Question 3
 print("3. Who is the captain of the Straw Hat Pirates?")
 print("a) Nico Robin")
 print("b) Franky")
 print("c) Monkey D. Luffy")
 answer = input("Your answer (a/b/c): ")
 if answer == "c":
     score += 1 
 
 # Question 4
 print("4. What is the name of the legendary treasure in One Piece?")
 print("a) Pirate King's Crown")
 print("b) One Piece")
 print("c) Red Line")
 answer = input("Your answer (a/b/c): ")
 if answer == "b":
     score += 1

 # Question 5
 print("5. Who is known as the 'Surgeon of Death' in One Piece?")
 print("a) Trafalgar Law") 
 print("b) Eustass Kid")
 print("c) Donquixote Doflamingo")
 answer = input("Your answer (a/b/c): ")
 if answer == "a":
     score += 1

 # Decision
 if score >= 4:
     print(f"Congratulations! You are a real One Piece fan!🤠🏴‍☠️ with a score of {score}")
 else:
     print(f"Sorry, you are a fake One Piece fan. with a score of {score} .Keep watching One Piece to become a Real Fan!🤠🏴‍☠️")


#QUIT
else:
 print(" NEVER GIVE UP! 🔰")
