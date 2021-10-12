description = """
# Text Based Adventure Jam (Devin McIntyre, 2021-10-12 12:28)

Our goal is two-fold:
​
1) Create a text based adventure game engine that can parse a standard file format
2) Create a text based adventure game using the standardized file format
​
We'll be looking to implement a very, very basic engine that includes support for rooms, items, doors, commands, and effects, as well as an inventory system.
​
## What you need to build
Provided below is a definition for a text based adventure game configuration.  The configuration contains a list of items, the commands they take, the effects they can have, the rooms that hold them, the doors that connect those rooms, the starting position and the final room.  Your goal is to build an engine that can parse this defintion, and any definition matching the standard, into a playable text based adventure game.
​
The basics of the game are as follows:
​
1) Players always start in the room defined by `startingRoomId`.
2) Players have an inventory of infinite size and space, which they can fill with items.
    - Items that are used for a task can be used ONLY ONCE.  After use they should be removed from a players inventory
3) Players can interact with the world by use of text commands.  
    - The expected commands are
      OK- LOOK
        - TAKE
        - READ
        - USE $A ON $B
      OK- GO $DIRECTION
      OK- INVENTORY
    - What these commands should do is outlined below
4) Using commands on items can produce effects
    - Expected effects are
        - UNLOCK_DOOR
        - LOCK_DOOR
        - CHANGE_ITEM_TEXT
    - What these effects should do is outlined below
5) A player's goal is to arrive at the room defined with the `endingRoomId` property
​
​
# File Format Breakdown
​
## Commands:
Commands are the building block of a users interaction with the world.  Users issue commands with or without targets, and are given feedback resulting from the command.  These are verbs, specifying an action, such as "GO", "READ" and "TAKE".
​
### Command structure
```
{
    "command" : string,
    "text" : string,
    "acceptedItems" : [
        {
            "itemId" : string,
            "text" : string,
            "effectIds" : string[]
        }
    ]
}
```
​
### Commands to implement:
**LOOK** - displays the text of the LOOK command for the specified object.  Valid objects are any visible objects in a room, and any object in a users inventory.  If no object given, instead display text of the current room, along with any doors and visible items.
- Use
    - Looking at an item : "LOOK book"
    - Looking at a room : "LOOK"
​
**TAKE** - adds item to inventory if available, hides item when looking at the room.  If no item provided, prompt for an item.  If item provided is invalid, display error message
- Use
    - Specifying no item: "TAKE"
    - Specifying item : "TAKE pizza box"
​
**READ** - displays the text of the READ command for the specified object.  If no object is given, prompt for an object.  If object is invalid, or object lacks read command, display error message
- Use
    - Specifying object : "READ cheese"
​
**USE $A ON $B** - Takes two objects and applies any effects if the object $A is allowed to be used on the object $B.  If objects are missing or the combination is invalid, display error message
- Use
    - Specifying objects : "USE book ON book shelf"
​
**GO $DIRECTION** - Attempts to move the player to the next room in the direction they specify.  If a door exists in the direction, and the door is unlocked, the player is moved to the next room.  If the door exists but is locked, display an error message about the doors status.  If the door doesn't exist, display an error message.
- Use
    - Specifying a direction : "GO north"
​
**INVENTORY** - Displays any items by name in the users inventory.
​
​
## Effects
Effects give us the ability to have latent actions following a users input.  Actions take 0 or more items or doors, specify an effect type, and can provide contextual text to accompany the effect (either by displaying the text to the user, or modifying existing text).  Examples of effects are "UNLOCK_DOOR" and "CHANGE_ITEM_TEXT"
​
### Effect Structure
```
{
    "id" : string,
    "type" : string,
    "doorIds" : string[],
    "itemIds" : string[],
    "text" : string
}
```
​
### Effects to implement
**UNLOCK_DOOR** - Unlocks any provided door IDs.  If text is provided, display the text to the user.
​
**LOCK_DOOR** - Locks any provided door IDs.  If text is provided, display the text to the user.
​
**CHANGE_ITEM_TEXT** - Updates the descriptive text of an item to the provided text.
​
## Items
Items provide the user with tools to solve puzzles between rooms.  Items contain lists of valid commands, an ID, a visibility state, and a name.
​
### Item Structure
```
{
    "id" : string,
    "name" : string,
    "commands" : Command[],
    "visible" : boolean
}
```
​
## Doors
Doors are used to signify a transition point between rooms. They may be locked or unlocked by effects, a state that is global to the door, and contain an id.
​
### Door Structure
```
{
    "id" : string,
    "locked" : boolean
}
```
​
## Rooms
Rooms represent areas of the world.  Each room may have up to 4 doors (One in each cardinal direction), descriptive text, zero or more items, and can be marked as the victory condition.  Reaching the room marked as the victory condition should end the game after printing the descriptive text.
​
### Room Structure
```
{
    "id" : string,
    "text" : string,
    "itemIds" : string[],
    "doors" : [
        {
            "doorId" : string,
            "direction" : string,
            "connectedRoomId" : string
        }
    ]
}
```
​
## Full Game Format Structure
```
{
    "items" : Item[],
    "effects" : Effect[],
    "doors" : Door[],
    "rooms" : Room[],
    "startingRoomId" : string,
    "endingRoomId" : string
}
```
​
"""


import json
        

class Player:
    def __init__(self, world):
        self.inventory = []

            
class Game:
    def __init__(self, jsonFilename):
        with open(jsonFilename, encoding="utf-8") as json_in:
            self.world = json.load(json_in)
        self.player = Player(self.world)

        # store a reference to the entire room where the player is
        self.playerRoom = self.getRoom(self.world['startingRoomId'])


    def showState(self):
        print(json.dumps(self.world, indent=2, sort_keys=True))


    def showTopLevel(self, key):
        print(json.dumps(self.world[key], indent=2, sort_keys=True))
        
        
    def parseAction(self, textCommand):
        """Dispatch to the appropriate method."""
        tokens = textCommand.split()
        if tokens[0] == "LOOK":
            self.look(textCommand)
        elif tokens[0] == "INVENTORY":
            print("You have:")
            if len(self.player.inventory) == 0:
                print("Nothing.")
            else:
                print("\n".join(self.player.inventory))
        elif tokens[0] == "GO":
            self.go(tokens[1])
        elif tokens[0] == "TAKE":
            self.take(textCommand)

            
    def getCommand(self, item, playerCommand):
        """Check if the command can be used on the item."""
        for command in item['commands']:
            if command['command'] == playerCommand:
                return command
        return f"getCommand ERROR: {playerCommand} not found for {item['text']}"

    
    def lookAtItem(self, itemName):
        """Return the text describing the item."""
        for item in self.world['items']:
            if item['name'].lower() == itemName.lower():
                if command := self.getCommand(item, "LOOK"):
                    return command['text']


    def describeItemById(self, itemId):
        for item in g.world['items']:
            if item['id'] == itemId:
                print(f"There is an item: '{item['name']}'.", end=" ")
                for command in item['commands']:
                    if command['command'] == 'LOOK':
                        print(command['text'])
                        
                
    def getRoom(self, roomId):
        """Find the room with the given ID"""
        for room in self.world['rooms']:
            if room['id'] == roomId:
                return room


    def isDoorLocked(self, doorId):
        for door in self.world['doors']:
            if door['id'] == doorId:
                return door['locked']

            
    def tryDoor(self, direction):
        """Check if the door is unlocked and return the connectedRoomId"""
        for door in self.playerRoom['doors']:
            if door['direction'] == direction:
                if not self.isDoorLocked(door['doorId']):
                    return door  # door is unlocked
                else:
                    print("tryDoor: door is locked.")
                    return False
        print(f"tryDoor: no door going {direction}.")
        return False
                
                
    def look(self, textCommand):
        tokens = textCommand.split()
        if len(tokens) == 1:
            room = self.playerRoom
            print("The room is:", room['text'])

            # print items in room
            for itemId in room['itemIds']:
                self.describeItemById(itemId)
                
            # check for doors
            print()
            for door in room['doors']:
                print("There is a door going", door['direction'])
        elif len(tokens) == 2:
            item = " ".join(tokens[1:])
            print(self.lookAtItem(item))

            
    def go(self, direction):
        if door := self.tryDoor(direction):
            self.playerRoom = self.getRoom(door['connectedRoomId'])
            print(f"You have moved {direction}.")
            if self.playerRoom['id'] == self.world['endingRoomId']:
                print("A WINNER IS YOU!!!!!11")


    def getItemId(self, itemName):
        for item in self.world['items']:
            if item['name'].lower() == itemName.lower():
                return item['id']
        print(f"getItemId ERROR: {itemName} not found.")
        
    
    def take(self, itemName):
        room = self.playerRoom
        roomItems = room['itemIds']
        itemId = getItemId(itemName)
        if itemId in roomItems:
            self.player.inventory.append(itemId)
            roomItems.remove(itemId)
        print(f"{itemName} is in hand.")
        

def sampleGame():
    return Game("sample_world.json")
