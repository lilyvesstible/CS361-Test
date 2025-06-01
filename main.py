from textInstructions import *
import zmq

#Display home page
#Page navigation works like nested pages. This way, going back a page (ex. store items page to home page) is as simple as ending the page function.
def homePage():
    homeExplain()
    while True:
        i = input()

        if i == "Exit":
            exit()
        elif i == "Store Items":
            storeItemsPage()
            homeExplain()
        elif i == "List Items":
            listPage()
            homeExplain()
        elif i == "Coupons":
            couponPage()
            homeExplain()
        else:
            print("Sorry, I don't understand. Please type the command again")

#Display store page
def storeItemsPage():
    storeItemsExplain()
    while True:
        i = input()
        
        if i == "Home":
            return
        #Categories return a 0 or 1. If 1, this means the command was go to home page, which means also exiting store items page.
        elif i == "Produce":
            if(categoryPage(produce, "produce") == 1):
                return
            storeItemsExplain()
        elif i == "Deli":
            if(categoryPage(deli, "deli") == 1):
                return
            storeItemsExplain()
        elif i == "Frozen Items":
            if(categoryPage(frozen, "frozen") == 1):
                return
            storeItemsExplain()
        elif i == "Shelf Items":
            if(categoryPage(shelf, "shelf") == 1):
                return
            storeItemsExplain()
        else:
            print("Sorry, I don't understand. Please type the command again")

#Display category page. Same page for each category, but changes which category based on input
def categoryPage(cat, catName):
    print("\nBelow is a list of " + catName + " items:\n")
    for i in cat:
        print("%s: $%s" % i)
    categoryExplain()
    while True:
        i = input()

        if i == "Store Items":
            return 0
        elif i == "Home":
            return 1
        elif i == "Add Item":
            addItem(cat)
            print("\nBelow is a list of produce items:\n")
            for i in cat:
                print("%s: $%.2f" % i)
            categoryExplain()
        else:
            print("Sorry, I don't understand. Please type the command again")

#Add an item to your list. Input: Desired category. Output: Updated list
def addItem(itemStock):
    #Tracks the tuple of the chosen item
    itemVal = (0,0)
    print("Which item would you like?")
    #Gathers name of product, and searches through given category for item.
    while True:
        itemName = input()
        for i in itemStock:
            if i[0] == itemName:
                itemVal = i
                break
        if itemVal != (0,0):
            break
        print("I'm sorry, that name doesn't match an item in our list. Please try again.")
    
    print("How many do you want?")
    while True:
        itemQuan = input()
        #If quantity is empty, assume to add only one item
        if itemQuan == "":
            print("Adding item...\n")
            itemList.append(itemVal)
            break
        #Check if the input is iterable, then add the item that many times.
        elif itemQuan.isdigit() == True:
            print("Adding items...\n")
            for i in range(int(itemQuan)):
                itemList.append(itemVal) 
            break
        else:
            print("I'm sorry, but that quantity is invalid. Please try again.")
    return

#Display list page
def listPage():
    printTermList()
    while True:
        i = input()
        if i == "Home":
            return
        elif i == "Remove Item":
            removeItem()
            printTermList()
        elif i == "Print":
            printFile()
            printTermList()
        elif i == "Enter Coupon":
            applyCoupon()
            printTermList()
        else:
            print("Sorry, I don't understand. Please type the command again")

#Prints your list, along with the commands for this page.
def printTermList():
    print("Below is your list of items:\n")
    for i in itemList:
        print("%s: $%.2f" % i)
    print("\nTotal: $%.2f\n" %(updateTotal()))
    listExplain()

#Gives the total cost of your list. Input: item list. Output: total cost of list
def updateTotal():
    listTotal = 0.0
    for i in itemList:
        listTotal += float(i[1])
    return listTotal

#Removes an item from your list.
def removeItem():
    #itemVal is chosen item as a tuple
    itemVal = (0,0)
    print("Which item would you like to remove?")
    #Gathers a name, and checks the list for any items with that name.
    while True:
        itemName = input()
        for i in itemList:
            if i[0] == itemName:
                itemVal = i
                break
        if itemVal != (0,0):
            break
        print("I'm sorry, that name doesn't match an item in our list. Please try again.")

    print("How many do you want to remove?")
    #Asks how many you want to remove
    while True:
        itemQuan = input()
        #If input is empty, assume you want to remove all of that item. Check an additional time for confirmation
        if itemQuan == "":
            print("Are you sure you want to delete all instances of this item? Type 'Yes' to confirm")
            check = input()
            if check == "Yes":
                print("Understood, deleting all items...\n")
                #Continue to remove that item until there is no more
                while True:
                    if itemVal in itemList:
                        itemList.remove(itemVal)
                    else:
                        break
            else:
                print("You did not type 'Yes'. Going back to your list...\n")
            break
        #Checks if itemQuan is iterable. If so, check if the item exists in the list, and if so remove it. 
        elif itemQuan.isdigit() == True:
            print("Deleting items...\n")
            for i in range(int(itemQuan)):
                if itemVal in itemList:
                    itemList.remove(itemVal)
                else:
                    break
            break
        else:
            print("I'm sorry, but that quantity is invalid. Please try again.")
    return

#Prints to a text file
def printFile():
    print("What would you like to call this file?")
    textFileName = input()
    print("Printing file...\n")
    file = open(textFileName + ".txt", "w")
    file.write("List of items to buy:\n")
    for i in itemList:
        file.write(i[0] + ": $" + str(i[1]) + "\n")
    file.write("\nTotal: $%.2f" %(updateTotal()))
    file.close()

def applyCoupon():
    itemVal = (0,0)
    print("Which item would you like to discount?")
    while True:
        itemName = input()
        for i in itemList:
            if i[0] == itemName:
                itemVal = i
                break
        if itemVal != (0,0):
            break
        print("I'm sorry, that name doesn't match an item in our list. Please try again.")

    print("Enter the coupon code")
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        coupon = input()
        socket.send_string("%s, %s" %(coupon, itemVal[1]))
        message = socket.recv()
        decode = message.decode()
        if decode == "Code Not Found":
            print("I'm sorry, that doesn't match a valid coupon code. Please try again.")
        else:
            itemList.remove(itemVal)
            itemList.append(("%s [DISCOUNTED]" % itemVal[0], float(decode)))
            break


def couponPage():
    print("\nBelow is a list of coupons, with their code and discount amount. Apply the code when viewing your items!\n")

    file = open("../couponList.txt", "r")
    for i in file.readlines():
        tmp = i.split(", ")
        print("%s: %s, %d%%" %(tmp[0], tmp[1], float(tmp[2])))
    file.close()
    couponExplain()

    while True:
        i = input()
        if i == "Home":
            return
        else:
            print("Sorry, I don't understand. Please type the command again")

#produce, deli, frozen, and shelf are lists that store the data of each item in that category. 
#Each item is stored as a tuple: The first element is the item name, and the second element is the item price
produce = []
#Reads the data from text files that store data for each category. Adds each line as a separate element in the list, and splits the data by a "," to signify the difference between name and price. All categories work the same.
file = open("produceList.txt", "r")
for i in file.readlines():
    tmp = i.split(",")
    produce.append((tmp[0], float(tmp[1])))
file.close()

deli = []
file = open("deliList.txt", "r")
for i in file.readlines():
    tmp = i.split(",")
    deli.append((tmp[0], float(tmp[1])))
file.close()

frozen = []
file = open("frozenList.txt", "r")
for i in file.readlines():
    tmp = i.split(",")
    frozen.append((tmp[0], float(tmp[1])))
file.close()

shelf = []
file = open("shelfList.txt", "r")
for i in file.readlines():
    tmp = i.split(",")
    shelf.append((tmp[0], float(tmp[1])))
file.close()

#itemList contains your list of items to purchase.
itemList = []

homePage()