class StoryTeller:
    def say(self, text):
        print(f"[ GAME ] : {text}")

    def ask(self, text, name):
        return input(f"[ GAME ] : {text}\n[ {name} ]: ")

class Character:
    def __init__(self, name, list_of_items, max_inv_len, isAlive):
        self.name = name
        self.list_of_items = list_of_items
        self.max_inv_len = max_inv_len
        self.isAlive = isAlive

    def stats(self):
        print(f"[ {self.name} ] : táskám tartalma: #{self.list_of_items}# táskámban lévő szabad helyek: {self.max_inv_len - len(self.list_of_items)}")

    def say(self, text):
        print(f"[ {self.name} ] : {text}")

class Dwarf:
    def __init__(self, name, list_of_questions):
        self.name = name
        self.list_of_questions = list_of_questions

    def say(self, text):
        print(f"[ Dwarf {self.name} ] : {text}")

    def ask(self, text, name):
        return input(f"[ Dwarf {self.name} ] : {text}\n[ {name} ]: ")

    def getQuestion(self, index):
        for key in self.list_of_questions[index]:
            print(key)
            return key
        
    def getAnsw(self, index):
        for key in self.list_of_questions[index]:
            return self.list_of_questions[index][key]

    def play(self, player):
        if player.isAlive == False:
            return player
        else:
            trys = 0
            while (trys <3):
                user_answ = self.ask(self.getQuestion(trys), player.name)
                if user_answ == self.getAnsw(trys):
                    self.say("Helyes válasz! Nem hittem volna hogy ezt kitalálod :( Tessék itt az élelemed")
                    player.list_of_items.append("élelem")
                    return player
                trys += 1
            self.say("Sajnos nem válaszoltál helyesen! Ezért mint ahogy itt --> aláírtad felnégyellek")
            player.isAlive = False
            return player

    

class Spider:
    def __init__(self, name, quest, answ):
        self.name = name
        self.quest = quest
        self.answ = answ

    def say(self, text):
        print(f"[ Spider {self.name} ] : {text}")

    def ask(self, text, name):
        return input(f"[ Spider {self.name} ] : {text}\n[ {name} ]: ")

    def play(self, player):
        if player.isAlive == False:
            return player
        else:
            answ = int(self.ask(self.quest))
            if answ == self.answ:
                self.say("Helyes válasz tovább mehetsz! És mostár vízed is van")
                player.list_of_items.append("víz")
                return player
            self.say("Helytelen válasz! Bele ragadtál a pókháloba :(")
            player.isAlive = False
            return player

def main():
    game = StoryTeller()
    
    player = Character(game.ask("mi a neved?", "player"), [], 3, True)
    
    dwarf0 = Dwarf("Erőske", [{"kerdes1?": "valasz1"}, {"kerdes2?": "valasz2"}, {"kerdes3?": "valasz3"}])
    spider0 = Spider("Soklábú", "50+50", 100)


    player = dwarf0.play(player)
    player = spider0.play(player)

    player.stats()

main()