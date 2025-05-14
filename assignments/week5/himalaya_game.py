import time

inventory = []
health = 100
current_room = "base camp"
rescued_climber = False

rooms = {
    "base camp": [
        {"name": "Protein Bar", "type": "food"},
        {"name": "Broken Beacon", "type": "quest"}
    ],
    "frozen cave": [
        {"name": "Bandage", "type": "healing", "uses": 1},
        {"name": "Beacon Parts", "type": "quest"}
    ],
    "ridge trail": [
        {"name": "Ice Pick", "type": "tool"},
        {"name": "Rope", "type": "tool"}
    ],
    "cliffside": []
}

room_paths = {
    "base camp": ["frozen cave", "ridge trail"],
    "frozen cave": ["base camp"],
    "ridge trail": ["base camp", "cliffside"],
    "cliffside": ["ridge trail"]
}

def show_intro():
    print("\U0001f328️ You awaken at the base of the Himalayas after a storm.")
    time.sleep(1)
    print("\U0001f9ed You must find the beacon parts to send a distress signal and survive.")
    time.sleep(1)
    print("\U0001f50d Explore the mountains, find useful items, and repair the beacon to escape.")
    time.sleep(1)

def show_inventory():
    if not inventory:
        print("\U0001f392 Inventory is empty.")
    else:
        print("\U0001f392 Inventory:")
        for item in inventory:
            line = f"- {item['name']} ({item['type']})"
            if item.get("uses"):
                line += f" (uses left: {item['uses']})"
            print(line)

def show_room():
    print(f"\nYou are at the {current_room.title()}.")
    if rooms[current_room]:
        print("You see:")
        for item in rooms[current_room]:
            print(f"- {item['name']} ({item['type']})")
    else:
        print("There's nothing of interest here.")
    print("\n🗺️ From here, you can go to:")
    for path in room_paths[current_room]:
        print(f"- {path.title()}")
    print("\n📌 What you can do:")
    print("- Type 'go [location]' to travel")
    print("- Type 'pickup [item]' to collect something")
    print("- Type 'use [item]' to use food, tools, or quest items")
    print("- Type 'inventory' to check your items")
    print("- Type 'status' to check your health and location")
    print("- Type 'examine [item]' to learn more about it")
    print("- Type 'drop [item]' to drop something")
    print("- Type 'map' to view a basic layout")
    print("- Type 'help' to see all commands")
    print("- Type 'quit' to leave the game")

def show_map():
    print("""
       ❄️ Ridge Trail
           |
       🧗 Cliffside
           |
       ❄️ Frozen Cave
           |
🏕️ Base Camp (You start here)
    """)

def pick_up(item_name):
    item_name = item_name.lower()
    for item in rooms[current_room]:
        if item["name"].lower() == item_name:
            if len(inventory) < 5:
                inventory.append(item)
                rooms[current_room].remove(item)
                print(f"✅ You picked up the {item['name']}.")
            else:
                print("❌ Your inventory is full (5 items max).")
            return
    print("❌ Item not found in this location.")

def drop(item_name):
    item_name = item_name.lower()
    for item in inventory:
        if item["name"].lower() == item_name:
            rooms[current_room].append(item)
            inventory.remove(item)
            print(f"🗑️ You dropped the {item['name']}.")
            return
    print("❌ You don't have that item.")

def use(item_name):
    global health, rescued_climber
    item_name = item_name.lower()

    found_item = None
    for item in inventory:
        if item["name"].lower() == item_name:
            found_item = item
            break

    if not found_item:
        print(f"❌ You don’t have {item_name}.")
        return

    if found_item["type"] == "healing":
        heal = 30
        health = min(100, health + heal)
        print(f"💊 You used {found_item['name']} and healed +{heal} health.")
        found_item["uses"] -= 1
        if found_item["uses"] == 0:
            inventory.remove(found_item)
            print(f"🗑️ {found_item['name']} is used up.")
        return

    if found_item["name"].lower() == "rope" and current_room == "cliffside":
        if not rescued_climber:
            print("🧗 You throw down the rope and help the lost climber up...")
            time.sleep(2)
            print("🙌 They thank you and stay with you at base camp.")
            rescued_climber = True
        else:
            print("🙌 You’ve already rescued the climber.")
        return

    if found_item["name"].lower() == "beacon parts" and current_room == "base camp":
        if any(i["name"].lower() == "broken beacon" for i in inventory):
            print("🔧 You repair the beacon...")
            time.sleep(2)
            if rescued_climber:
                print("📡 Signal sent! The rescue team finds both of you. You survived and saved someone! 🏔️🎉")
            else:
                print("📡 Signal sent! You are rescued, but the lost climber was never found... 🏔️")
            print("🏁 GAME OVER 🏁")
            exit()
        else:
            print("🧩 You need the Broken Beacon in your inventory to repair it.")
        return

    if found_item["type"] == "food":
        print(f"🍎 You ate the {found_item['name']}. It gave you a little energy.")
        inventory.remove(found_item)
        return

    print(f"🧪 You used the {found_item['name']}, but nothing happened.")

def examine(item_name):
    item_name = item_name.lower()
    for item in inventory:
        if item["name"].lower() == item_name:
            print(f"🔎 {item['name']} is a {item['type']} item.")
            return
    print("❌ You don’t have that item.")

def status():
    print(f"❤️ Health: {health}")
    print(f"📍 Location: {current_room.title()}")

def help_menu():
    print("Commands: inventory, pickup [item], drop [item], use [item], examine [item], go [location], status, map, help, quit")

def game_loop():
    global current_room
    show_intro()
    show_room()
    while True:
        command = input("\n> ").strip().lower()
        if command == "inventory":
            show_inventory()
        elif command.startswith("pickup "):
            pick_up(command[7:])
        elif command.startswith("drop "):
            drop(command[5:])
        elif command.startswith("use "):
            use(command[4:])
        elif command.startswith("examine "):
            examine(command[8:])
        elif command.startswith("go "):
            destination = command[3:]
            if destination in room_paths[current_room]:
                current_room = destination
                print(f"🚶 You travel to the {current_room.title()}.")
                show_room()
            else:
                print("❌ You can’t go there from here.")
        elif command == "status":
            status()
        elif command == "map":
            show_map()
        elif command == "help":
            help_menu()
        elif command == "quit":
            print("👋 Thanks for playing. Stay warm!")
            break
        else:
            print("❓ Unknown command. Type 'help' for options.")


game_loop()
