#---------------------------------
# List Refresher
# Sydney Loerzel
# Dec 30, 2019
#---------------------------------

bts = ["Jin", "Yoongi", "Hoseok", "Namjoon", "Jimin", "Taehyung", "Jungkook"]
superm = ["Mark", "Taeyong", "Taemin", "Baekhyun", "Lucas", "Kai", "Ten"]
fruit = ["Apple", "Carrot", "Orange"]

def list_one():
    choice = input("Do you want list 1 (1) or do you want to create a list(2)") #Type your choice 1 or 2
    if choice == "1":
        one = input("You chose a list. Would you like to list BTS (a) or SuperM (b)?") #Type choice a or b
        if one == "a":
            print("You chose BTS!")
            print(bts)
        elif one == "b":
            print("You chose SuperM")
            print(superm)
    elif choice == "2":
        print("You chose to create your own list")
        inventory = [ ] #Creates an empty inventory
        inventory.append(input("Pick an item to list")) #Pick an item to go at the end
        inventory.append(input("Add another item")) #Adds new item to the end
        inventory.append(input("Safe keeping might as well add another"))
        inventory.append(input("Last one"))
        print(inventory)
        
def list_two():
    print("How about we look at a list of fruit")
    print(fruit)
    print("Wait a minute. Something doesn't fit here.. Lets just get rid of that")
    option = input("If we start counting at 0. (0,1,2,3...) What number is the wrong one in?") #Type 0,1,2
    if option == "1":
        print("Correct!")
        fruit.remove("Carrot")
        print(fruit)
    elif option == "0":
        print("That's not right, Carrots may look like it's in the fourth spot")
        print("But if you start at 0. Its in the third")
        print("lets just remove it now")
        fruit.remove("Carrot")
    elif option == "2":
        print("That's not right, Carrots may look like it's in the fourth spot")
        print("But if you start at 0. Its in the third")
        print("lets just remove it now")
        fruit.remove("Carrot")
    print("I want to add watermelon but I want it to be first")
    fruit.insert(0, "Watermelon") #Adds watermelon into postion 0
    print(fruit)
    print("Lets look at the fruit list differently")
    fruit.reverse() #reverses the order the list is in
    print(fruit)
    fruit.sort() #sorts the list
    print(fruit)

def list_three():
    print("Lets take a look at the BTS list you may have used first")
    print(bts)
    print("So what if you are too lazy to count the names. How many members are there?")
    print(len(bts)) #prints the length of the list
    print("Thats how many members are in BTS")
    print("The BTS list is in order from oldest to youngest")
    print("Lets see who the three youngest are")
    print(bts[4:]) #returns the items in position 4 until the end
    print("Lets look at them 'listed' in a different way")
    for member in bts: #Lists the items one at a time
        print(member)
    print("Lets see who the '3rd' member is according to the 0, 1, 2 count")
    print(bts[3]) #Returns the item in the '3' spot
    print("Where is Yoongi is on the list")
    spot = bts.index("Yoongi") #returns the position of item named
    print("Yoongi is in the", spot, "spot")
    
def main():
    list_one()
    print("Lets look at a new list!")
    list_two()
    print("Now at the last thing")
    list_three()
    
main() #runs the actual code