# write your code here
# PART 1
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30.0
    elif court_type == "outdoor":
        return 20.0
    else:
        return False

# PART 2
def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100.0
    elif racket_brand == "Nox":
        return 140.0
    elif racket_brand == "Siux":
        return 200.0
    else:
        return False
 # PART 3
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2.0
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5.0
    else:
        return False
    
# PART 4

def padel_game_cost():
    padel_court = input(" enter the court type: ")
    brand = input("enter the racket brand: ")
    balls = int(input("enter the number of ball boxes: ") )
    total = padel_balls_cost(balls) + rackets_cost(brand) + padel_court_cost(padel_court)
    return total
print(padel_game_cost())







'''court cost = {padel_court_cost(padel_court)}
                racket cost = {rackets_cost(brand)}
                 balls cost = {padel_balls_cost(balls)}
                 total = '''


    


        
