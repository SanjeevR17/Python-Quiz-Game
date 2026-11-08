print("Welcome to my quiz")

playing = input("Are you willing to play this game?(yes/no): ")

if playing.lower().strip() != "yes":
    quit()

print("Okay! lets play :)")   

score = 0

# question 1 
answer = input("What does CPU stand for?: ")

if answer.lower().strip() == "central processing unit":
    print("Correct")
    score += 1 
else:
    print("incorrect!")   

# question 2
answer = input("What does GPU stand for?: ")

if answer.lower().strip() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect!")

# question 3
answer = input("What does RAM stand for?: ")

if answer.lower().strip() == "random access memory":
    print("Correct")
    score += 1
else:
    print("incorrect!")


# question 4
answer = input("What does PSU stand for?: ")

if answer.lower().strip() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("incorrect!")     

    # question 5
answer = input("What does ROM stand for?: ")

if answer.lower().strip() == "read only memory":
    print("Correct")
    score += 1
else:
    print("incorrect!")      

    # question 6
answer = input("What does USB stand for?: ")

if answer.lower().strip() == "universal serial bus":
    print("Correct")
    score += 1
else:
    print("incorrect!")  

    # question 7
answer = input("What does SSD stand for?: ")

if answer.lower().strip() == "solid state drive":
    print("Correct")
    score += 1
else:
    print("incorrect!")  

    # question 8
answer = input("What does WWW stand for?: ")

if answer.lower().strip() == "world wide web":
    print("Correct")
    score += 1
else:
    print("incorrect!")          


print(f"your score is {score} out of 8 questions")
print(f"your percentage is {score/8 * 100}%")


