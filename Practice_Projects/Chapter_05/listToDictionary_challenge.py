#Imagine that a vanquished dragon’s loot is represented as a 
# list of strings like this:
#   dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#Write a function named addToInventory(inventory, addedItems),
# where the inventory parameter is a dictionary representing 
# the player’s inventory (like in the previous project) and the 
# addedItems parameter is a list like dragonLoot. The 
# addToInventory() function should return a dictionary that 
# represents the updated inventory. Note that the addedItems 
# list can contain multiples of the same item. Your code could 
# look something like this:
#   def addToInventory(inventory, addedItems):
#       # your code goes here
#       inv = {'gold coin': 42, 'rope': 1}
#   dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#   inv = addToInventory(inv, dragonLoot)
#   displayInventory(inv)
#The previous program (with your displayInventory() function 
# from the previous project) would output the following:
#   Inventory:
#   45 gold coin
#   1 rope
#   1 ruby
#   1 dagger
#   Total number of items: 48

#stuff = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print("Inventory:")
    
    item_total = 0
    
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v

    print(f'\nTotal number of items: {item_total}')

def addToInventory(inventory, addedItems):

    # Goes through each added item in the list addedItems
    for i in addedItems:
        # If key from addedItems does not exist in inventory, create it
        inventory.setdefault(i, 0)
        # Add 1 to the value of the key
        inventory[i] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)
