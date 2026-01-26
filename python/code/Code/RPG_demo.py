import random
import time

class Player:
    def __init__(self):
        self.health = 100
        self.max_health = 1001
        self.attack_power = 15
        self.gold = 0
        self.potions = 1
        self.level = 1
        self.exp = 0
        self.exp_to_level = 50

class Enemy:
    def __init__(self, name, health, attack_power, gold_reward, exp_reward):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.gold_reward = gold_reward
        self.exp_reward = exp_reward

def create_enemy(level):
    enemies = [
        Enemy("Goblin", 30 + level*5, 5 + level*2, 10 + level*3, 20 + level*5),
        Enemy("Skeleton", 25 + level*6, 8 + level*2, 15 + level*4, 25 + level*5),
        Enemy("Orc", 40 + level*7, 10 + level*3, 20 + level*5, 30 + level*6)
    ]
    return random.choice(enemies)

def print_section(title, content):
    """Print a clearly separated section"""
    print(f"\n{'='*50}")
    print(f"🎯 {title}")
    print(f"{'='*50}")
    print(content)

def print_status(player):
    """Print current player status"""
    status = f"Level: {player.level} | HP: {player.health}/{player.max_health} | "
    status += f"Gold: {player.gold} | Potions: {player.potions} | "
    status += f"EXP: {player.exp}/{player.exp_to_level}"
    print_section("CHARACTER STATUS", status)

def combat(player, enemy):
    print_section("COMBAT START", f"A wild {enemy.name} appears!")

    round_num = 1
    while enemy.health > 0 and player.health > 0:
        print_section(f"COMBAT ROUND {round_num}",
                     f"{enemy.name}: HP {enemy.health} | You: HP {player.health}/{player.max_health}")

        print("\nAvailable actions:")
        print("1. attack - Attack the enemy")
        print("2. potion - Use a health potion (+30 HP)")
        print("3. run - Try to escape (50% chance)")

        action = input("\nChoose action (1-3 or name): ").lower().strip()

        if action in ["1", "attack"]:
            # Player attacks
            player_damage = random.randint(player.attack_power-5, player.attack_power+5)
            enemy.health -= player_damage
            print(f"\n🗡️  You attack the {enemy.name} for {player_damage} damage!")

            if enemy.health > 0:
                # Enemy attacks back
                enemy_damage = random.randint(enemy.attack_power-3, enemy.attack_power+3)
                player.health -= enemy_damage
                print(f"💢 The {enemy.name} attacks you for {enemy_damage} damage!")
            else:
                print(f"✅ The {enemy.name} is defeated!")

        elif action in ["2", "potion"]:
            if player.potions > 0:
                heal_amount = 30
                player.health = min(player.max_health, player.health + heal_amount)
                player.potions -= 1
                print(f"\n🧪 You drink a potion and recover {heal_amount} HP!")
                # Enemy still attacks
                if enemy.health > 0:
                    enemy_damage = random.randint(enemy.attack_power-3, enemy.attack_power+3)
                    player.health -= enemy_damage
                    print(f"💢 The {enemy.name} attacks you for {enemy_damage} damage!")
            else:
                print("\n❌ You have no potions left!")
                continue

        elif action in ["3", "run"]:
            if random.random() < 0.5:
                print("\n🏃 You successfully escaped!")
                return False
            else:
                print("\n❌ You failed to escape!")
                enemy_damage = random.randint(enemy.attack_power-3, enemy.attack_power+3)
                player.health -= enemy_damage
                print(f"💢 The {enemy.name} attacks you for {enemy_damage} damage!")

        else:
            print("\n❌ Invalid action! Choose 'attack', 'potion', or 'run'")
            continue

        round_num += 1
        time.sleep(1)  # Brief pause between rounds

    if player.health <= 0:
        print_section("DEFEAT", "You have been defeated...")
        return False
    else:
        print_section("VICTORY", f"You defeated the {enemy.name}!")
        player.gold += enemy.gold_reward
        player.exp += enemy.exp_reward
        print(f"💰 Gained {enemy.gold_reward} gold")
        print(f"⭐ Gained {enemy.exp_reward} experience")
        return True

def level_up(player):
    if player.exp >= player.exp_to_level:
        player.level += 1
        player.exp -= player.exp_to_level
        player.exp_to_level = int(player.exp_to_level * 1.5)
        player.max_health += 20
        player.health = player.max_health
        player.attack_power += 5
        print_section("LEVEL UP",
                     f"Congratulations! You are now level {player.level}!\n"
                     f"Max HP increased to {player.max_health}!\n"
                     f"Attack power increased to {player.attack_power}!")

def shop(player):
    print_section("SHOP", f"Welcome! You have {player.gold} gold")

    items = [
        ("Health Potion", 25, "Restores 30 HP"),
        ("Better Sword", 100, "+5 attack power"),
        ("Leave shop", 0, "Return to adventure")
    ]

    for i, (item, price, desc) in enumerate(items, 1):
        print(f"{i}. {item} - {price} gold - {desc}")

    while True:
        choice = input("\nWhat would you like to buy? (1-3): ").strip()

        if choice == "1":
            if player.gold >= 25:
                player.gold -= 25
                player.potions += 1
                print_section("PURCHASE", "You bought a health potion!")
                break
            else:
                print("❌ Not enough gold!")

        elif choice == "2":
            if player.gold >= 100:
                player.gold -= 100
                player.attack_power += 5
                print_section("PURCHASE", "You bought a better sword! Attack power increased!")
                break
            else:
                print("❌ Not enough gold!")

        elif choice == "3":
            print("You leave the shop.")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3")

def main():
    player = Player()

    print_section("WELCOME", "🌟 Text RPG Adventure 🌟\n"
                 "Commands: explore, rest, shop, status, quit")

    while player.health > 0:
        print_section("LOCATION", "You are in a peaceful clearing")
        print_status(player)

        print("\nAvailable actions:")
        print("1. explore - Venture into the wilderness (70% encounter chance)")
        print("2. rest - Rest and recover 25 HP")
        print("3. shop - Visit the shop to buy items")
        print("4. status - View detailed character information")
        print("5. quit - End your adventure")

        action = input("\nWhat would you like to do? ").lower().strip()

        if action in ["1", "explore"]:
            print_section("EXPLORATION", "You venture into the wilderness...")
            time.sleep(1)

            if random.random() < 0.7:
                enemy = create_enemy(player.level)
                if combat(player, enemy):
                    level_up(player)
                    if random.random() < 0.3:
                        found_gold = random.randint(5, 15)
                        player.gold += found_gold
                        print_section("LOOT", f"You found {found_gold} gold on the ground!")
            else:
                print("You explore peacefully but find nothing of interest.")

        elif action in ["2", "rest"]:
            heal_amount = 25
            player.health = min(player.max_health, player.health + heal_amount)
            print_section("REST", f"You rest and recover {heal_amount} HP")

        elif action in ["3", "shop"]:
            shop(player)

        elif action in ["4", "status"]:
            print_section("DETAILED STATUS",
                         f"Level: {player.level}\n"
                         f"Health: {player.health}/{player.max_health}\n"
                         f"Attack Power: {player.attack_power}\n"
                         f"Gold: {player.gold}\n"
                         f"Experience: {player.exp}/{player.exp_to_level}\n"
                         f"Potions: {player.potions}")

        elif action in ["5", "quit"]:
            print_section("FAREWELL", "Thanks for playing!")
            break

        else:
            print_section("ERROR", "Invalid command! Try: explore, rest, shop, status, quit")

        # Brief pause before next turn
        time.sleep(1)

    if player.health <= 0:
        print_section("GAME OVER",
                     f"Your adventure has come to an end.\n"
                     f"You reached level {player.level} and collected {player.gold} gold.")

if __name__ == "__main__":
    main()
