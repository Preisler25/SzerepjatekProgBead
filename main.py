class StoryTeller:
    def say(self, text):
        print(f"[ game ] : '{text}'")

    def ask(self, text, name):
        return input(f"[ game ]: '{text}'\n[ {name} ]: ")

class Character:
    def __init__(self, name, list_of_items, max_inv_len):
        self.name = name
        self.list_of_items = list_of_items
        self.max_inv_len = max_inv_len

    def stats(self):
        print(f"[ {self.name} ] : 'your items: {self.list_of_items} and your storage capacity: {self.max_inv_len}'")

    def say(self, text):
        print(f"[ {self.name} ] : '{text}'")

class Dwarf:
    def __init__(self, name, list_of_questions):
        self.name = name
        self.list_of_questions = list_of_questions

    def play(self, player_name):
        question_aswered_correctly = False
        trys = 0
        while (question_aswered_correctly == False or trys <4):
            self.ask(self.list_of_questions[trys], player_name)

    def say(self, text):
        print(f"[ Dwarf {self.name} ]: '{text}'")

    def ask(self, text, name):
        return input(f"[ Dwarf {self.name} ]: '{text}'\n[ {name} ]: ")


def main():
    game = StoryTeller()
    player = Character(game.ask("mi a neved?", "player"), [], 3)
    dwarf0 = Dwarf("Erőske],", [{"kerdes1?", "valasz1"}, {"kerdes2?", "valasz2"}, {"kerdes3?", "valasz3"}])
    game.say(f"Hello {player.name}!")

main()