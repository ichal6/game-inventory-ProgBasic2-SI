
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the specification.


def display_inventory(inventory):
    '''Display the inventory like this:
    rope: 1
    torch: 6
    '''
    # inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    for key, val in inventory.items():
        print(key, ": ", val, sep="")


def add_to_inventory(inventory, added_items):
    '''Add to the inventory dictionary a list of items from added_items.'''
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def print_table(inventory, order=None):
    '''
    Take your inventory and display it in a well-organized table with
    each column right-justified like this:

    -----------------
    item name | count
    -----------------
         rope |     1
        torch |     6
    -----------------

    The 'order' parameter (string) works as follows:
    - None (by default) means the table is unordered
    - "count,desc" means the table is ordered by count (of items in the
      inventory) in descending order
    - "count,asc" means the table is ordered by count in ascending order
    '''
    length = 0
    for item_name in inventory:
        if len(item_name) > length:
            length = len(item_name)
    # print(length)

    if length < 9:
        length = 9

    list_inventory = []

    for key, value in inventory.items():
        temp = [key, value]
        list_inventory.append(temp)
    format_str = "{:>" + str(length) + "} |{:>6}"
    # print(list_inventory)
    print("-----------------")
    print("item name | count")
    print("-----------------")
    for line in inventory.items():
        # print('{:>9} |{:>6}'.format(*line))
        print(format_str.format(*line))
    print("-----------------")


def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Import new inventory items from a file.

    The filename comes as an argument, but by default it's
    "import_inventory.csv". The import automatically merges items by name.

    The file format is plain text with comma separated values (CSV).
    '''

    pass


def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Export the inventory into a .csv file.

    If the filename argument is None, it creates and overwrites a file
    called "export_inventory.csv".

    The file format is plain text with comma separated values (CSV).
    '''

    pass


inv = {'rope': 1, 'torch': 6}

# display_inventory(inv)

print_table(inv)
