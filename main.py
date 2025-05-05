from textInstructions import *

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
        else:
            print("Sorry, I don't understand. Please type the command again")

def storeItemsPage():
    storeItemsExplain()
    while True:
        i = input()
        
        if i == "Home":
            return
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

def addItem(itemStock):
    itemVal = (0,0)
    print("Which item would you like?")
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
        if itemQuan == "":
            itemList.append(itemVal)
            break
        elif itemQuan.isdigit() == True:
            for i in range(int(itemQuan)):
                itemList.append(itemVal) 
            break
        else:
            print("I'm sorry, but that quantity is invalid. Please try again.")
    return

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
        else:
            print("Sorry, I don't understand. Please type the command again")

def printTermList():
    print("Below is your list of items:\n")
    for i in itemList:
        print("%s: $%.2f" % i)
    print("\nTotal: $%.2f\n" %(updateTotal()))
    listExplain()

def updateTotal():
    listTotal = 0.0
    for i in itemList:
        listTotal += float(i[1])
    return listTotal

def removeItem():
    itemVal = (0,0)
    print("Which item would you like to remove?")
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
    while True:
        itemQuan = input()
        if itemQuan == "":
            while True:
                if itemVal in itemList:
                    itemList.remove(itemVal)
                else:
                    break
            break
        elif itemQuan.isdigit() == True:
            for i in range(int(itemQuan)):
                if itemVal in itemList:
                    itemList.remove(itemVal)
                else:
                    break
            break
        else:
            print("I'm sorry, but that quantity is invalid. Please try again.")
    return

def printFile():
    print("What would you like to call this file?")
    textFileName = input()
    file = open(textFileName + ".txt", "w")
    file.write("List of items to buy:\n")
    for i in itemList:
        file.write(i[0] + ": $" + str(i[1]) + "\n")
    file.write("\nTotal: $%.2f" %(updateTotal()))
    file.close()

produce = []
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

itemList = []

homePage()