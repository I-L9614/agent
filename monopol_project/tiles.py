class Tile:
    def __init__(self, tile_name, tile_type):
        self.name = tile_name
        self.type = tile_type

        
class PropertyTile(Tile):
    def __init__(self, tile_name, tile_type,city, price, rent):
        super().__init__(tile_name, tile_type)
        self.city = city
        self.price = price
        self.rent = rent
        self.is_available = True
        self.owners = None
    
    def by(self):
        print(f"Available. Do you want to by for {self.price}?")
    
    def rent(self):
        print(f'ned to pay rent {self.rent}')
        
class RailTile(PropertyTile):
    def __init__(self, tile_name, tile_type,city, price, rent):
        super().__init__(self, tile_name, tile_type,city, price, rent)
        



class JailTile(Tile):
    def __init__(self, tile_name, tile_type):
        super().__init__(self, tile_name, tile_type)
        
    def visit_jail():
        print("you stayin her for one round ")

class TaxTile(Tile):
    def __init__(self, tile_name, tile_type, give_money):
        super().__inint__(self, tile_name, tile_type)
        self.tax = give_money
    
    def massage(self):
        print(f"taxtile. you must pay {self.tax}")




class GoToJailTile(Tile):
    def __init__(self, tile_name, tile_type):
        super().__init__(self, tile_name, tile_type)
    def massage():
        print("you are going to jail for 3 rounds")

class Bonus(Tile):
    def __init__(self, tile_name, tile_type, get_monay):
        super().__init__(self, tile_name, tile_type)
        self.get_money = get_monay
    def getmoney(self):
        print(f"bonus tile, you get {self.get_money}")


class Start(Tile):
    def __init__(self, tile_name, tile_type):
        super().__init__(self, tile_name, tile_type)
        