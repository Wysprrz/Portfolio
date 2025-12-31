import sys
import time
import string
import random
import tkinter as tk
from tkinter import ttk

# -----------------------------
# Fighter class
# -----------------------------
class Fighter:
    def __init__(self, name, hp, attack_range, parry_window):
        self.fighter_name = name
        self.fighter_hp = hp
        self.fighter_attack = attack_range
        self.fighter_window = parry_window
        self.rest_charges = 3

    def attack(self):
        return random.randint(self.fighter_attack[0], self.fighter_attack[1])

    def take_damage(self, amount):
        self.fighter_hp -= amount
        if self.fighter_hp < 0:
            self.fighter_hp = 0
        return self.fighter_hp

    def rest(self):
        if self.rest_charges <= 0:
            return 0, False
        self.rest_charges -= 1
        missing_hp = 100 - self.fighter_hp
        heal_amount = int(missing_hp * 0.5)
        self.fighter_hp += heal_amount
        return heal_amount, True

# -----------------------------
# Battle logic
# -----------------------------
class BattleSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def resolve_attack(self, player_action="attack", parry_success=False):
        messages = []

        if player_action == "attack":
            dmg_to_enemy = self.player.attack()
            self.enemy.take_damage(dmg_to_enemy)
            messages.append(f"{self.player.fighter_name} attacks and deals {dmg_to_enemy} damage!")

        elif player_action == "rest":
            heal, allowed = self.player.rest()
            if allowed:
                messages.append(f"{self.player.fighter_name} rests and recovers {heal} HP! Rests left: {self.player.rest_charges}")
            else:
                messages.append(f"{self.player.fighter_name} cannot rest; no heals left.")

        # Enemy attack
        enemy_dmg = self.enemy.attack()
        if parry_success:
            reduced = int(enemy_dmg * 0.6)
            self.player.take_damage(reduced)
            messages.append(f"Enemy attacks! Damage reduced to {reduced} due to parry.")
        else:
            self.player.take_damage(enemy_dmg)
            if player_action == "rest":
                messages.append(f"Parry failed during rest! You did not heal and took {enemy_dmg} damage.")
            else:
                messages.append(f"Enemy attacks! You take {enemy_dmg} damage.")

        return {"player_hp": self.player.fighter_hp, "enemy_hp": self.enemy.fighter_hp, "log": messages}

# -----------------------------
# GUI logic
# -----------------------------
class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Goblin Battle")
        self.turn_locked = False
        self.parry_active = False
        self.parry_success = False
        self.parry_key = None
        self.root.bind("<Key>", self.check_parry_key)

        # Fonts & colors
        self.font_title = ("Creepster", 16, "bold")
        self.font_normal = ("Courier New", 12)
        self.bg_color = "#1e1e1e"
        self.fg_color = "#f5f5dc"
        self.button_bg = "#444444"
        self.button_fg = "#f5f5dc"
        self.player_bar_color = "#6b8e23"
        self.enemy_bar_color = "#ff7f50"

        self.root.configure(bg=self.bg_color)
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Left frame
        self.left_frame = tk.Frame(self.root, padx=8, pady=8, bg=self.bg_color)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(2, weight=1)

        # HP frame
        self.hp_frame = tk.Frame(self.left_frame, bg=self.bg_color)
        self.hp_frame.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        self.hp_frame.columnconfigure(0, weight=1)
        self.hp_frame.columnconfigure(1, weight=1)
        tk.Label(self.hp_frame, text="Player HP", font=self.font_normal, bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, sticky="w")
        tk.Label(self.hp_frame, text="Enemy HP", font=self.font_normal, bg=self.bg_color, fg=self.fg_color).grid(row=0, column=1, sticky="w")

        # Progress bars
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure("green.Horizontal.TProgressbar", troughcolor="#333", background=self.player_bar_color)
        style.configure("red.Horizontal.TProgressbar", troughcolor="#333", background=self.enemy_bar_color)
        self.player_hp_bar = ttk.Progressbar(self.hp_frame, maximum=100, length=150, style="green.Horizontal.TProgressbar")
        self.player_hp_bar.grid(row=1, column=0, sticky="ew", padx=(0,8))
        self.enemy_hp_bar = ttk.Progressbar(self.hp_frame, maximum=100, length=150, style="red.Horizontal.TProgressbar")
        self.enemy_hp_bar.grid(row=1, column=1, sticky="ew")

        # HP numbers
        self.player_hp_label = tk.Label(self.hp_frame, text="100 / 100", font=self.font_normal, bg=self.bg_color, fg=self.fg_color)
        self.player_hp_label.grid(row=2, column=0)
        self.enemy_hp_label = tk.Label(self.hp_frame, text="100 / 100", font=self.font_normal, bg=self.bg_color, fg=self.fg_color)
        self.enemy_hp_label.grid(row=2, column=1)

        # Canvas
        self.canvas = tk.Canvas(self.left_frame, height=160, bg="#2b2b2b", highlightthickness=1, highlightbackground="#444")
        self.canvas.grid(row=1, column=0, sticky="ew", pady=(0,8))
        self.canvas.create_text(80, 80, text="Dungeon Arena", fill="#dcdcdc", font=("Creepster", 16))

        # Action log
        log_frame = tk.Frame(self.left_frame, bg=self.bg_color)
        log_frame.grid(row=2, column=0, sticky="nsew")
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        self.log_text = tk.Text(log_frame, wrap="word", height=8, bg="#111111", fg=self.fg_color, font=("Courier New", 11))
        self.log_text.grid(row=0, column=0, sticky="nsew")
        self.log_scroll = tk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_scroll.grid(row=0, column=1, sticky="ns")
        self.log_text.config(yscrollcommand=self.log_scroll.set, state="disabled")

        # Buttons
        self.button_frame = tk.Frame(self.left_frame, bg=self.bg_color)
        self.button_frame.grid(row=3, column=0, sticky="ew", pady=(8,0))
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.attack_button = tk.Button(self.button_frame, text="Attack", command=self.attack_action,
                                       width=12, bg=self.button_bg, fg=self.button_fg)
        self.attack_button.grid(row=0, column=0, padx=4)
        self.rest_button = tk.Button(self.button_frame, text="Rest", command=self.rest_action,
                                     width=12, bg=self.button_bg, fg=self.button_fg)
        self.rest_button.grid(row=0, column=1, padx=4)

        # Story frame
        self.story_frame = tk.Frame(self.root, padx=8, pady=8, bg=self.bg_color)
        self.story_frame.grid(row=0, column=1, sticky="nsew")
        tk.Label(self.story_frame, text="Storyline", font=self.font_title, bg=self.bg_color, fg=self.fg_color).pack(anchor="w")
        self.story_text = tk.Text(self.story_frame, width=30, height=20, wrap="word",
                                  bg="#111111", fg=self.fg_color, font=("Courier New", 11))
        self.story_text.pack(fill="both", expand=True, pady=(8,0))

        # Name overlay
        self.name_frame = tk.Frame(self.root, bd=2, relief="groove", padx=12, pady=12, bg="#333")
        self.name_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self.name_frame, text="Enter your name:", font=self.font_normal, bg="#333", fg=self.fg_color).pack(pady=(0,6))
        self.name_entry = tk.Entry(self.name_frame, font=self.font_normal)
        self.name_entry.pack(pady=(0,8))
        tk.Button(self.name_frame, text="Start", command=self.start_game, bg=self.button_bg, fg=self.button_fg).pack()

        self.root.update_idletasks()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.attack_button.config(state="disabled")
        self.rest_button.config(state="disabled")

    # -----------------------------
    # Log helper
    # -----------------------------
    def update_log(self, message, delay=20):
        self.log_text.config(state="normal")
        for char in message:
            self.log_text.insert(tk.END, char)
            self.log_text.update()
            time.sleep(delay/1000)
        self.log_text.insert(tk.END, "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    # -----------------------------
    # Start game
    # -----------------------------
    def start_game(self):
        name = self.name_entry.get().strip() or "Player"
        self.player_name = name
        self.name_frame.destroy()

        self.player = Fighter(self.player_name, 100, (6, 12), 2)
        self.enemy = Fighter("Goblin", 100, (4, 14), 0)
        self.battle_system = BattleSystem(self.player, self.enemy)

        self.update_hp_labels()
        self.update_log(f"Welcome, {self.player_name}! The goblin growls!")
        self.attack_button.config(state="normal")
        self.rest_button.config(state="normal")

    # -----------------------------
    # Update HP labels
    # -----------------------------
    def update_hp_labels(self):
        self.player_hp_bar['value'] = self.player.fighter_hp
        self.enemy_hp_bar['value'] = self.enemy.fighter_hp
        self.player_hp_label.config(text=f"{self.player.fighter_hp} / 100")
        self.enemy_hp_label.config(text=f"{self.enemy.fighter_hp} / 100")

    # -----------------------------
    # Player actions
    # -----------------------------
    def attack_action(self):
        if self.turn_locked: return
        self.turn_locked = True
        self.attack_button.config(state="disabled")
        self.rest_button.config(state="disabled")
        self.start_parry_window(context="attack")

    def rest_action(self):
        if self.turn_locked: return
        self.turn_locked = True
        self.attack_button.config(state="disabled")
        self.rest_button.config(state="disabled")
        self.start_parry_window(context="rest")

    # -----------------------------
    # Parry system
    # -----------------------------
    def start_parry_window(self, duration=1200, context="attack"):
        self.parry_active = True
        self.parry_success = False
        self.parry_key = random.choice(string.ascii_uppercase)
        action = "rest" if context == "rest" else "attack"
        self.update_log(f"Hurry! Press '{self.parry_key}' to parry before enemy {action}!")
        self.root.after(duration, lambda: self.resolve_enemy_attack(context))

    def check_parry_key(self, event):
        if self.parry_active:
            pressed = event.char.upper()
            if pressed == self.parry_key:
                self.parry_success = True
                self.parry_active = False
                self.update_log(f"Parry succeeded! You pressed '{self.parry_key}'.")

    # -----------------------------
    # Enemy resolution
    # -----------------------------
    def resolve_enemy_attack(self, context="attack"):
        self.parry_active = False
        result = self.battle_system.resolve_attack(player_action=context, parry_success=self.parry_success)
        for line in result["log"]:
            self.update_log(line)
        self.update_hp_labels()

        # Check deaths
        if self.player.fighter_hp <= 0:
            self.update_log("You have been defeated!")
            self.attack_button.config(state="disabled")
            self.rest_button.config(state="disabled")
        elif self.enemy.fighter_hp <= 0:
            self.update_log("The goblin has been defeated!")
            self.attack_button.config(state="disabled")
            self.rest_button.config(state="disabled")
        else:
            self.turn_locked = False
            self.attack_button.config(state="normal")
            self.rest_button.config(state="normal" if self.player.rest_charges > 0 else "disabled")


# -----------------------------
# Run GUI
# -----------------------------
if __name__ == "__main__":
    gui = MyGui()
    gui.root.mainloop()
