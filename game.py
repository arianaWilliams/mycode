import random

rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room'
    },

    'Kitchen': {
        'north': 'Hall',
        'up': 'Up Stairs',
        'item': ['Dragon'],
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'Potion'
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Up Stairs': {
        'down': 'Kitchen',
        'west': 'Bedroom',
        'east': 'Study'
    },
    'Bedroom': {
        'east': 'Up Stairs'
    },
    'Study': {
        'item': 'Book',
        'west': 'Up Stairs'
    }
}

# sight words list
wordsEasy = ["all", "am", "are", "at", "ate", "be", "black", "brown", "but", "came", "did", "do", "eat", "four", "get", "good", "have", "he", "into", "like", "must", "new", "no", "now", "on", "our",
             "out", "please", "pretty", "ran", "ride", "saw", "say", "she", "so", "soon", "that", "there", "they", "this", "too", "under", "want", "was", "well", "went", "what", "white", "who", "will", "with", "yes"]
wordsMedium = ["and",	"can",	"come",	"i",	"in",	"is",	"not", "out",	"said",	"you", "get",	"go",
               "no", "the",	"this",	"up",	"we",	"will",	"yes",	"a", "be",	"big",	"do",	"down",	"how",	"it",	"now"]
wordsHard = ["are",	"easy",	"listen", "second",	"make",	"enough", "about",
             "float",	"found", "usually", "another",	"first", "many", "said",	"girl"]
# riddles
riddles = {
    "Q: Give me a drink, and I will die. Feed me, and I'll get bigger. What am I?":
        "fire",
    "Q: What word begins with E and ends with E, but only has one letter?":
        "envelope",
    "Q: What appears once in a minute, twice in a moment, but not once in a thousand years?":
        "the letter m",
    "Q: What has many rings but no fingers?":
        "telephone",
    "Q: What goes up but never comes back down?":
        "your age",
    "Q: I go all around the world, but never leave the corner. What am I?":
        "stamp",
    "Q: If you drop a yellow hat in the Red Sea, what does it become?":
        "wet",
    "Q: I’m always on the dinner table, but you don’t get to eat me. What am I?":
        "plates and silverware",
    "Q: What goes in a birdbath but never gets wet?":
        "the bird's shadow",
    "Q: What two things can you never eat for breakfast?":
        "lunch and dinner",
    "Q: If you drop me, I’m sure to crack, but smile at me and I’ll smile back. What am I?":
        "mirror",
    "Q: What has hands and a face, but can’t hold anything or smile?":
        "clock",
    "Q: You’ll find me in Mercury, Earth, Mars and Jupiter, but not in Venus or Neptune. What am I?":
        "the letter r",
    "Q: I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?":
        "your breath",
    "Q: I have cities, but no houses. I have forests, but no trees. I have water, but no fish. What am I?":
        "map",
    "Q: What can you break, even if you never pick it up or touch it?":
        "promise",
    "Q: What is yours but mostly used by others?":
        "your name",
    "Q: Which question can you never answer 'yes' to?":
        "are you asleep",
    "Q: What's something that, the more you take, the more you leave behind?":
        "footsteps"
}


def objective1():
    # print the objective to the screen
    print('$$$ OBJECTIVE 1 $$$')
    print('find the key and add it to your inventory')


def objective2(player):
    print('=========HORRAY=============')
    print('you got the key')
    print('$$$ OBJECTIVE 2 $$$')
    print('destroy the garden gnome to reveal the dugeon door')
    rooms['Garden']['item'] = ['Gnome', 'Dragon']
    rooms['Hall']['item'] = ['Wand']
    rooms['Dining Room']['item'] = ['Dragon']
    rooms['Up Stairs']['item'] = ['Dragon']
    player['inventory'].remove('Key')
    player['inventory'].append('Dungeon_key')


def objective3(player):
    print('=========HORRAY=============')
    print('you destroyed the garden gnome')
    print('$$$ OBJECTIVE 3 $$$')
    print('destroy the boss')
    addRoom('Dungeon Stairs', {
            'east': 'Hall',
            'item': ['lock']
            })
    rooms['Hall']["west"] = "Dungeon Stairs"


class Creature:
    def __init__(self, name, strength):
        self.name = name
        self.stregnth = strength

    def attack(self):
        print(f"{self.name} is attacking...")


class Dragon(Creature):
    def attack(self, dragon_strength, currentRoom, dragon_defeated, book, player):
        player['dragon_defeated']
        counter = player['counter']
        print(f"The dragon's strength is: {dragon_strength}")
        print("--If you have a wand in your inventory, you can use it--")
        print("To use the wand, type 'use wand'")
        max = len(wordsEasy) - 1
        word_index = random.randint(0, max)
        word = wordsEasy[word_index]
        print("You need to spell the word: " + word + '\n')
        spelling = input().lower().strip()
        if player['health'] <= 0:
            return
        elif spelling == "use wand":
            useWand(word, counter, currentRoom, player)
        else:
            matching_count = matchingWords(word, spelling)
            word_length = len(word)
            if spelling == word:
                rooms[currentRoom]['item'].remove('Dragon')
                print("You defeated the Dragon")
                player['dragon_defeated'] += 1
                addRoom('Bathroom', {
                    'south': 'Bedroom',
                    'item': ['Griffin', 'extra_strength']
                })
                rooms["Bedroom"]["north"] = "Bathroom"
            elif matching_count >= word_length / 2:
                player['health'] -= (dragon_strength * 10) / 2
                print(
                    f"Oh no, you took half damage! Your health is now: {player['health']}")
                book.append(word)
                print(
                    "You have to defeat the dragon or get the book before you can get the key")
            elif matching_count < word_length / 2:
                player['health'] -= (dragon_strength * 10)
                print(
                    f"NOOO... you took full damage! Your health is now: {player['health']}")
                book.append(word)
                print(
                    "You have to defeat the dragon or get the book before you can get the key")


class Griffin(Creature):
    def attack(self, griffin_strength, currentRoom, player):
        # griffin strength will be higher than the first creature
        griffin_health = 100
        print('fight the griffin her strength is: ' +
              str(griffin_strength) + '0')
        print('it will take more than one word to defeat this griffin')
        print('you can type run if you want to run away')
        print('ready..........')
        print('set.............')
        print('fight............')
        # get a random index from wordsEasy
        while griffin_health > 0:
            if player['health'] <= 0:
                print("you died............")
                return
            max = len(wordsMedium) - 1
            word_index = random.randint(0, max)
            # using the random int from above get a random from word list 2
            word = wordsMedium[word_index]
            print("you need to spell the word: " + word + '\n')
            spelling = input().lower().strip()
            # call the matchingWords function to count how many letters match
            matching_count = matchingWords(word, spelling)
            word_length = len(word)

            # allow the user to excape
            if spelling == 'run':
                print('you are running away find a potion to heal yourself')
                rooms['Hall']['item'] = ['Potion']
                return True
            # if spelling matches damage the dragon it will take more than one correct work to beat the dragon
            if spelling == word:
                griffin_health -= (word_length*10)
                print(
                    f"GREAT WORK you damaged the griffin her health is {griffin_health}")
            # if the user got half of the letters correct they take half damage and dragon remains in that room
            elif matching_count >= word_length/2:
                # decrease the health bar by half the dragons strength
                player['health'] -= (griffin_strength+10)/2
                print(
                    f"Oh no you took half damage your health is now: {player['health'] }")
            # if the user got less than half the letters correct they take full damage
            elif matching_count < word_length/2:
                # decrease the strength by full dragon_strength
                player['health'] -= (griffin_strength*10)
                print(
                    f"NOOO... you took full damage your health is now: {player['health'] }")
        if griffin_health <= 0:
            print("AWSOME YOU DEFEATED THE GRIFFIN")
            rooms[currentRoom]['item'].remove('Griffin')
            rooms[currentRoom]['item'].remove('extra_strength')
            print("get the key to complete objective 1")
            rooms[currentRoom]['item'].append('Key')
            show_status(player)
            return False


class Gnome(Creature):
    def attack(self, currentRoom, player):
        get_gnome = False
        while get_gnome == False:
            random_riddle = random.choice(list(riddles.keys()))
            answer = riddles[random_riddle].lower()
            print("############################################")
            print("Destroy the gnome to reveal the dungeon door")
            print("To destroy the gnome solve the riddle.....")
            print(random_riddle)
            riddle_answer = input().lower().strip()
            if answer == riddle_answer:
                print("You destroyed the gnome")
                get_gnome = True
                rooms[currentRoom]['item'].remove('Gnome')
                objective3(player)
            else:
                print("Try another riddle")


class Sphinx(Creature):
    def attack(self, currentRoom, player, sphinx_strength):
        sphinx_health = 100
        while True:
            if player['health'] <= 0:
                return
            random_riddle = random.choice(list(riddles.keys()))
            answer = riddles[random_riddle].lower()
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Defeat the sphinx to win the game")
            print("_______________________________________________")
            print(random_riddle)
            riddle_answer = input().lower().strip()
            if answer == riddle_answer:
                sphinx_health -= 10
                print(
                    f"You weakened the sphinx his strength is {sphinx_strength}")
                while sphinx_health > 0:
                    max = len(wordsHard) - 1
                    word_index = random.randint(0, max)
                    # using the random int from above get a random from word list 3
                    word = wordsHard[word_index]
                    print("you need to spell the word: " + word + '\n')
                    spelling = input().lower().strip()
                    # call the matchingWords function to count how many letters match
                    matching_count = matchingWords(word, spelling)
                    word_length = len(word)
                    # if spelling matches damage the sphinx it will take more than one correct work to beat the sphinx
                    if spelling == word:
                        sphinx_health -= (word_length*10)
                        print(
                            f"GREAT WORK you damaged the sphinx his health is {sphinx_health}")
                    # if the user got half of the letters correct they take half damage and sphinx remains in that room
                    elif matching_count >= word_length/2:
                        # decrease the health bar by half the dragons strength
                        player['health'] -= (sphinx_strength+10)/2
                        print(
                            f"Oh no you took half damage your health is now: {player['health'] }")
                    # if the user got less than half the letters correct they take full damage
                    elif matching_count < word_length/2:
                        # decrease the strength by full dragon_strength
                        player['health'] -= (sphinx_strength*10)
                        print(
                            f"NOOO... you took full damage your health is now: {player['health'] }")
                else:
                    print("Try another riddle")
            if sphinx_health <= 0:
                rooms[currentRoom]['item'].remove('Sphinx')
                print("AWSOME YOU DEFEATED THE SPHINX")
                player['inventory'].append('TROPHY')
                return


def show_instructions():
    """Show the game instructions"""
    # Print the game instructions
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      map ['m']
      use [item]
      instructions  ['i']
      status ['s']
    ''')
    print('''
    To win the game defeat
    the boss dragon
    in the final room located in the dungeon
    ''')
    print('''
    along the way you will spell different sight words
    if you spell them incorrect you will take damage!
    ''')
    print('''
    There are several power ups
    so be on the look out
    ''')


def show_status(player):
    """Print the player's current status"""
    print('---------------------------')
    print(f"You are in the {player['current_room']}")
    # print what the player is carrying
    print('Inventory:', player['inventory'])
    # print how many dragons the player has killed
    print('Dragons slayed: ', player['dragon_defeated'])
    # check if there's an item in the room, if so print it
    print('Health bar', player['health'])

    if "item" in rooms[player['current_room']]:
        item = rooms[player['current_room']]['item']
        if isinstance(item, list):
            print('You see the following items:', ', '.join(item))
        else:
            print('You see a ' + item)
    print("---------------------------")

# function to show a map


def show_map(player):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    # print the current room
    print('From the ', player['current_room'])
    # show each direction you can go from the current room
    for direction, room in rooms[player['current_room']].items():
        if direction != "item":
            print('go ', direction, ' to get to ' + room)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def go(player, input_command):
    """Move the player to a new room"""
    currentRoom = player['current_room']

    command_parts = input_command.lower().split(" ", 1)
    command = command_parts[0]

    if command == 'go':
        if len(command_parts) > 1:
            direction = command_parts[1]
            if direction in rooms[currentRoom]:
                # Set the current room to the new room
                player['current_room'] = rooms[currentRoom][direction]
                currentRoom = player['current_room']
                print("You are in the", currentRoom)
                print("=======================================")
                if "item" in rooms[currentRoom]:
                    item = rooms[currentRoom]['item']
                    if type(item) is list:
                        print('You see the following items:', ', '.join(item))
                        print("--------------------------------------")
                    else:
                        print("You see a", item)
                        print("--------------------------------------")
            else:
                print("You can't go that way.")
        else:
            print('Please provide a direction after "go".')
    else:
        print('Invalid command!')

    return player


def get(player, item):
    currentRoom = player['current_room']

    if "item" in rooms[currentRoom]:
        room_items = rooms[currentRoom]['item']
        if isinstance(room_items, list) and item in room_items:
            # add the item to their inventory
            player['inventory'].append(item)
            # display a helpful message
            print(f"CONGRADULATION you got the {item}!")
            # delete the item key:value pair from the room's dictionary
            room_items.remove(item)
        elif room_items == item:
            player['inventory'].append(item)
            del rooms[currentRoom]['item']
            print(f"CONGRADULATIONS you got the {item}!")
    # if there's no item in the room or the item doesn't match
    else:
        # tell them they can't get it
        print('Can\'t get ' + item + '!')
    return player


def use(player, item):
    """Use an item from the player's inventory"""
    if item == 'Potion':
        usePotion(player, item)
    elif item == 'Book':
        useBook(player, item)
    elif item == 'Wand':
        useWand(player, item)
    elif item == 'Dungeon_key':
        useKey(player, item)
    else:
        print("That item is not available")


def usePotion(player, item):
    health = player['health']
    inventory = player['inventory']
    # increase the health if potion can be used
    if 'Potion' in inventory:
        if health <= 90:
            player['health'] += 10
            # remove the potion from the inventory
            inventory.remove('Potion')
            # display a helpful message
            print('Potion used!')
        else:
            # print helpful message
            print(f"You are too healthy to use the {item}")
    else:
        print(f"You don't have a {item} in your inventory.")


def useBook(player, item):
    inventory = player['inventory']
    book = player['book']

    # check if the book is in the inventory
    if 'Book' in inventory:
        while True:
            # Iterate ove the book to get the words
            for word in book:
                # the player must spell the words to practice
                practice = input("Spell: " + word + " ")
                # if the player spells the word correctly
                if practice == word:
                    # remove the word from the book
                    book.remove(word)
                else:
                    print("Incorrect spelling. Try again.")
            if len(book) == 0:
                print("You spelled all the words correcly. Now you can get the key.")
                # Add the bathroom with a dragon and key as items dynamically
                addRoom('Bathroom', {
                    'south': 'Bedroom',
                    'item': ['Griffin', 'extra_strength']
                })
                rooms["Bedroom"]["north"] = "Bathroom"
                break
    else:
        print("You don\'t have a book in your inventory.")

# function to add a room dynamically


def addRoom(room_name, room_properties):
    rooms[room_name] = room_properties


def matchingWords(word, user_input):
    count = 0
    for i in range(len(word)):
        if i < len(user_input) and word[i] == user_input[i]:
            count += 1
    return count


def useWand(word, counter, currentRoom, player):
    # if the  wand is in the plaayer inventory
    if 'Wand' in player['inventory']:
     # runs only if the counter is less than 4
        if counter < 4:
           # make sure the word is more than 1 character
            if len(word) > 1:
                rooms[currentRoom]['item'].remove('Dragon')
                print("You defeated the Dragon")
                # increase the dragon_defeated counter by 1
                player['dragon_defeated'] += 1
                # increment the counter
                counter += 1
        else:
            player['inventory'].remove('Wand')
    else:
        print("The wand is not in your inventory")
        print("any character to start fighting the dragon again")
    return counter


def useKey(player, item):
    if 'Dungeon_key' in player['inventory']:
        print("You unlocked the dungeon....")
        addRoom('Dungeon', {
            'up': 'Dungeon Stairs',
            'item': ['Sphinx']
        })
        rooms['Dungeon Stairs']["down"] = "Dungeon"
        player['inventory'].remove('Dungeon_key')
        del rooms[player['current_room']]['item']
    else:
        print("You can\'t use the dungeon key")


def main():
    # Initialize the player object and set the starting room
    player = {
        'current_room': 'Hall',
        'inventory': ['map'],
        'health': 100,
        'counter': 0,
        'dragon_defeated': 0,
        'book': []
    }

    show_instructions()
    objective1()
    show_status(player)

    while player['health'] > 0:

        # Get user input
        command = input("> ").lower()
        command_parts = command.split(" ", 1)
        action = command_parts[0]

        if action == 'go':
           # direction = command_parts[1]
            go(player, command)
        elif action == 'get':
            item = command_parts[1].capitalize()
            get(player, item)
        elif action == 'use':
            item = command_parts[1].capitalize()
            use(player, item)
        elif action == 'i':
            show_instructions()
        elif action == 's':
            show_status(player)
        elif action == 'm':
            show_map(player)
        else:
            print("Invalid command. Type 'i' for instructions.")

            # if the player enters the room with the book
        if 'item' in rooms[player['current_room']] and 'Book' in rooms[player['current_room']]['item']:
            print("get the book if you didn't defeat the dragon in the kitchen")

        # if player enters a room with a lock
        if 'item' in rooms[player['current_room']] and 'lock' in rooms[player['current_room']]['item']:
            print("use the \'dungeon_key' to unlock the dungeon")

        # handle dragon
        if 'item' in rooms[player['current_room']] and 'Dragon' in rooms[player['current_room']]['item']:
            dragonDefeated = player['dragon_defeated']
            currentRoom = player['current_room']
            health = player['health']
            book = player['book']
            dragon_strength = random.randint(1, 5)
            dragon = Dragon("Dragon", dragon_strength)
            dragon.attack(dragon_strength, currentRoom,
                          dragonDefeated, book, player)

        # handle Griffin
        if 'item' in rooms[player['current_room']] and 'Griffin' in rooms[player['current_room']]['item']:
            griffin_strength = random.randint(5, 7)
            currentRoom = player['current_room']
            health = player['health']
            griffin = Griffin("Griffin", griffin_strength)
            escaped = griffin.attack(griffin_strength, currentRoom, player)
            if escaped:
                player['current_room'] = 'Bedroom'
                rooms['Hall']['item'] = ['Potion']

        # handle Gnome
        if 'item' in rooms[player['current_room']] and 'Gnome' in rooms[player['current_room']]['item']:
            currentRoom = player['current_room']
            gnome = Gnome("Gnome", 0)
            gnome.attack(currentRoom, player)

        # handle Sphinx
        if 'item' in rooms[player['current_room']] and 'Sphinx' in rooms[player['current_room']]['item']:
            sphinx_strength = random.randint(7, 10)
            currentRoom = player['current_room']
            sphinx = Sphinx("Sphinx", sphinx_strength)
            sphinx.attack(currentRoom, player, sphinx_strength)

        if 'Key' in player['inventory']:
            objective2(player)

        if 'Gnome' in player['inventory']:
            objective3(player)

        if 'TROPHY' in player['inventory']:
            break

    if player['health'] <= 0:
        print("You died............")
    else:
        print("%%%%%%%%%%%  YOU WIN %%%%%%%%%%%%")


if __name__ == "__main__":
    main()
