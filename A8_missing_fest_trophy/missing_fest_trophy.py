class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def collect(self, item):
        self.bag.append(item)
        print(f"{self.name} collected: {item}")

    def has_item(self, item):
        return item in self.bag

    def show_bag(self):
        print("Bag:", self.bag)


class Place:
    def __init__(self, name, item=None, locked=False, required_item=None):
        self.name = name
        self.item = item
        self.locked = locked
        self.required_item = required_item

    def visit(self, player):
        if self.locked and not player.has_item(self.required_item):
            print(f"{self.name} is locked. You need {self.required_item}.")
            return None
        print(f"You entered {self.name}.")
        if self.item:
            player.collect(self.item)
            found = self.item
            self.item = None
            return found
        return None


class Chest:
    def __init__(self, code):
        self.code = code
        self.opened = False

    def open(self, entered_code):
        if entered_code == self.code:
            self.opened = True
            print("The chest opens! You found the trophy. YOU WIN!")
        else:
            print("The code is incorrect. The chest stays locked.")


def run_failed_route():
    print("\\n=== FAILED ROUTE ===")
    player = Player("Player")
    lab = Place("Computer Lab", item="secret code 4821", locked=True, required_item="key")
    stage = Place("Main Stage", locked=True, required_item="secret code 4821")
    chest = Chest("4821")
    lab.visit(player)
    stage.visit(player)
    player.show_bag()
    chest.open("0000")


def run_winning_route():
    print("\\n=== WINNING ROUTE ===")
    player = Player("Player")
    canteen = Place("Canteen", item="key")
    lab = Place("Computer Lab", item="secret code 4821", locked=True, required_item="key")
    stage = Place("Main Stage", locked=True, required_item="secret code 4821")
    chest = Chest("4821")

    canteen.visit(player)
    lab.visit(player)
    stage.visit(player)
    player.show_bag()
    chest.open("4821")


if __name__ == "__main__":
    run_failed_route()
    run_winning_route()
