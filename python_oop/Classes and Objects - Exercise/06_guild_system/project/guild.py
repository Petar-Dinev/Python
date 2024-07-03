from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player = next((p for p in self.players if p.name == player_name), None)
        if player:
            player.guild = "Unaffiliated"
            self.players.remove(player)
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        for player in self.players:
            result.append(f"{player.player_info()}")
        return '\n'.join(result)
