class Player:
    def __init__(self, _id : str, name : str, number : int) -> None:
        self.id = _id
        self.name = name
        self.number = number

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "number" : self.number
        }
    
    @staticmethod
    def from_dict(obj : dict):
        try:
            return Player(
                obj['id'],
                obj['name'],
                obj['number']
            )
        except:
            return None