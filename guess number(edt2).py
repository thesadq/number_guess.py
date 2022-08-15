import random
import math
 

lower = int(input("Enter your lower bound:"))

upper = int(input("Enter your upper bound:"))


random_number = random.randint(lower, upper)

try_chance =round(math.log(upper - lower + 1, 2))
print("you have only", try_chance,"chance to guess")

count = 0
point = 100

while count < try_chance :
    count += 1
    point -= 10
    guess =int(input("Enter your Geuss:"))

    if guess == random_number:
        print("-----------------------------")
        print("congratulations,you did it at",count,"time")
        print("your score is",point)
        break
    
    elif guess < random_number :
        print("your geuss is too low")
    
    elif guess > random_number:
        print("your guess is too high")
        
    
while count >= try_chance:
    count += 1
    if guess == random_number:
        break
    
    elif count >= try_chance:
        print("-----------------------------")
        print("GAME OVER\nthe answer was",random_number)
        break
        
    
   









































