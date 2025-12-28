import sys
import time
import msvcrt
import random
import string


def typewriter(text, speed=0.03):
    """Print text like a typewriter safely, even in .exe builds."""
    for char in text:
        try:
            sys.stdout.write(char)
            sys.stdout.flush()
        except Exception:
            # fallback in case stdout is unavailable
            print(char, end='', flush=True)
        time.sleep(speed)
    print()


# Create a fighter class
class Fighter:
    def __init__(self, name, hp, attack_range, parry_window):
        self.fighter_name = name  # (figure out how to get player input)
        self.fighter_hp = hp  # HP of player
        self.fighter_attack = attack_range  # (min, max)
        self.fighter_window = parry_window  # fighter parry window

    def attack(self):
        # Assigning variables to the values so we can change them
        min_damage = self.fighter_attack[0]
        max_damage = self.fighter_attack[1]
        damage = random.randint(min_damage, max_damage)
        return damage

    def take_damage(self, amount):
        self.fighter_hp -= amount
        return self.fighter_hp

    def parry_window(self):
        action_key = None
        parry_key = random.choice(string.ascii_uppercase + " ")
        typewriter(f"Hurry! Press {parry_key} to parry!")
        start_time = time.time()
        while time.time() - start_time < self.fighter_window:
            if msvcrt.kbhit():
                key_stroke = msvcrt.getch()
                action_key = key_stroke.decode('utf-8').upper()
            if action_key == parry_key:
                return True
        return False

    def rest(self):
        missing_hp = 100 - self.fighter_hp
        heal_amount = int(missing_hp * 0.5)
        self.fighter_hp += heal_amount
        typewriter(f"{self.fighter_name} takes a rest and recovers {heal_amount} HP! Current HP: {self.fighter_hp}")

        

# -----------------------------
# MAIN PROGRAM STARTS HERE
# -----------------------------

# Step 1: Ask for player name
typewriter("\n=== A Goblin growls: What is your name, challenger? ===\n")
player_name = input("Enter name: ")

# Step 2: Decide stats
player = Fighter(player_name, 100, (6, 12), 2)
enemy = Fighter("Goblin", 80, (4, 14), 0)

while player.fighter_hp > 0 and enemy.fighter_hp > 0:

    # PLAYER INPUT
    action = input("Choose an action: [1] Attack  [2] Rest: ").strip()

    # Loop for invalid choice
    while action not in ("1", "2"):
        action = input("Invalid choice!\nChoose: [1] Attack [2] Rest: ").strip()

    # -------------------------------
    # PLAYER TURN
    # -------------------------------
    if action == "1":  # Attack
        dmg = player.attack()
        enemy.take_damage(dmg)
        typewriter(f"{player.fighter_name} dealt {dmg} damage! Enemy HP: {enemy.fighter_hp}")

    elif action == "2":
        player.rest()

    # Check enemy death
    if enemy.fighter_hp <= 0:
        typewriter(f"Congrats {player.fighter_name} you've conquered the {enemy.fighter_name}!")
        break

    # -------------------------------
    # ENEMY TURN
    # -------------------------------
    enemy_dmg = enemy.attack()
    parry_success = player.parry_window()
    reduced_damage = enemy_dmg * 0.6

    if parry_success:
        player.take_damage(int(reduced_damage))
        typewriter(f"You successfully parried, {enemy.fighter_name} dealt {int(reduced_damage)} damage! Your HP: {player.fighter_hp}")
    else:
        player.take_damage(enemy_dmg)
        typewriter(f"Your parry failed! {enemy.fighter_name} dealt {enemy_dmg} damage! Your HP: {player.fighter_hp}")

    # Check if player died
    if player.fighter_hp <= 0:
        typewriter("You've died!")
        break
