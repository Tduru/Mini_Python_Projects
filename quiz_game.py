print("Welcome to my computer")
score = 0

playing = input("Would you like to play?(yes/no): ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("What does RAM stand for? ").lower()
if answer == "Random Access Memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does ROM stand for? ").lower()
if answer == "Read Only Memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
print("You got " + str(score) + " questions correct.")
print("You got " + str((score/4) * 100) + "%")

    
