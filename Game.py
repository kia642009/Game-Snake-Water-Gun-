import random  # install Random 
my_list=["Snake","Water","Gun"]

computer=random.choice(my_list)

print("Snake\nWater\nGun")

user=input("Enter your choice:")


if(user=="Snake " and computer=="Water"):
    print("Snake Win and also You Win")

elif(user=="Water" and computer=="Gun"):
    print("Water Win and also you Win")

elif(user=="Gun" and computer=="Water"):
    print("Water defated and you Lose")

elif(user=="Water" and computer=="Snake"):
    print("Snake drink water and you lose")

elif(user=="Snake" and computer=="Gun"):
    print("Snake Was kill by gun and you Lose")

elif(user=="Gun" and computer=="Snake"):
    print("gun kill Snake and also You win")

elif(user=="Snake" and computer=="Water"):
    print("Snake drink water and you won")

elif(user=="Water" and computer=="Water"):
    print("Tie")

elif(user=="Snake" and computer=="Snake"):
    print("Tie")

elif(user=="Gun" and computer=="Gun"):
    print("Tie")