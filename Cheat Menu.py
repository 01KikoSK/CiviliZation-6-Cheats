class CheatMenu:
    def __init__(self, game):
        self.game = game
        self.cheats = {
            "add_gold": self.add_gold,
            "add_faith": self.add_faith,
            "complete_production": self.complete_production,
            "add_era_points": self.add_era_points,
            "add_movement": self.add_movement,
            "complete_research": self.complete_research
        }

    def show(self):
        print("Cheat Menu")
        print("==========")
        for cheat in self.cheats.keys():
            print(f"{cheat}: {self.cheats[cheat].__doc__}")

    def add_gold(self, amount=1000):
        """Adds gold to the player's treasury."""
        self.game.player.gold += amount

    def add_faith(self, amount=100):
        """Adds faith to the player's pool."""
        self.game.player.faith += amount

    def complete_production(self, city_index=None):
        """Completes production in a city."""
        if city_index is None:
            city_index = self.game.current_city_index
        self.game.cities[city_index].production = 0

    def add_era_points(self, amount=10):
        """Adds era points to the player's total."""
        self.game.player.era_points += amount

    def add_movement(self, unit_index=None, amount=1):
        """Adds movement points to a unit."""
        if unit_index is None:
            unit_index = self.game.current_unit_index
        self.game.units[unit_index].movement += amount

    def complete_research(self, tech_index=None, civic_index=None):
        """Completes research for a technology or civic."""
        if tech_index is not None:
            self.game.tech_tree[tech_index].researched = True
        if civic_index is not None:
            self.game.civic_tree[civic_index].researched = True

# Example usage:
cheat_menu = CheatMenu(game)
cheat_menu.show()
cheat_menu.cheats["add_gold"](999999999)