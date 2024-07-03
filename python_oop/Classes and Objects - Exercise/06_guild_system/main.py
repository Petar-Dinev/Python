from project.guild import Guild
from project.player import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
player1 = Player('Petar', 100, 50)
print(player1.add_skill("Ultimate", 100))
print(guild.assign_player(player1))
print(guild.guild_info())
print(guild.kick_player('pesho'))
print(guild.kick_player('Petar'))
print(guild.guild_info())
