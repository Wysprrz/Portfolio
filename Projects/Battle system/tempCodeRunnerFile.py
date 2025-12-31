heal, allowed = self.player.rest()
        if allowed && :
            messages.append(f"{self.player.fighter_name} rests and recovers {heal} HP! Rests left: {self.player.rest_charges}")
        else:
            messages.append(f"{self.player.fighter_name} cannot rest; no heals left.")