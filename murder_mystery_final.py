def instructions():
    print('Murder Mystery Game')
    print('Find 6 items to win, or get caught by the killer!')
    print('Commands: North, South, East, West')
    print('To add to inventory: get \'item name\'')


rooms = {
    'Foyer': {'North': 'Dining Room', 'East': 'Kitchen', 'South': 'Bedroom',
              'West': 'Mudroom'},
    'Dining Room': {'East': 'Balcony', 'South': 'Foyer'},
    'Kitchen': {'North': 'Library', 'West': 'Foyer'},
    'Bedroom': {'East': 'Bathroom', 'North': 'Foyer'},
    'Mudroom': {'East': 'Foyer'},
    'Balcony': {'West': 'Dining Room'},
    'Bathroom': {'West': 'Bedroom'},
}
items = {
    'Dining Room': 'Knife', 'Balcony': 'Security Camera', 'Kitchen':
    'Rubber Gloves', 'Bathroom': 'Toothbrush', 'Bedroom': 'Journal', 'Mudroom':
    'Keys', 'Library': 'Killer'
}

room = 'Foyer'
inventory = []

instructions()

while True:
    print(f'You are in the {room}')
    if room != 'Foyer':
        item = items[room]
        if item == 'Killer':
            print('You found the Killer! Game over.')
            break
        if item not in inventory:
            print(f'You see a {item}')
            grab_item = input('Enter you move: ')
            if grab_item == f'get {item}':
                inventory.append(item)
                print(f'Inventory = {inventory}')
            else:
                while grab_item != f'get {item}':
                    print('Couldn\'t collect item. Try again!')
                    grab_item = input('Enter you move: ')
                inventory.append(item)
                print(f'Inventory = {inventory}')

    if len(inventory) == 6:
        print('You collected all of the items!')
        break
    direction = input('Chose a direction: ').title()
    if direction in rooms[room]:
        room = rooms[room][direction]
    else:
        while direction not in rooms[room]:
            print('Can\'t go that way.')
            direction = input('Enter a different direction: ').title()
        room = rooms[room][direction]







