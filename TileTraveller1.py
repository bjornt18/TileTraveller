#Byrja á því að búa til svæðið sem leikmaðurinn er í, leyfa leikmanninum að færa sig í átt sem hægt er að færa sig í. Setja síðan inn markmiðið, staðinn sem leikmaðurinn þarf að komast til að vinna
position = 1.1
att = "(N)orth"
while position != 3.1:
    position = round(position, 1)
    print("You can travel:", att, position)
    direction = input("Direction: ")
    if direction == "n":
        position = position + 0.1
    elif direction == "s":
        position = position - 0.1
    elif direction == "w":
        position = position - 1
    elif direction == "e":
        position = position + 1
    else:
        print("Not a valid direction!")
    if position == 1.1:
        att = "(N)orth"
    if position == 1.2:
        att = "(N)orth or (E)ast or (S)outh"
    if position == 1.3:
        att = "(E)ast or (S)outh"
    if position == 2.1:
        att = "(N)orth"
    if position == 2.2:
        att = "(W)est or (S)outh"
    if position == 2.3:
        att = "(E)ast or (W)est"
    if position == 3.1:
        att = "(N)orth"
    if position == 3.2:
        att = "(N)orth or (S)outh"
    if position == 3.3:
        att = "(W)est or (S)outh"
    print(att)
print("Victory!")
