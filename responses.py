# responses.py
import random

active_games = {}

def biased_roll(max_value: int) -> int:
    if max_value <= 2:  
        return random.randint(1, max_value)
    return max(1, int(random.uniform(max_value * 0.5, max_value)))

def start_deathroll(player1: int, player2: int) -> str:
    if player1 == player2:
        return "You cannot play Deathroll against yourself!"
    
    if any(player in game for game in active_games.values() for player in [player1, player2]):
        return "A Deathroll game is already in progress for one of the players!"
    
    game_id = f"{player1}-{player2}"
    active_games[game_id] = {"player1": player1, "player2": player2, "current_player": player1, "current_number": 1000}
    return f"🔥 Deathroll started between <@{player1}> and <@{player2}>!\n<@{player1}>, type `!roll 1000` to start."

def roll_deathroll(player: int, number: str) -> str:
    game_id = next((gid for gid in active_games if str(player) in gid), None)
    
    if not game_id:
        return "You're not in an active Deathroll game! Start one with `!deathroll @opponent`."
    
    game = active_games[game_id]

    if game["current_player"] != player:
        return f"❌ It's not your turn! <@{game['current_player']}>, type `!roll {game['current_number']}`."
    
    try:
        if int(number) != game["current_number"]:
            return f"❌ Invalid roll! <@{game['current_player']}>, you must type `!roll {game['current_number']}`."
    except ValueError:
        return "❌ Invalid roll input! Please enter a number."
    
    rolled_number = biased_roll(game["current_number"])
    response = f"🎲 <@{game['current_player']}> rolled {rolled_number} (1-{game['current_number']})"
    
    if rolled_number == 1:
        winner = game["player1"] if game["current_player"] == game["player2"] else game["player2"]
        loser = game["current_player"]
        del active_games[game_id]
        return f"💀 <@{loser}> rolled a 1 and lost the game! <@{winner}> wins!"
    
    game["current_number"] = rolled_number
    game["current_player"] = game["player1"] if game["current_player"] == game["player2"] else game["player2"]
    
    return response + f"\n🔄 <@{game['current_player']}>, type `!roll {rolled_number}` to continue!"

def forfeit_deathroll(player: int) -> str:
    game_id = next((gid for gid in active_games if str(player) in gid), None)
    
    if not game_id:
        return "You're not in an active Deathroll game! Start one with `!deathroll @opponent`."
    
    game = active_games[game_id]
    winner = game["player1"] if game["player2"] == player else game["player2"]
    del active_games[game_id]
    return f"🏳️ <@{player}> has forfeited the game! <@{winner}> wins!"

def finish_deathroll(player: int) -> str:
    game_id = next((gid for gid in active_games if str(player) in gid), None)
    
    if not game_id:
        return "You're not in an active Deathroll game! Start one with `!deathroll @opponent`."
    
    del active_games[game_id]
    return f"🛑 <@{player}> has ended the current Deathroll game."
