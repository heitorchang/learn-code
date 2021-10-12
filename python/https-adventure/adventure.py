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
      OK- TAKE
      OK- READ
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


def convertListOfObjects(rawList):
    convertedDict = {}
    for obj in rawList:
        if 'id' in obj:
            convertedDict[obj['id']] = obj
        elif 'command' in obj:
            convertedDict[obj['command']] = obj
        elif 'doorId' in obj:
            convertedDict[obj['doorId']] = obj
    return convertedDict


def convertWorldToKeys(rawWorld):
    """Add objects with ID attributes to a dict, where the value is
    the object itself, associated to the ID as key.
    (Avoid linear searches to retrieve an item.)"""
    
    world = {}

    # iterate over top-level keys
    for k in rawWorld:
        if isinstance(rawWorld[k], str):
            world[k] = rawWorld[k]
        else:
            world[k] = convertListOfObjects(rawWorld[k])
            if k == 'items':
                for item in world['items'].values():
                    item['commands'] = convertListOfObjects(item['commands'])
            elif k == 'rooms':
                for room in world['rooms'].values():
                    if 'doors' in room:
                        room['doors'] = convertListOfObjects(room['doors'])
    return world


class Player:
    def __init__(self, world):
        self.inventory = []


class Game:
    def __init__(self, jsonFilename):
        with open(jsonFilename, encoding="utf-8") as json_in:
            self.rawWorld = json.load(json_in)
        self.world = convertWorldToKeys(self.rawWorld)
        self.player = Player(self.world)

        # store a reference to the entire room where the player is
        self.playerRoom = self.world['rooms'][self.world['startingRoomId']]


    def showState(self):
        print(json.dumps(self.world, indent=2, sort_keys=True))


    def showTopLevel(self, key):
        print(json.dumps(self.world[key], indent=2, sort_keys=True))
        
        
    def act(self, textCommand):
        """Dispatch to the appropriate method."""
        tokens = textCommand.split()
        tokens[0] = tokens[0].upper()  # allow lowercase input
        
        if tokens[0] == "LOOK":
            self.look(textCommand)
        elif tokens[0] == "READ":
            self.read(textCommand)
        elif tokens[0] == "INVENTORY":
            print("You have:")
            if len(self.player.inventory) == 0:
                print("Nothing.")
            else:
                print("\n".join(self.world['items'][itemId]['name'] for itemId in self.player.inventory))
        elif tokens[0] == "GO":
            self.go(tokens[1])
        elif tokens[0] == "TAKE":
            self.take(" ".join(tokens[1:]))
        elif tokens[0] == "USE":
            body = " ".join(tokens[1:]).lower()
            obj, target = body.split(" on ")
            self.use(obj, target)
        else:
            print("act ERROR: unknown action.")
                
    
    def lookAtItem(self, itemName, alternativeAction=None):
        """Return the text describing the item. Apply READ if optional parameter is given"""
        action = "LOOK"
        if alternativeAction is not None:
            action = alternativeAction
        for item in self.world['items'].values():
            if item['name'].lower() == itemName.lower():                
                print(item['commands'][action]['text'])
                break
        else:
            print("lookAtItem: Item not found.")


    def describeItemById(self, itemId):
        print(f"There is an item: '{self.world['items'][itemId]['name']}'.", end=" ")
        print(self.world['items'][itemId]['commands']['LOOK']['text'])
                        
                
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
            for door in room['doors'].values():
                print("There is a door going", door['direction'])
        elif len(tokens) > 1:
            item = " ".join(tokens[1:])
            self.lookAtItem(item)


    def read(self, textCommand):
        tokens = textCommand.split()
        if len(tokens) > 1:
            item = " ".join(tokens[1:])
            self.lookAtItem(item, "READ")  # apply READ instead of LOOK
        else:
            "read: An object must be given."
            
            
    def tryDoor(self, direction):
        """Check if the door is unlocked and return the connectedRoomId"""
        for door in self.playerRoom['doors'].values():
            if door['direction'].lower() == direction.lower():
                if not self.world['doors'][door['doorId']]['locked']:
                    return door['doorId']
                else:
                    print("tryDoor: door is locked.")
                    return False
        print(f"tryDoor: no door going {direction}.")
        return False
                
                
    def go(self, direction):
        if doorId := self.tryDoor(direction):
            self.playerRoom = self.world['rooms'][self.playerRoom['doors'][doorId]['connectedRoomId']]
            print(f"You have moved {direction}.")
            if self.playerRoom['id'] == self.world['endingRoomId']:
                print("A WINNER IS YOU!!!!!11")


    def getItemId(self, itemName):
        for item in self.world['items'].values():
            if item['name'].lower() == itemName.lower():
                return item['id']
        print(f"getItemId ERROR: {itemName} not found.")
        
    
    def take(self, itemName):
        room = self.playerRoom
        roomItems = room['itemIds']
        itemId = self.getItemId(itemName)
        if itemId in roomItems:
            self.player.inventory.append(itemId)
            roomItems.remove(itemId)
            print(f"{itemName} is in hand.")
        else:
            print("take ERROR: item not found.")


    def use(self, objName, targetName):
        objId = self.getItemId(objName)
        targetId = self.getItemId(targetName)
        if objId in self.player.inventory:
            if targetId in self.playerRoom['itemIds']:
                if "USE" in self.world['items'][targetId]['commands']:
                    print(f"Using {objName} on {targetName}")
                    for item in self.world['items'][targetId]['commands']['USE']['acceptedItem']:
                        if item['itemId'] == objId:
                            # apply effects
                            print(item['text'])
                            self.applyEffects(item['effectIds'])
                    self.player.inventory.remove(objId)
                else:
                    print(f"use ERROR: {targetName} cannot be targeted.")
                    return
            else:
                print(f"use ERROR: {targetName} not present in the room.")
        else:
            print(f"use ERROR: {objName} is not in your inventory.")


    def alterDoor(self, doorId, alterType):
        lockStatus = False if alterType == 'UNLOCK_DOOR' else True
        self.world['doors'][doorId]['locked'] = lockStatus        
        
    
    def applyEffects(self, effectIds):
        for effect in self.world['effects'].values():
            if effect['id'] in effectIds:
                print(effect['text'])
                effectType = effect['type']
                if 'LOCK_DOOR' in effectType:
                    for doorId in effect['doorIds']:
                        self.alterDoor(doorId, effectType)
                elif 'CHANGE_ITEM_TEXT' == effectType:
                    for itemId in effect['itemIds']:
                        self.world['items'][itemId]['commands']['LOOK']['text'] = effect['text']
        

def sampleGame():
    return Game("sample_world.json")


def testPlay():
    g = sampleGame()
    g.act("look")
    g.act("look book")
    g.act("take book")
    g.act("inventory")
    g.act("look")
    g.act("go north")
    g.act("go south")
    g.act("go east")
    g.act("go north")
    g.act("look")
    g.act("use book on book shelf")
    g.act("look")
    g.act("go south")
    g.act("go east")
    
