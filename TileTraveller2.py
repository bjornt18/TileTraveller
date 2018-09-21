#Byrja á því að búa til svæðið sem leikmaðurinn er í, leyfa leikmanninum að færa sig í átt sem hægt er að færa sig í. Setja síðan inn markmiðið, staðinn sem leikmaðurinn þarf að komast til að vinna
def att1(a):
    if position == 1.1:
        att = "(N)orth."
    if position == 1.2:
        att = "(N)orth or (E)ast or (S)outh."
    if position == 1.3:
        att = "(E)ast or (S)outh."
    if position == 2.1:
        att = "(N)orth."
    if position == 2.2:
        att = "(S)outh or (W)est."
    if position == 2.3:
        att = "(E)ast or (W)est."
    if position == 3.1:
        att = "(N)orth."
    if position == 3.2:
        att = "(N)orth or (S)outh."
    if position == 3.3:
        att = "(S)outh or (W)est."
    return att

def position1(p, d):
    if d == "n":
        if p == 1.1 or p == 1.2 or p == 3.2 or p == 2.1:
            p = p + 0.1
        return p
    elif d == "s":
        if p == 1.2 or p == 1.3 or p == 2.2 or p == 3.3 or p == 3.2:
            p = p - 0.1
        return p
    elif d == "w":
        if p == 2.3 or p == 2.2 or p == 3.3:
            p = p - 1
        return p
    elif d == "e":
        if p == 1.2 or p == 1.3 or p == 2.3:
            p = p + 1
        return p
    else:
        return p

position = 1.1
villa = 1
while position != 3.1:
    if villa == 1:
        print("You can travel:", att1(position))
        direction = input("Direction: ").lower()
    else:
        direction = input("Direction: ").lower()
        villa = villa - 1
    if position1(position, direction) == position:
        print("Not a valid direction!")
        villa = villa + 1
    else:
        position = position1(position, direction)
    position = round(position, 1)
print("Victory!")
#Github: https://github.com/bjornt18/TileTraveller
