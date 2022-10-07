#this is a game for options

print("Welcome to my first Game!")
u_name = input("What is your name ? ")
u_age = int(input("What is your age ? "))

if u_age>18:
    print("You are old enough to play!")
else:
    print("You are too young for this game , come back next year")

play = input("Do you want to play ? type 'Yes' or 'No' ")
if play.islower()=="Yes":
    print("You are starting with 10 Health")
    print("Let's Play!")

u_choice = input("First Choice... Left or Right (left/right)? ")
if u_choice=="left":
    acc_arr = input("Nice, you follow the path and reach a lake... Do you want to swim across or go around (across/around)? ")
    if acc_arr=="across":
        print("You managed to swim across but were bit by a fish and lost 5 health. ")
        riv_house = input("You Notice a House and a river , what do you choose (house/river) ? ")
        if riv_house=="river":
            print("You fell in the river and lost ...")
        elif riv_house=="house":
            print("You reached the destination, You win")

if u_choice=="right":
    print("You fell down and lost !!!")

