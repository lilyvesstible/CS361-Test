#All static text instructions

def homeExplain():
    print("\n"\
        "Welcome to the Doug’s Deals Grocery Store Item Checklist! Here, you can look at the items we sell, add them to a shopping list, and take it with you on the go!\n" \
        "Below are a list of commands you can perform. Phrases starting with a “>” are commands you can enter, followed by a description of their function.\n\n" \
        
        ">Store Items\n" \
        "Here, you can view the items we have in store, and add them to your shopping list.\n\n" \
        
        ">List Items\n" \
        "Here, you can view your list, delete items, or print your list.\n\n" \
        
        ">Coupons\n" \
        "Here, you can view coupons available to you.\n\n" \
        
        ">Exit\n" \
        "This allows you to exit the program.\n")
    
def storeItemsExplain():
    print("\n"\
        "Here, you can view the items we have in store, and add them to your shopping list. Items are sorted into categories. Inside each category, items and their price will be displayed. Once you add your items, you can look at other categories, or return to the home screen to view your list!\n"\
        "Below are a list of commands you can perform. Phrases starting with a “>” are commands you can enter, followed by a description of their function.\n\n"\
            
        ">Produce\n"\
        "View produce items here.\n\n"\
            
        ">Deli\n"\
        "View deli items here.\n\n"\
            
        ">Frozen Items\n"\
        "View frozen items here.\n\n"\
        
        ">Shelf Items\n"\
        "View shelf items here\n\n"\
        
        ">Home\n"\
        "Return to home page\n"\
    )

def categoryExplain():
    print("\n"\
        "Below are a list of commands you can perform. Phrases starting with a “>” are commands you can enter, followed by a description of their function.\n\n" \

        ">Add Item\n"\
        "This adds an item to your shopping list. Once entered, the program will prompt you to list the item name. Enter the name exactly how it's formatted above. If we have multiple items of that brand, then you can then choose between the various brands. Then, enter the amount you want. If you simply want to enter one of that item, you can press enter without entering an amount.\n\n"\
        
        ">Store Items\n"\
        "Return to the store items page.\n\n"\
        
        ">Home\n"\
        "Return to the home page.\n"
    )

def listExplain():
    print("\n"\
        "Below are a list of commands you can perform. Phrases starting with a “>” are commands you can enter, followed by a description of their function.\n\n"\
        
        ">Remove Item\n" \
        "This removes an item from your list. Once entered, the program will prompt you to list the item name. Enter the name exactly how it's formatted above. Then, enter the amount you want to remove. If you want to remove all items, leave the quantity blank. The program will ask you to confirm, where you will be asked to type “Yes”\n\n"\
        
        ">Print\n"\
        "This exports your list onto a .txt file. From there, you may print this list on a printer.\n\n"\
        
        ">Enter Coupon\n"\
        "This allows you to apply a coupon of your choice to one item. Enter an item, then enter the coupon code. There will then be a discount applied to the item, along with a name change.\n\n"\
        
        ">Home\n"\
        "Return to the home page.\n"
    )

def couponExplain():
    print("\n"\
        "Below are a list of commands you can perform. Phrases starting with a “>” are commands you can enter, followed by a description of their function.\n\n"\
        
        ">Home\n"\
        "Return to the home page.\n"
    )

def locationExplain():
    print("\n"\
        "Before you begin, you must pick a location to shop from:\n\n" \

        "Corvallis Location\n" \
        "Albany Location\n" \
        "Salem Location\n\n" \
        
        "Please type the chosen location below."
    )