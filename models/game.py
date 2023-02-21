from enum import StrEnum
from .players import Player

class GameState(StrEnum):
    START = 'start'
    DURING = 'during'
    END = 'end'


class Game:
    def __init__(self, _id, 
                 creator : dict, 
                 max_players=2, 
                 players : list[Player]=[],
                 state=GameState.START) -> None:
        self.id = _id
        if players:
            self.players = [Player.from_dict(player) for player in players] 
        else:
            self.players = [None for i in range(max_players - 1)] + [Player.from_dict(creator)]
        self.state =state
        self.creator = creator["_id"]

    def __add__(self, player_data : dict):
        for index, data in enumerate(self.players):
            if not data:
                self.players[index] = Player.from_dict(player_data)
                return True
        return False
    
    def __sub__(self, player_id : str):
        for index, data in enumerate(self.players):
            if data and data.id == player_id:
                del self.players[index]
                return True
        return False
    

    def serialize(self):
        return self.id , {
            "players": [player.serialize() if player else "" for player in self.players],
            "state": self.state,
            "creator" : self.creator
        }

    def check_winner(self, value):
        for player in self.players:
            if player.number == value:
                return player
        return None

    def set_state(self, state):
        self.state = state

    @staticmethod
    def from_dict(_id, game_dict : dict):
        try:
            return Game(
                _id,
                game_dict['creator'],
                players=game_dict["players"],
                state=GameState(game_dict["state"])
            )
        except:
            return None