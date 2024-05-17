print("Welcome to my Computer quiz!")
playing = input("Do you want to play?")
# "Name:"

# text = "Tim IS GReat!"
# print(text.lower())

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score +=1
else:
    print("Incoorect!")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Incoorect!")

answer = input("What does PSU stand for?")
if answer.lower() == "power supply":
    print("Correct!")
    score +=1
else:
    print("Incoorect!")
print("You got" +str(score) + " question correct!")
print("You got" +str((score /4)*100) + "%")